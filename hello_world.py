"""
This is a simple python hello world script,
That can be executed only in python 3.x.
"""

#Language specific strings
EN = {'h_world':  "Hello world!", 'p_key': "Press Enter to close this program"}
DE = {'h_world':  "Hallo Welt!", 'p_key': "Druecke Enter um das Programm zu schliessen"}
DE1 = {'h_world':  "Hallo Weld!",
       'p_key': "Hau uff'd Ender-Daschde druff ums Brogram z'schliesse!"}
vie = {'h_world': "Chào thế giới!", 'p_key': "Nhấn Enter để đóng chương trình này"}
Th={'h_world':  "สวัสดีชาวโลก!", 'p_key': "กด Enter เพื่อปิดโปรแกรมนี้"}           
zulu = {'h_world':  "Sawubona Mhlaba", 'p_key': "Cindezela u-Enter ukuze uvale lolu hlelo"}
West_Frisian={'h_world': 'Hallo wrâld!', 'p_key': 'Druk op Enter om dit programma te sluten.'}
yoruba = {'h_world':  "Mo ki O Ile Aiye!", 'p_key': "Tẹ Tẹ lati pa eto yii"}
Tamil = {"h_world": "வணக்கம் உலகம்", "p_key": "இந்த நிரலை மூட Enter ஐ அழுத்தவும்"}  
Tamil = {"h_world": "வணக்கம் உலகம்", "p_key": "இந்த நிரலை மூட Enter ஐ அழுத்தவும்"}
Yidi = {'h_world': 'העלא וועלט !', 'p_key': 'דרוק אַרייַן צו פאַרמאַכן דעם פּראָגראַם'}


#Available language dicts       
Language_dicts = {'English': EN, 'Deutsch': DE, 'Swabian German': DE1, 'Vietnamese': vie,
                  'Thai': Th, 'Zulu': zulu, 'Western Frisian': West_Frisian,    
                  'Yoruba': yoruba, 'Tamil': Tamil, 'Yiddish' : Yidi}

print("\nThe following languages are available:")
for key in Language_dicts.keys():
	print("- ", key)

L = input('\nSelect language by typing in a valid language:\n')
print(Language_dicts[L]['h_world'])
input(Language_dicts[L]['p_key'])