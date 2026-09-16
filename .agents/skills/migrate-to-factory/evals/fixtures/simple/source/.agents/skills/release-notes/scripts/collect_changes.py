import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("--output", required=True)
args = parser.parse_args()
Path(args.output).write_text("Release notes draft\n", encoding="utf-8")
