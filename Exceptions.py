
class ParseException(Exception):
    def __init__(self, line, expected, got):
        self.line = line
        self.expected = expected
        self.got = got
    def __str__(self):
        return "Error at %d: expected %s, but got %s" % (self.line, self.expected, self.got)

class LexException(Exception):
    def __init__(self, line, got):
        self.line = line
        self.got = got
    def __str__(self):
        return "Error at %d: invalid symbol %c" % (self.line, self.got)

class EvalException(Exception):
    def __init__(self, node):
        self.node = node
    def __str__(self):
        return "Error: eval not implemented for " + self.node

