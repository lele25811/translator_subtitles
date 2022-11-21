# !/usr/bin/python3
# -*- coding: utf-8 -*-

# Se aperto tramite python3 funziona, se aperto tramite linux teminal no

# primo parametro -> nome file
# secondo parametro -> lingua destinazione, default = 'it'
#tusla king S01 -> 4,35

import sys
from googletrans import Translator

file = sys.argv[1]
print('file:',file)
if len(sys.argv) == 2:
    language = 'it'
if len(sys.argv) == 3:
    language = sys.argv[2]
    print('dest:', language)
translator = Translator()
text = []
timestamp = []
with open(file, 'r') as f:
    f.readline()
    timestamp.append(f.readline())
    for i in f:
        if len(i) <= 2:
            f.readline()
            timestamp.append(f.readline())
        line = []
        line = i
        translation = translator.translate(line, dest=language)
        text.append(translation.text)
with open(language+'_'+file, 'w') as f:
    f.writelines(str(1)+'\n')
    f.writelines('00:00:00,000 --> 00:00:02,000\n')
    f.writelines('subtitles created by\n') 
    f.writelines('lele25811\'s Python script\n')
    f.writelines('\n')
    for i in range(len(timestamp)):
        f.writelines(str(i+2)+'\n')
        f.writelines(timestamp[i])
        j = 0
        while True:
            if j >= len(text):
                break
            if text[j] == '':
                text = text[j+1:]
                break
            f.writelines(text[j]+'\n')
            j+=1
        f.writelines('\n')
print('new file: '+language+'_'+file)