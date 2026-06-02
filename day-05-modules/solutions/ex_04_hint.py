"""Hints for ex_04

    import argparse
    import json
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser()
    parser.add_argument("config_file")
    parser.add_argument("key", nargs="?")
    args = parser.parse_args()

    try:
        data = json.loads(Path(args.config_file).read_text())
    except FileNotFoundError:
        print(f"Error: {args.config_file} not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: {args.config_file} is not valid JSON")
        sys.exit(1)

    if args.key:
        # Handle nested keys like "settings.theme"
        keys = args.key.split(".")
        value = data
        for k in keys:
            value = value.get(k) if isinstance(value, dict) else None
            if value is None:
                print(f"Key '{args.key}' not found")
                sys.exit(1)
        print(json.dumps(value, indent=2))
    else:
        print(json.dumps(data, indent=2))
"""
