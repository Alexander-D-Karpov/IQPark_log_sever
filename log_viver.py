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
    cur_len_lines = len(lines)
    file = open('users.log', 'r')
    lines = file.read().splitlines()
    len_lines = len(lines)
    file.close()
    if len_lines > cur_len_lines:
        t.insert(END, lines[cur_len_lines] + '\n')
    root.mainloop()
    time.sleep(1)

