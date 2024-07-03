import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

ui = tk.Tk()
ui.minsize(350, 350)
ui.title("Group8 LR4 Exercise 2")

def openFile():
    filepath = fd.askopenfilename(initialdir="\home\drpdayan\LocalRepo\SoftDes\Activities\CPE106L-4_E01_Q2324_LabReports\CPE106L_GRP8_LR4", title="Select a Text File", filetypes= (("text files","*.txt"),("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

button = Button(text="Open",command=openFile)
button.pack()
ui.mainloop()