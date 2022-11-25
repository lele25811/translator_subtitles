#!/usr/bin/env python

from googletrans import Translator
import tkinter as tk
import os

language_list = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'}

window = tk.Tk()
window.geometry('400x450')
window.title('Subtitle Translator')

# file 
file_label =  tk.Label(window, text = 'FILE NAME.srt (same folder)',padx=10, pady=10)
file_label.grid(row=1, column=0, sticky='WN')

file_input = tk.Entry()
file_input.grid(row=2, column=0, padx=10, sticky='WN')

#controllo file trovato -> stamp name or error
file_check = tk.Label(window, text='')
file_check.grid(row=2, column=2, padx=30)

# language
language_label = tk.Label(window, text = 'LANGUAGE')
language_label.grid(row=4, column=0, padx=10, pady=10, sticky='WN')

language_listbox = tk.Listbox(window)
language_listbox.grid(row=5, column=0, padx=10, sticky='NWES')
scrollbar = tk.Scrollbar(window, orient= 'vertical', command= language_listbox.yview)
scrollbar.grid(row=5, column=1, sticky='NS')
language_listbox['yscrollcommand'] = scrollbar.set

for item in language_list.values():
    language_listbox.insert('end', item)

# Button start

def TakeInput():
    if file_input.get():
        file_name = file_input.get()
        file_check.config(text='File:\n'+file_name)
    else:
        file_check.config(text='Write a file name.srt\n (in same folder)')
    if language_listbox.get('anchor'):
        language = language_listbox.get('anchor')
        language_input.config(text='Language selected:\n'+language_listbox.get('anchor'))
    else: 
        language_input.config(text='Select a language')
    if os.path.isfile(file_name):
        new_file_name = translate(file_name, language)
    else: 
        file_check.config(text='File: '+file_name+'\ndont\' found')
    new_file.config(text='Done!\nNew file:\n'+new_file_name)
    


button_start = tk.Button(window, text='Translate', command=TakeInput)
button_start.grid(row=6, column=0, pady=10)

# language selected

language_input = tk.Label(window, text='')
language_input.grid(row=5, column=2, padx=30)

# Stamp new file
new_file = tk.Label(window, text='')
new_file.grid(row=6, column=2, padx=30)

credits_label = tk.Label(window, text='credits: lele25811')
credits_label.grid(row=10, column=0, pady=10, sticky='S')

#func

def translate(file_name, language):
    translator = Translator()
    text = []
    timestamp = []
    with open(file_name, 'r') as f:
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
    with open(language+'_'+file_name, 'w') as f:
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
    return language+'_'+file_name





if __name__ == '__main__':
    window.mainloop()
