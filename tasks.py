#!/usr/bin/env python3
import glob
import os
import sys
import subprocess
import scripts.openapi
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

# Set up a custom exception handler to print friendly errors to stderr
def error_handler(exctype, value, traceback):
    print(f"Error: {value}", file=sys.stderr)
    exit(1)

sys.excepthook = error_handler

# Check if the git repository is pristine and does not contain
# any uncommitted changes.
def is_repo_pristine(directory = None):
    return subprocess.check_output("git diff --stat", shell=True, cwd=directory).decode(encoding="utf-8") == ""

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

@task
def build(c):
    """ 
    Build the specifcation (all versions) from the source files.
    """
    build_bikeshed([
        Dependency("build/faq/index.html", ["spec/faq/index.bs"]),
        Dependency("build/v1/index.html", ["spec/v1/index.bs", "spec/v1/examples/*", "LICENSE.md"]),
        Dependency("build/v2/index.html", ["spec/v2/index.bs", "spec/v2/examples/*", "LICENSE.md"]),
        Dependency("build/v3/index.html", ["spec/v3/index.md", "spec/v3/*.md", "spec/v3/examples/*", "LICENSE.md"])
        ])

    build_mermaid([
        Dependency(target, [source]) for source,target in fileset("./spec/**/*.mmd", "./build/**/*.svg")
        ])

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
def experiment(c):
    """
    Experimental generation of data models, based on OpenAPI schema
    """
    scripts.openapi.generate_data_model("spec/v3/openapi.yaml", "spec/v3/datamodel")
