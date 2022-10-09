from genericpath import exists
from tkinter import *
from tkinter import filedialog
import tkinter
from PIL import Image, ImageTk
import os
from pytube import YouTube
from tkinter import messagebox
from tkinter.ttk import Progressbar 
import urllib
import requests
import validators

# Set Current Directory
path = os.getcwd()

# Functions
def directory():
    global path
    path = filedialog.askdirectory()
    canvas1.itemconfigure(id, text=path)


def pclick(event):
    bar.config(state=NORMAL)
    bar.delete(0, END)
    

def download():
    valid = validators.url(str(link.get()))
    if link.get() != "Enter Link" and link.get()!="" and valid ==True:
        url = YouTube(str(link.get()))
        video = url.streams.get_highest_resolution()
        vide_title = url.title +' - '+ url.author
        choice = messagebox.askyesno('Confirm Download',vide_title)
        if choice == True:
            video.download(path)
            messagebox.showinfo("Download Complete", "File Successfully Downloaded")
        else:
            messagebox.showinfo("Download Cancelled", "File Download Cancelled")
    else:
        bar.config(state=NORMAL)
        bar.delete(0, END)
        messagebox.askretrycancel("Error", "Please Enter Valid Link To Download")
        bar.insert(0, 'Enter Link')
        bar.config(state=DISABLED)
        bar.bind('<Button-1>', pclick)



# Create object
root = Tk()
root.resizable(height=FALSE, width=FALSE)
root.title('Youtube Downloader')
root.iconbitmap('yt.ico')

# Adjust size
root.geometry("500x400")

# Add image file
bg = PhotoImage(file="bg.png")

# Create Canvas
canvas1 = Canvas(root, width=400,height=400)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,anchor="nw")

# Add Text
canvas1.create_text(250, 50, text="YOUTUBE DOWNLOADER",font=("CaskaydiaCove NF", 25), anchor=CENTER,fill='black')
id = canvas1.create_text(265, 280, text=path,anchor=CENTER, font=("CaskaydiaCove NF", 8))

# Add Input Bar
link = StringVar()
bar = Entry(root, textvariable=link)
bar.place(x=80, y=100, width=350)
bar.insert(0, "Enter Link")
bar.config(fg="black", state=DISABLED, font=("CaskaydiaCove NF", 10))
clicked = bar.bind('<Button-1>', pclick)

# Create Buttons
button1 = Button(root, text="Fetch", bg='black',fg='white', font=("CaskaydiaCove NF", 10), command=download,padx=10)
button2 = Button(root, text="Change Path", command=directory,bg='black',fg='white', font=("CaskaydiaCove NF", 10),padx=10)

# Display Buttons
button1_canvas = canvas1.create_window(225, 140,anchor="nw",window=button1)

button2_canvas = canvas1.create_window(200, 300,anchor="nw",window=button2)

# Execute tkinter
root.mainloop()
