#!/usr/bin/env python3

# Imports

import argparse

# Parse command line arguments

parser = argparse.ArgumentParser(description="Process CLI args.")
parser.add_argument("-m", "--mode", help="check mode", required=False)
args = parser.parse_args()

# MAIN #

if __name__ == '__main__':

    if args.mode == "a":
        print("a.")