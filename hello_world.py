﻿"""
This is a simple python hello world script,
That can be executed only in python 3.x.
Chinese, sanscrict, and Urdu are not compatible
with python 2.x file encoding.
"""

#Language specific strings
EN = {'h_world':  "Hello world!",
'p_key': "Press Enter to close this program"}
DE = {'h_world':  "Hallo Welt!",
'p_key': "Druecke Enter um das Programm zu schliessen"}
DE1 = {'h_world':  "Hallo Weld!",
'p_key': "Hau uff'd Ender-Daschde druff ums Brogram z'schliesse!"}
ES = {'h_world': "¡Hola Mundo!",
'p_key': 'Aprieta Enter para cerrar el programa'}
CHN = {'h_world': "你好，世界！",
'p_key': '请按回车键关闭程序'}
ITA = {'h_world': "Ciao mondo!",
'p_key': "Premi Enter per chiudere il programma"}
OK = {'h_world':  "Hey Ya'll!",
'p_key':  "Gotta shut-er down, y'all!"}
SK = {'h_world':  "जगत नमस्कारः ",
'p_key':  "Hit Enter to shut this program down"}
URD = {'h_world': " السلام علیکم",
'p_key':  "Hit Enter to shut this program down"}
PUNJ = {'h_world': "Sati srī akāla duni'ā",
'p_key':  "Hit Enter to shut this program down"}
BEN = {'h_world': "ওহে  বিশ্ব",
'p_key':  "Hit Enter to shut this program down"}
YO = {'h_world': "Mo ki O Ile Aiye!",
'p_key': "Tẹ Tẹ lati pa eto yii"}
VI = {'h_world': "Chào thế giới!",
'p_key': "Hit Enter to shut this program down"}
BUR = {'h_world': "မင်္ဂလာပါကမ္ဘာလောက!",
'p_key': "ဤအစီအစဉ်ပိတ်ပစ်ရန် Enter ကိုနှိပ်ပါ"}
KOR = {'h_world': "여러분 안녕하세요!",
'p_key':  "창을 닫으시려면 엔터를 누르세요"}
CEB = {'h_world':"Hello sa kalibutan",
'p_key': "Magpilit sa pagsira niini nga programa"}
TAM = {'h_world':"வணக்கம்!",
       'p_key': "இந்த நிரலை மூட Enter ஐ அழுத்தவும்"}
WF = {'h_world':  "Hallo wrâld!",
'p_key': "Druk op Enter om dit programma te sluten"}
YID = {'h_world':  "העלא וועלט",
'p_key': "דרוק אַרייַן צו פאַרמאַכן"}
SIN = {'h_world': "හෙලෝ වර්ල්ඩ්!",
       'p_key': "මෙම වැඩසටහන වසා දමන්න"}
       
Language_dicts = {'English': EN,
         'Deutsch': DE, 'Swabian German': DE1, 'Espanol': ES, 
         'Chinese': CHN, 'Italian': ITA, 'Okie': OK, 'Sanskrit': SK,
         'Urdu': URD,'Punjabi': PUNJ, 'BENGALI': BEN, 'Yoruba': YO,
          'Vietnamese':VI,'Burmese': BUR, 'Korean': KOR, 'Cebuano': CEB, 'Tamil': TAM,
                  'Western Frisian': WF, 'Sinhala':SIN}

print(Language_dicts.keys())

L = input('Select language_ ')
print(Language_dicts[L]['h_world'])
input(Language_dicts[L]['p_key'])
input()
