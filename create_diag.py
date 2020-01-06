from tkinter import *
import os
import predigame

root = Tk()
root.title('Create New Game')

def chooseFolder():
    sys.argv = ['pred', 'new', str(en.get())]
    predigame.bootstrap()
    import subprocess
    subprocess.Popen(["python", "edit.py", os.path.join(en.get(), 'game.py')])
    root.destroy()

# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

lab = Label(root, text='Game Name')
en = Entry(root, width =25)
but = Button(root, text='Create It!', command = chooseFolder)
lab.grid(row=0, column=0)
en.grid(row=0, column=1)
but.grid(row=0, column=2)
root.mainloop()



#directory = filedialog.askdirectory(title='Select folder to save results')
#print(directory)

#sys.argv = ['pred', 'new', directory]
#predigame.bootstrap()
