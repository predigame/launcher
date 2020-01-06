from tkinter import Tk, filedialog
import os, subprocess

root = Tk()
root.withdraw()

file = filedialog.askdirectory(title='Load Game', initialdir='.', mustexist=True)

subprocess.Popen(["python", "edit.py", os.path.join(file, 'game.py')])
