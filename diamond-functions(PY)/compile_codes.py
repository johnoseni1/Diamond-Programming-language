from . import *
from .run_python import run_python

def execute_code(func_name, line, variables, index, lines, functions, python_funcs_and_vars):
    if func_name == 'say':
        text = get_variable(line[0], variables, line)

        say(text)
    elif func_name == 'create_var':
        var_name = line[0]
        var_value = line[1]

        create_variable(var_name, var_value, variables)
    elif func_name == 'create_function':
        create_function(line[0], lines)
    elif func_name in functions:
        function_lines = functions[func_name]
        
        for i in range(len(functions[func_name])):
            run_function(function_lines[i], variables, i, lines, functions)
    elif func_name == 'import':
        module_name = line[0]
        if not module_name.endswith('.cobra'):
            module_name += '.cobra'
        elif module_name.endswith('.cobra'):
            pass
        else:
            syntax_error()

        with open(module_name, 'r') as f:
            module_code = f.read()

        module_code = module_code.split('\n')
        for i in range(len(module_code)):
            run_main(module_code[0], variables, 0, module_code, functions)
    elif func_name == 'run_python':
        query = line[0]
        run_python(query, variables, line, python_funcs_and_vars)
    elif func_name == '' or func_name.startswith('#'):
        pass
    else:
        function_not_recognized(func_name)