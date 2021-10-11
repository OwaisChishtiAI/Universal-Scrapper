import tkinter as tk
from tkinter import ttk
from tkinter import * 
import random
import urllib.request

from numpy.lib.type_check import imag
from crawler import Crawler


TEXT = "No Data"
TABLES = "No Data"
VIDEOS = "No Data"
IMAGES = "No Data"
DATA_WINDOW = None
SCR = None
HSCR = None
LV = None

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = tInput.get()
	return userInput


# This is a function which increases the progress bar value by the given increment amount
def makeProgress():
	progessBarOne['value']=progessBarOne['value'] + 1
	root.update_idletasks()

def destroyer(objects):
    for each in objects:
        each.destroy()

def create_data_window_text():
    global DATA_WINDOW, TEXT, TABLES, SCR, LV, HSCR
    if SCR and LV and HSCR:
        destroyer([SCR, LV, HSCR])
    scrollbar = Scrollbar(DATA_WINDOW, orient=VERTICAL)
    scrollbar.pack( side = RIGHT, fill = Y )

    hscrollbar = Scrollbar(DATA_WINDOW, orient=HORIZONTAL)
    hscrollbar.pack( side = BOTTOM, fill = X )

    mylist = Listbox(DATA_WINDOW, yscrollcommand = scrollbar.set,xscrollcommand=hscrollbar.set, width=145, height=25)
    if isinstance(TEXT, str):
        TEXT = [TEXT]
    for line in range(len(TEXT)):
        mylist.insert(END, str(line) + ") " + TEXT[line])

    mylist.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview )
    hscrollbar.config( command = mylist.xview )
    SCR = scrollbar
    LV = mylist
    HSCR = hscrollbar

def create_data_window_images():
    global DATA_WINDOW, IMAGES, SCR, LV, HSCR
    if SCR and LV and HSCR:
        destroyer([SCR, LV, HSCR])
    scrollbar = Scrollbar(DATA_WINDOW)
    scrollbar.pack( side = RIGHT, fill = Y )

    hscrollbar = Scrollbar(DATA_WINDOW, orient=HORIZONTAL)
    hscrollbar.pack( side = BOTTOM, fill = X )

    mylist = Listbox(DATA_WINDOW, yscrollcommand = scrollbar.set,xscrollcommand=hscrollbar.set,  width=145, height=25)
    if isinstance(IMAGES, str):
        IMAGES = [IMAGES]
    for line in range(len(IMAGES)):
        mylist.insert(END, str(line) + ") " + IMAGES[line])

    mylist.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview )
    hscrollbar.config( command = mylist.xview )
    SCR = scrollbar
    LV = mylist
    HSCR = hscrollbar

def create_data_window_videos():
    global DATA_WINDOW, VIDEOS, SCR, LV, HSCR
    if SCR and LV and HSCR:
        destroyer([SCR, LV, HSCR])
    scrollbar = Scrollbar(DATA_WINDOW)
    scrollbar.pack( side = RIGHT, fill = Y )

    hscrollbar = Scrollbar(DATA_WINDOW, orient=HORIZONTAL)
    hscrollbar.pack( side = BOTTOM, fill = X )

    mylist = Listbox(DATA_WINDOW, yscrollcommand = scrollbar.set,xscrollcommand=hscrollbar.set,  width=145, height=25)
    if isinstance(VIDEOS, str):
        VIDEOS = [VIDEOS]
    for line in range(len(VIDEOS)):
        mylist.insert(END, str(line) + ") " + VIDEOS[line])

    mylist.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview )
    hscrollbar.config( command = mylist.xview )
    SCR = scrollbar
    LV = mylist
    HSCR = hscrollbar

def create_data_window_tables():
    global DATA_WINDOW, TABLES, SCR, LV, HSCR
    if SCR and LV and HSCR:
        destroyer([SCR, LV, HSCR])
    scrollbar = Scrollbar(DATA_WINDOW)
    scrollbar.pack( side = RIGHT, fill = Y )

    hscrollbar = Scrollbar(DATA_WINDOW, orient=HORIZONTAL)
    hscrollbar.pack( side = BOTTOM, fill = X )

    mylist = Listbox(DATA_WINDOW, yscrollcommand = scrollbar.set,xscrollcommand=hscrollbar.set,  width=145, height=25)
    if isinstance(TABLES, str):
        TABLES = [TABLES]
    for line in range(len(TABLES)):
        mylist.insert(END, "Table# {}".format(line+1))
        mylist.insert(END, "_______________________")
        for i in range(len(TABLES[line])):
            mylist.insert(END, TABLES[line].iloc[i, :])

    mylist.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview )
    hscrollbar.config( command = mylist.xview )
    SCR = scrollbar
    LV = mylist
    HSCR = hscrollbar


# this is the function called when the button is clicked
def btnClickFunction():
    global  DATA_WINDOW
    print('clicked')
    window = tk.Toplevel(root)
    disp_wind = tk.Canvas(window, height=592, width=891)
    disp_wind.pack()
    disp_wind.configure(background='#FFFFFF')
    text_data = Button(window, text='Text Data', bg='#00FF00', font=('arial', 12, 'normal'), command=create_data_window_text, state="normal")
    text_data.place(x=100+120, y=50)
    tables_data = Button(window, text='Tablular Data', bg='#00FF00', font=('arial', 12, 'normal'), command=create_data_window_tables, state="normal")
    tables_data.place(x=185+120, y=50)
    images_data = Button(window, text='Media - Images', bg='#00FF00', font=('arial', 12, 'normal'), command=create_data_window_images, state="normal")
    images_data.place(x=295+120, y=50)
    videos_data = Button(window, text='Media - Videos', bg='#00FF00', font=('arial', 12, 'normal'), command=create_data_window_videos, state="normal")
    videos_data.place(x=420+120, y=50)
    ttk.Separator(window, orient='horizontal').place(x=0, y=85, relwidth=6)
    data_window = tk.Canvas(window, height=450, width=891)
    data_window.place(x=0, y=95)
    DATA_WINDOW = data_window
    # data_label = Label(window, text=TEXT, fg='#00FF00' , font=('arial', 12, 'normal'))
    # data_label.place(x=0, y=95)
    # # myentry = ttk.Entry(data_window, textvariable=TEXT,fg='#00FF00', state='readonly')

    # myscroll = ttk.Scrollbar(data_window, orient='vertical', command=data_window.xview)
    # data_window.config(xscrollcommand=myscroll.set)
    

    # data_window.grid()
    # myentry.place(x=0, y=10)
    # myscroll.grid(row=2, sticky='ew')

def validate_url(url):
    try:
        # urllib.request.urlopen(url)
        return True
    except Exception as e:
        print("Not a real URL", str(e))
        return False

def btnStartScraping():
    is_valid_url = False
    global error_msg_lbl, status_msg_lbl, TEXT, TABLES, IMAGES, VIDEOS
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
        crawl.set_url(url)
        text = crawl.scrape_text()
        if text:
            TEXT = text
        print(text)
        tables = crawl.scrape_tables()
        if tables:
            TABLES = tables
        print(tables)
        images, videos = crawl.scrape_media()
        if images:
            IMAGES = images
        if videos:
            VIDEOS = videos
        print("IMAGES ", images)
        print("VIDEOS ", videos)

    # with open("test_text.txt", "w", encoding='utf8', errors='ignore')as f:
    #     f.write(text)
    show_data.config(state="normal")
    save_data.config(state="normal")
    
    
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
def on_enter_show_data(e):
    show_data['background'] = '#006400'

def on_leave_show_data(e):
    show_data['background'] = '#00FF00'

def on_enter_save_data(e):
    save_data['background'] = '#006400'

def on_leave_save_data(e):
    save_data['background'] = '#00FF00'

# This is the section of code which creates a button
show_data = Button(root, text='Show Data', bg='#00FF00', font=('arial', 12, 'normal'), command=btnClickFunction, state="normal")#disabled
show_data.place(x=272, y=413)
show_data.bind("<Enter>", on_enter_show_data)
show_data.bind("<Leave>", on_leave_show_data)

# This is the section of code which creates a button
save_data = Button(root, text='Save without Show', bg='#00FF00', font=('arial', 12, 'normal'), state="normal")
save_data.place(x=370, y=413)
save_data.bind("<Enter>", on_enter_save_data)
save_data.bind("<Leave>", on_leave_save_data)

root.mainloop()
