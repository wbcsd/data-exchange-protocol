#!/usr/bin/env python3
import glob
import os
import sys
import subprocess
from scripts.patchup import patchup
from scripts.build import Dependency, fileset
from invoke import task


# Display and run the command
def run(cmd):
    print(cmd)
    os.system(cmd)

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
            run(f"mmdc -i {dependency.sources[0]} -o {dependency.target} --theme default")

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
        Dependency("build/v3/index.html", ["spec/v3/index.bs", "spec/v3/*.md", "spec/v3/examples/*", "LICENSE.md"])
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
    title, date, version, status = scripts.patchup.parse_bikeshed_file(input)
    print(f"Building release version {version}", file=sys.stderr)

    if status != "Release":
        raise Exception("Not a release version")
    if not is_repo_pristine("."):
        raise Exception("Working tree is dirty. Finish committing files or stash, then try again.")
        
    print("Building release version", version) 

@task(help={"ver": "Major version to serve, can be v2 or v3"}) 
def serve(c, ver="v3"):
    build(c)
    run(f"bikeshed --allow-nonlocal-files serve spec/{ver}/index.bs build/{ver}/index.html")


