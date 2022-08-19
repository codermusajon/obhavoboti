import tkinter as tk
from math import *
bot = tk.Tk()

bot.title('kalkulyator')
bot.geometry('300x300')
bot.config(bg='yellow')
#kvadrat funksiyasi
def kv():
    number=entry1.get()
    result = int(number) * int(number)
    label=tk.Label(bot, text=f'javobi:   {result}')
    label.grid(row=3, column=0)

#ildiz funksiyasi
def ildiz():
    number=entry1.get()
    result = sqrt(int(number))
    label=tk.Label(bot, text=f'javobi:   {result}')
    label.grid(row=3, column=0)

#qo`shish funksiyasi
def qushish():
    number = entry1.get()
    number2=entry2.get()
    result = float(number) + float(number2)
    label=tk.Label(bot, text=f'javobi:   {result}')
    label.grid(row=3, column=0)

#ayirish funksiyasi
def ayirish():
    number = entry1.get()
    number2=entry2.get()
    result = float(number) - float(number2)
    label=tk.Label(bot, text=f'javobi:   {result}')
    label.grid(row=3, column=0)

#kupaytirish funksiyasi
def kup():
    number = entry1.get()
    number2=entry2.get()
    result = float(number) * float(number2)
    label=tk.Label(bot, text=f'javobi:   {result}')
    label.grid(row=3, column=0)

#bulish funksiyasi
def bul():
    number = entry1.get()
    number2=entry2.get()
    result = float(number) / float(number2)
    label=tk.Label(bot, text=f'javobi:   {result}')
    label.grid(row=3, column=0)

#tkinter funksiyasi
entry1=tk.Entry(bot)
entry1.grid(row=1, column=0)
entry1.update()

entry2=tk.Entry(bot)
entry2.grid(row=1, column=1)

button=tk.Button(bot, text='kvadrat', command=kv)
button.grid(row=2, column=0)

button=tk.Button(bot, text='ildiz', command=ildiz)
button.grid(row=1, column=2)

button=tk.Button(bot, text='qo`shish', command=qushish)
button.grid(row=2, column=1)

button=tk.Button(bot, text='ayirish', command=ayirish)
button.grid(row=2, column=2)

button=tk.Button(bot, text='ko`paytirish', command=kup)
button.grid(row=3, column=1)

button=tk.Button(bot, text='bo`lish', command=bul)
button.grid(row=3, column=2)

bot.mainloop()