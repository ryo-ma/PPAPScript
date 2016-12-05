import ply.lex as lex
import re

tokens = (
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'DECLARE',
    'PRINT',
    'NAME',
)


# Token rule by regex
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'


# Ignored characters
t_ignore = " \t"
t_ignore_COMMENT = r'\#.*'


# Regex and action code
def t_STRING(t):
    r"""\".*\""""
    t.value = str(t.value)[1:-1]
    return t


def t_NUMBER(t):
    r"""\d+"""
    t.value = int(t.value)
    return t


def t_DECLARE(t):
    r"""I_have_(an|a)"""
    return t


def t_PRINT(t):
    r"""Ah!"""
    return t


def t_NAME(t):
    r"""(?!PPAP)[a-zA-Z_][a-zA-Z0-9_]*"""
    pattern = re.compile(r'^(apple|pineapple|pen)+', re.IGNORECASE)
    if pattern.match(t.value):
        return t
    else:
        print("This variable name can't be used '%s'.\n "
              "Variable can use 'apple', 'pineapple', 'pen'." % t.value)
        t.lexer.skip(t)


# Count line number
def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count("\n")


# Token Parse Error
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(t)


# Build the lexer
lex.lex(debug=0)
