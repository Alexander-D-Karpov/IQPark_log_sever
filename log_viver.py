from tkinter import *
import tkinter as tk
import time
from watchdog.observers import Observer
from watchdog.events import FileModifiedEvent
file = open('logs/users.log', 'r')
lines = file.read().splitlines()[::-1]
file.close()

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

def update():
    with open("logs/users.log","r") as f:
        lines = file.read().splitlines()[::-1]
        t.delete("1.0", "end")
        for x in lines:
            t.insert(END, x + '\n')
        t.pack()
    T.after(1000, update)

class EventHandler():
    def on_any_event(self, event):
        update()


root=tk.Tk()
app=FullScreenApp(root)
t = Text(root)
for x in lines:
    t.insert(END, x + '\n')
t.pack()

if __name__ == "__main__":
    path = "logs/"
    event_handler = FileModifiedEvent('users.log')
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            root.mainloop()
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()