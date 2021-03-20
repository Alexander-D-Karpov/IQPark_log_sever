from tkinter import *
import time
file = open('users.log', 'r')
lines = file.read().splitlines()
file.close()

length = 0
root = Tk()
t = Text(root)
for x in lines:
    t.insert(END, x + '\n')
    length += 1
t.pack()
while True:
    file = open('users.log', 'r')
    lines = file.read().splitlines()
    lines_len = len(lines)
    file.close()
    if lines_len > length:
        for i in range(length, lines_len):
            t.insert(END, lines[i] + '\n')

    time.sleep(1)
    root.mainloop()

