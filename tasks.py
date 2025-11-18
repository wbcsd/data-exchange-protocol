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
from scripts.build import Dependency, fileset, dependencies
from invoke import task
from packaging.version import Version


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
def render_markdown(input, output: str):
    rel_root_path = (output.count('/')-1) * "../"
    header = f"""<!doctype html>
<html lang="en">
<head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"><html>
    <link href="./assets/default.css" rel="stylesheet" />
</head>
<body>
    """
    footer = """</body>
</html>"""
    with open(input, "r") as input_file:
        html = header + markdown.markdown(
            input_file.read(), 
            extensions=['tables','md_in_html']
            ) + footer
        with open(output, "w") as output_file:
            output_file.write(html)

# Copy a file
def copy_file(input, output):
    run(f"cp {input} {output}")

# Generic build task
def build_task(dependencies, task):
    for dependency in dependencies:
        if dependency.outdated():
            logging.info(f"Building {dependency.target}")
            dependency.makedir()
            task(dependency.sources[0], dependency.target)


# Build Bikeshed files, and patch up title and status based on metadata
def build_bikeshed(dependencies):
    for dependency in dependencies:
        if dependency.outdated():
            logging.info(f"Building {dependency.target}")
            dependency.makedir()
            run(f"bikeshed -f --no-update --allow-nonlocal-files spec {dependency.sources[0]} {dependency.target}")
            patchup(dependency.sources[0], dependency.target)

# Build Mermaid diagrams.
def build_mermaid(dependencies):
    for dependency in dependencies:
        if dependency.outdated():
            logging.info(f"Building {dependency.target}")
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
        Dependency("spec/v3/rest-api.generated.md", ["spec/v3/openapi.yaml"])],
        scripts.openapi.generate_rest_api
        )
    build_task([
        Dependency("build/v2/pact-simplified.xlsx", ["spec/v2/openapi.yaml"]),
        Dependency("build/v3/pact-simplified.xlsx", ["spec/v3/openapi.yaml"])],
        lambda source, target: scripts.excel.generate_simplified_datamodel(source, target, "PACT Simplified Data Model", "ProductFootprint")
        )
    build_bikeshed([
        Dependency("build/v1/index.html", ["spec/v1/index.bs", "spec/v1/examples/*", "LICENSE.md"]),
        Dependency("build/v2/index.html", ["spec/v2/index.bs", "spec/v2/examples/*", "LICENSE.md"]),
        Dependency("build/v3/index.html", ["spec/v3/index.md", "spec/v3/*.md", "spec/v3/examples/*", "LICENSE.md"])
        ])
    build_mermaid(
        dependencies("./build/v2/**/*.svg", "./spec/v2/**/*.mmd")
        )
    build_task([
        Dependency("build/index.html", ["index.md"]), 
        Dependency("build/release-plan.html", ["RELEASE-PLAN.md"]),
        Dependency("build/faq.html", ["faq.md"]),
        Dependency("build/v3/license.html", ["LICENSE.md"])
        ], 
        render_markdown
        )
    build_task(
        dependencies('./build/v2/assets/**/*', './assets/**/*') +
        dependencies('./build/v3/assets/**/*', './assets/**/*') +
        dependencies('./build/assets/**/*', './assets/**/*') +
        dependencies('./build/v*/*.yaml', './spec/v*/*.yaml'),
        copy_file
        )

@task(help={"ver": "Major version to release, can be v2 or v3"})
def release(c, ver="v3"):
    """
    Release a version of the specification. Specify the major 
    version to release, this can be v1, v2 or v3.
    """
    input = f"./spec/{ver}/index.bs" 
    input = f"./spec/{ver}/index.md" if not os.path.exists(input) else input
    title, date, version, status = parse_bikeshed_file(input)
    year = date[0:4]
    logging.info(f"Version: {version}, Date: {date}, Status: {status} Year: {year}")
    destination  = "../tr"

    schema = scripts.schema.load_openapi_file(f"spec/{ver}/openapi.yaml")
    if schema.get("info", {}).get("version") != version:
        raise Exception(f"Version mismatch: OpenAPI schema version {schema.get('info', {}).get('version')} != expected version {version}")

    if not os.path.exists(destination):
         raise Exception(f"Destination {destination} does not exist. Expecting the local path to the TR repository.")
    if status != "Release":
        raise Exception(f"Not a release version: {version}: {status}")
    if not is_repo_pristine("."):
        raise Exception("Working tree is dirty. Finish committing files or stash, then try again.")
    if os.path.exists(f"{destination}/{date}"):
        raise Exception(f"Destination {destination}/{date} already exists. Expecting a new release.")

    print(f"Building release version {version}", file=sys.stderr)
    clean(c)
    build(c)

    print("Publishing release") 
    c.run(f"mkdir -p {destination}/{year}/data-exchange-protocol-{date}")
    c.run(f"cp -R build/{ver}/* {destination}/{year}/data-exchange-protocol-{date}")

    c.run(f"mkdir -p {destination}/data-exchange-protocol/{version}")
    c.run(f"cp -R build/{ver}/* {destination}/data-exchange-protocol/{version}")

    # determine latest version by listing the directory destination/data-exchange-protocol/*
    versions = [
        Version(dir) for dir in os.listdir(f"{destination}/data-exchange-protocol")
        if os.path.isdir(f"{destination}/data-exchange-protocol/{dir}") and dir[0].isdigit()
    ]
    current_version = Version(version)
    latest_same_major_minor_version = max((v for v in versions if v.major == current_version.major and v.minor == current_version.minor), default=None)
    latest_version = max(versions, default=None)
    
    logging.info(f"Current version: {current_version}")
    logging.info(f"Latest same major version: {latest_same_major_minor_version}")
    logging.info(f"Latest version: {latest_version}")

    if latest_same_major_minor_version is None or latest_same_major_minor_version <= current_version:
        c.run(f"rm -rf {destination}/data-exchange-protocol/{current_version.major}.{current_version.minor}")    
        c.run(f"cp -R {destination}/data-exchange-protocol/{current_version} {destination}/data-exchange-protocol/{current_version.major}.{current_version.minor}")

    if latest_version is None or latest_version <= current_version:
        c.run(f"rm -rf {destination}/data-exchange-protocol/latest")    
        c.run(f"cp -R {destination}/data-exchange-protocol/{current_version} {destination}/data-exchange-protocol/latest")

    print(f"Published release version {version} to {destination}")
    print(f"Commit and merge the pull request in the TR repository")


@task(help={"ver": "Major version to serve, can be v2 or v3"}) 
def serve(c, ver="v3"):
    build(c)
    print(f"Open your browser at \033[4mhttp://localhost:8000/build/{ver}\033[0m")
    print(f"Press Ctrl+C to stop the server\n")
    run(f"bikeshed --allow-nonlocal-files --no-update serve spec/{ver}/index.bs build/{ver}/index.html")

@task
def validate(c):
    """
    Validate OpenAPI schema and example JSON files
    """

    # Validate OpenAPI schema files
    run("openapi-spec-validator spec/v2/openapi.yaml")
    run("openapi-spec-validator spec/v3/openapi.yaml")

    # Validate example JSON files against the OpenAPI schema
    checks = {
        # v2
        "spec/v2/examples/list-footprints-response.json": "spec/v2/openapi.yaml#paths/%2F2%2Ffootprints/get/responses/200/content/application%2Fjson/schema", 
        "spec/v2/examples/get-footprint-response.json": "spec/v2/openapi.yaml#paths/%2F2%2Ffootprints%2F{id}/get/responses/200/content/application%2Fjson/schema", 
        "spec/v2/examples/pf-response-event.json": "spec/v2/openapi.yaml#components/schemas/RequestFulfilledEvent",
        "spec/v2/examples/invalid-response-all-properties.json": "spec/v2/openapi.yaml#paths/%2F2%2Ffootprints/get/responses/200/content/application%2Fjson/schema", 
        "spec/v2/examples/error-response-access-denied.json": "spec/v2/openapi.yaml#paths/%2F2%2Ffootprints/get/responses/403/content/application%2Fjson/schema",
        # v3
        "spec/v3/examples/list-footprints-response.json": "spec/v3/openapi.yaml#paths/%2F3%2Ffootprints/get/responses/200/content/application%2Fjson/schema", 
        "spec/v3/examples/get-footprint-response.json": "spec/v3/openapi.yaml#paths/%2F3%2Ffootprints%2F{id}/get/responses/200/content/application%2Fjson/schema", 
        "spec/v3/examples/pf-response-event.json": "spec/v3/openapi.yaml#components/schemas/RequestFulfilledEvent",
        "spec/v3/examples/invalid-response-all-properties.json": "spec/v3/openapi.yaml#paths/%2F3%2Ffootprints/get/responses/200/content/application%2Fjson/schema", 
        "spec/v3/examples/error-response-access-denied.json": "spec/v3/openapi.yaml#paths/%2F3%2Ffootprints/get/responses/403/content/application%2Fjson/schema",
        "spec/v3/examples/example-1.json": "spec/v3/openapi.yaml#components/schemas/ProductFootprint",
        "spec/v3/examples/example-2.json": "spec/v3/openapi.yaml#components/schemas/ProductFootprint",
        "spec/v3/examples/example-3.json": "spec/v3/openapi.yaml#components/schemas/ProductFootprint",
        "spec/v3/examples/example-4.json": "spec/v3/openapi.yaml#components/schemas/ProductFootprint",
    }
    for data, schema in checks.items():
        try:
            scripts.schema.validate_json_data(schema, data)
        except Exception as e:
            print(f"Validation failed for {data} against {schema}: {e}")
            raise



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
    # schexma = scripts.schema.load_openapi_file("spec/v3/openapi.yaml")
    # schema = scripts.schema.navigate_to(schema, "components/schemas/RequestCreatedEvent")
    # print(scripts.schema.dump_schema(schema))

    if False:
        def yaml_to_json(inp, out):
            logging.info(f"Building {out}")
            scripts.schema.yaml_to_json_file(inp, out)
            scripts.schema.validate_json_data("spec/v3/openapi.yaml#components/schemas/ProductFootprint", out)

        build_task([
            Dependency("spec/v3/examples/example-1.json", ["spec/v3/examples/example-1.yaml"]),
            Dependency("spec/v3/examples/example-2.json", ["spec/v3/examples/example-2.yaml"]),
            Dependency("spec/v3/examples/example-3.json", ["spec/v3/examples/example-3.yaml"]),
            Dependency("spec/v3/examples/example-4.json", ["spec/v3/examples/example-4.yaml"])
            ],
            yaml_to_json
        )
