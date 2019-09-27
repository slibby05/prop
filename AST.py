from enum import Enum
from Exceptions import EvalException

############################################################################################
# These classes represent the different types of propositional logic expressions.
# 
# Remember each expression can be represented as a Tree.
# So (a || b) && ~c is really the tree:
#        &&
#       /  \
#      /    \
#     ||     ~
#    /  \    |
#   /    \   c
#  a      b   
#
# We can construct this tree in python with:
# And(Or(Var("a"), Var("b")), Not(Var("c")))
#
# Since variables make this code harder to read
# for the rest of this file I'll use the variables
# a = Var("a")
# b = Var("b")
# c = Var("c")
# Now the above expression can be rewritten as
# And(Or(a,b), Not(c))
############################################################################################

# This tells us what type of Node we've created
# You don't need to worry about this part.
class Node(Enum):
    ARROW = 1
    OR    = 2
    AND   = 3
    NOT   = 4
    LIT   = 5
    VAR   = 6

############################################################################################
# An And node represents the expression a && b
# Each and node has a 
# 1. left hand side (lhs)
# 2. right hand side (rhs)
#
# In this case the lhs = "a", and the rhs = "b"
#
# The And node (along with every other type of expression)
# has several methods that we can call
#
# __init__() is the constructor, this is what is called when we write And(a,b)
#
# __str__()  returns a string representing the expression (this is what str() calls)
# example:
#  str(And(a,b)) returns the string "(a && b)"
#
# __eq__()   returns a True if both expressions are identical (this is what a == b calls)
# example:
#  And(a,b) == And(b,a) returns False.
#  Even though these two expressions are equivalent,
#  they are not literally the same expression.
#
# vars()     returns the set of all variables is the expression
# Example:
#  And(a,b).vars() returns {"a","b"}
#
# type()     returns the type of the node (this isn't used)
# Example:
#  And(a,b).type() returns Node.AND
#
# eval()     given the variables in env, return if the expression evaluates to True of False
#            env is the environment, it is a dictionary containing all of the values for variables.
#            if env = {"a" : True, "b" : False, "c" : False}
#            then env["a"] == True
# Example:
#  And(a,b).eval({"a" : True, "b" : False}) returns False
#  because env["b"] == False, and True && False == False
#
#  Or(And(a,b), Not(c)).eval({"a" : True, "b" : False, "c" : False}) returns True
#
#  We can see this by splitting it up
#
#  And(a,b).eval({"a" : True, "b" : False, "c" : False}) returns False
#  but 
#  Not(c).eval({"a" : True, "b" : False, "c" : False}) returns True
#
#  and False || True == True
# 
############################################################################################
class And():
    def __init__(self, l, r):
        self.lhs = l
        self.rhs = r

    def __str__(self):
        return "(" + str(self.lhs) + " && " + str(self.rhs) + ")"

    def __eq__(self, other):
        return self.type() == other.type() and \
                self.lhs == other.lhs and \
                self.rhs == other.rhs

    def vars(self):
        return self.lhs.vars() | self.rhs.vars()

    def type(self):
        return Node.AND

    def eval(self, env):
        raise EvalException("And")

############################################################################################
# An Or node represents the expression a || b
# We can construct one with Or(a,b)
# 
# You'll notice that this is very similar to the And node
############################################################################################
class Or():
    def __init__(self, l, r):
        self.lhs = l
        self.rhs = r

    def __str__(self):
        return "(" + str(self.lhs) + " || " + str(self.rhs) + ")"

    def __eq__(self, other):
        return self.type() == other.type() and \
                self.lhs == other.lhs and \
                self.rhs == other.rhs

    def vars(self):
        return self.lhs.vars() | self.rhs.vars()

    def type(self):
        return Node.OR

    def eval(self, env):
        raise EvalException("Or")

############################################################################################
# An Arrow node represents the expression a -> B
# We can construct one with Arrow(a,b)
# 
# You'll notice that this is very similar to the And node
############################################################################################
class Arrow():
    def __init__(self, l, r):
        self.lhs = l
        self.rhs = r

    def __str__(self):
        return "(" + str(self.lhs) + " -> " + str(self.rhs) + ")"

    def __eq__(self, other):
        return self.type() == other.type() and \
                self.lhs == other.lhs and \
                self.rhs == other.rhs

    def vars(self):
        return self.lhs.vars() | self.rhs.vars()

    def type(self):
        return Node.ARROW

    def eval(self, env):
        raise EvalException("Arrow")

############################################################################################
# A Not node represents the expression ~a
# We can construct one with Not(a)
# 
# This is different from the And node in that it only has 1 child the lhs
############################################################################################
class Not():
    def __init__(self, l):
        self.lhs = l

    def __str__(self):
        return "(~ " + str(self.lhs) + ")"

    def __eq__(self, other):
        return self.type() == other.type() and \
                self.lhs == other.lhs

    def vars(self):
        return self.lhs.vars()

    def type(self):
        return Node.NOT

    def eval(self, env):
        raise EvalException("Not")

############################################################################################
# A Lit node represents a literal value (T or F)
# We can construct one with true() or false()
# 
# Lit nodes don't have any children, but they do have a value (True or False)
############################################################################################
class Lit():
    def __init__(self, val):
        self.val = val

    def __str__(self):
        if self.val:
            return "T"
        else:
            return "F"

    def __eq__(self, other):
        return self.type() == other.type() and \
                self.val == other.val

    def vars(self):
        return set()

    def type(self):
        return Node.LIT

    def eval(self, env):
        raise EvalException("Lit")

# these are for convenience
# Don't call Lit(True) directly, just use true()
def true():
    return Lit(True)
def false():
    return Lit(False)

############################################################################################
# A Var node represents a variable
# We can construct one with Var("a")
# The string can be any string we want, but you should maksure it only consists of letter
# also, try to avoid T, F, true, True, False, false
# It won't break anything, but it will look confusing with printing the output.
# 
# Var nodes don't have any children, but they have a name
# to evaluate a Var we need to look it up in the environment.
############################################################################################
class Var:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.type() == other.type() and \
                self.name == other.name


    def vars(self):
        return {self.name}

    def type(self):
        return Node.VAR

    def eval(self, env):
        raise EvalException("Var")

############################################################################################
# Prints out a truth table for an expression
# The specifics of how this works aren't too important
# The idea is that we make every possible environment, 
# and then we evaulate the expression with each environment.
# 
# Since I don't know how many variables an expression might have,
# I need to construct the environment recursively.
############################################################################################
def truth_table(e):
    vs = sorted(list(e.vars()))
    print("%s | %s" % (" ".join(vs), str(e)))
    print("%s+-%s" % ("--"*len(vs), "-"*len(str(e))))
    rec_eval(e,vs,0,{})

def rec_eval(e, vs, i, env):
    if i < len(vs):
        for val in [True,False]:
            env[vs[i]] = val
            rec_eval(e,vs,i+1,env)
    else:
        print(" ".join([TorF(env[v]) for v in vs]), end=" ")
        print("| ", TorF(e.eval(env)))

def TorF(b):
    if b: return "T"
    else: return "F"

