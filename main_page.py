import tkinter as tk
from tkinter import ttk
from tkinter import * 
import random
import urllib.request
from crawler import Crawler

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = tInput.get()
	return userInput


# This is a function which increases the progress bar value by the given increment amount
def makeProgress():
	progessBarOne['value']=progessBarOne['value'] + 1
	root.update_idletasks()


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')

def validate_url(url):
    try:
        # urllib.request.urlopen(url)
        return True
    except Exception as e:
        print("Not a real URL", str(e))
        return False

def btnStartScraping():
    is_valid_url = False
    global error_msg_lbl, status_msg_lbl
    status_msg_lbl.destroy()
    status_msg_lbl = Label(root, text='', fg='#00FF00', bg='#FFFFFF', font=('arial', 12, 'normal'))
    status_msg_lbl.config(text='Validating URL')
    status_msg_lbl.place(x=300, y=220)
    root.update()
    url = tInput.get()
    print("URL: ", url)
    valid_url = validate_url(url)
    if valid_url:
        print("URL is valid")
        error_msg_lbl.config(text="URL is valid")
        error_msg_lbl.place(x=300, y=250)
        is_valid_url = True
    else:
        print("URL not valid")
        error_msg_lbl.config(text="URL not valid")
        error_msg_lbl.place(x=300, y=250)
        error_msg_lbl.config(fg="red")
    status_msg_lbl.config(text='Ready')
    status_msg_lbl.place(x=300, y=220)

    if is_valid_url:
        text = crawl.scrap_text(url)
        print(text)


def gui_status(prompter=None):
    if prompter:
        return prompter + "..."
    return "Ready..."
    

root = Tk()
crawl = Crawler()
rect_header = Canvas(root, height=100, width=460)

# This is the section of code which creates the main window
root.geometry('891x592')
root.configure(background='#FFFFFF')
root.title('Universal Web Scrapper')


# First, we create a canvas to put the picture on
worthAThousandWords= Canvas(root, height=100, width=100)
# Then, we actually create the image file to use (it has to be a *.gif)
picture_file = PhotoImage(file = 'assets/images/logo-m.png')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
worthAThousandWords.create_image(100, 0, anchor=NE, image=picture_file)
worthAThousandWords.place(x=18, y=15)

rect_header.create_rectangle(200,140, 460,170)
rect_header.place(x=170, y=115)
# rect_header.pack()
# This is the section of code which creates the a label
Label(root, text='Enter URL', fg='#00FF00', bg='#FFFFFF', font=('arial', 12, 'normal')).place(x=200, y=150)


# This is the section of code which creates a text input box
tInput=Entry(root, width=50, borderwidth=2)
tInput.insert(0, 'http://example.com')
tInput.bind("<Return>", btnStartScraping)
tInput.pack()
tInput.place(x=303, y=152)
Button(root, text='START', bg='#00FF00', font=('arial', 12, 'normal'), command=btnStartScraping).place(x=545, y=184)

Label(root, text="Current Status: ", font=('arial', 12, 'bold'), bg='#FFFFFF').place(x=170, y=220)
status_msg_lbl = Label(root, text='Ready', fg='#00FF00', bg='#FFFFFF', font=('arial', 12, 'normal'))
status_msg_lbl.pack()
status_msg_lbl.place(x=300, y=220)


Label(root, text="Error Message: ", font=('arial', 12, 'bold'), bg='#FFFFFF').place(x=170, y=250)
error_msg_lbl = Label(root, text='No Errors', fg='#00FF00', bg='#FFFFFF', font=('arial', 12, 'normal'))
error_msg_lbl.pack()
error_msg_lbl.place(x=300, y=250)

# print("TYPE: ", type(error_msg_lbl))
# This is the section of code which creates a color style to be used with the progress bar
# progessBarOne_style = ttk.Style()
# progessBarOne_style.theme_use('clam')
# progessBarOne_style.configure('progessBarOne.Horizontal.TProgressbar', foreground='#F0F8FF', background='#F0F8FF')


# This is the section of code which creates a progress bar
# progessBarOne=ttk.Progressbar(root, style='progessBarOne.Horizontal.TProgressbar', orient='horizontal', length=236, mode='determinate', maximum=100, value=1)
# progessBarOne.place(x=98, y=160)


# This is the section of code which creates a button
Button(root, text='Show Data', bg='#00FF00', font=('arial', 12, 'normal'), command=btnClickFunction, state="disabled").place(x=272, y=413)


# This is the section of code which creates a button
Button(root, text='Save without Show', bg='#00FF00', font=('arial', 12, 'normal'), command=btnClickFunction, state="disabled").place(x=370, y=413)


root.mainloop()
