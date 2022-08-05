
##########################################################################################
########################         ANALISIS LEXICO            ##############################
##########################################################################################

reserved = {
    'true': 'restrue',
    'false': 'resfalse',
    'let': 'reslet',
    'mut': 'resmut',
    'i64': 'resi64',#TIPO ENTERO
    'f64': 'resf64',#TIPO FLOTANTE
    'bool': 'resbool',
    'char': 'reschar',
    'String': 'resString',
    '&str': 'resStr',#REVISAR MAS ADELANTEEE
    'struct': 'resstruct',
    'println' : 'resprint',
}


tokens  = [
    'pariz',
    'parder',
    'mas',
    'menos',
    'por',
    'divid',
    'igual',
    'modulo',
    'decimal',
    'cadena',
    'entero',
    'caracter',
    'id',
    'puntycom',
    'dospunt',
    'not'
]+ list(reserved.values())

t_pariz     = r'\('
t_parder    = r'\)'
t_mas       = r'\+'
t_menos     = r'-'
t_por       = r'\*'
t_divid     = r'/'
t_puntycom  = r';'
t_dospunt   = r':'
t_modulo    = r'%'
t_not       = r'!'
t_igual     = r'='
def t_id(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'id')
    t.value = t.value.lower()
    return t


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

def t_cadena(t):
    r'(\"([^"\\]|(\\n)|(\\\\)|(\\\")|(\\t)|(\\\'))*\")'
    t.value = t.value[1:-1] 
    t.value = str(t.value).replace('\\n', '\n').replace('\\\\', '\\').replace('\\\"', '\"').replace('\\t', '\t').replace('\\\'', '\'')
    return t

def t_caracter(t):
    r'(\'([^\'\\]|(\\n)|(\\\\)|(\\\")|(\\t)|(\\\'))\')'
    t.value = t.value[1:-1]
    t.value = str(t.value).replace('\\n', '\n').replace('\\\\', '\\').replace('\\\"', '\"').replace('\\t', '\t').replace('\\\'', '\'')
    return t


def t_comentariosimple(t):
    r'\\.*\n'
    t.lexer.lineno += 1


t_ignore = " \t"

def getColumn(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

from expresion.variable import variable
from instrucciones.declarar import declarar
import ply.lex as lex
lexer = lex.lex()


##########################################################################################
#######################        ANALISIS SINTACTICO           #############################
##########################################################################################

from expresion.aritmetica import aritmetica
from expresion.Tipo import Tipo
from expresion.nativo import nativo
from instrucciones.Print import Print

precedence = (
    ('left','mas','menos'),
    ('left','por','divid','modulo'),
    ('right','Umenos'),
    )

def p_inicial(t):
    '''INIT   :  INSTRUCCIONES '''
    t[0]=t[1]

def p_instrucciones_lista_conjunto(t):
    '''INSTRUCCIONES    :  INSTRUCCIONES INSTRUCCION'''
    if t[2] != "":
       t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_lista_unica(t):
    '''INSTRUCCIONES    : INSTRUCCION '''
    if t[1] != "":
       t[0]=[t[1]]
    else:
        t[0]=[]
        
def p_instrucciones_evaluar(t):
    '''INSTRUCCION :  PRINT  puntycom
                | DECLARAR puntycom'''
    t[0]=t[1]

def p_impresion(t):
    '''PRINT :  resprint not  pariz EXPRESION parder'''
    t[0]=Print(t.lineno(1), t.lexpos(1),t[4])

def p_declarar_mut_tipo(t):
    '''DECLARAR : reslet resmut id dospunt TIPOVAL igual EXPRESION'''
    t[0]= declarar(t.lineno(1), t.lexpos(1),t[3],t[5],t[7],True)

def p_declarar_mut(t):
    '''DECLARAR : reslet resmut id igual EXPRESION'''
    t[0]= declarar(t.lineno(1), t.lexpos(1),t[3],None,t[5],True)

def p_declarar_tipo(t):
    '''DECLARAR : reslet id dospunt TIPOVAL igual EXPRESION'''
    t[0]= declarar(t.lineno(1), t.lexpos(1),t[2],t[4],t[6],False)

def p_declarar(t):
    '''DECLARAR : reslet id igual EXPRESION'''
    t[0]= declarar(t.lineno(1), t.lexpos(1),t[2],None,t[4],False)

def p_tipoval(t):
    '''TIPOVAL : resi64
            | resf64
            | resbool
            | reschar
            | resString
            | resStr'''
    if (str(t[1])=="i64"):t[0]=Tipo.ENTERO
    elif (str(t[1])=="f64"):t[0]=Tipo.DECIMAL
    elif (str(t[1])=="bool"):t[0]=Tipo.BOOL
    elif (str(t[1])=="char"):t[0]=Tipo.CHAR
    elif (str(t[1])=="char"):t[0]=Tipo.CHAR
    elif (str(t[1])=="String"):t[0]=Tipo.STRING
    elif (str(t[1])=="&str"):t[0]=Tipo.STRING

def p_expresion_binaria(t):
    '''EXPRESION : EXPRESION mas EXPRESION
                  | EXPRESION menos EXPRESION
                  | EXPRESION por EXPRESION
                  | EXPRESION modulo EXPRESION
                  | EXPRESION divid EXPRESION'''
    t[0]= aritmetica(t.lineno(1), t.lexpos(1),t[1],t[3],t[2])

def p_expresion_unaria(t):
    'EXPRESION : menos EXPRESION %prec Umenos'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'EXPRESION : pariz EXPRESION parder'
    t[0] = t[2]

def p_expresion_entero(t):
    'EXPRESION    : entero'
    t[0] = nativo(t.lineno(1), t.lexpos(1),Tipo.ENTERO,t[1])

def p_expresion_decimal(t):
    'EXPRESION    : decimal'
    t[0] = nativo(t.lineno(1), t.lexpos(1),Tipo.DECIMAL,t[1])

def p_expresion_cadena(t):
    'EXPRESION    : cadena'
    t[0] = nativo(t.lineno(1), t.lexpos(1),Tipo.STRING,t[1])

def p_expresion_caracter(t):
    'EXPRESION    : caracter'
    t[0] = nativo(t.lineno(1), t.lexpos(1),Tipo.CHAR,t[1])

def p_expresion_id(t):
    'EXPRESION    : id'
    t[0] = variable(t.lineno(1),t.lexpos(1),t[1])

def p_expresion_boolean(t):
    '''EXPRESION    : restrue
                    | resfalse '''
    t[0] = nativo(t.lineno(1), t.lexpos(1),Tipo.BOOL,t[1])

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


