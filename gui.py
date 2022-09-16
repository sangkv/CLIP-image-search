import tkinter
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

from PIL import Image
from PIL import ImageTk

class GUI():
    def __init__(self):
        # Init GUI
        self.root = tkinter.Tk()
        self.root.title('IMAGE SEARCH')
        self.root.configure(background='gainsboro')

        # Window size
        self.guiW = 1280
        self.guiH = 720
        self.root.geometry(str(self.guiW)+'x'+str(self.guiH))
        self.root.resizable(height=False, width=False)

        # Menu
        self.menubar = Menu(self.root)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command = self.donothing)
        self.filemenu.add_command(label = "Open", command = self.donothing)
        self.filemenu.add_command(label = "Save", command = self.donothing)
        self.filemenu.add_command(label = "Save as...", command = self.donothing)
        self.filemenu.add_command(label = "Close", command = self.donothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Exit", command = self.root.quit)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label = "Undo", command = self.donothing)
        self.editmenu.add_separator()
        self.editmenu.add_command(label = "Cut", command = self.donothing)
        self.editmenu.add_command(label = "Copy", command = self.donothing)
        self.editmenu.add_command(label = "Paste", command = self.donothing)
        self.editmenu.add_command(label = "Delete", command = self.donothing)
        self.menubar.add_cascade(label = "Edit", menu = self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label = "Help Index", command = self.donothing)
        self.helpmenu.add_command(label = "About...", command = self.donothing)
        self.menubar.add_cascade(label = "Help", menu = self.helpmenu)
        self.root.config(menu = self.menubar)

        # Font
        self.font=('Times', 24, 'normal')

        # 1. Group Search
        self.labelframe_search = LabelFrame(self.root, bd=0, height=120, width=1240)
        self.labelframe_search.grid(row=0, column=0)

        # Entry
        self.entry = tkinter.Entry(self.labelframe_search, font=self.font, width=50)
        self.entry.grid(row=0, column=0, padx=100, pady=50)

        # Button
        self.btnSearch = Button(self.labelframe_search, font=self.font, text='Search', relief=RAISED, bg='red', command=None)
        self.btnSearch.grid(row=0, column=1, padx=30, pady=50)

        # 2. Group Results
        self.labelframe_results = LabelFrame(self.root, bd=0, text='', font=self.font, height=550, width=1240)
        self.labelframe_results.grid(row=1,column=0, padx=20)
        

        # Show GUI
        self.root.mainloop()

    
    def donothing(self):
        messagebox.showinfo('Contact:', 'sangkv.work@gmail.com')
    

if __name__=='__main__':
    GUI()