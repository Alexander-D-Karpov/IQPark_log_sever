from tkinter import *
import time
from watchdog.observers import Observer
from watchdog.events import FileModifiedEvent
file = open('logs/users.log', 'r')
lines = file.read().splitlines()[::-1]
file.close()

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


root = Tk()
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