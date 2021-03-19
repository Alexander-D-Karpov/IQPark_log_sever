from tkinter import *
file = open('users.log', 'r')
lines = file.read().splitlines()
file.close()

x = 0
root = Tk()
t = Text(root)
for x in lines:
    t.insert(END, x + '\n')
t.pack()
root.mainloop()

def add_new_line(str):
    t.insert(str, x + '\n')
    x += 1
