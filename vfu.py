import re, sys, os
from diff import * 

def func_lookup(argv):
    fname = argv[1]
    if(fname == "diff"):
        diff(argv)
    elif(fname == "grep"):
        grep(argv)
    elif(fname == "bulkrename"):
        diff(argv)
    elif(fname == "pwd"):
        diff(argv)

def call_version():
    print("Vince's File Utils v0.1")
    print("Author: https://github.com/vincebel7\n")

def call_help():
    print("usage: python3 vfu.py [--help] <function> [<args>]\n")

if(len(sys.argv) == 1):
    call_help()
if(len(sys.argv) >= 2):
    if(sys.argv[1] == "--help"):
        call_help()
    elif(sys.argv[1] == "--version"):
        call_version()
    else:
        func_lookup((sys.argv))
