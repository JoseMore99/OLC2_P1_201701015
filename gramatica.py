
##########################################################################################
########################         ANALISIS LEXICO            ##############################
##########################################################################################

tokens  = (
    'pariz',
    'parder',
    'mas',
    'menos',
    'por',
    'divid',
    'decimal',
    'entero',
    'puntycom'
)

t_pariz     = r'\('
t_parder    = r'\)'
t_mas       = r'\+'
t_menos     = r'-'
t_por       = r'\*'
t_divid     = r'/'
t_puntycom  = r';'

def t_decimal(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()


##########################################################################################
#######################        ANALISIS SINTACTICO           #############################
##########################################################################################

precedence = (
    ('left','mas','menos'),
    ('left','por','divid'),
    ('right','Umenos'),
    )

def p_instrucciones_lista(t):
    '''INSTRUCCIONES    : INSTRUCCION INSTRUCCIONES
                        | INSTRUCCION '''

def p_instrucciones_evaluar(t):
    'INSTRUCCION :  EXPRESION  puntycom'
    print('El valor de la expresión es: ' + str(t[1]))

def p_expresion_binaria(t):
    '''EXPRESION : EXPRESION mas EXPRESION
                  | EXPRESION menos EXPRESION
                  | EXPRESION por EXPRESION
                  | EXPRESION divid EXPRESION'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    'EXPRESION : menos EXPRESION %prec Umenos'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'EXPRESION : pariz EXPRESION parder'
    t[0] = t[2]

def p_expresion_number(t):
    '''EXPRESION    : entero
                    | decimal'''
    t[0] = t[1]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


