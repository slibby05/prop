
# Prop: representing propositional logic

This project demonstrates how we can represent propositional logic formulas.

You can run this with 
> python3 main.py "expression"

You must put quotes around the expression,
otherwise the command line will be very confused.
example:
> python3 main.py "(a && b) || ~c"

This program will support the following expressions
* a && b - And
* a || b - Or
* a -> b - Implication
* ~a     - Not
* T      - True
* F      - False
* v      - variable

We have 4 different files.
* AST.py The Abstract syntax tree representing boolean expression
* Parser.py a file for parsing boolean expressions for the command line
* Exceptions.py a file containing the verious exceptions
* Main.py A simple program to read a single command line argument

Fortunately you only need to worry about Main.py and AST.py
