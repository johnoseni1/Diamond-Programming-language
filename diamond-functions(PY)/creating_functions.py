
# syntax for creating functions


from .show_erros import syntax_error 

from ..rundiamond import modulefunctions

def create_function(function_name, current_lines):
    function_lines = []

    if not function_name.endswith(':'):
        syntax_error()

    function_name = function_name[:len(function_name) - 1]

    for current_line in current_lines:
        if current_line.startswith(''):
            function_lines.append(current_line.replace('',''))

    modulefunctions[function_name] = function_lines