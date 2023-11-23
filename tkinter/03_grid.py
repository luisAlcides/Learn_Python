import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Manejo de Grid')
window.iconbitmap('icon.ico')


# methods for events
def event1():
    btn1.config(text='Boton 1 presionado')


def event2():
    btn2.config(text='boton 2 presionado')


# button
btn1 = ttk.Button(window, text='Boton 1', command=event1)
btn1.grid(row=0, column=0)

btn2 = ttk.Button(window, text='Boton 2', command=event2)
btn2.grid(row=1, column=0)

window.mainloop()
