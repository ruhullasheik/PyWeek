"""Example 4: CLI Tool with argparse

Run: python day-05-modules/topic/example_04_cli_tool.py --name Alice --greeting Yo --count 3
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="A customizable greeter")
    parser.add_argument("--name", required=True, help="Name to greet")
    parser.add_argument("--greeting", default="Hello", help="Greeting word")
    parser.add_argument("--count", type=int, default=1, help="Times to repeat")

    args = parser.parse_args()

    for _ in range(args.count):
        print(f"{args.greeting}, {args.name}!")


if __name__ == "__main__":
    main()
