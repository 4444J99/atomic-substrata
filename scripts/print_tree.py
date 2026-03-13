from pathlib import Path

def walk(path: Path, prefix: str = ""):
    entries = sorted([p for p in path.iterdir()], key=lambda p: (p.is_file(), p.name))
    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry.name)
        if entry.is_dir():
            extension = "    " if i == len(entries) - 1 else "│   "
            walk(entry, prefix + extension)

root = Path(".")
print(root.resolve().name)
walk(root)
