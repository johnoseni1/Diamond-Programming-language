import os
import sys

from rundiamond import run_main

filename = sys.argv[1]

with open(filename, 'r') as f:
    data = f.read()

variables = {
    'test': 'Hello',
    'true': True,
    'false': False
}

_functions = {}
python_funcs_and_vars = locals()

lines = data.split('\n')
for i in range(len(lines)):
    run_main(lines[0], variables, 0, lines, _functions, python_funcs_and_vars)