import sys

def function_not_recognized(function_name):
    print(f"'{function_name}'isn't recognized as a function.")
    sys.exit()

def variable_not_found(variable_name):
    print(f'{variable_name} not Defined')
    sys.exit()

def syntax_error():
    print('Syntax Error')
    sys.exit()
