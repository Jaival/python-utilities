from pathlib import Path


def generate_all_files(root: Path, only_files: bool = True):
    for loc in root.rglob("*"):
        if only_files and not loc.is_file():
            continue
        yield loc


for p in generate_all_files(Path("./location"), only_files=False):
    print(p)
