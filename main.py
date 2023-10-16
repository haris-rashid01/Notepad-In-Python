from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def exit():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def Help():
    showinfo("Notepad", "Notepad By Haris Rashid")
if __name__ == '__main__':
    root = Tk()
    root.geometry("600x400")
    root.title("Notepad")
    root.wm_iconbitmap("m1.ico")
    TextArea = Text(root, font="lucida 13")
    TextArea.pack(expand=True, fill=BOTH)
    file = None

    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=exit)

    MenuBar.add_cascade(label="File", menu=FileMenu)
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="Help", command=Help)
    MenuBar.add_cascade(label="About", menu=HelpMenu)
    root.config(menu=MenuBar)
    ScrollBar = Scrollbar(TextArea)
    ScrollBar.pack(side=RIGHT, fill=Y)
    ScrollBar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=ScrollBar.set)


    root.mainloop()
