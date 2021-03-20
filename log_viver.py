from tkinter import *
import tkinter as tk
import time
import datetime

root = tk.Tk()
t = Text(root)

def update():
    filename='logs/{}.log'.format(datetime.datetime.now().date())
    file = open(filename, 'r')
    lines = file.read().splitlines()[::-1]
    file.close()
    t.delete("1.0", "end")
    for x in lines:
        t.insert(END, x + '\n')
    t.pack()
    root.after(1000, update)

while True:
    update()
    root.mainloop()

