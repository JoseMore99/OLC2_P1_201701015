
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftmasmenosleftpordividmodulorightUmenosand cadena caracter com decimal divid dospunt entero id igual llaveder llaveiz mas mayorque menorque menos modulo not or parder pariz por puntycom resbool resbreak reschar rescontinue reselse resf64 resfalse resfn resi64 resif reslet resmut resprint resreturn resstruct restring restrue reswhile strINIT   :  INSTRUCCIONES INSTRUCCIONES    :  INSTRUCCIONES INSTRUCCIONINSTRUCCIONES    : INSTRUCCION INSTRUCCION :  PRINT  puntycom\n                | DECLARAR puntycom\n                | ASIGNAR puntycom\n                | INSTFUNC \n                | LLAMARFUNC puntycom\n                | INSTIF\n                | INSTWHILE\n                | INSTBREAK puntycom\n                | INSTCONTINUE puntycom\n                | INSTRETURN puntycom INSTBREAK : resbreak\n                | resbreak EXPRESIONINSTCONTINUE : rescontinueINSTRETURN : resreturn\n                |  resreturn EXPRESIONPRINT :  resprint not  pariz EXPRESION parderPRINT :  resprint not  pariz EXPRESION com LISTAEXP parderDECLARAR : reslet resmut id dospunt TIPOVAL igual EXPRESIONDECLARAR : reslet resmut id igual EXPRESIONDECLARAR : reslet id dospunt TIPOVAL igual EXPRESIONDECLARAR : reslet id igual EXPRESIONASIGNAR :  id igual EXPRESIONINSTIF : resif  EXPRESION  llaveiz BLOQUE llaveder INSTIF : resif  EXPRESION  llaveiz BLOQUE llaveder INSTELSEINSTELSE : reselse INSTIFINSTELSE : reselse llaveiz BLOQUE llavederINSTWHILE : reswhile  EXPRESION  llaveiz BLOQUE llaveder INSTFUNC : resfn id pariz parder llaveiz BLOQUE llavederINSTFUNC : resfn id pariz PARAMETROS parder llaveiz BLOQUE llavederINSTFUNC : resfn id pariz PARAMETROS parder menos mayorque TIPOVAL llaveiz BLOQUE llavederLLAMARFUNC : id pariz parderLLAMARFUNC : id pariz LISTAEXP parderBLOQUE : INSTRUCCIONESLISTAEXP : LISTAEXP com EXPRESION LISTAEXP : EXPRESION PARAMETROS : PARAMETROS com id dospunt TIPOVAL PARAMETROS : id dospunt TIPOVAL TIPOVAL : resi64\n            | resf64\n            | resbool\n            | reschar\n            | restring\n            | strEXPRESION : EXPRESION mas EXPRESION\n                  | EXPRESION menos EXPRESION\n                  | EXPRESION por EXPRESION\n                  | EXPRESION modulo EXPRESION\n                  | EXPRESION divid EXPRESIONEXPRESION : EXPRESION menorque EXPRESIONEXPRESION : EXPRESION mayorque EXPRESIONEXPRESION : EXPRESION menorque igual EXPRESIONEXPRESION : EXPRESION mayorque igual EXPRESIONEXPRESION : EXPRESION igual igual EXPRESIONEXPRESION : EXPRESION not igual EXPRESIONEXPRESION : EXPRESION and and EXPRESIONEXPRESION : EXPRESION or or EXPRESIONEXPRESION : not EXPRESIONEXPRESION : menos EXPRESION %prec UmenosEXPRESION : pariz EXPRESION parderEXPRESION    : enteroEXPRESION    : decimalEXPRESION    : cadenaEXPRESION    : caracterEXPRESION    : idEXPRESION    : restrue\n                    | resfalse '
    
_lr_action_items = {'resprint':([0,2,3,7,9,10,23,24,25,26,27,28,29,30,60,75,93,116,119,126,132,135,139,143,144,145,149,150,152,],[14,14,-3,-7,-9,-10,-2,-4,-5,-6,-8,-11,-12,-13,14,14,14,14,-26,-30,14,-27,-31,-28,14,-32,14,-29,-33,]),'reslet':([0,2,3,7,9,10,23,24,25,26,27,28,29,30,60,75,93,116,119,126,132,135,139,143,144,145,149,150,152,],[15,15,-3,-7,-9,-10,-2,-4,-5,-6,-8,-11,-12,-13,15,15,15,15,-26,-30,15,-27,-31,-28,15,-32,15,-29,-33,]),'id':([0,2,3,7,9,10,15,17,18,19,20,22,23,24,25,26,27,28,29,30,32,34,35,38,39,40,51,54,59,60,61,62,63,64,65,66,67,75,78,88,93,100,102,103,104,105,106,110,113,116,118,119,126,128,132,135,139,143,144,145,149,150,152,],[16,16,-3,-7,-9,-10,33,36,45,45,45,45,-2,-4,-5,-6,-8,-11,-12,-13,52,45,45,45,45,45,45,45,89,16,45,45,45,45,45,45,45,16,45,45,16,45,45,45,45,45,45,45,45,16,134,-26,-30,45,16,-27,-31,-28,16,-32,16,-29,-33,]),'resfn':([0,2,3,7,9,10,23,24,25,26,27,28,29,30,60,75,93,116,119,126,132,135,139,143,144,145,149,150,152,],[17,17,-3,-7,-9,-10,-2,-4,-5,-6,-8,-11,-12,-13,17,17,17,17,-26,-30,17,-27,-31,-28,17,-32,17,-29,-33,]),'resif':([0,2,3,7,9,10,23,24,25,26,27,28,29,30,60,75,93,116,119,126,132,135,136,139,143,144,145,149,150,152,],[18,18,-3,-7,-9,-10,-2,-4,-5,-6,-8,-11,-12,-13,18,18,18,18,-26,-30,18,-27,18,-31,-28,18,-32,18,-29,-33,]),'reswhile':([0,2,3,7,9,10,23,24,25,26,27,28,29,30,60,75,93,116,119,126,132,135,139,143,144,145,149,150,152,],[19,19,-3,-7,-9,-10,-2,-4,-5,-6,-8,-11,-12,-13,19,19,19,19,-26,-30,19,-27,-31,-28,19,-32,19,-29,-33,]),'resbreak':([0,2,3,7,9,10,23,24,25,26,27,28,29,30,60,75,93,116,119,126,132,135,139,143,144,145,149,150,152,],[20,20,-3,-7,-9,-10,-2,-4,-5,-6,-8,-11,-12,-13,20,20,20,20,-26,-30,20,-27,-31,-28,20,-32,20,-29,-33,]),'rescontinue':([0,2,3,7,9,10,23,24,25,26,27,28,29,30,60,75,93,116,119,126,132,135,139,143,144,145,149,150,152,],[21,21,-3,-7,-9,-10,-2,-4,-5,-6,-8,-11,-12,-13,21,21,21,21,-26,-30,21,-27,-31,-28,21,-32,21,-29,-33,]),'resreturn':([0,2,3,7,9,10,23,24,25,26,27,28,29,30,60,75,93,116,119,126,132,135,139,143,144,145,149,150,152,],[22,22,-3,-7,-9,-10,-2,-4,-5,-6,-8,-11,-12,-13,22,22,22,22,-26,-30,22,-27,-31,-28,22,-32,22,-29,-33,]),'$end':([1,2,3,7,9,10,23,24,25,26,27,28,29,30,119,126,135,139,143,145,150,152,],[0,-1,-3,-7,-9,-10,-2,-4,-5,-6,-8,-11,-12,-13,-26,-30,-27,-31,-28,-32,-29,-33,]),'llaveder':([3,7,9,10,23,24,25,26,27,28,29,30,92,93,108,119,126,131,135,139,140,143,145,148,150,151,152,],[-3,-7,-9,-10,-2,-4,-5,-6,-8,-11,-12,-13,119,-36,126,-26,-30,139,-27,-31,145,-28,-32,150,-29,152,-33,]),'puntycom':([4,5,6,8,11,12,13,20,21,22,41,42,43,44,45,46,47,49,50,55,56,72,73,86,87,94,95,96,97,98,99,101,107,109,112,120,121,122,123,124,125,129,137,138,],[24,25,26,27,28,29,30,-14,-16,-17,-63,-64,-65,-66,-67,-68,-69,-15,-18,-25,-34,-61,-60,-24,-35,-47,-48,-49,-50,-51,-52,-53,-62,-19,-22,-54,-55,-56,-57,-58,-59,-23,-20,-21,]),'not':([14,18,19,20,22,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,58,61,62,63,64,65,66,67,72,73,74,76,78,86,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,112,113,114,120,121,122,123,124,125,128,129,138,],[31,39,39,39,39,39,39,69,39,39,39,-63,-64,-65,-66,-67,-68,-69,69,69,69,39,39,69,69,39,39,39,39,39,39,39,-61,69,69,69,39,69,39,-47,-48,-49,-50,-51,69,39,69,39,39,39,39,39,-62,39,69,39,69,69,69,69,69,69,69,39,69,69,]),'resmut':([15,],[32,]),'igual':([16,33,37,41,42,43,44,45,46,47,48,49,50,52,55,58,66,67,68,69,72,73,74,76,79,80,81,82,83,84,85,86,94,95,96,97,98,99,101,107,111,112,114,120,121,122,123,124,125,129,138,],[34,54,68,-63,-64,-65,-66,-67,-68,-69,68,68,68,78,68,68,100,102,103,104,-61,68,68,68,113,-41,-42,-43,-44,-45,-46,68,-47,-48,-49,-50,-51,68,68,-62,128,68,68,68,68,68,68,68,68,68,68,]),'pariz':([16,18,19,20,22,31,34,35,36,38,39,40,51,54,61,62,63,64,65,66,67,78,88,100,102,103,104,105,106,110,113,128,],[35,40,40,40,40,51,40,40,59,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'menos':([18,19,20,22,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,58,61,62,63,64,65,66,67,72,73,74,76,78,86,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,112,113,114,117,120,121,122,123,124,125,128,129,138,],[38,38,38,38,38,38,62,38,38,38,-63,-64,-65,-66,-67,-68,-69,62,62,62,38,38,62,62,38,38,38,38,38,38,38,-61,62,62,62,38,62,38,-47,-48,-49,-50,-51,62,38,62,38,38,38,38,38,-62,38,62,38,62,133,62,62,62,62,62,62,38,62,62,]),'entero':([18,19,20,22,34,35,38,39,40,51,54,61,62,63,64,65,66,67,78,88,100,102,103,104,105,106,110,113,128,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'decimal':([18,19,20,22,34,35,38,39,40,51,54,61,62,63,64,65,66,67,78,88,100,102,103,104,105,106,110,113,128,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'cadena':([18,19,20,22,34,35,38,39,40,51,54,61,62,63,64,65,66,67,78,88,100,102,103,104,105,106,110,113,128,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'caracter':([18,19,20,22,34,35,38,39,40,51,54,61,62,63,64,65,66,67,78,88,100,102,103,104,105,106,110,113,128,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'restrue':([18,19,20,22,34,35,38,39,40,51,54,61,62,63,64,65,66,67,78,88,100,102,103,104,105,106,110,113,128,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'resfalse':([18,19,20,22,34,35,38,39,40,51,54,61,62,63,64,65,66,67,78,88,100,102,103,104,105,106,110,113,128,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'dospunt':([33,52,89,134,],[53,77,115,142,]),'parder':([35,41,42,43,44,45,46,47,57,58,59,72,73,74,76,80,81,82,83,84,85,91,94,95,96,97,98,99,101,107,114,120,121,122,123,124,125,127,130,147,],[56,-63,-64,-65,-66,-67,-68,-69,87,-38,90,-61,-60,107,109,-41,-42,-43,-44,-45,-46,117,-47,-48,-49,-50,-51,-52,-53,-62,-37,-54,-55,-56,-57,-58,-59,137,-40,-39,]),'llaveiz':([37,41,42,43,44,45,46,47,48,72,73,80,81,82,83,84,85,90,94,95,96,97,98,99,101,107,117,120,121,122,123,124,125,136,146,],[60,-63,-64,-65,-66,-67,-68,-69,75,-61,-60,-41,-42,-43,-44,-45,-46,116,-47,-48,-49,-50,-51,-52,-53,-62,132,-54,-55,-56,-57,-58,-59,144,149,]),'mas':([37,41,42,43,44,45,46,47,48,49,50,55,58,72,73,74,76,86,94,95,96,97,98,99,101,107,112,114,120,121,122,123,124,125,129,138,],[61,-63,-64,-65,-66,-67,-68,-69,61,61,61,61,61,-61,61,61,61,61,-47,-48,-49,-50,-51,61,61,-62,61,61,61,61,61,61,61,61,61,61,]),'por':([37,41,42,43,44,45,46,47,48,49,50,55,58,72,73,74,76,86,94,95,96,97,98,99,101,107,112,114,120,121,122,123,124,125,129,138,],[63,-63,-64,-65,-66,-67,-68,-69,63,63,63,63,63,-61,63,63,63,63,63,63,-49,-50,-51,63,63,-62,63,63,63,63,63,63,63,63,63,63,]),'modulo':([37,41,42,43,44,45,46,47,48,49,50,55,58,72,73,74,76,86,94,95,96,97,98,99,101,107,112,114,120,121,122,123,124,125,129,138,],[64,-63,-64,-65,-66,-67,-68,-69,64,64,64,64,64,-61,64,64,64,64,64,64,-49,-50,-51,64,64,-62,64,64,64,64,64,64,64,64,64,64,]),'divid':([37,41,42,43,44,45,46,47,48,49,50,55,58,72,73,74,76,86,94,95,96,97,98,99,101,107,112,114,120,121,122,123,124,125,129,138,],[65,-63,-64,-65,-66,-67,-68,-69,65,65,65,65,65,-61,65,65,65,65,65,65,-49,-50,-51,65,65,-62,65,65,65,65,65,65,65,65,65,65,]),'menorque':([37,41,42,43,44,45,46,47,48,49,50,55,58,72,73,74,76,86,94,95,96,97,98,99,101,107,112,114,120,121,122,123,124,125,129,138,],[66,-63,-64,-65,-66,-67,-68,-69,66,66,66,66,66,-61,66,66,66,66,-47,-48,-49,-50,-51,66,66,-62,66,66,66,66,66,66,66,66,66,66,]),'mayorque':([37,41,42,43,44,45,46,47,48,49,50,55,58,72,73,74,76,86,94,95,96,97,98,99,101,107,112,114,120,121,122,123,124,125,129,133,138,],[67,-63,-64,-65,-66,-67,-68,-69,67,67,67,67,67,-61,67,67,67,67,-47,-48,-49,-50,-51,67,67,-62,67,67,67,67,67,67,67,67,67,141,67,]),'and':([37,41,42,43,44,45,46,47,48,49,50,55,58,70,72,73,74,76,86,94,95,96,97,98,99,101,107,112,114,120,121,122,123,124,125,129,138,],[70,-63,-64,-65,-66,-67,-68,-69,70,70,70,70,70,105,-61,70,70,70,70,-47,-48,-49,-50,-51,70,70,-62,70,70,70,70,70,70,70,70,70,70,]),'or':([37,41,42,43,44,45,46,47,48,49,50,55,58,71,72,73,74,76,86,94,95,96,97,98,99,101,107,112,114,120,121,122,123,124,125,129,138,],[71,-63,-64,-65,-66,-67,-68,-69,71,71,71,71,71,106,-61,71,71,71,71,-47,-48,-49,-50,-51,71,71,-62,71,71,71,71,71,71,71,71,71,71,]),'com':([41,42,43,44,45,46,47,57,58,72,73,76,80,81,82,83,84,85,91,94,95,96,97,98,99,101,107,114,120,121,122,123,124,125,127,130,147,],[-63,-64,-65,-66,-67,-68,-69,88,-38,-61,-60,110,-41,-42,-43,-44,-45,-46,118,-47,-48,-49,-50,-51,-52,-53,-62,-37,-54,-55,-56,-57,-58,-59,88,-40,-39,]),'resi64':([53,77,115,141,142,],[80,80,80,80,80,]),'resf64':([53,77,115,141,142,],[81,81,81,81,81,]),'resbool':([53,77,115,141,142,],[82,82,82,82,82,]),'reschar':([53,77,115,141,142,],[83,83,83,83,83,]),'restring':([53,77,115,141,142,],[84,84,84,84,84,]),'str':([53,77,115,141,142,],[85,85,85,85,85,]),'reselse':([119,],[136,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INIT':([0,],[1,]),'INSTRUCCIONES':([0,60,75,116,132,144,149,],[2,93,93,93,93,93,93,]),'INSTRUCCION':([0,2,60,75,93,116,132,144,149,],[3,23,3,3,23,3,3,3,3,]),'PRINT':([0,2,60,75,93,116,132,144,149,],[4,4,4,4,4,4,4,4,4,]),'DECLARAR':([0,2,60,75,93,116,132,144,149,],[5,5,5,5,5,5,5,5,5,]),'ASIGNAR':([0,2,60,75,93,116,132,144,149,],[6,6,6,6,6,6,6,6,6,]),'INSTFUNC':([0,2,60,75,93,116,132,144,149,],[7,7,7,7,7,7,7,7,7,]),'LLAMARFUNC':([0,2,60,75,93,116,132,144,149,],[8,8,8,8,8,8,8,8,8,]),'INSTIF':([0,2,60,75,93,116,132,136,144,149,],[9,9,9,9,9,9,9,143,9,9,]),'INSTWHILE':([0,2,60,75,93,116,132,144,149,],[10,10,10,10,10,10,10,10,10,]),'INSTBREAK':([0,2,60,75,93,116,132,144,149,],[11,11,11,11,11,11,11,11,11,]),'INSTCONTINUE':([0,2,60,75,93,116,132,144,149,],[12,12,12,12,12,12,12,12,12,]),'INSTRETURN':([0,2,60,75,93,116,132,144,149,],[13,13,13,13,13,13,13,13,13,]),'EXPRESION':([18,19,20,22,34,35,38,39,40,51,54,61,62,63,64,65,66,67,78,88,100,102,103,104,105,106,110,113,128,],[37,48,49,50,55,58,72,73,74,76,86,94,95,96,97,98,99,101,112,114,120,121,122,123,124,125,58,129,138,]),'LISTAEXP':([35,110,],[57,127,]),'TIPOVAL':([53,77,115,141,142,],[79,111,130,146,147,]),'PARAMETROS':([59,],[91,]),'BLOQUE':([60,75,116,132,144,149,],[92,108,131,140,148,151,]),'INSTELSE':([119,],[135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INIT","S'",1,None,None,None),
  ('INIT -> INSTRUCCIONES','INIT',1,'p_inicial','gramatica.py',169),
  ('INSTRUCCIONES -> INSTRUCCIONES INSTRUCCION','INSTRUCCIONES',2,'p_instrucciones_lista_conjunto','gramatica.py',173),
  ('INSTRUCCIONES -> INSTRUCCION','INSTRUCCIONES',1,'p_instrucciones_lista_unica','gramatica.py',180),
  ('INSTRUCCION -> PRINT puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',187),
  ('INSTRUCCION -> DECLARAR puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',188),
  ('INSTRUCCION -> ASIGNAR puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',189),
  ('INSTRUCCION -> INSTFUNC','INSTRUCCION',1,'p_instrucciones_evaluar','gramatica.py',190),
  ('INSTRUCCION -> LLAMARFUNC puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',191),
  ('INSTRUCCION -> INSTIF','INSTRUCCION',1,'p_instrucciones_evaluar','gramatica.py',192),
  ('INSTRUCCION -> INSTWHILE','INSTRUCCION',1,'p_instrucciones_evaluar','gramatica.py',193),
  ('INSTRUCCION -> INSTBREAK puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',194),
  ('INSTRUCCION -> INSTCONTINUE puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',195),
  ('INSTRUCCION -> INSTRETURN puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',196),
  ('INSTBREAK -> resbreak','INSTBREAK',1,'p_break','gramatica.py',200),
  ('INSTBREAK -> resbreak EXPRESION','INSTBREAK',2,'p_break','gramatica.py',201),
  ('INSTCONTINUE -> rescontinue','INSTCONTINUE',1,'p_continue','gramatica.py',208),
  ('INSTRETURN -> resreturn','INSTRETURN',1,'p_return','gramatica.py',212),
  ('INSTRETURN -> resreturn EXPRESION','INSTRETURN',2,'p_return','gramatica.py',213),
  ('PRINT -> resprint not pariz EXPRESION parder','PRINT',5,'p_impresion','gramatica.py',220),
  ('PRINT -> resprint not pariz EXPRESION com LISTAEXP parder','PRINT',7,'p_impresion_lista','gramatica.py',224),
  ('DECLARAR -> reslet resmut id dospunt TIPOVAL igual EXPRESION','DECLARAR',7,'p_declarar_mut_tipo','gramatica.py',228),
  ('DECLARAR -> reslet resmut id igual EXPRESION','DECLARAR',5,'p_declarar_mut','gramatica.py',232),
  ('DECLARAR -> reslet id dospunt TIPOVAL igual EXPRESION','DECLARAR',6,'p_declarar_tipo','gramatica.py',236),
  ('DECLARAR -> reslet id igual EXPRESION','DECLARAR',4,'p_declarar','gramatica.py',240),
  ('ASIGNAR -> id igual EXPRESION','ASIGNAR',3,'p_asignar','gramatica.py',244),
  ('INSTIF -> resif EXPRESION llaveiz BLOQUE llaveder','INSTIF',5,'p_if','gramatica.py',248),
  ('INSTIF -> resif EXPRESION llaveiz BLOQUE llaveder INSTELSE','INSTIF',6,'p_if_else','gramatica.py',252),
  ('INSTELSE -> reselse INSTIF','INSTELSE',2,'p_elseif','gramatica.py',256),
  ('INSTELSE -> reselse llaveiz BLOQUE llaveder','INSTELSE',4,'p_else','gramatica.py',260),
  ('INSTWHILE -> reswhile EXPRESION llaveiz BLOQUE llaveder','INSTWHILE',5,'p_while','gramatica.py',264),
  ('INSTFUNC -> resfn id pariz parder llaveiz BLOQUE llaveder','INSTFUNC',7,'p_funcion','gramatica.py',268),
  ('INSTFUNC -> resfn id pariz PARAMETROS parder llaveiz BLOQUE llaveder','INSTFUNC',8,'p_funcion_parametros','gramatica.py',276),
  ('INSTFUNC -> resfn id pariz PARAMETROS parder menos mayorque TIPOVAL llaveiz BLOQUE llaveder','INSTFUNC',11,'p_funcion_tipo_parametros','gramatica.py',280),
  ('LLAMARFUNC -> id pariz parder','LLAMARFUNC',3,'p_llamar_f','gramatica.py',284),
  ('LLAMARFUNC -> id pariz LISTAEXP parder','LLAMARFUNC',4,'p_llamar_f_parametros','gramatica.py',288),
  ('BLOQUE -> INSTRUCCIONES','BLOQUE',1,'p_funcion_tipo','gramatica.py',292),
  ('LISTAEXP -> LISTAEXP com EXPRESION','LISTAEXP',3,'p_lista_expre_conjunto','gramatica.py',296),
  ('LISTAEXP -> EXPRESION','LISTAEXP',1,'p_lista_expre','gramatica.py',302),
  ('PARAMETROS -> PARAMETROS com id dospunt TIPOVAL','PARAMETROS',5,'p_lista_para_conjunto','gramatica.py',309),
  ('PARAMETROS -> id dospunt TIPOVAL','PARAMETROS',3,'p_lista_para','gramatica.py',315),
  ('TIPOVAL -> resi64','TIPOVAL',1,'p_tipoval','gramatica.py',322),
  ('TIPOVAL -> resf64','TIPOVAL',1,'p_tipoval','gramatica.py',323),
  ('TIPOVAL -> resbool','TIPOVAL',1,'p_tipoval','gramatica.py',324),
  ('TIPOVAL -> reschar','TIPOVAL',1,'p_tipoval','gramatica.py',325),
  ('TIPOVAL -> restring','TIPOVAL',1,'p_tipoval','gramatica.py',326),
  ('TIPOVAL -> str','TIPOVAL',1,'p_tipoval','gramatica.py',327),
  ('EXPRESION -> EXPRESION mas EXPRESION','EXPRESION',3,'p_expresion_binaria','gramatica.py',338),
  ('EXPRESION -> EXPRESION menos EXPRESION','EXPRESION',3,'p_expresion_binaria','gramatica.py',339),
  ('EXPRESION -> EXPRESION por EXPRESION','EXPRESION',3,'p_expresion_binaria','gramatica.py',340),
  ('EXPRESION -> EXPRESION modulo EXPRESION','EXPRESION',3,'p_expresion_binaria','gramatica.py',341),
  ('EXPRESION -> EXPRESION divid EXPRESION','EXPRESION',3,'p_expresion_binaria','gramatica.py',342),
  ('EXPRESION -> EXPRESION menorque EXPRESION','EXPRESION',3,'p_expresion_binaria_menor','gramatica.py',346),
  ('EXPRESION -> EXPRESION mayorque EXPRESION','EXPRESION',3,'p_expresion_binaria_mayor','gramatica.py',350),
  ('EXPRESION -> EXPRESION menorque igual EXPRESION','EXPRESION',4,'p_expresion_binaria_menor_igual','gramatica.py',354),
  ('EXPRESION -> EXPRESION mayorque igual EXPRESION','EXPRESION',4,'p_expresion_binaria_mayor_igual','gramatica.py',358),
  ('EXPRESION -> EXPRESION igual igual EXPRESION','EXPRESION',4,'p_expresion_binaria_igual','gramatica.py',362),
  ('EXPRESION -> EXPRESION not igual EXPRESION','EXPRESION',4,'p_expresion_binaria_no_igual','gramatica.py',366),
  ('EXPRESION -> EXPRESION and and EXPRESION','EXPRESION',4,'p_expresion_binaria_and','gramatica.py',370),
  ('EXPRESION -> EXPRESION or or EXPRESION','EXPRESION',4,'p_expresion_binaria_or','gramatica.py',374),
  ('EXPRESION -> not EXPRESION','EXPRESION',2,'p_expresion_unaria_not','gramatica.py',378),
  ('EXPRESION -> menos EXPRESION','EXPRESION',2,'p_expresion_unaria','gramatica.py',382),
  ('EXPRESION -> pariz EXPRESION parder','EXPRESION',3,'p_expresion_agrupacion','gramatica.py',386),
  ('EXPRESION -> entero','EXPRESION',1,'p_expresion_entero','gramatica.py',390),
  ('EXPRESION -> decimal','EXPRESION',1,'p_expresion_decimal','gramatica.py',394),
  ('EXPRESION -> cadena','EXPRESION',1,'p_expresion_cadena','gramatica.py',398),
  ('EXPRESION -> caracter','EXPRESION',1,'p_expresion_caracter','gramatica.py',402),
  ('EXPRESION -> id','EXPRESION',1,'p_expresion_id','gramatica.py',406),
  ('EXPRESION -> restrue','EXPRESION',1,'p_expresion_boolean','gramatica.py',410),
  ('EXPRESION -> resfalse','EXPRESION',1,'p_expresion_boolean','gramatica.py',411),
]
