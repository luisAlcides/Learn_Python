import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title='Select a file to compress')
    return filename


window = tk.Tk()
window.title('Compresssion engine')
window.geometry('600x400')


compress_func = lambda: compress(open_file(), 'comprimido.txt')

compress_btn = tk.Button(window, text='Compress', command=compress_func)

compress_btn.grid(row=2, column=1)

window.mainloop()
