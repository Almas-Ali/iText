from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess

ws = Tk()
ws.title('Python Guides')

Cpath = ''

def Openthisfile():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.5', END)
        editor.insert('1.5', code)
        global Cpath
        Cpath = path

def SavethisfileAs():
    global gpath
    if Cpath =='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = Cpath    
    with open(path, 'w') as file:
        code = editor.get('1.5', END)
        file.write(code)

editor = Text()
editor.config(bg='white', fg='blue', insertbackground='black')
editor.pack()

Result = Text(height=7)
Result.config(bg='black', fg='green')
Result.pack()
 
Menu_option = Menu(ws)

File_option = Menu(Menu_option, tearoff=0)
File_option.add_command(label='Open', command = Openthisfile)
