#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
	print("USAGE: command_line_argument.py <password>")
else:
	print("password", sys.argv[1])
