'''
qr_code_generator.py
Preston J Greenwood
12/21/2024

This program reads an input string
and generates a Quick Response code
representing that string
'''

import segno
import tkinter as tk

window = tk.Tk()
window.title("QR Code Generator")

directions = tk.Label(window , text='Enter Link').grid(row=1,column=0)
link_to_qr = tk.StringVar()
entry = tk.Entry(window, textvariable=link_to_qr).grid(row=1,column=1)

def do_thing():
    link = link_to_qr.get()
    qr_code = segno.make_qr(link)

    qr_code.save(link[2:5] + ".png")

enter = tk.Button(window, text='Enter' , command=do_thing).grid(row=1,column=2)

window.mainloop()
