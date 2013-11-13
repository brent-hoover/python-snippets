# define token names, and a regular expression per each token
tokens = 'OPEN_PAREN', 'CLOS_PAREN', 'OTHR_CHARS'
t_OPEN_PAREN = r'\('
t_CLOS_PAREN = r'\)'
t_OTHR_CHARS = r'[^()]+'          # RE meaning: one or more non-parentheses
def t_error(t): t.skip(1)
# make the lexer (AKA tokenizer)
import lex
lexer = lex.lex(optimize=1)
# define syntax action-functions, with syntax rules in docstrings
def p_balanced(p):
    ''' balanced : balanced OPEN_PAREN balanced CLOS_PAREN balanced
                 | OTHR_CHARS
                 | '''
    if len(p) == 1:
        p[0] = ''
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]+p[2]+p[3]+p[4]+p[5]
def p_error(p): pass
# make the parser (AKA scanner)
import yacc
parser = yacc.yacc()
def has_balanced_parentheses(s):
    if not s: return True
    result = parser.parse(s, lexer=lexer)
    return s == result
