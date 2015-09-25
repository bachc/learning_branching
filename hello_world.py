"""
This is a simple python hello world script,
That can be executed in both, python 2.x and 3.x
"""

#Language specific string
EN = {'h_world':  "Hello world!",
'p_key': "Press Enter to close this program"}
DE = {'h_world':  "Hallo Welt!",
'p_key': "Druecke Enter um das Programm zu schliessen"}
DE1 = {'h_world':  "Hallo Weld!",
'p_key': "Hau uff'd Ender-Daschde druff ums Brogram z'schliesse!"}
ES = {'h_world': "¡Hola Mundo!",
'p_key': 'Aprieta Enter para cerrar el programa'}
CHN = {'h_world': "??????",
'p_key': '?????????'}
BDR2 = {'h_world':  "Hello world!",
'p_key': "Press Enter to close this program"}
BDR3 = {'h_world':  "Hello world!",
'p_key': "Press Enter to close this program"}

Language_dicts = {'English': EN,
         'German': DE, 'Swabian German': DE1, 'Spanish': ES, 'Chinese': CHN}

L = input('Select language ')

print(Language_dicts[L]['h_world'])
input(Language_dicts[L]['p_key'])
