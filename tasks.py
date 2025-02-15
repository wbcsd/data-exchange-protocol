#!/usr/bin/env python3
import os
import sys
import subprocess
import logging
import logging.config
import markdown
import scripts.openapi
import scripts.excel
from scripts.schema import schema_diff
from scripts.patchup import patchup, parse_bikeshed_file
from scripts.build import Dependency, fileset
from invoke import task


# Tasks for building the bikeshed documentation and releasing the specification.
# The tasks are implemented using python Invoke. For setting up your local
# editing environment, see EDITING.md
#
# Tasks include:
# - clean: Clean the build directory
# - build: Build the specification from the source files
# - release: Release a version of the specification
# - serve: Serve the specification for browsing locally  

# Display and run the command
def run(cmd):
    print(cmd)
    os.system(cmd)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up a custom exception handler to print friendly errors to stderr
def error_handler(exctype, value, traceback):
    print(f"Error: {value}", file=sys.stderr)
    exit(1)

old_excepthook = sys.excepthook
sys.excepthook = error_handler

# Check if the git repository is pristine and does not contain
# any uncommitted changes.
def is_repo_pristine(directory = None):
    return subprocess.check_output("git diff --stat", shell=True, cwd=directory).decode(encoding="utf-8") == ""

# Generate html from markdown
def render_markdown(input, output):
    template = """<html>
    <head>
    <link href="assets/markdown.css" rel="stylesheet" />
    </head>
    <body>
    """
    with open(input, "r") as input_file:
        html = template + markdown.markdown(input_file.read()) + "</body></html>"
        with open(output, "w") as output_file:
            output_file.write(html)

# Copy a file
def copy_file(input, output):
    run(f"cp {input} {output}")

# Generic build task
def build_task(dependencies, task):
    for dependency in dependencies:
        if dependency.outdated():
            dependency.makedir()
            task(dependency.sources[0], dependency.target)


# Build Bikeshed files, and patch up title and status based on metadata
def build_bikeshed(dependencies):
    for dependency in dependencies:
        if dependency.outdated():
            dependency.makedir()
            run(f"bikeshed -f --no-update --allow-nonlocal-files spec {dependency.sources[0]} {dependency.target}")
            patchup(dependency.sources[0], dependency.target)

# Build Mermaid diagrams.
def build_mermaid(dependencies):
    for dependency in dependencies:
        if dependency.outdated():
            dependency.makedir()
            # running with .github/puppeteer-config.json to avoid rendering issues on GitHub Actions
            run(f"mmdc -i {dependency.sources[0]} -o {dependency.target} --theme default -p .github/puppeteer-config.json")

@task
def clean(c):
    """
    Clean the build directory
    """
    c.run("rm -rf ./build")    
    c.run("rm -f ./spec/v2/data-model.generated.md")
    c.run("rm -f ./spec/v3/data-model.generated.md")

@task
def build(c):
    """ 
    Build the specifcation (all versions) from the source files.
    """
    build_task([
        Dependency("spec/v3/data-model.generated.md", ["spec/v3/openapi.yaml"]),
        Dependency("spec/v2/data-model.generated.md", ["spec/v2/openapi.yaml"])],
        scripts.openapi.generate_data_model
        )
    build_task([
        Dependency("build/v2/pact-simplified.xlsx", ["spec/v2/openapi.yaml"]),
        Dependency("build/v3/pact-simplified.xlsx", ["spec/v3/openapi.yaml"])],
        lambda source, target: scripts.excel.openapi_to_excel(source, target, "PACT Simplified Data Model", ["ProductFootprint"])
        )
    build_bikeshed([
        Dependency("build/faq/index.html", ["spec/faq/index.bs"]),
        Dependency("build/v1/index.html", ["spec/v1/index.bs", "spec/v1/examples/*", "LICENSE.md"]),
        Dependency("build/v2/index.html", ["spec/v2/index.bs", "spec/v2/examples/*", "LICENSE.md"]),
        Dependency("build/v3/index.html", ["spec/v3/index.md", "spec/v3/*.md", "spec/v3/examples/*", "LICENSE.md"])
        ])
    build_mermaid([
        Dependency(target, [source]) for source,target in fileset("./spec/**/*.mmd", "./build/**/*.svg")
        ])
    build_task([
        Dependency("build/index.html", ["index.md"])], 
        render_markdown
        )
    build_task([
        Dependency("build/assets/logo.svg", ["assets/logo.svg"]), 
        Dependency("build/assets/logo-dark.svg", ["assets/logo-dark.svg"]), 
        Dependency("build/assets/markdown.css", ["assets/markdown.css"]), 
        Dependency("build/v2/openapi.yaml", ["spec/v3/openapi.yaml"]), 
        Dependency("build/v3/openapi.yaml", ["spec/v3/openapi.yaml"])], 
        copy_file
        )


@task(help={"ver": "Major version to release, can be v2 or v3"})
def release(c, ver="v2"):
    """
    Release a version of the specification. Specify the major 
    version to release, this can be v1, v2 or v3.
    """
    input = f"./spec/{ver}/index.bs"
    title, date, version, status = parse_bikeshed_file(input)
    print(f"Building release version {version}", file=sys.stderr)

    if status != "Release":
        raise Exception("Not a release version")
    if not is_repo_pristine("."):
        raise Exception("Working tree is dirty. Finish committing files or stash, then try again.")
        
    print("Building release version", version) 

@task(help={"ver": "Major version to serve, can be v2 or v3"}) 
def serve(c, ver="v3"):
    build(c)
    print(f"Open your browser at \033[4mhttp://localhost:8000/build/{ver}\033[0m")
    print(f"Press Ctrl+C to stop the server\n")
    run(f"bikeshed --allow-nonlocal-files --no-update serve spec/{ver}/index.bs build/{ver}/index.html")

@task
def validate(c):
    """
    Validate OpenAPI schema
    """
    run("openapi-spec-validator spec/v2/openapi.yaml")
    run("openapi-spec-validator spec/v3/openapi.yaml")
    # TODO: Add markdownlint and bikeshed validation

@task
def debug(c):
    logging.info("Debugging")
    logging.basicConfig(level=logging.DEBUG)
    sys.excepthook = old_excepthook


@task
def diff(c):
    scripts.schema.schema_diff("spec/v2/openapi.yaml", "spec/v3/openapi.yaml")

@task
def experiment(c):
    """
    Experimental generation of data models, based on OpenAPI schema
    """
    # scripts.openapi.test("spec/v3/openapi.yaml")
    # scripts.schema.validate_json_data("spec/v3/openapi.yaml", "spec/v3/examples/list-footprints-response.json")
    scripts.schema.validate_json_data(
        "spec/v3/openapi.yaml#paths/\/3\/footprints/get/responses/200/content/application\/json/schema", 
        "spec/v3/examples/list-footprints-response.json"
        )
    scripts.schema.validate_json_data(
        "spec/v3/openapi.yaml#paths/\/3\/footprints/get/responses/200/content/application\/json/schema", 
        "spec/v3/examples/invalid-response-all-properties.json"
        )
    scripts.schema.validate_json_data(
        "spec/v3/openapi.yaml#paths/\/3\/footprints\/{id}/get/responses/200/content/application\/json/schema", 
        "spec/v3/examples/get-footprint-response.json"
        )
    scripts.schema.validate_json_data(
        "spec/v3/openapi.yaml#components/schemas/RequestFulfilledEvent", 
        "spec/v3/examples/pf-response-event.json"
        )
    scripts.schema.validate_json_data(
        "spec/v3/openapi.yaml#paths/\/3\/footprints/get/responses/403/content/application\/json/schema", 
        "spec/v3/examples/error-response-access-denied.json"
        )
