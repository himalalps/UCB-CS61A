# Expressions

An expression describes a computation and evaluates to a value

$$f(x)$$

All expressions can use function call notation

## anatomy

operators and operands are also expressions, so evaluate to values

evaluation procedure:

1. evaluate operator and operand subexpressions
2. apply the function

nested expression - tree(evaluate from root to leaf, calculate from leaf to root)

## type

primitive - number, name, string

call - `max(2, 3)`

# Environment diagrams

[PythonTutor](https://pythontutor.com/cp/composingprograms.html#mode=edit)

to visualize interpreter's process

code + frames

## Defining functions

assignment is a simple means of abstraction: bind names to values

function definition is a more powerful means of abstraction: bind names to expressions

```python
>>> def <name>(<formal parameters>): # -> function signature
        return <return expression>   # -> function body
```

execution procedure:
1. create a function with signature
2. set the body of the function to be thing indented after the first line
3. bind `<name>` to that function in the current frame

call/apply procedure:
1. add a local frame, form a new environment
2. bind the function's formal parameters to its arguments in the frame
3. execute the function in the new environment

*return value is not a binding*

## looking up names in environments

every expression is evaluated in the context of an environment

**An environment is a sequence of frames.**

**A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found.**

