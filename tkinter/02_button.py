import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Hello world')
window.iconbitmap('icon.ico')


# image = tk.PhotoImage(file='editar.png')


def event_clic():
    print('change btn')
    btn.config(text='Boton presionado')
    print('Add button')
    btn2 = ttk.Button(window, text='Btn2')
    btn2.pack()


btn = ttk.Button(window, text='Dar clic', command=event_clic, state='normal')
btn.pack()

window.mainloop()
