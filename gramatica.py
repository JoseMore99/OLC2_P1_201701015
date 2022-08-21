
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
    'string': 'restring',
    'struct': 'resstruct',
    'fn': 'resfn',
    'if': 'resif',
    'else': 'reselse',
    'println' : 'resprint',
    'while' : 'reswhile',
    'break' : 'resbreak',
    'continue' : 'rescontinue',
    'return' : 'resreturn'
}


tokens  = [
    'str',
    'pariz',
    'parder',
    'llaveiz',
    'llaveder',
    'mas',
    'menos',
    'por',
    'divid',
    'igual',
    'mayorque',
    'menorque',
    'modulo',
    'decimal',
    'cadena',
    'entero',
    'caracter',
    'id',
    'puntycom',
    'com',
    'dospunt',
    'not',
    'and',
    'or'
]+ list(reserved.values())

t_str       = r'&str'
t_pariz     = r'\('
t_parder    = r'\)'
t_llaveiz     = r'\{'
t_llaveder    = r'\}'
t_mas       = r'\+'
t_menos     = r'-'
t_por       = r'\*'
t_divid     = r'/'
t_puntycom  = r';'
t_com       = r','
t_dospunt   = r':'
t_modulo    = r'%'
t_not       = r'!'
t_igual     = r'='
t_mayorque  = r'>'
t_menorque  = r'<'
t_and       = r'&'
t_or        = r'\|'

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
    r'//.*\n'
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


import re
from expresion.TipoR import TipoR
from expresion.relaciones import relaciones
from expresion.variable import variable
from instrucciones.Break import Break
from instrucciones.Continue import Continue
from instrucciones.If import If
from instrucciones.Return import Return
from instrucciones.While import While
from instrucciones.asignar import asignar
from instrucciones.bloque import bloque
from instrucciones.declarar import declarar
from instrucciones.funcion import funcion
from expresion.aritmetica import aritmetica
from expresion.Tipo import Tipo
from expresion.nativo import nativo
from instrucciones.Print import Print
from instrucciones.llamarfunc import llamarfunc

import ply.lex as lex
lexer = lex.lex()


##########################################################################################
#######################        ANALISIS SINTACTICO           #############################
##########################################################################################



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
    if (t[2] != ""):
       t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_lista_unica(t):
    '''INSTRUCCIONES    : INSTRUCCION '''
    if (t[1] != ""):
       t[0]=[t[1]]
    else:
        t[0]=[]
        
def p_instrucciones_evaluar(t):
    '''INSTRUCCION :  PRINT  puntycom
                | DECLARAR puntycom
                | ASIGNAR puntycom
                | INSTFUNC 
                | LLAMARFUNC puntycom
                | INSTIF
                | INSTWHILE
                | INSTBREAK puntycom
                | INSTCONTINUE puntycom
                | INSTRETURN puntycom '''
    t[0]=t[1]

def p_break(t):
    '''INSTBREAK : resbreak
                | resbreak EXPRESION'''
    if(len(t)==2):
        t[0]=Break(t.lineno(1), t.lexpos(1))
    else:
        t[0]=Break(t.lineno(1), t.lexpos(1),t[1])

def p_continue(t):
    '''INSTCONTINUE : rescontinue'''
    t[0]=Continue(t.lineno(1), t.lexpos(1))

def p_return(t):
    '''INSTRETURN : resreturn
                |  resreturn EXPRESION'''
    if(len(t)==2):
        t[0]=Return(t.lineno(1), t.lexpos(1))
    else:
        t[0]=Return(t.lineno(1), t.lexpos(1),t[2])

def p_impresion(t):
    '''PRINT :  resprint not  pariz EXPRESION parder'''
    t[0]=Print(t.lineno(1), t.lexpos(1),t[4],[])

def p_impresion_lista(t):
    '''PRINT :  resprint not  pariz EXPRESION com LISTAEXP parder'''
    t[0]=Print(t.lineno(1), t.lexpos(1),t[4],t[6])

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
    
def p_asignar(t):
    '''ASIGNAR :  id igual EXPRESION'''
    t[0]= asignar(t.lineno(1), t.lexpos(1),t[1],t[3])

def p_if(t):
    '''INSTIF : resif  EXPRESION  llaveiz BLOQUE llaveder '''
    t[0]= If(t.lineno(1), t.lexpos(1),t[2],t[4],None)

def p_if_else(t):
    '''INSTIF : resif  EXPRESION  llaveiz BLOQUE llaveder INSTELSE'''
    t[0]= If(t.lineno(1), t.lexpos(1),t[2],t[4],t[6])
    
def p_elseif(t):
    '''INSTELSE : reselse INSTIF'''
    t[0]=t[2]

def p_else(t):
    '''INSTELSE : reselse llaveiz BLOQUE llaveder'''
    t[0]=t[3]

def p_while(t):
    '''INSTWHILE : reswhile  EXPRESION  llaveiz BLOQUE llaveder '''
    t[0]= While(t.lineno(1), t.lexpos(1),t[2],t[4])

def p_funcion(t):
    '''INSTFUNC : resfn id pariz parder llaveiz BLOQUE llaveder'''
    t[0]= funcion(t.lineno(1), t.lexpos(1),t[2],None,t[6],[])

def p_funcion_tipo(t):
    '''INSTFUNC : resfn id pariz parder menos mayorque TIPOVAL llaveiz BLOQUE llaveder'''
    t[0]= funcion(t.lineno(1), t.lexpos(1),t[2],t[7],t[9],[])

def p_funcion_parametros(t):
    '''INSTFUNC : resfn id pariz PARAMETROS parder llaveiz BLOQUE llaveder'''
    t[0]= funcion(t.lineno(1), t.lexpos(1),t[2],None,t[7],t[4])

def p_funcion_tipo_parametros(t):
    '''INSTFUNC : resfn id pariz PARAMETROS parder menos mayorque TIPOVAL llaveiz BLOQUE llaveder'''
    t[0]= funcion(t.lineno(1), t.lexpos(1),t[2],t[8],t[10],t[4])

def p_llamar_f(t):
    '''LLAMARFUNC : id pariz parder'''
    t[0]=llamarfunc(t.lineno(1), t.lexpos(1),t[1],[])

def p_llamar_f_parametros(t):
    '''LLAMARFUNC : id pariz LISTAEXP parder'''
    t[0]=llamarfunc(t.lineno(1), t.lexpos(1),t[1],t[3])

def p_funcion_tipo(t):
    '''BLOQUE : INSTRUCCIONES'''
    t[0]= bloque(t.lineno(1), t.lexpos(1),t[1])

def p_lista_expre_conjunto(t):
    '''LISTAEXP : LISTAEXP com EXPRESION '''
    if (t[3] != ""):
       t[1].append(t[3])
    t[0] = t[1]
    
def p_lista_expre(t):
    '''LISTAEXP : EXPRESION '''
    if (t[1] != ""):
       t[0]=[t[1]]
    else:
        t[0]=[]

def p_lista_para_conjunto(t):
    '''PARAMETROS : PARAMETROS com id dospunt TIPOVAL '''
    if (t[3] != ""):
       t[1].append(declarar(t.lineno(1), t.lexpos(1),t[3],t[5],None,True))
    t[0] = t[1]
    
def p_lista_para(t):
    '''PARAMETROS : id dospunt TIPOVAL '''
    if (t[1] != ""):
       t[0]=[declarar(t.lineno(1), t.lexpos(1),t[1],t[3],None,True)]
    else:
        t[0]=[]

def p_tipoval(t):
    '''TIPOVAL : resi64
            | resf64
            | resbool
            | reschar
            | restring
            | str'''
    #print(t[1])
    if (str(t[1])=="i64"):t[0]=Tipo.ENTERO
    elif (str(t[1])=="f64"):t[0]=Tipo.DECIMAL
    elif (str(t[1])=="bool"):t[0]=Tipo.BOOL
    elif (str(t[1])=="char"):t[0]=Tipo.CHAR
    elif (str(t[1])=="char"):t[0]=Tipo.CHAR
    elif (str(t[1])=="string"):t[0]=Tipo.STRING
    elif (str(t[1])=="&str"):t[0]=Tipo.STRING

def p_expresion_binaria(t):
    '''EXPRESION : EXPRESION mas EXPRESION
                  | EXPRESION menos EXPRESION
                  | EXPRESION por EXPRESION
                  | EXPRESION modulo EXPRESION
                  | EXPRESION divid EXPRESION'''
    t[0]= aritmetica(t.lineno(1), t.lexpos(1),t[1],t[3],t[2])

def p_expresion_binaria_menor(t):
    '''EXPRESION : EXPRESION menorque EXPRESION'''
    t[0]= relaciones(t.lineno(1), t.lexpos(1),t[1],t[3],TipoR.MENORQUE)

def p_expresion_binaria_mayor(t):
    '''EXPRESION : EXPRESION mayorque EXPRESION'''
    t[0]= relaciones(t.lineno(1), t.lexpos(1),t[1],t[3],TipoR.MAYORQUE)

def p_expresion_binaria_menor_igual(t):
    '''EXPRESION : EXPRESION menorque igual EXPRESION'''
    t[0]= relaciones(t.lineno(1), t.lexpos(1),t[1],t[4],TipoR.MENORIGUAL)

def p_expresion_binaria_mayor_igual(t):
    '''EXPRESION : EXPRESION mayorque igual EXPRESION'''
    t[0]= relaciones(t.lineno(1), t.lexpos(1),t[1],t[4],TipoR.MAYORIGUAL)

def p_expresion_binaria_igual(t):
    '''EXPRESION : EXPRESION igual igual EXPRESION'''
    t[0]= relaciones(t.lineno(1), t.lexpos(1),t[1],t[4],TipoR.IGUAL)
    
def p_expresion_binaria_no_igual(t):
    '''EXPRESION : EXPRESION not igual EXPRESION'''
    t[0]= relaciones(t.lineno(1), t.lexpos(1),t[1],t[4],TipoR.DIFERENTE)

def p_expresion_binaria_and(t):
    '''EXPRESION : EXPRESION and and EXPRESION'''
    t[0]= relaciones(t.lineno(1), t.lexpos(1),t[1],t[4],TipoR.AND)

def p_expresion_binaria_or(t):
    '''EXPRESION : EXPRESION or or EXPRESION'''
    t[0]= relaciones(t.lineno(1), t.lexpos(1),t[1],t[4],TipoR.OR)

def p_expresion_unaria_not(t):
    '''EXPRESION : not EXPRESION'''
    t[0]= relaciones(t.lineno(1), t.lexpos(1),t[2],t[2],TipoR.NOT)

def p_expresion_unaria(t):
    'EXPRESION : menos EXPRESION %prec Umenos'
    t[0]= aritmetica(t.lineno(1), t.lexpos(1),nativo(t.lineno(1), t.lexpos(1),Tipo.ENTERO,"0"),t[2],t[1])

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


