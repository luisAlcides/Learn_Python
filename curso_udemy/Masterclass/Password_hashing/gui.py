from tkinter import *
import bcrypt


def validate(password):
    hash = b'$2b$12$I66Kjgcq/f8uw0epRmY4PuOjdFSuMQrXFFbimjTIXSGE9x48My6La'
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hash):
        print('Login successful')
    else:
        print('Invalid password')



root = Tk()
root.geometry('300x300')

password_entry = Entry(root)
password_entry.pack()
password_entry.get()

button = Button(text='validate', command=lambda: validate(password_entry.get()))
button.pack()

root.mainloop()