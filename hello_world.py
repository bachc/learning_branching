"""
This is a simple python hello world script,
That can be executed only in python 3.x.
"""

#Language specific strings
EN = {'h_world':  "Hello world!",
'p_key': "Press Enter to close this program"}
DE = {'h_world':  "Hallo Welt!",
'p_key': "Druecke Enter um das Programm zu schliessen"}
DE1 = {'h_world':  "Hallo Weld!",
'p_key': "Hau uff'd Ender-Daschde druff ums Brogram z'schliesse!"}

#Available language dicts       
Language_dicts = {'English': EN,
         'Deutsch': DE, 'Swabian German': DE1}

print("\nThe following languages are available:")
for key in Language_dicts.keys():
	print("- ", key)

L = input('\nSelect language by typing in a valid language:\n')
print(Language_dicts[L]['h_world'])
input(Language_dicts[L]['p_key'])
