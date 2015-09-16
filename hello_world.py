"""
This is a simple python hello world script,
That can be executed in both, python 2.x and 3.x
"""
import sys

#Select language
<<<<<<< HEAD
L = 'English'
#L= 'German'

#Language specific string
EN = {'h_world':  "Hello world!",
'p_key': "Press Enter to close this program"}
DE = {'h_world':  "Hello Welt!",
'p_key': "Druecke Enter um das Programm zu schliessen"}
words = {'English': EN,
         'German': DE}

if sys.version_info[0]< 3:
    print words[L]['h_world']
else:
    print(words[L]['h_world'])

raw_input(words[L]['p_key'])
=======
#L = 'English'
#L= 'German'



#Language specific string
EN = {'h_world':  "Hello world!",
'p_key': "Press Enter to close this program"}
DE = {'h_world':  "Hallo Welt!",
'p_key': "Druecke Enter um das Programm zu schliessen"}
words = {'English': EN,
         'German': DE}
"""
if sys.version_info[0]< 3:
    print words[L]['h_world']
else:"""
#print(words[L]['h_world'])

L = input('Select language ')
print(words[L]['h_world'])
input(words[L]['p_key'])
>>>>>>> master
