import glob
import os

# Get all input files matching a given pattern and iterate
# over them. For each input file, yield the input and output
# file paths.
# example usage: "doc/**/*.md", "build/**/*.html"
def fileset(input_pattern, output_pattern):
    segments = input_pattern.split("*")
    input_prefix = segments[0]
    input_suffix = segments[-1] if len(segments) > 1 else ""
    segments = output_pattern.split("*")
    output_prefix = segments[0]
    output_suffix = segments[-1] if len(segments) > 1 else ""
    for input in glob.iglob(input_pattern, recursive=True):
        if len(input_suffix) > 0:
            output = output_prefix + input[len(input_prefix):-len(input_suffix)] + output_suffix
        else:
            output = output_prefix + input[len(input_prefix):] + output_suffix
        yield (input, output)


# A Dependency object represents a target file and its source files.
# It checks if the target file is outdated based on the modification times
# of the source files. If the target file does not exist or any of the
# source files are newer than the target file, it is considered outdated.
class Dependency:
    def __init__(self, target, sources):
        self.target = target
        self.sources = []
        for source in sources:
            self.sources += [path for path in glob.iglob(source)]

    def outdated(self):
        return not os.path.exists(self.target) \
            or any(source for source in self.sources if os.path.getmtime(source) > os.path.getmtime(self.target))
    
    def makedir(self):
        os.makedirs(os.path.dirname(self.target), exist_ok=True)


# Iterate over all input files matching a given pattern
# and yield a Dependency object for each file. If the output
# file is outdated or forceUpdate is True, the Dependency
# object will be created. If createDirs is True, the output
# directory will be created if it does not exist.
def dependencies(output_pattern, input_pattern):
    return [Dependency(output, [input]) for input, output in fileset(input_pattern, output_pattern)]
