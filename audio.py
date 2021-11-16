# import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound

# Initialized window
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.config(bg = '#FFE873')
root.title('TEXT_TO_SPEECH')


# heading
Label(root, text = 'TEXT TO SPEECH', font='arial 20 bold', bg ='#FFE873').pack()
Label(root, text ='Deepak Barnwal', font ='arial 15 bold', bg = '#FFE873').pack(side = BOTTOM)

# label
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='#FFE873').place(x=200, y=60)

# text variable
Msg = StringVar()

#Entry
entry_field = Entry(root, textvariable =Msg, width ='75')
entry_field.place(x=20, y=100)

# define function
# speech the text
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('python.mp3')
    playsound('python.mp3')

# reset function
def Reset():
    Msg.set("")

# exit function
def Exit():
    root.destroy()

# Button
Button(root, text = "PLAY", font = 'arial 15 bold', command = Text_to_speech, width =5, bg='lime').place(x=135, y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset, bg='yellow', width=5).place(x=210, y =140)
Button(root, text = 'EXIT', font = 'arial 15 bold', command = Exit, bg='red').place(x=285, y=140)

# infinite loop to run program
root.mainloop()
