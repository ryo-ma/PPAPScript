import ply.yacc as yacc

# Import tokens
from ppaplex import tokens


# Precedence rules for the arithmetic operators
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# Variable field
names = {}


def p_statement_assign(p):
    """statement : DECLARE NAME EQUALS expression"""
    names[p[2]] = p[4]


def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    """expression : MINUS expression %prec UMINUS"""
    p[0] = -p[2]


def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]


def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]


def p_expression_string(p):
    """expression : STRING"""
    p[0] = p[1]


def p_expression_name(p):
    """expression : NAME"""
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_statement_expr(p):
    """statement : expression"""
    p[0] = p[1]


def p_statement_print_expr(p):
    """statement : PRINT expression"""
    print(p[2])


def p_error(p):
    if p is not None:
        print("Syntax error at '%s'" % p.value)


parser = yacc.yacc()

# Started flag is true by "PPAP" command
has_started = False


def parse(data, debug=0):
    if data == "PPAP":
        global has_started
        has_started = True
        print("Welcome to PPAPScript!")
        return

    if has_started:
        return yacc.parse(data, debug=debug)
    else:
        print('Be sure to enter "PPAP" after you start the PPAPScript.'
              'Otherwise PPAPScript will not run.')
        return
