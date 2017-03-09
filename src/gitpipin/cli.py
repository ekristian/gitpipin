#!/usr/bin/env python

import sys
import argparse


def hello_world(name="Mr. Fancy Pants"):
    print("Hello {}!".format(name))

def hello_world_args(args):
    """Put your argument parser in a function like this.
    That way you can get the necessary command-line arguments and pass them
    to your Python function.
    Decoupling the cli call and the Python function allows you to easily
    call your function from other Python code, not just the CLI!
    """
    description = "Say hello to your little friend"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-n", "--name", default="World",
                        help="To whom should we greet?")
    retval = vars(parser.parse_args(args))
    return retval

def hello_world_cli():
    args = hello_world_args(sys.argv[1:])
    hello_world(args['name'])


if __name__ == "__main__":
    hello_world()
