from sys import argv
from AST import (truth_table, Var, true, false, And, Or, Not, Arrow)
from Parser import parse
from Exceptions import (EvalException, ParseException, LexException)
                   orIL, orIR, orE, assume, assumed, arrowI, arrowE, \
                   notI, notE, TI, FE, LEM)

def main():
    if len(argv) < 2:
        print("Error: you need to enter an expression")

    try:
        expr = parse(argv[1])
        print(expr)
        truth_table(expr)
    except (LexException, ParseException, EvalException) as e:
        print(str(e))


if __name__ == "__main__":
    main()
