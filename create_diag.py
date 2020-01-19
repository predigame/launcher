from tkinter import *
from tkinter import messagebox
#from tkinter.ttk import *
from tkinter.font import *
import os, re, shutil
import predigame

root = Tk()
root.title('Create New Game')
labels = Font(family='Helvetica', size=30, weight='bold')
inputs = Font(family='Helvetica', size=30, weight='normal')
def chooseFolder(event=None):
    game = entext.get()
    if game:

        if os.path.isdir(os.path.join('games', game)):
            messagebox.showerror('Game Exists', 'A game by the name ' + game + ' already exists. Try using another name!')
            return

        os.chdir('games')
        sys.argv = ['pred', 'new', game]
        predigame.bootstrap()
        import subprocess
        os.chdir('..')
        subprocess.Popen(["python", "edit.py", os.path.join('games', game, 'game.py')])
        root.destroy()
    else:
        messagebox.showerror("Missing Name", "A game name is required!")

def validate(event):
    val = entext.get()
    if not val.isalnum():
        entext.set(re.sub('[^0-9a-zA-Z]+', '', val))

def close(event):
    root.destroy()

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

lab = Label(root, text='Game Name', font=labels)

entext = StringVar()
en = Entry(root, textvariable=entext, width=20, font=inputs)
en.focus()

but = Button(root, text=' Game On! ', command=chooseFolder, font=labels, bg='green', highlightcolor='green', highlightbackground='green')

lab.grid(row=0, column=0)
en.grid(row=0, column=1)
but.grid(row=0, column=2)

root.bind('<Return>', chooseFolder)
root.bind('<Key>', validate)
root.bind('<Escape>', close)
root.mainloop()
