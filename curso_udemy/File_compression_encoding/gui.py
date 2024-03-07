import tkinter as tk
from compressmodule import compress, decompress

window = tk.Tk()
window.title('Compresssion engine')
window.geometry('600x400')

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window, text='File to be compressed')
output_label = tk.Label(window, text='Name of the compressed file')

input_decompress_label = tk.Label(window, text='File to be decompress')
output_decompress_label = tk.Label(window, text='outputfile to be compress')

input_decompress_entry = tk.Entry(window)
output_decompress_entry = tk.Entry(window)

compress_func = lambda: compress(input_entry.get(), output_entry.get())
decompress_func = lambda: decompress(input_decompress_entry.get(), output_decompress_entry.get())

compress_btn = tk.Button(window, text='Compress', command=compress_func)
decompress_btn = tk.Button(window, text='Decompress', command=decompress_func)

input_label.grid(row=0, column=0)
output_label.grid(row=1, column=0)
input_entry.grid(row=0, column=1)
output_entry.grid(row=1, column=1)
compress_btn.grid(row=2, column=1)
input_decompress_label.grid(row=4, column=0)
output_decompress_label.grid(row=5, column=0)
input_decompress_entry.grid(row=4, column=1)
output_decompress_entry.grid(row=5, column=1)
decompress_btn.grid(row=6, column=1)


window.mainloop()
