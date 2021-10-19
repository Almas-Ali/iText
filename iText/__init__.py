from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, showwarning
import subprocess
import json
import glob
# import os

# os.chdir('iText/plugins/')
plugins = glob.glob1(dirname='iText/plugins', pattern='*.py')

# for plugin in plugins:
#     exec('from %s import *' % (plugin))

with open('iText/config.json', 'r') as cf:
    theme = json.load(cf)
# print(theme['Theme'])


root = Tk()
root.title('iText')
root.geometry('500x600')

# Frames
MainFrame = Frame(root, bg=theme['Theme']['Background'])
MainFrame.pack(expand=True, fill='both')

LineFrame = Frame(root, bg=theme['Theme']['Background'], width=25)
LineFrame.pack(expand=False, fill='left')

# Text Area
MainTextArea = Text(
    MainFrame, bg=theme['Theme']['Background'], fg=theme['Theme']['Foreground'])
MainTextArea.pack(expand=True, fill='both')

def linenumber(event=None):
    line, column = MainTextArea.index(END).split('.')
    # Creating line number toolbar
    try:
        LineFrame.pack_forget()
        LineFrame.destroy()
        

MainTextArea.bind("<Any-KeyPress>", linenumber)


full_path = ''


def set_file_path(path):
    global full_path
    full_path = path
    return full_path


def open_file():
    global MainTextArea
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        MainTextArea.delete('1.0', END)
        MainTextArea.insert('1.0', code)
        set_file_path(path)
        # debug
        print(code)


def save():
    global full_path
    global MainTextArea
    if full_path == '':
        path = asksaveasfilename(
            filetypes=[('Python Files', '*.py')])
    else:
        path = full_path
    with open(path, 'w') as file:
        code = MainTextArea.get('1.0', END)
        file.write(code)
        set_file_path(path)
        # debug
        print(code)


def save_as():
    global full_path
    global MainTextArea
    if full_path == '':
        path = asksaveasfilename(
            filetypes=[('Python Files', '*.py')])
    else:
        path = full_path
    with open(path, 'w') as file:
        code = MainTextArea.get('1.0', END)
        file.write(code)
        set_file_path(path)
        # debug
        print(code)


def run():
    global full_path
    global Result
    if full_path == '':
        showwarning('Warning', 'Please save the code before run !')
        return
    Command = f'python {full_path}'
    process = subprocess.Popen(
        Command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    result, error = process.communicate()
    Result.insert('1.0', result)
    Result.insert('1.0', error)


Result = Text(height=7)
Result.config(bg='black', fg='green')
Result.pack()

menu_bar = Menu(root)

File_option = Menu(menu_bar, tearoff=0)
File_option.add_command(label='Open', command=open_file)
File_option.add_command(label='Save', command=save)
File_option.add_command(label='SaveAs', command=save_as)
File_option.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=File_option)

Compile_option = Menu(menu_bar, tearoff=0)
Compile_option.add_command(label='compile', command=run)
menu_bar.add_cascade(label='compile', menu=Compile_option)

root.config(menu=menu_bar)

root.mainloop()
