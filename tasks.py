#!/usr/bin/env python3
import glob
import os
import sys
import subprocess
import scripts.patchup
from invoke import task

# Set up a custom exception handler to print errors to stderr
sys.excepthook = (lambda extype,value,trace: 
    print(f"Error: {value}", file=sys.stderr))

# Get all input files matching a given pattern and iterate
# over them. For each input file, yield the input and output
# file paths.
# example usage: "doc/**/*.md", "build/**/*.html"
def fileset(input_pattern, output_pattern, forceUpdate=False, createDirs=True):
    segments = input_pattern.split("*")
    input_prefix = segments[0]
    input_suffix = segments[-1] if len(segments) > 1 else ""
    segments = output_pattern.split("*")
    output_prefix = segments[0]
    output_suffix = segments[-1] if len(segments) > 1 else ""
    for input in glob.iglob(input_pattern, recursive=True):
        output = output_prefix + input[len(input_prefix):-len(input_suffix)] + output_suffix
        if forceUpdate or not os.path.exists(output) or os.path.getmtime(input) > os.path.getmtime(output):
            # file needs to be updated
            if createDirs:
                os.makedirs(os.path.dirname(output), exist_ok=True)
            yield (input, output)

# Display and run the command
def run(cmd):
    print(cmd)
    os.system(cmd)

# Check if the git repository is pristine and does not contain
# any uncommitted changes.
def is_repo_pristine(directory = None):
    return subprocess.check_output("git diff --stat", shell=True, cwd=directory).decode(encoding="utf-8") == ""

# Build Bikeshed files, and patch up title and status based on metadat
def build_bikeshed(input_pattern, output_pattern):
    for input, output in fileset(input_pattern, output_pattern):
        run(f"bikeshed -f --allow-nonlocal-files spec {input} {output}")
        scripts.patchup.patch_spec(input, output)

# Build Mermaid diagrams.
def build_mermaid(input_pattern, output_pattern):
    for input, output in fileset(input_pattern, output_pattern):
        run(f"mmdc -i {input} -o {output} --theme default")

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
    build_bikeshed("./spec/**/*.bs", "./build/**/*.html")
    build_mermaid("./spec/**/*.mmd", "./build/**/*.svg")

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

