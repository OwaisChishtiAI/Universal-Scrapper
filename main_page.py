import tkinter as tk
from tkinter import ttk
from tkinter import * 
import random
import urllib.request
import os
import pandas as pd
from database import DataBase
from time import sleep
from urllib.parse import urlparse

from numpy.lib.type_check import imag
from crawler import Crawler


PARENT_PATH = 'assets/images/.cache/.database'
URL = None
TEXT = "No Data"
TABLES = "No Data"
VIDEOS = "No Data"
IMAGES = "No Data"
DATA_WINDOW = None
SECOND_WINDOW = None
SCR = None
HSCR = None
LV = None

DB_TEXT = "No Data"
DB_TABLES = "No Data"
DB_VIDEOS = "No Data"
DB_IMAGES = "No Data"
DB_DATA_WINDOW = None
DB_SECOND_WINDOW = None
DB_SCR = None
DB_HSCR = None
DB_LV = None


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
        if isinstance(TABLES[line], pd.core.frame.DataFrame):
            mylist.insert(END, "Table# {}".format(line+1))
            mylist.insert(END, "_______________________")
            for i in range(len(TABLES[line])):
                mylist.insert(END, TABLES[line].iloc[i, :])
        else:
            mylist.insert(END, TABLES[line])

    mylist.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview )
    hscrollbar.config( command = mylist.xview )
    SCR = scrollbar
    LV = mylist
    HSCR = hscrollbar

############################################################################################################################################
def create_data_window_text_db():
    global DB_DATA_WINDOW, DB_TEXT, DB_TABLES, DB_SCR, DB_LV, DB_HSCR
    if DB_SCR and DB_LV and DB_HSCR:
        destroyer([DB_SCR, DB_LV, DB_HSCR])
    scrollbar = Scrollbar(DB_DATA_WINDOW, orient=VERTICAL)
    scrollbar.pack( side = RIGHT, fill = Y )

    hscrollbar = Scrollbar(DB_DATA_WINDOW, orient=HORIZONTAL)
    hscrollbar.pack( side = BOTTOM, fill = X )

    mylist = Listbox(DB_DATA_WINDOW, yscrollcommand = scrollbar.set,xscrollcommand=hscrollbar.set, width=145, height=25)
    if isinstance(DB_TEXT, str):
        DB_TEXT = [DB_TEXT]
    for line in range(len(DB_TEXT)):
        mylist.insert(END, str(line) + ") " + DB_TEXT[line])

    mylist.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview )
    hscrollbar.config( command = mylist.xview )
    DB_SCR = scrollbar
    DB_LV = mylist
    DB_HSCR = hscrollbar

def create_data_window_images_db():
    global DB_DATA_WINDOW, DB_IMAGES, DB_SCR, DB_LV, DB_HSCR
    if DB_SCR and DB_LV and DB_HSCR:
        destroyer([DB_SCR, DB_LV, DB_HSCR])
    scrollbar = Scrollbar(DB_DATA_WINDOW)
    scrollbar.pack( side = RIGHT, fill = Y )

    hscrollbar = Scrollbar(DB_DATA_WINDOW, orient=HORIZONTAL)
    hscrollbar.pack( side = BOTTOM, fill = X )

    mylist = Listbox(DB_DATA_WINDOW, yscrollcommand = scrollbar.set,xscrollcommand=hscrollbar.set,  width=145, height=25)
    if isinstance(DB_IMAGES, str):
        DB_IMAGES = [DB_IMAGES]
    for line in range(len(DB_IMAGES)):
        mylist.insert(END, str(line) + ") " + DB_IMAGES[line])

    mylist.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview )
    hscrollbar.config( command = mylist.xview )
    DB_SCR = scrollbar
    DB_LV = mylist
    DB_HSCR = hscrollbar

def create_data_window_videos_db():
    global DB_DATA_WINDOW, DB_VIDEOS, DB_SCR, DB_LV, DB_HSCR
    if DB_SCR and DB_LV and DB_HSCR:
        destroyer([DB_SCR, DB_LV, DB_HSCR])
    scrollbar = Scrollbar(DB_DATA_WINDOW)
    scrollbar.pack( side = RIGHT, fill = Y )

    hscrollbar = Scrollbar(DB_DATA_WINDOW, orient=HORIZONTAL)
    hscrollbar.pack( side = BOTTOM, fill = X )

    mylist = Listbox(DB_DATA_WINDOW, yscrollcommand = scrollbar.set,xscrollcommand=hscrollbar.set,  width=145, height=25)
    if isinstance(DB_VIDEOS, str):
        DB_VIDEOS = [DB_VIDEOS]
    for line in range(len(DB_VIDEOS)):
        mylist.insert(END, str(line) + ") " + DB_VIDEOS[line])

    mylist.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview )
    hscrollbar.config( command = mylist.xview )
    DB_SCR = scrollbar
    DB_LV = mylist
    DB_HSCR = hscrollbar

def create_data_window_tables_db():
    global DB_DATA_WINDOW, DB_TABLES, DB_SCR, DB_LV, DB_HSCR
    if DB_SCR and DB_LV and DB_HSCR:
        destroyer([DB_SCR, DB_LV, DB_HSCR])
    scrollbar = Scrollbar(DB_DATA_WINDOW)
    scrollbar.pack( side = RIGHT, fill = Y )

    hscrollbar = Scrollbar(DB_DATA_WINDOW, orient=HORIZONTAL)
    hscrollbar.pack( side = BOTTOM, fill = X )

    mylist = Listbox(DB_DATA_WINDOW, yscrollcommand = scrollbar.set,xscrollcommand=hscrollbar.set,  width=145, height=25)
    if isinstance(DB_TABLES, str):
        DB_TABLES = [DB_TABLES]
    for line in range(len(DB_TABLES)):
        if isinstance(DB_TABLES[line], pd.core.frame.DataFrame):
            mylist.insert(END, "Table# {}".format(line+1))
            mylist.insert(END, "_______________________")
            for i in range(len(DB_TABLES[line])):
                mylist.insert(END, DB_TABLES[line].iloc[i, :])
        else:
            mylist.insert(END, DB_TABLES[line])

    mylist.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = mylist.yview )
    hscrollbar.config( command = mylist.xview )
    DB_SCR = scrollbar
    DB_LV = mylist
    DB_HSCR = hscrollbar
############################################################################################################################################

def save_data_to_database():
    global PARENT_PATH, TEXT, TABLES, IMAGES, VIDEOS, SECOND_WINDOW, URL

    unique_key = DataBase().parse_key(URL)
    if os.path.isdir(os.path.join(PARENT_PATH, unique_key)):
        pass #ToDo Matching and differences algorithm
    else:
        os.makedirs(os.path.join(PARENT_PATH, unique_key))
    save_path = os.path.join(PARENT_PATH, unique_key)

    with open(os.path.join(save_path, 'text'), "w", encoding='utf8', errors='ignore')as f:
        f.write("\n".join(TEXT))
    with open(os.path.join(save_path, 'images'), "w", encoding='utf8', errors='ignore')as f:
        f.write("\n".join(IMAGES))
    with open(os.path.join(save_path, 'videos'), "w", encoding='utf8', errors='ignore')as f:
        f.write("\n".join(VIDEOS))
    for i in range(len(TABLES)):
        if isinstance(TABLES[i], pd.core.frame.DataFrame):
            TABLES[i].to_csv(os.path.join(save_path, "table-{}.csv".format(i)))
    print("[INFO] Data Saved Successfully.")
    SECOND_WINDOW.destroy()

def destroy_second_window():
    global SECOND_WINDOW
    SECOND_WINDOW.destroy()

# this is the function called when the button is clicked
def show_data_window():
    global  DATA_WINDOW, SECOND_WINDOW
    print('clicked')
    window = tk.Toplevel(root)
    SECOND_WINDOW = window
    disp_wind = tk.Canvas(window, height=592, width=891)
    window.resizable(0, 0)
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
    save_data_inside = Button(window, text='Save', bg='#00FF00', font=('arial', 12, 'normal'),command=save_data_to_database, state="normal")#disabled
    save_data_inside.place(x=450-40, y=550)
    gp_back = Button(window, text='Discard', bg='#00FF00', font=('arial', 12, 'normal'), command=destroy_second_window, state="normal")
    gp_back.place(x=880-70, y=550)


def show_database_window():
    global DB_DATA_WINDOW, DB_SECOND_WINDOW
    def list_urls_tab_value(selection):
        global DB_TEXT, DB_IMAGES, DB_VIDEOS, DB_TABLES
        key = urls_ids[selection]
        print("[INFO] FOLDER KEY ", key)
        data_path = os.path.join(PARENT_PATH, key)
        text = []
        images = []
        videos = []
        tables = []
        csv_cnt = 0
        with open(os.path.join(data_path, 'text'), encoding='utf8', errors='ignore')as f:
            text = f.read().split("\n")
        with open(os.path.join(data_path, 'images'), encoding='utf8', errors='ignore')as f:
            images = f.read().split("\n")
        with open(os.path.join(data_path, 'videos'), encoding='utf8', errors='ignore')as f:
            videos = f.read().split("\n")
        csv_files = os.listdir(data_path)
        for each in csv_files:
            if '.csv' in each:
                csv_cnt += 1
        print("[INFO] {} CSV Files Found".format(str(csv_cnt)))
        for i in range(csv_cnt):
            tables.append(pd.read_csv(os.path.join(data_path, "table-{}.csv".format(i) )))
        DB_TEXT = text
        DB_IMAGES = images
        DB_VIDEOS = videos
        DB_TABLES = tables
        ##################################################### INNER FUNCTION ENDS HERE

    window3 = tk.Toplevel(root)
    disp_wind = tk.Canvas(window3, height=592, width=891)
    window3.resizable(0, 0)
    DB_SECOND_WINDOW = window3
    disp_wind.pack()
    disp_wind.configure(background='#FFFFFF')
    text_data = Button(window3, text='Text Data', bg='#00FF00', font=('arial', 12, 'normal'), command=create_data_window_text_db, state="normal")
    text_data.place(x=100+120, y=50)
    tables_data = Button(window3, text='Tablular Data', bg='#00FF00', font=('arial', 12, 'normal'), command=create_data_window_tables_db, state="normal")
    tables_data.place(x=185+120, y=50)
    images_data = Button(window3, text='Media - Images', bg='#00FF00', font=('arial', 12, 'normal'), command=create_data_window_images_db, state="normal")
    images_data.place(x=295+120, y=50)
    videos_data = Button(window3, text='Media - Videos', bg='#00FF00', font=('arial', 12, 'normal'), command=create_data_window_videos_db, state="normal")
    videos_data.place(x=420+120, y=50)
    ttk.Separator(window3, orient='horizontal').place(x=0, y=85, relwidth=6)
    data_window = tk.Canvas(window3, height=450, width=891)
    data_window.place(x=0, y=95)
    DB_DATA_WINDOW = data_window
    urls_ids = DataBase().get_urls()
    if isinstance(urls_ids, dict):
        list_urls = []
        for each in urls_ids.keys():
            list_urls.append(each)
        variable = StringVar(window3)
        variable.set("Select URL")
        list_urls_tab = OptionMenu(window3, variable, *list_urls, command=list_urls_tab_value)
        list_urls_tab.config(bg='#00FF00')
        list_urls_tab.place(x=0, y=0)

def validate_url(url):
    try:
        result = urlparse(url)
        sleep(1.5)
        return all([result.scheme, result.netloc])
    except:
        return False

def btnStartScraping():
    is_valid_url = False
    global error_msg_lbl, status_msg_lbl, TEXT, TABLES, IMAGES, VIDEOS, URL, show_data, save_data
    status_msg_lbl.destroy()
    status_msg_lbl = Label(root, text='', fg='#00FF00', bg='#FFFFFF', font=('arial', 12, 'normal'))
    status_msg_lbl.config(text='Validating URL')
    status_msg_lbl.config(fg="black")
    status_msg_lbl.place(x=300, y=220)
    root.update()
    url = tInput.get()
    URL = url
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
    

    if is_valid_url:
        status_msg_lbl.destroy()
        status_msg_lbl = Label(root, text='', fg='#00FF00', bg='#FFFFFF', font=('arial', 12, 'normal'))
        status_msg_lbl.config(text='Scrapping Data...')
        status_msg_lbl.config(fg="black")
        status_msg_lbl.place(x=300, y=220)
        root.update()
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
    status_msg_lbl.destroy()
    status_msg_lbl = Label(root, text='', fg='#00FF00', bg='#FFFFFF', font=('arial', 12, 'normal'))
    status_msg_lbl.config(text='Ready')
    status_msg_lbl.place(x=300, y=220)
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
root.resizable(0, 0)


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
show_data = Button(root, text='Show Data', bg='#00FF00', font=('arial', 12, 'normal'), command=show_data_window, state="disabled")#disabled
show_data.place(x=272, y=413)
show_data.bind("<Enter>", on_enter_show_data)
show_data.bind("<Leave>", on_leave_show_data)

# This is the section of code which creates a button
save_data = Button(root, text='Show Saved Data', bg='#00FF00', font=('arial', 12, 'normal'), command=show_database_window, state="normal")
save_data.place(x=370, y=413)
save_data.bind("<Enter>", on_enter_save_data)
save_data.bind("<Leave>", on_leave_save_data)

root.mainloop()
