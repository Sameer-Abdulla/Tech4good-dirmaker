import argparse
import os
import shutil
import sys

__version__ = "1.1.0"

def main():
    """Run the CLI."""
    p = argparse.ArgumentParser(
        description="A simple static site generator for generating directory websites.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    p.add_argument("-v", "--version", action="store_true", dest="version", help="display version")

    n = p.add_argument_group("new")
    n.add_argument("-n", "--new", action="store_true",
                   dest="new", help="initialize a new site")
    n.add_argument("-p", "--path", action="store", type=str, default="example",
                   dest="exampledir", help="path to create the example site")

