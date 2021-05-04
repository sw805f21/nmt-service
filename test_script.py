import argparse
import time

# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("--model", "-m", help="show model", action="store_true")
parser.add_argument("--version", "-v", help="show program version", action="store_true")
parser.add_argument("--qwe", "-qwe", help="show program version", action="store_true")

# Read arguments from the command line
args = parser.parse_args()

# Check for --version or -V
if args.version:
    time.sleep(3.4)
    print("This is myprogram version 0.1")

# Check for --version or -V
if args.model:
    print("This is model")

# Check for --version or -V
if args.qwe:
    print("This is qwe")