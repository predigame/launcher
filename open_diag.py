from tkinter import *
from tkinter import messagebox
#from tkinter.ttk import *
from tkinter.font import *
import os, re, shutil, subprocess
import predigame

root = Tk()
root.title('Create New Game')
labels = Font(family='Helvetica', size=30, weight='bold')
inputs = Font(family='Helvetica', size=30, weight='normal')

def close(event):
    root.destroy()

def loadgame():
    file = entext.get()
    print(file)
    if file is not None and os.path.isdir(os.path.join('games', file)) and os.path.isfile(os.path.join('games', file, 'game.py')):
        subprocess.Popen(["python", "edit.py", os.path.join('games', file, 'game.py')])
    root.destroy()

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))


lab = Label(root, text='Game', font=labels)

games = os.listdir('games')
games.sort()

entext = StringVar()
entext.set('<Select a Game>')
option = OptionMenu(root, entext, *games)
option.config(font=inputs, width=25)
but = Button(root, text=' Load Game! ', command=loadgame, font=labels, bg='green', highlightcolor='green', highlightbackground='green')

lab.grid(row=0, column=0)
option.grid(row=0, column=1)
but.grid(row=0, column=2)

root.bind('<Escape>', close)
root.mainloop()
