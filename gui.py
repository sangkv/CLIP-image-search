import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

from search import search


class GUI():
    def __init__(self, path_database):
        # Initialize the search engine
        self.machine = search(path_database)

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
        self.filemenu.add_command(label="New", command = self.contact)
        self.filemenu.add_command(label = "Open", command = self.contact)
        self.filemenu.add_command(label = "Save", command = self.contact)
        self.filemenu.add_command(label = "Save as...", command = self.contact)
        self.filemenu.add_command(label = "Close", command = self.contact)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Exit", command = self.root.quit)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label = "Undo", command = self.contact)
        self.editmenu.add_separator()
        self.editmenu.add_command(label = "Cut", command = self.contact)
        self.editmenu.add_command(label = "Copy", command = self.contact)
        self.editmenu.add_command(label = "Paste", command = self.contact)
        self.editmenu.add_command(label = "Delete", command = self.contact)
        self.menubar.add_cascade(label = "Edit", menu = self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label = "Help Index", command = self.contact)
        self.helpmenu.add_command(label = "About...", command = self.contact)
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

        self.list_position = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                              (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]

        self.number_results = len(self.list_position)

        self.list_label = [Label(self.labelframe_results) for i in range(self.number_results)]
        
        # Show GUI
        self.root.mainloop()

    def contact(self):
        messagebox.showinfo('Contact:', 'sangkv.work@gmail.com')
    
    def resizeShow(self, img):
        w, h = img.size

        if w >= h:
            if w > self.showW:
                imgH = int(h/(w/self.showW))
                return img.resize((self.showW, imgH))
            return img
        else:
            if h > self.showH:
                imgW = int(w/(h/self.showH))
                return img.resize((imgW, self.showH))
            return img
    
    def showImg(self, image_path, idx):
        # Image
        img = Image.open(image_path)
        imgtk = ImageTk.PhotoImage(self.resizeShow(img))
        self.list_label[idx] = Label(self.labelframe_results, image=imgtk)
        self.list_label[idx].image = imgtk
        # Position
        row = self.list_position[idx][0]
        col = self.list_position[idx][1]
        # Show Image
        self.list_label[idx].grid(row=row, column=col, padx=5, pady=10, sticky='')
            
    def search(self):
        # Delete the old image displayed on the GUI
        for label in self.list_label:
            label.image = None
        
        # Get input text
        input_data = self.entry.get()

        # Search
        if input_data != '':
            results = self.machine.search(input_data=input_data, n_result=self.number_results)

            for idx, elem in enumerate(results):
                self.showImg(elem['path_image'], idx)


if __name__=='__main__':
    GUI('./database/Corel-1000')