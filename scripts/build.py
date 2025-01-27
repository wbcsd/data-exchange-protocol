import glob
import os

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
        yield (input, output)

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
