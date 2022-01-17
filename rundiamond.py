import functions as _functions_module

def run_function(index, python_funcs_and_vars, line, lines, _functions, variables):
    line = line.split(' ')

    func_name = line[0]
    del line[0]

    _functions_module.execute_code(
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
