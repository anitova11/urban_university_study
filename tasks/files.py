import tkinter
import os
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title='select file',
                                          filetypes=(('text file', '.txt'), ('all files', '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x400')
window.configure(bg='pink')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл', height=5, width=50, background='white', foreground='violet')
text.place(x=50, y=10)
# text.grid(column=2, row=1)
button_select = tkinter.Button(window, height=3, width=20, text='Выберите файл', background='white',
                               foreground='violet', command=file_select)
button_select.place(x=150, y=100)
# button_select.grid(column=1, row=2, pady=5)
window.mainloop()
