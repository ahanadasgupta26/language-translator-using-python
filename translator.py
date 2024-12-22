from tkinter import *
from tkinter import ttk,messagebox
from deep_translator import GoogleTranslator
import pyttsx3

try:
    texttospeech=pyttsx3.init()
except Exception as e:
    raise Exception(f"Failed to initialize TTS engine:{e}")

try:
    voices=texttospeech.getProperty('voices')  
    if not voices:
        raise Exception("No voices found.Check your TTS setup.")
    texttospeech.setProperty('voice',voices[0].id) 
    texttospeech.setProperty('rate',150) 
except Exception as e:
    raise Exception(f"Error configuring voice properties:{e}")
root=Tk()
root.title("Translator")
root.geometry("1000x400")
root.resizable(False,False)

translate=GoogleTranslator()

def label_change():
    b1=box1.get()
    b2=box2.get()
    label1.configure(text=b1)
    label2.configure(text=b2)
    root.after(1000,label_change)

def translate_now():
    try:
        texts=text1.get(1.0,END).strip()
        source_lang=box1.get()
        target_lang=box2.get()
        
        if texts and target_lang!="Select a language":
            source_code=list(languages.keys())[list(languages.values()).index(source_lang)]
            target_code=list(languages.keys())[list(languages.values()).index(target_lang)]
            
            translated_text=GoogleTranslator(source=source_code,target=target_code).translate(texts)
            
            text2.delete(1.0,END)
            text2.insert(END,translated_text)
        else:
            messagebox.showwarning("Warning","Please enter text and select languages.")
    except Exception as e:
        messagebox.showerror("Error",f"Translation failed:{e}")

def speak_text(content):
    try:
        texttospeech.say(content)
        texttospeech.runAndWait()
    except Exception as e:
        messagebox.showerror("Error",f"Speech synthesis failed:{e}")

def speak_input():
    content=text1.get(1.0,END).strip()
    if content:
        speak_text(content)
    else:
        messagebox.showwarning("Warning","Input text is empty.")

def speak_translated():
    content=text2.get(1.0,END).strip()
    if content:
        speak_text(content)
    else:
        messagebox.showwarning("Warning","Translated text is empty.")

languages={
    'af':'Afrikaans',
    'sq':'Albanian',
    'am':'Amharic',
    'ar':'Arabic',
    'hy':'Armenian',
    'az':'Azerbaijani',
    'eu':'Basque',
    'be':'Belarusian',
    'bn':'Bengali',
    'bs':'Bosnian',
    'bg':'Bulgarian',
    'ca':'Catalan',
    'zh-CN':'Chinese(simplified)',
    'zh-TW':'Chinese(traditional)',
    'hr':'Croatian',
    'cs':'Czech',
    'da':'Danish',
    'nl':'Dutch',
    'en':'English',
    'et':'Estonian',
    'fi':'Finnish',
    'fr':'French',
    'gl':'Galician',
    'ka':'Georgian',
    'de':'German',
    'el':'Greek',
    'gu':'Gujarati',
    'ht':'Haitian creole',
    'he':'Hebrew',
    'hi':'Hindi',
    'hu':'Hungarian',
    'is':'Icelandic',
    'id':'Indonesian',
    'ga':'Irish',
    'it':'Italian',
    'ja':'Japanese',
    'kn':'Kannada',
    'ko':'Korean',
    'ku':'Kurdish',
    'lv':'Latvian',
    'lt':'Lithuanian',
    'mk':'Macedonian',
    'ms':'Malay',
    'ml':'Malayalam',
    'mt':'Maltese',
    'mi':'Maori',
    'mr':'Marathi',
    'mn':'Mongolian',
    'my':'Myanmar (burmese)',
    'ne':'Nepali',
    'no':'Norwegian',
    'or':'Oriya',
    'ps':'Pashto',
    'fa':'Persian',
    'pl':'Polish',
    'pt':'Portuguese',
    'pa':'Punjabi',
    'ro':'Romanian',
    'ru':'Russian',
    'sr':'Serbian',
    'st':'Sesotho',
    'si':'Sinhala',
    'sk':'Slovak',
    'sl':'Slovenian',
    'es':'Spanish',
    'sw':'Swahili',
    'sv':'Swedish',
    'tg':'Tajik',
    'ta':'Tamil',
    'te':'Telugu',
    'th':'Thai',
    'tr':'Turkish',
    'uk':'Ukrainian',
    'ur':'Urdu',
    'uz':'Uzbek',
    'vi':'Vietnamese',
    'cy':'Welsh',
    'xh':'Xhosa',
    'yi':'Yiddish',
    'yo':'Yoruba',
    'zu':'Zulu',
}

langs=list(languages.values())

box1=ttk.Combobox(root,values=langs,font="Arial")
box1.place(x="100",y="30")
box1.set("English")

label1=Label(root,text="English",font="Arial",bg="yellow",width=20,bd=5,relief=GROOVE)
label1.place(x=100,y=90)

fr1=Frame(root,bg="black",bd=5)
fr1.place(x=20,y=150,height=200,width=400)

text1=Text(fr1,font="Arial",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,height=190,width=390)

scollbar1=Scrollbar(fr1)
scollbar1.pack(side="right",fill="y")
scollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scollbar1.set)

box2=ttk.Combobox(root,values=langs,font="Arial")
box2.place(x="650",y="30")
box2.set("Select a language")

label2=Label(root,text="English",font="Arial",bg="yellow",width=20,bd=5,relief=GROOVE)
label2.place(x=650,y=90)

fr2=Frame(root,bg="black",bd=5)
fr2.place(x=580,y=150,height=200,width=400)

text2=Text(fr2,font="Arial",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,height=190,width=390)

scollbar2=Scrollbar(fr2)
scollbar2.pack(side="right",fill="y")
scollbar2.configure(command=text2.yview)
text1.configure(yscrollcommand=scollbar2.set)

translate=Button(root,text="Translate",font="Arial",activebackground="pink",cursor="hand2",bd=5,bg="red",fg="white",command=translate_now)
translate.place(x=443,y=250)

speak_input_btn=Button(root,text="Speak Input",font="Arial",bg="blue",fg="white",command=speak_input)
speak_input_btn.place(x=150,y=360)

speak_translated_btn=Button(root,text="Speak Translated",font="Arial",bg="green",fg="white",command=speak_translated)
speak_translated_btn.place(x=700,y=360)

label_change()
root.configure(bg="#f4f4f4")
root.mainloop()