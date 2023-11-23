import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('600x400')
window.title('My first hello world on tkinter')
window.iconbitmap('icon.ico')

btn = ttk.Button(window, text='Hello')
btn.pack()

window.mainloop()