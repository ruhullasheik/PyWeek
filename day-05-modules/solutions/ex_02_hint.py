"""Hints for ex_02

    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default=".")
    parser.add_argument("--prefix", default="file")
    args = parser.parse_args()

    directory = Path(args.dir)
    for i, f in enumerate(directory.glob("*.txt"), start=1):
        new_name = f"{args.prefix}_{i:03d}{f.suffix}"
        f.rename(f.parent / new_name)
        print(f"{f.name} -> {new_name}")
"""
