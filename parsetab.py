
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftmasmenosleftpordividmodulorightUmenosand apunta barra cadena caracter com corcheteder corcheteiz decimal defaul divid dospunt entero id igual llaveder llaveiz mas mayorque menorque menos modulo not or parder pariz por puntdos puntycom resbool resbreak reschar rescontinue reselse resf64 resfalse resfn resfor resi64 resif resin reslet resloop resmatch resmut resnew resprint resreturn resstruct restring restrue resvec reswhile strINIT   :  INSTRUCCIONES INSTRUCCIONES    :  INSTRUCCIONES INSTRUCCIONINSTRUCCIONES    : INSTRUCCION INSTRUCCION :  PRINT  puntycom\n                | DECLARAR puntycom\n                | ASIGNAR puntycom\n                | INSTFUNC \n                | LLAMARFUNC puntycom\n                | INSTIF\n                | INSTWHILE\n                | INSFOR\n                | INSLOOP\n                | INSMATCH\n                | INSTBREAK puntycom\n                | INSTCONTINUE puntycom\n                | INSTRETURN puntycom \n                | INSTARRAY puntycom\n                | INSTASIGNARARRAY puntycomINSTBREAK : resbreak\n                | resbreak EXPRESIONINSTCONTINUE : rescontinueINSTRETURN : resreturn\n                |  resreturn EXPRESIONPRINT :  resprint not  pariz EXPRESION parderPRINT :  resprint not  pariz EXPRESION com LISTAEXP parderINSTARRAY : reslet id igual ARRAYINSTARRAY : reslet id igual resvec not ARRAYINSTARRAY : reslet resmut id igual ARRAYINSTARRAY : reslet resmut id igual resvec not ARRAYINSTARRAY : reslet id dospunt TIPOARRAY igual ARRAYINSTARRAY : reslet id dospunt resvec menorque TIPOVAL mayorque igual ARRAYINSTARRAY : reslet resmut id dospunt TIPOARRAY igual ARRAY INSTASIGNARARRAY : id ACCESO igual EXPRESION ARRAY : corcheteiz LISTAEXP corcheteder\n            | corcheteiz LISTARREY corcheteder ARRAY : resvec not corcheteiz LISTAEXP corcheteder\n            | resvec not corcheteiz LISTARREY corcheteder ARRAY : resvec not corcheteiz EXPRESION puntycom entero corcheteder ARRAY : resvec dospunt dospunt resnew pariz parder LISTARREY : LISTARREY com ARRAY LISTARREY : ARRAY DECLARAR : reslet resmut id dospunt TIPOVAL igual EXPRESIONDECLARAR : reslet resmut id igual EXPRESIONDECLARAR : reslet id dospunt TIPOVAL igual EXPRESIONDECLARAR : reslet id igual EXPRESIONASIGNAR :  id igual EXPRESIONINSTIF : resif  EXPRESION  llaveiz BLOQUE llaveder INSTIF : resif  EXPRESION  llaveiz BLOQUE llaveder INSTELSEINSTELSE : reselse INSTIFINSTELSE : reselse llaveiz BLOQUE llavederINSMATCH : resmatch  EXPRESION  llaveiz COINCIDENCIAS llaveder COINCIDENCIAS : COINCIDENCIAS COINCIDENCIA    COINCIDENCIAS : COINCIDENCIA COINCIDENCIA :  LISTACOIN apunta llaveiz BLOQUE llaveder COINCIDENCIA :  LISTACOIN apunta INSTRUCCION comCOINCIDENCIA :  LISTACOIN apunta EXPRESION comLISTACOIN : LISTACOIN barra EXPRESION LISTACOIN : EXPRESION LISTACOIN : defaul INSTWHILE : reswhile  EXPRESION  llaveiz BLOQUE llaveder INSLOOP : resloop llaveiz BLOQUE llaveder INSFOR : resfor id resin EXPRESION llaveiz BLOQUE llaveder  INSFOR : resfor id resin EXPRESION puntdos EXPRESION llaveiz BLOQUE llaveder  INSTFUNC : resfn id pariz parder llaveiz BLOQUE llavederINSTFUNC : resfn id pariz parder menos mayorque TIPOVAL llaveiz BLOQUE llavederINSTFUNC : resfn id pariz PARAMETROS parder llaveiz BLOQUE llavederINSTFUNC : resfn id pariz PARAMETROS parder menos mayorque TIPOVAL llaveiz BLOQUE llavederLLAMARFUNC : id pariz parderLLAMARFUNC : id pariz LISTAEXP parderBLOQUE : INSTRUCCIONESLISTAEXP : LISTAEXP com EXPRESION LISTAEXP : EXPRESION PARAMETROS : PARAMETROS com id dospunt TIPOVAL PARAMETROS : id dospunt TIPOVAL TIPOVAL : resi64\n            | resf64\n            | resbool\n            | reschar\n            | restring\n            | str TIPOARRAY : corcheteiz TIPOARRAY puntycom EXPRESION corcheteder TIPOARRAY : corcheteiz TIPOVAL puntycom EXPRESION corchetederEXPRESION : EXPRESION mas EXPRESION\n                  | EXPRESION menos EXPRESION\n                  | EXPRESION por EXPRESION\n                  | EXPRESION modulo EXPRESION\n                  | EXPRESION divid EXPRESIONEXPRESION : EXPRESION menorque EXPRESIONEXPRESION : EXPRESION mayorque EXPRESIONEXPRESION : EXPRESION menorque igual EXPRESIONEXPRESION : EXPRESION mayorque igual EXPRESIONEXPRESION : EXPRESION igual igual EXPRESIONEXPRESION : EXPRESION not igual EXPRESIONEXPRESION : EXPRESION and and EXPRESIONEXPRESION : EXPRESION or EXPRESIONEXPRESION : not EXPRESIONEXPRESION : menos EXPRESION %prec UmenosEXPRESION : pariz EXPRESION parderEXPRESION    : enteroEXPRESION    : decimalEXPRESION    : cadenaEXPRESION    : caracterEXPRESION    : idEXPRESION    : id ACCESO EXPRESION    : INSMATCH EXPRESION    : LLAMARFUNC EXPRESION    : restrue\n                    | resfalse ACCESO : ACCESO corcheteiz EXPRESION corcheteder ACCESO : corcheteiz EXPRESION corcheteder '
    
_lr_action_items = {'resprint':([0,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,64,80,96,99,143,170,174,180,181,183,185,206,209,213,233,238,239,240,241,255,256,268,269,270,272,274,],[19,19,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,19,19,19,19,-61,19,-47,-60,19,-51,19,19,-48,19,-64,-49,19,-62,19,19,-66,19,-50,-63,-65,-67,]),'reslet':([0,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,64,80,96,99,143,170,174,180,181,183,185,206,209,213,233,238,239,240,241,255,256,268,269,270,272,274,],[20,20,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,20,20,20,20,-61,20,-47,-60,20,-51,20,20,-48,20,-64,-49,20,-62,20,20,-66,20,-50,-63,-65,-67,]),'id':([0,2,3,7,9,10,11,12,13,20,22,23,24,25,27,28,30,31,32,33,34,35,36,37,38,39,40,42,44,45,47,50,51,52,64,68,71,76,77,79,80,81,82,83,84,85,86,87,91,96,97,99,100,103,117,119,133,135,136,137,138,143,145,146,150,156,170,173,174,180,181,182,183,184,185,186,188,194,195,197,206,209,213,232,233,238,239,240,241,243,244,255,256,261,268,269,270,272,274,],[21,21,-3,-7,-9,-10,-11,-12,-13,43,48,57,57,63,57,57,57,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,69,57,57,57,57,57,57,21,57,57,57,57,123,21,57,57,57,57,57,57,57,57,21,57,21,57,57,57,57,57,57,57,57,57,-61,57,-53,57,57,21,208,-47,-60,21,57,-51,-52,218,57,57,57,57,57,21,-48,21,57,-64,-49,21,-62,21,-55,-56,21,-66,-54,21,-50,-63,-65,-67,]),'resfn':([0,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,64,80,96,99,143,170,174,180,181,183,185,206,209,213,233,238,239,240,241,255,256,268,269,270,272,274,],[22,22,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,22,22,22,22,-61,22,-47,-60,22,-51,22,22,-48,22,-64,-49,22,-62,22,22,-66,22,-50,-63,-65,-67,]),'resif':([0,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,64,80,96,99,143,170,174,180,181,183,185,206,209,210,213,233,238,239,240,241,255,256,268,269,270,272,274,],[23,23,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,23,23,23,23,-61,23,-47,-60,23,-51,23,23,-48,23,23,-64,-49,23,-62,23,23,-66,23,-50,-63,-65,-67,]),'reswhile':([0,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,64,80,96,99,143,170,174,180,181,183,185,206,209,213,233,238,239,240,241,255,256,268,269,270,272,274,],[24,24,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,24,24,24,24,-61,24,-47,-60,24,-51,24,24,-48,24,-64,-49,24,-62,24,24,-66,24,-50,-63,-65,-67,]),'resfor':([0,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,64,80,96,99,143,170,174,180,181,183,185,206,209,213,233,238,239,240,241,255,256,268,269,270,272,274,],[25,25,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,25,25,25,25,-61,25,-47,-60,25,-51,25,25,-48,25,-64,-49,25,-62,25,25,-66,25,-50,-63,-65,-67,]),'resloop':([0,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,64,80,96,99,143,170,174,180,181,183,185,206,209,213,233,238,239,240,241,255,256,268,269,270,272,274,],[26,26,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,26,26,26,26,-61,26,-47,-60,26,-51,26,26,-48,26,-64,-49,26,-62,26,26,-66,26,-50,-63,-65,-67,]),'resmatch':([0,2,3,7,9,10,11,12,13,23,24,27,28,30,31,32,33,34,35,36,37,38,39,40,44,45,47,50,51,52,64,68,71,76,77,80,81,82,83,84,85,86,87,91,96,97,99,100,103,117,119,133,135,136,137,138,143,145,146,150,156,170,174,180,181,182,183,184,185,186,188,194,195,197,206,209,213,232,233,238,239,240,241,243,244,255,256,261,268,269,270,272,274,],[27,27,-3,-7,-9,-10,-11,-12,-13,27,27,27,27,27,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-61,27,-53,27,27,27,-47,-60,27,27,-51,-52,27,27,27,27,27,27,27,-48,27,27,-64,-49,27,-62,27,-55,-56,27,-66,-54,27,-50,-63,-65,-67,]),'resbreak':([0,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,64,80,96,99,143,170,174,180,181,183,185,206,209,213,233,238,239,240,241,255,256,268,269,270,272,274,],[28,28,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,28,28,28,28,-61,28,-47,-60,28,-51,28,28,-48,28,-64,-49,28,-62,28,28,-66,28,-50,-63,-65,-67,]),'rescontinue':([0,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,64,80,96,99,143,170,174,180,181,183,185,206,209,213,233,238,239,240,241,255,256,268,269,270,272,274,],[29,29,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,29,29,29,29,-61,29,-47,-60,29,-51,29,29,-48,29,-64,-49,29,-62,29,29,-66,29,-50,-63,-65,-67,]),'resreturn':([0,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,64,80,96,99,143,170,174,180,181,183,185,206,209,213,233,238,239,240,241,255,256,268,269,270,272,274,],[30,30,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,30,30,30,30,-61,30,-47,-60,30,-51,30,30,-48,30,-64,-49,30,-62,30,30,-66,30,-50,-63,-65,-67,]),'$end':([1,2,3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,143,174,180,183,209,233,238,240,256,269,270,272,274,],[0,-1,-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,-61,-47,-60,-51,-48,-64,-49,-62,-66,-50,-63,-65,-67,]),'llaveder':([3,7,9,10,11,12,13,31,32,33,34,35,36,37,38,39,40,98,99,126,141,143,145,146,174,180,183,184,204,209,211,233,235,238,240,242,243,244,256,259,260,261,267,269,270,272,273,274,],[-3,-7,-9,-10,-11,-12,-13,-2,-4,-5,-6,-8,-14,-15,-16,-17,-18,143,-70,174,180,-61,183,-53,-47,-60,-51,-52,233,-48,240,-64,256,-49,-62,261,-55,-56,-66,269,270,-54,272,-50,-63,-65,274,-67,]),'puntycom':([4,5,6,8,14,15,16,17,18,28,29,30,53,54,55,56,57,58,59,60,61,66,67,72,73,92,93,95,107,108,109,110,111,112,114,115,118,120,122,127,128,129,130,131,132,134,139,140,149,153,154,159,160,168,175,176,177,178,179,183,191,192,196,199,200,216,220,221,222,223,229,247,248,249,250,262,264,265,266,271,],[32,33,34,35,36,37,38,39,40,-19,-21,-22,-99,-100,-101,-102,-103,-105,-106,-107,-108,-20,-23,-46,-68,-97,-96,-104,-75,-76,-77,-78,-79,-80,-45,-26,-69,-33,-110,-83,-84,-85,-86,-87,-88,-89,-95,-98,-24,-43,-28,194,195,-109,-90,-91,-92,-93,-94,-51,-44,-30,-27,-34,-35,35,-25,-42,-32,-29,251,-81,-82,-34,-35,-31,-39,-36,-37,-38,]),'com':([7,9,10,11,12,32,33,34,35,36,37,38,39,40,53,54,55,56,57,58,59,60,61,73,74,75,92,93,95,101,107,108,109,110,111,112,118,122,125,127,128,129,130,131,132,134,139,140,143,163,164,165,167,168,174,175,176,177,178,179,180,183,187,199,200,203,209,214,215,216,217,218,227,228,229,231,233,238,240,245,253,254,256,258,264,265,266,269,270,271,272,274,],[-7,-9,-10,-11,-12,-4,-5,-6,-8,-14,-15,-16,-17,-18,-99,-100,-101,-102,-103,-105,-106,-107,-108,-68,119,-72,-97,-96,-104,150,-75,-76,-77,-78,-79,-80,-69,-110,173,-83,-84,-85,-86,-87,-88,-89,-95,-98,-61,119,201,-41,-71,-109,-47,-90,-91,-92,-93,-94,-60,-51,119,-34,-35,-74,-48,243,244,-106,-13,-103,119,201,-72,-40,-64,-49,-62,-104,119,201,-66,-73,-39,-36,-37,-50,-63,-38,-65,-67,]),'not':([19,23,24,27,28,30,44,45,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,65,66,67,68,71,72,73,75,76,77,78,81,82,83,84,85,86,87,91,92,93,94,95,97,100,101,103,114,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,144,145,146,150,153,155,156,166,167,168,175,176,177,178,179,182,183,184,185,186,188,191,194,195,197,212,215,216,217,218,219,221,225,226,229,232,243,244,245,261,],[41,51,51,51,51,51,51,51,51,89,51,51,51,-99,-100,-101,-102,-103,-105,-106,-107,-108,89,89,89,89,51,51,89,-68,89,51,51,89,51,51,51,51,51,51,51,51,-97,89,89,-104,51,51,89,51,89,161,51,-69,51,89,89,-110,-83,-84,-85,-86,-87,89,51,89,51,51,51,51,89,-98,89,89,51,-53,51,89,190,51,202,89,-109,89,89,89,89,89,51,-51,-52,51,51,51,89,51,51,51,89,89,-106,-105,-103,89,89,89,89,89,51,-55,-56,-104,-54,]),'resmut':([20,],[42,]),'igual':([21,43,46,49,53,54,55,56,57,58,59,60,61,62,65,66,67,69,72,73,75,78,86,87,88,89,92,93,94,95,101,104,105,107,108,109,110,111,112,114,118,120,121,122,127,128,129,130,131,132,134,139,140,142,144,151,152,153,167,168,175,176,177,178,179,183,191,212,215,216,217,218,219,221,224,225,226,229,245,247,248,],[44,71,76,88,-99,-100,-101,-102,-103,-105,-106,-107,-108,88,88,88,88,103,88,-68,88,88,133,135,136,137,-97,88,88,-104,88,156,157,-75,-76,-77,-78,-79,-80,88,-69,88,88,-110,-83,-84,-85,-86,-87,88,88,88,-98,88,88,188,189,88,88,-109,88,88,88,88,88,-51,88,88,88,-106,-105,44,88,88,246,88,88,88,76,-81,-82,]),'pariz':([21,23,24,27,28,30,41,44,45,47,48,50,51,52,57,68,71,76,77,81,82,83,84,85,86,87,91,97,100,103,117,119,133,135,136,137,138,145,146,150,156,182,184,185,186,188,194,195,197,218,230,232,243,244,261,],[45,52,52,52,52,52,68,52,52,52,79,52,52,52,45,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-53,52,52,52,-52,52,52,52,52,52,52,45,252,52,-55,-56,-54,]),'corcheteiz':([21,46,57,70,71,95,102,103,113,117,122,157,161,168,189,190,197,201,202,218,232,245,246,],[47,77,47,113,117,77,113,117,113,117,-110,117,197,-109,117,197,117,117,232,47,117,77,117,]),'menos':([23,24,27,28,30,44,45,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,65,66,67,68,71,72,73,75,76,77,78,81,82,83,84,85,86,87,91,92,93,94,95,97,100,101,103,114,117,118,119,120,121,122,124,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,144,145,146,150,153,156,167,168,172,175,176,177,178,179,182,183,184,185,186,188,191,194,195,197,212,215,216,217,218,219,221,225,226,229,232,243,244,245,261,],[50,50,50,50,50,50,50,50,82,50,50,50,-99,-100,-101,-102,-103,-105,-106,-107,-108,82,82,82,82,50,50,82,-68,82,50,50,82,50,50,50,50,50,50,50,50,-97,82,82,-104,50,50,82,50,82,50,-69,50,82,82,-110,171,-83,-84,-85,-86,-87,82,50,82,50,50,50,50,82,-98,82,82,50,-53,50,82,50,82,-109,207,82,82,82,82,82,50,-51,-52,50,50,50,82,50,50,50,82,82,-106,-105,-103,82,82,82,82,82,50,-55,-56,-104,-54,]),'entero':([23,24,27,28,30,44,45,47,50,51,52,68,71,76,77,81,82,83,84,85,86,87,91,97,100,103,117,119,133,135,136,137,138,145,146,150,156,182,184,185,186,188,194,195,197,232,243,244,251,261,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-53,53,53,53,-52,53,53,53,53,53,53,53,-55,-56,263,-54,]),'decimal':([23,24,27,28,30,44,45,47,50,51,52,68,71,76,77,81,82,83,84,85,86,87,91,97,100,103,117,119,133,135,136,137,138,145,146,150,156,182,184,185,186,188,194,195,197,232,243,244,261,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-53,54,54,54,-52,54,54,54,54,54,54,54,-55,-56,-54,]),'cadena':([23,24,27,28,30,44,45,47,50,51,52,68,71,76,77,81,82,83,84,85,86,87,91,97,100,103,117,119,133,135,136,137,138,145,146,150,156,182,184,185,186,188,194,195,197,232,243,244,261,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-53,55,55,55,-52,55,55,55,55,55,55,55,-55,-56,-54,]),'caracter':([23,24,27,28,30,44,45,47,50,51,52,68,71,76,77,81,82,83,84,85,86,87,91,97,100,103,117,119,133,135,136,137,138,145,146,150,156,182,184,185,186,188,194,195,197,232,243,244,261,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-53,56,56,56,-52,56,56,56,56,56,56,56,-55,-56,-54,]),'restrue':([23,24,27,28,30,44,45,47,50,51,52,68,71,76,77,81,82,83,84,85,86,87,91,97,100,103,117,119,133,135,136,137,138,145,146,150,156,182,184,185,186,188,194,195,197,232,243,244,261,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-53,60,60,60,-52,60,60,60,60,60,60,60,-55,-56,-54,]),'resfalse':([23,24,27,28,30,44,45,47,50,51,52,68,71,76,77,81,82,83,84,85,86,87,91,97,100,103,117,119,133,135,136,137,138,145,146,150,156,182,184,185,186,188,194,195,197,232,243,244,261,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,-53,61,61,61,-52,61,61,61,61,61,61,61,-55,-56,-54,]),'llaveiz':([26,49,53,54,55,56,57,58,59,60,61,62,65,73,92,93,95,107,108,109,110,111,112,118,122,124,127,128,129,130,131,132,134,139,140,142,168,172,175,176,177,178,179,183,185,210,212,234,257,],[64,80,-99,-100,-101,-102,-103,-105,-106,-107,-108,96,100,-68,-97,-96,-104,-75,-76,-77,-78,-79,-80,-69,-110,170,-83,-84,-85,-86,-87,-88,-89,-95,-98,181,-109,206,-90,-91,-92,-93,-94,-51,213,239,241,255,268,]),'dospunt':([43,69,116,123,155,162,166,208,],[70,102,162,169,162,198,162,237,]),'parder':([45,53,54,55,56,57,58,59,60,61,73,74,75,79,92,93,94,95,101,107,108,109,110,111,112,118,122,125,127,128,129,130,131,132,134,139,140,167,168,175,176,177,178,179,183,187,203,252,258,],[73,-99,-100,-101,-102,-103,-105,-106,-107,-108,-68,118,-72,124,-97,-96,140,-104,149,-75,-76,-77,-78,-79,-80,-69,-110,172,-83,-84,-85,-86,-87,-88,-89,-95,-98,-71,-109,-90,-91,-92,-93,-94,-51,220,-74,264,-73,]),'mas':([49,53,54,55,56,57,58,59,60,61,62,65,66,67,72,73,75,78,92,93,94,95,101,114,118,120,121,122,127,128,129,130,131,132,134,139,140,142,144,153,167,168,175,176,177,178,179,183,191,212,215,216,217,218,219,221,225,226,229,245,],[81,-99,-100,-101,-102,-103,-105,-106,-107,-108,81,81,81,81,81,-68,81,81,-97,81,81,-104,81,81,-69,81,81,-110,-83,-84,-85,-86,-87,81,81,81,-98,81,81,81,81,-109,81,81,81,81,81,-51,81,81,81,-106,-105,-103,81,81,81,81,81,-104,]),'por':([49,53,54,55,56,57,58,59,60,61,62,65,66,67,72,73,75,78,92,93,94,95,101,114,118,120,121,122,127,128,129,130,131,132,134,139,140,142,144,153,167,168,175,176,177,178,179,183,191,212,215,216,217,218,219,221,225,226,229,245,],[83,-99,-100,-101,-102,-103,-105,-106,-107,-108,83,83,83,83,83,-68,83,83,-97,83,83,-104,83,83,-69,83,83,-110,83,83,-85,-86,-87,83,83,83,-98,83,83,83,83,-109,83,83,83,83,83,-51,83,83,83,-106,-105,-103,83,83,83,83,83,-104,]),'modulo':([49,53,54,55,56,57,58,59,60,61,62,65,66,67,72,73,75,78,92,93,94,95,101,114,118,120,121,122,127,128,129,130,131,132,134,139,140,142,144,153,167,168,175,176,177,178,179,183,191,212,215,216,217,218,219,221,225,226,229,245,],[84,-99,-100,-101,-102,-103,-105,-106,-107,-108,84,84,84,84,84,-68,84,84,-97,84,84,-104,84,84,-69,84,84,-110,84,84,-85,-86,-87,84,84,84,-98,84,84,84,84,-109,84,84,84,84,84,-51,84,84,84,-106,-105,-103,84,84,84,84,84,-104,]),'divid':([49,53,54,55,56,57,58,59,60,61,62,65,66,67,72,73,75,78,92,93,94,95,101,114,118,120,121,122,127,128,129,130,131,132,134,139,140,142,144,153,167,168,175,176,177,178,179,183,191,212,215,216,217,218,219,221,225,226,229,245,],[85,-99,-100,-101,-102,-103,-105,-106,-107,-108,85,85,85,85,85,-68,85,85,-97,85,85,-104,85,85,-69,85,85,-110,85,85,-85,-86,-87,85,85,85,-98,85,85,85,85,-109,85,85,85,85,85,-51,85,85,85,-106,-105,-103,85,85,85,85,85,-104,]),'menorque':([49,53,54,55,56,57,58,59,60,61,62,65,66,67,72,73,75,78,92,93,94,95,101,106,114,118,120,121,122,127,128,129,130,131,132,134,139,140,142,144,153,167,168,175,176,177,178,179,183,191,212,215,216,217,218,219,221,225,226,229,245,],[86,-99,-100,-101,-102,-103,-105,-106,-107,-108,86,86,86,86,86,-68,86,86,-97,86,86,-104,86,158,86,-69,86,86,-110,-83,-84,-85,-86,-87,86,86,86,-98,86,86,86,86,-109,86,86,86,86,86,-51,86,86,86,-106,-105,-103,86,86,86,86,86,-104,]),'mayorque':([49,53,54,55,56,57,58,59,60,61,62,65,66,67,72,73,75,78,92,93,94,95,101,107,108,109,110,111,112,114,118,120,121,122,127,128,129,130,131,132,134,139,140,142,144,153,167,168,171,175,176,177,178,179,183,191,193,207,212,215,216,217,218,219,221,225,226,229,245,],[87,-99,-100,-101,-102,-103,-105,-106,-107,-108,87,87,87,87,87,-68,87,87,-97,87,87,-104,87,-75,-76,-77,-78,-79,-80,87,-69,87,87,-110,-83,-84,-85,-86,-87,87,87,87,-98,87,87,87,87,-109,205,87,87,87,87,87,-51,87,224,236,87,87,-106,-105,-103,87,87,87,87,87,-104,]),'and':([49,53,54,55,56,57,58,59,60,61,62,65,66,67,72,73,75,78,90,92,93,94,95,101,114,118,120,121,122,127,128,129,130,131,132,134,139,140,142,144,153,167,168,175,176,177,178,179,183,191,212,215,216,217,218,219,221,225,226,229,245,],[90,-99,-100,-101,-102,-103,-105,-106,-107,-108,90,90,90,90,90,-68,90,90,138,-97,90,90,-104,90,90,-69,90,90,-110,-83,-84,-85,-86,-87,90,90,90,-98,90,90,90,90,-109,90,90,90,90,90,-51,90,90,90,-106,-105,-103,90,90,90,90,90,-104,]),'or':([49,53,54,55,56,57,58,59,60,61,62,65,66,67,72,73,75,78,92,93,94,95,101,114,118,120,121,122,127,128,129,130,131,132,134,139,140,142,144,153,167,168,175,176,177,178,179,183,191,212,215,216,217,218,219,221,225,226,229,245,],[91,-99,-100,-101,-102,-103,-105,-106,-107,-108,91,91,91,91,91,-68,91,91,-97,91,91,-104,91,91,-69,91,91,-110,-83,-84,-85,-86,-87,91,91,91,-98,91,91,91,91,-109,91,91,91,91,91,-51,91,91,91,-106,-105,-103,91,91,91,91,91,-104,]),'corcheteder':([53,54,55,56,57,58,59,60,61,73,75,78,92,93,95,118,121,122,127,128,129,130,131,132,134,139,140,163,164,165,167,168,175,176,177,178,179,183,199,200,225,226,227,228,229,231,253,254,263,264,265,266,271,],[-99,-100,-101,-102,-103,-105,-106,-107,-108,-68,-72,122,-97,-96,-104,-69,168,-110,-83,-84,-85,-86,-87,-88,-89,-95,-98,199,200,-41,-71,-109,-90,-91,-92,-93,-94,-51,-34,-35,247,248,249,250,-72,-40,265,266,271,-39,-36,-37,-38,]),'puntdos':([53,54,55,56,57,58,59,60,61,73,92,93,95,118,122,127,128,129,130,131,132,134,139,140,142,168,175,176,177,178,179,183,],[-99,-100,-101,-102,-103,-105,-106,-107,-108,-68,-97,-96,-104,-69,-110,-83,-84,-85,-86,-87,-88,-89,-95,-98,182,-109,-90,-91,-92,-93,-94,-51,]),'apunta':([53,54,55,56,57,58,59,60,61,73,92,93,95,118,122,127,128,129,130,131,132,134,139,140,144,147,148,168,175,176,177,178,179,183,219,],[-99,-100,-101,-102,-103,-105,-106,-107,-108,-68,-97,-96,-104,-69,-110,-83,-84,-85,-86,-87,-88,-89,-95,-98,-58,185,-59,-109,-90,-91,-92,-93,-94,-51,-57,]),'barra':([53,54,55,56,57,58,59,60,61,73,92,93,95,118,122,127,128,129,130,131,132,134,139,140,144,147,148,168,175,176,177,178,179,183,219,],[-99,-100,-101,-102,-103,-105,-106,-107,-108,-68,-97,-96,-104,-69,-110,-83,-84,-85,-86,-87,-88,-89,-95,-98,-58,186,-59,-109,-90,-91,-92,-93,-94,-51,-57,]),'resin':([63,],[97,]),'resvec':([70,71,103,117,157,161,189,190,197,201,232,246,],[106,116,155,166,166,166,166,166,166,166,166,166,]),'resi64':([70,102,113,158,169,205,236,237,],[107,107,107,107,107,107,107,107,]),'resf64':([70,102,113,158,169,205,236,237,],[108,108,108,108,108,108,108,108,]),'resbool':([70,102,113,158,169,205,236,237,],[109,109,109,109,109,109,109,109,]),'reschar':([70,102,113,158,169,205,236,237,],[110,110,110,110,110,110,110,110,]),'restring':([70,102,113,158,169,205,236,237,],[111,111,111,111,111,111,111,111,]),'str':([70,102,113,158,169,205,236,237,],[112,112,112,112,112,112,112,112,]),'defaul':([100,145,146,184,243,244,261,],[148,148,-53,-52,-55,-56,-54,]),'reselse':([174,],[210,]),'resnew':([198,],[230,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INIT':([0,],[1,]),'INSTRUCCIONES':([0,64,80,96,170,181,206,213,239,241,255,268,],[2,99,99,99,99,99,99,99,99,99,99,99,]),'INSTRUCCION':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[3,31,3,3,3,31,3,3,214,3,3,3,3,3,3,]),'PRINT':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'DECLARAR':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'ASIGNAR':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'INSTFUNC':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'LLAMARFUNC':([0,2,23,24,27,28,30,44,45,47,50,51,52,64,68,71,76,77,80,81,82,83,84,85,86,87,91,96,97,99,100,103,117,119,133,135,136,137,138,145,150,156,170,181,182,185,186,188,194,195,197,206,213,232,239,241,255,268,],[8,8,59,59,59,59,59,59,59,59,59,59,59,8,59,59,59,59,8,59,59,59,59,59,59,59,59,8,59,8,59,59,59,59,59,59,59,59,59,59,59,59,8,8,59,216,59,59,59,59,59,8,8,59,8,8,8,8,]),'INSTIF':([0,2,64,80,96,99,170,181,185,206,210,213,239,241,255,268,],[9,9,9,9,9,9,9,9,9,9,238,9,9,9,9,9,]),'INSTWHILE':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'INSFOR':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'INSLOOP':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'INSMATCH':([0,2,23,24,27,28,30,44,45,47,50,51,52,64,68,71,76,77,80,81,82,83,84,85,86,87,91,96,97,99,100,103,117,119,133,135,136,137,138,145,150,156,170,181,182,185,186,188,194,195,197,206,213,232,239,241,255,268,],[13,13,58,58,58,58,58,58,58,58,58,58,58,13,58,58,58,58,13,58,58,58,58,58,58,58,58,13,58,13,58,58,58,58,58,58,58,58,58,58,58,58,13,13,58,217,58,58,58,58,58,13,13,58,13,13,13,13,]),'INSTBREAK':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'INSTCONTINUE':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'INSTRETURN':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'INSTARRAY':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'INSTASIGNARARRAY':([0,2,64,80,96,99,170,181,185,206,213,239,241,255,268,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'ACCESO':([21,57,218,],[46,95,245,]),'EXPRESION':([23,24,27,28,30,44,45,47,50,51,52,68,71,76,77,81,82,83,84,85,86,87,91,97,100,103,117,119,133,135,136,137,138,145,150,156,182,185,186,188,194,195,197,232,],[49,62,65,66,67,72,75,78,92,93,94,101,114,120,121,127,128,129,130,131,132,134,139,142,144,153,75,167,175,176,177,178,179,144,75,191,212,215,219,221,225,226,229,229,]),'LISTAEXP':([45,117,150,197,232,],[74,163,187,227,253,]),'BLOQUE':([64,80,96,170,181,206,213,239,241,255,268,],[98,126,141,204,211,235,242,259,260,267,273,]),'TIPOVAL':([70,102,113,158,169,205,236,237,],[104,151,160,193,203,234,257,258,]),'TIPOARRAY':([70,102,113,],[105,152,159,]),'ARRAY':([71,103,117,157,161,189,190,197,201,232,246,],[115,154,165,192,196,222,223,165,231,165,262,]),'PARAMETROS':([79,],[125,]),'COINCIDENCIAS':([100,],[145,]),'COINCIDENCIA':([100,145,],[146,184,]),'LISTACOIN':([100,145,],[147,147,]),'LISTARREY':([117,197,232,],[164,228,254,]),'INSTELSE':([174,],[209,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INIT","S'",1,None,None,None),
  ('INIT -> INSTRUCCIONES','INIT',1,'p_inicial','gramatica.py',196),
  ('INSTRUCCIONES -> INSTRUCCIONES INSTRUCCION','INSTRUCCIONES',2,'p_instrucciones_lista_conjunto','gramatica.py',200),
  ('INSTRUCCIONES -> INSTRUCCION','INSTRUCCIONES',1,'p_instrucciones_lista_unica','gramatica.py',207),
  ('INSTRUCCION -> PRINT puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',214),
  ('INSTRUCCION -> DECLARAR puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',215),
  ('INSTRUCCION -> ASIGNAR puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',216),
  ('INSTRUCCION -> INSTFUNC','INSTRUCCION',1,'p_instrucciones_evaluar','gramatica.py',217),
  ('INSTRUCCION -> LLAMARFUNC puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',218),
  ('INSTRUCCION -> INSTIF','INSTRUCCION',1,'p_instrucciones_evaluar','gramatica.py',219),
  ('INSTRUCCION -> INSTWHILE','INSTRUCCION',1,'p_instrucciones_evaluar','gramatica.py',220),
  ('INSTRUCCION -> INSFOR','INSTRUCCION',1,'p_instrucciones_evaluar','gramatica.py',221),
  ('INSTRUCCION -> INSLOOP','INSTRUCCION',1,'p_instrucciones_evaluar','gramatica.py',222),
  ('INSTRUCCION -> INSMATCH','INSTRUCCION',1,'p_instrucciones_evaluar','gramatica.py',223),
  ('INSTRUCCION -> INSTBREAK puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',224),
  ('INSTRUCCION -> INSTCONTINUE puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',225),
  ('INSTRUCCION -> INSTRETURN puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',226),
  ('INSTRUCCION -> INSTARRAY puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',227),
  ('INSTRUCCION -> INSTASIGNARARRAY puntycom','INSTRUCCION',2,'p_instrucciones_evaluar','gramatica.py',228),
  ('INSTBREAK -> resbreak','INSTBREAK',1,'p_break','gramatica.py',232),
  ('INSTBREAK -> resbreak EXPRESION','INSTBREAK',2,'p_break','gramatica.py',233),
  ('INSTCONTINUE -> rescontinue','INSTCONTINUE',1,'p_continue','gramatica.py',240),
  ('INSTRETURN -> resreturn','INSTRETURN',1,'p_return','gramatica.py',244),
  ('INSTRETURN -> resreturn EXPRESION','INSTRETURN',2,'p_return','gramatica.py',245),
  ('PRINT -> resprint not pariz EXPRESION parder','PRINT',5,'p_impresion','gramatica.py',252),
  ('PRINT -> resprint not pariz EXPRESION com LISTAEXP parder','PRINT',7,'p_impresion_lista','gramatica.py',256),
  ('INSTARRAY -> reslet id igual ARRAY','INSTARRAY',4,'p_array','gramatica.py',260),
  ('INSTARRAY -> reslet id igual resvec not ARRAY','INSTARRAY',6,'p_vector','gramatica.py',264),
  ('INSTARRAY -> reslet resmut id igual ARRAY','INSTARRAY',5,'p_array_mut','gramatica.py',268),
  ('INSTARRAY -> reslet resmut id igual resvec not ARRAY','INSTARRAY',7,'p_vector_mut','gramatica.py',272),
  ('INSTARRAY -> reslet id dospunt TIPOARRAY igual ARRAY','INSTARRAY',6,'p_array_tipado','gramatica.py',276),
  ('INSTARRAY -> reslet id dospunt resvec menorque TIPOVAL mayorque igual ARRAY','INSTARRAY',9,'p_vector_tipado','gramatica.py',280),
  ('INSTARRAY -> reslet resmut id dospunt TIPOARRAY igual ARRAY','INSTARRAY',7,'p_array_mut_tipado','gramatica.py',285),
  ('INSTASIGNARARRAY -> id ACCESO igual EXPRESION','INSTASIGNARARRAY',4,'p_array_asignar','gramatica.py',289),
  ('ARRAY -> corcheteiz LISTAEXP corcheteder','ARRAY',3,'p_lista_array','gramatica.py',293),
  ('ARRAY -> corcheteiz LISTARREY corcheteder','ARRAY',3,'p_lista_array','gramatica.py',294),
  ('ARRAY -> resvec not corcheteiz LISTAEXP corcheteder','ARRAY',5,'p_lista_vectores','gramatica.py',298),
  ('ARRAY -> resvec not corcheteiz LISTARREY corcheteder','ARRAY',5,'p_lista_vectores','gramatica.py',299),
  ('ARRAY -> resvec not corcheteiz EXPRESION puntycom entero corcheteder','ARRAY',7,'p_vector_especial','gramatica.py',303),
  ('ARRAY -> resvec dospunt dospunt resnew pariz parder','ARRAY',6,'p_vector_new','gramatica.py',309),
  ('LISTARREY -> LISTARREY com ARRAY','LISTARREY',3,'p_lista_array_conjunto','gramatica.py',314),
  ('LISTARREY -> ARRAY','LISTARREY',1,'p_lista_array_unica','gramatica.py',320),
  ('DECLARAR -> reslet resmut id dospunt TIPOVAL igual EXPRESION','DECLARAR',7,'p_declarar_mut_tipo','gramatica.py',327),
  ('DECLARAR -> reslet resmut id igual EXPRESION','DECLARAR',5,'p_declarar_mut','gramatica.py',331),
  ('DECLARAR -> reslet id dospunt TIPOVAL igual EXPRESION','DECLARAR',6,'p_declarar_tipo','gramatica.py',335),
  ('DECLARAR -> reslet id igual EXPRESION','DECLARAR',4,'p_declarar','gramatica.py',339),
  ('ASIGNAR -> id igual EXPRESION','ASIGNAR',3,'p_asignar','gramatica.py',343),
  ('INSTIF -> resif EXPRESION llaveiz BLOQUE llaveder','INSTIF',5,'p_if','gramatica.py',347),
  ('INSTIF -> resif EXPRESION llaveiz BLOQUE llaveder INSTELSE','INSTIF',6,'p_if_else','gramatica.py',351),
  ('INSTELSE -> reselse INSTIF','INSTELSE',2,'p_elseif','gramatica.py',355),
  ('INSTELSE -> reselse llaveiz BLOQUE llaveder','INSTELSE',4,'p_else','gramatica.py',359),
  ('INSMATCH -> resmatch EXPRESION llaveiz COINCIDENCIAS llaveder','INSMATCH',5,'p_match','gramatica.py',363),
  ('COINCIDENCIAS -> COINCIDENCIAS COINCIDENCIA','COINCIDENCIAS',2,'p_match_coin_conjunto','gramatica.py',367),
  ('COINCIDENCIAS -> COINCIDENCIA','COINCIDENCIAS',1,'p_match_coin_unica','gramatica.py',374),
  ('COINCIDENCIA -> LISTACOIN apunta llaveiz BLOQUE llaveder','COINCIDENCIA',5,'p_match_coin','gramatica.py',381),
  ('COINCIDENCIA -> LISTACOIN apunta INSTRUCCION com','COINCIDENCIA',4,'p_match_coin_ins','gramatica.py',385),
  ('COINCIDENCIA -> LISTACOIN apunta EXPRESION com','COINCIDENCIA',4,'p_match_coin_exp','gramatica.py',389),
  ('LISTACOIN -> LISTACOIN barra EXPRESION','LISTACOIN',3,'p_lista_coin_conjunto','gramatica.py',393),
  ('LISTACOIN -> EXPRESION','LISTACOIN',1,'p_lista_coin','gramatica.py',399),
  ('LISTACOIN -> defaul','LISTACOIN',1,'p_lista_coin_defaul','gramatica.py',406),
  ('INSTWHILE -> reswhile EXPRESION llaveiz BLOQUE llaveder','INSTWHILE',5,'p_while','gramatica.py',413),
  ('INSLOOP -> resloop llaveiz BLOQUE llaveder','INSLOOP',4,'p_lup','gramatica.py',417),
  ('INSFOR -> resfor id resin EXPRESION llaveiz BLOQUE llaveder','INSFOR',7,'p_for','gramatica.py',421),
  ('INSFOR -> resfor id resin EXPRESION puntdos EXPRESION llaveiz BLOQUE llaveder','INSFOR',9,'p_for_range','gramatica.py',425),
  ('INSTFUNC -> resfn id pariz parder llaveiz BLOQUE llaveder','INSTFUNC',7,'p_funcion','gramatica.py',429),
  ('INSTFUNC -> resfn id pariz parder menos mayorque TIPOVAL llaveiz BLOQUE llaveder','INSTFUNC',10,'p_funcion_tipo','gramatica.py',433),
  ('INSTFUNC -> resfn id pariz PARAMETROS parder llaveiz BLOQUE llaveder','INSTFUNC',8,'p_funcion_parametros','gramatica.py',437),
  ('INSTFUNC -> resfn id pariz PARAMETROS parder menos mayorque TIPOVAL llaveiz BLOQUE llaveder','INSTFUNC',11,'p_funcion_tipo_parametros','gramatica.py',441),
  ('LLAMARFUNC -> id pariz parder','LLAMARFUNC',3,'p_llamar_f','gramatica.py',445),
  ('LLAMARFUNC -> id pariz LISTAEXP parder','LLAMARFUNC',4,'p_llamar_f_parametros','gramatica.py',449),
  ('BLOQUE -> INSTRUCCIONES','BLOQUE',1,'p_bloque','gramatica.py',453),
  ('LISTAEXP -> LISTAEXP com EXPRESION','LISTAEXP',3,'p_lista_expre_conjunto','gramatica.py',457),
  ('LISTAEXP -> EXPRESION','LISTAEXP',1,'p_lista_expre','gramatica.py',463),
  ('PARAMETROS -> PARAMETROS com id dospunt TIPOVAL','PARAMETROS',5,'p_lista_para_conjunto','gramatica.py',470),
  ('PARAMETROS -> id dospunt TIPOVAL','PARAMETROS',3,'p_lista_para','gramatica.py',476),
  ('TIPOVAL -> resi64','TIPOVAL',1,'p_tipoval','gramatica.py',483),
  ('TIPOVAL -> resf64','TIPOVAL',1,'p_tipoval','gramatica.py',484),
  ('TIPOVAL -> resbool','TIPOVAL',1,'p_tipoval','gramatica.py',485),
  ('TIPOVAL -> reschar','TIPOVAL',1,'p_tipoval','gramatica.py',486),
  ('TIPOVAL -> restring','TIPOVAL',1,'p_tipoval','gramatica.py',487),
  ('TIPOVAL -> str','TIPOVAL',1,'p_tipoval','gramatica.py',488),
  ('TIPOARRAY -> corcheteiz TIPOARRAY puntycom EXPRESION corcheteder','TIPOARRAY',5,'p_tipoarray','gramatica.py',499),
  ('TIPOARRAY -> corcheteiz TIPOVAL puntycom EXPRESION corcheteder','TIPOARRAY',5,'p_tipoarray_exp','gramatica.py',505),
  ('EXPRESION -> EXPRESION mas EXPRESION','EXPRESION',3,'p_expresion_binaria','gramatica.py',509),
  ('EXPRESION -> EXPRESION menos EXPRESION','EXPRESION',3,'p_expresion_binaria','gramatica.py',510),
  ('EXPRESION -> EXPRESION por EXPRESION','EXPRESION',3,'p_expresion_binaria','gramatica.py',511),
  ('EXPRESION -> EXPRESION modulo EXPRESION','EXPRESION',3,'p_expresion_binaria','gramatica.py',512),
  ('EXPRESION -> EXPRESION divid EXPRESION','EXPRESION',3,'p_expresion_binaria','gramatica.py',513),
  ('EXPRESION -> EXPRESION menorque EXPRESION','EXPRESION',3,'p_expresion_binaria_menor','gramatica.py',517),
  ('EXPRESION -> EXPRESION mayorque EXPRESION','EXPRESION',3,'p_expresion_binaria_mayor','gramatica.py',521),
  ('EXPRESION -> EXPRESION menorque igual EXPRESION','EXPRESION',4,'p_expresion_binaria_menor_igual','gramatica.py',525),
  ('EXPRESION -> EXPRESION mayorque igual EXPRESION','EXPRESION',4,'p_expresion_binaria_mayor_igual','gramatica.py',529),
  ('EXPRESION -> EXPRESION igual igual EXPRESION','EXPRESION',4,'p_expresion_binaria_igual','gramatica.py',533),
  ('EXPRESION -> EXPRESION not igual EXPRESION','EXPRESION',4,'p_expresion_binaria_no_igual','gramatica.py',537),
  ('EXPRESION -> EXPRESION and and EXPRESION','EXPRESION',4,'p_expresion_binaria_and','gramatica.py',541),
  ('EXPRESION -> EXPRESION or EXPRESION','EXPRESION',3,'p_expresion_binaria_or','gramatica.py',545),
  ('EXPRESION -> not EXPRESION','EXPRESION',2,'p_expresion_unaria_not','gramatica.py',549),
  ('EXPRESION -> menos EXPRESION','EXPRESION',2,'p_expresion_unaria','gramatica.py',553),
  ('EXPRESION -> pariz EXPRESION parder','EXPRESION',3,'p_expresion_agrupacion','gramatica.py',557),
  ('EXPRESION -> entero','EXPRESION',1,'p_expresion_entero','gramatica.py',561),
  ('EXPRESION -> decimal','EXPRESION',1,'p_expresion_decimal','gramatica.py',565),
  ('EXPRESION -> cadena','EXPRESION',1,'p_expresion_cadena','gramatica.py',569),
  ('EXPRESION -> caracter','EXPRESION',1,'p_expresion_caracter','gramatica.py',573),
  ('EXPRESION -> id','EXPRESION',1,'p_expresion_id','gramatica.py',577),
  ('EXPRESION -> id ACCESO','EXPRESION',2,'p_expresion_id_array','gramatica.py',581),
  ('EXPRESION -> INSMATCH','EXPRESION',1,'p_expresion_mach','gramatica.py',585),
  ('EXPRESION -> LLAMARFUNC','EXPRESION',1,'p_expresion_func','gramatica.py',589),
  ('EXPRESION -> restrue','EXPRESION',1,'p_expresion_boolean','gramatica.py',593),
  ('EXPRESION -> resfalse','EXPRESION',1,'p_expresion_boolean','gramatica.py',594),
  ('ACCESO -> ACCESO corcheteiz EXPRESION corcheteder','ACCESO',4,'p_acceso_conjunto','gramatica.py',598),
  ('ACCESO -> corcheteiz EXPRESION corcheteder','ACCESO',3,'p_acceso_unica','gramatica.py',604),
]
