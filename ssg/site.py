from pathlib import Path

class Site:

    def __init__(self, source, dest):
        self._source = source
        self._dest = dest

    def source(self):
        return Path(self._source)

    def dest(self):
        return Path(self._dest)


    def create_dir(self, path):
        part1 = path.relative_to(self.source())
        part2 = self.dest()
        directory = Path(part1.joinpath(part2))
        directory.mkdir(parents=True, exist_ok=True)


    def build(self):
        self.dest().mkdir(parents=True, exist_ok=True)
        for path in self.source().rglob("*"):
            if Path(path).is_dir:
                self.create_dir(path)