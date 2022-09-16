import tkinter
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from PIL import Image
from PIL import ImageTk

from features import extract_features
from index import index
from search import query

class GUI():
    def __init__(self):
        # Init GUI
        self.root = tkinter.Tk()
        self.root.title('IMAGE SEARCH')
        self.root.configure(background='gainsboro')

        # Window size
        self.guiW = 1280
        self.guiH = 720
        self.showW = int(self.guiW/5.5)
        self.showH = int(self.guiH/3)
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
        self.btnSearch = Button(self.labelframe_search, font=self.font, text='Search', relief=RAISED, bg='red', command=self.search)
        self.btnSearch.grid(row=0, column=1, padx=30, pady=50)

        # 2. Group Results
        self.labelframe_results = LabelFrame(self.root, bd=0, text='', font=self.font, height=550, width=1240)
        self.labelframe_results.grid(row=1,column=0, padx=20)
        

        # Show GUI
        self.root.mainloop()

    
    def donothing(self):
        messagebox.showinfo('Contact:', 'sangkv.work@gmail.com')
    
    def resizeShow(self, img):
        w, h = img.size

        if w >= h:
            if w > self.showW:
                imgH = int(h/(w/self.showW))
                print(self.showW, imgH)
                return img.resize((self.showW, imgH))
            return img
        else:
            if h > self.showH:
                imgW = int(w/(h/self.showH))
                print(imgW, self.showH)
                return img.resize((imgW, self.showH))
            return img
    
    def showImg(self, image_path, position):
        # Image
        img = Image.open(image_path)
        imgtk = ImageTk.PhotoImage(self.resizeShow(img))
        label = Label(self.labelframe_results, image=imgtk)
        label.image = imgtk
        # Position
        row = position[0]
        col = position[1]
        # Show Image
        label.grid(row=row, column=col, padx=5, pady=10, sticky='')


    def search(self):
        list_position = [(0, 0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1, 3), (1, 4)]
        '''
        image_path = 'Corel-1000/0.jpg'
        for i in list_position:
            self.showImg(image_path, i)
        '''
        Q = query()
        input_data = self.entry.get()
        results = Q.search(input_data=input_data)

        for i, elem in enumerate(results):
            self.showImg(elem['path_image'], list_position[i])
    

if __name__=='__main__':
    GUI()