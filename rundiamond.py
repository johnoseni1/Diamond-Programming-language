   
# MIT License

# Copyright (c) 2022 John Oseni

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import functions as modulefunctions

def run_function(index, python_funcs_and_vars, lines, line, _functions, variables):
    line = line.split(' ')

    func_name = line[0]
    del line[0]

    modulefunctions.execute_code(
        func_name,
        line,
        variables,
        index,
        lines,
        _functions,
        python_funcs_and_vars
    )

def run_main(line, variables, index, lines, _functions_dict, python_funcs_and_vars):
    run_function(line, variables, index, lines, _functions_dict, python_funcs_and_vars)
    del lines[index]
