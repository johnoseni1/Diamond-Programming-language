<div align="center">
 <h1> Diamond Programming Language </h1>
 </div>

## Requirements to run Diamond 

- All needed right now is nothing but the python programming langauge, and you could learn how to download and set it up [here](https://medium.com/co-learning-lounge/how-to-download-install-python-on-windows-2021-44a707994013)

# Usage (Diamond PL)

### How to run

#### Mac or Linux
```bash
./diamond.sh <diamondfilename>
```

What to write to run the codes:

```shell
python execute.py <diamondfilename>
```

#### Windows
```batch
diamond <diamondfilename>
```

You could check out my `Schemacodes.diamond` in folder DIR

You can run it by running the following command in your terminal:
```shell
python execute.py Schemacodes.diamond 
```
or by using the above: [Windows](#windows), [Mac or Linux](#mac-or-linux).

### Syntax
The basic syntax for a diamond programming language program is: `name of function any arguments to be passed in to the function`.
For example, 
if you input `spill Hello, World!`, `spill` is the function  in diamond
and `Hello, World!` is the argument passed to it. To create a comment, use the # sign. 
For example: `# Of cause we know that this is a comment and it would be ignored by diamond PL`.

### Functions
The current functions for diamond are:
#### spill
Task: Print this in the console
<br>
Arguments will be like :
- text: e.g (`hello world`)

Sample: `spill Hello, World!`

#### create_variables in Diamond
 Create a variable in diamond

<br>
Arguments:
- name: Variable name
- value: Variable value. Could be a existing variable or string before

Example: `create_variable dior "this is me"`

#### create_function
Description: Creates a function
<br>
Arguments:
- name: Name the function

Example:
```
create_function my_world:
    spill "hello"
```

when you wanna execute a function?:
```
# Type the function's name down
my_world
```

#### import a file in diamond
Task: Import another file into your own file
<br>
Arguments:
- The filename: The name of the file you want to import could end with .diamonod or maybe not.

Example: `import hiworld`

In hiworld.diamond, there is a function called `my_function`. To run it, just type it in.
```
import hiworld
my_function
```
The `import` function will always import everything in the file for now

#### python_run
Task: Runs a line of Python code in the diamond environment.
<br>
Arguments:
- query: The query that you want to run.

Sample : `python_run "print('Hello World!')"`

This makes it go in line with python programming language, because it was written in python

For other samples check the folder `Schemacodes.diamond` file in the root DIR.

 <div>
     <h3>  Author  <a href="https://linktr.ee/johnoseni">John Oseni</a> </h3>
 </div>