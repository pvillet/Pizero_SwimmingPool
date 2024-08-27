import paramiko
import sys
from tkinter import *
import ttkbootstrap as tb
from collections import OrderedDict
import threading


metersize1 = 150

# Global variables
filtering_choice="auto"

def set_filtering_choice(choice):
    filtering_choice=choice
    print("Filering_Choice=%s"%filtering_choice)


root = tb.Window(themename="superhero")
root.title("My Swimming Pool")
root.geometry('1000x500')
my_notebook = tb.Notebook(root)
my_notebook.grid()

tab1 = tb.Frame(my_notebook)
tab2 = tb.Frame(my_notebook)

my_notebook.add(tab1, text="  Cockpit  ")
my_notebook.add(tab2, text="  Summary  ")

style = tb.Style()
style.configure('TNotebook.Tab', font=('URW Gothic L','30','bold'), padding=[50, 50])

# Create a Frame for Filtering stuff
filter_frame = Frame(tab1)
#filter_frame.pack(pady=50,padx=10)
filter_frame.grid(row=0,column=0,padx=10)

filter_label        = tb.Label(filter_frame,  text="FILTRATION", anchor='center',font=('bold'),bootstyle="inverse",width=12)
stop_filter_button  = tb.Button(filter_frame, text="ARRET",  command=lambda: set_filtering_choice("stop") , width=12)
start_filter_button = tb.Button(filter_frame, text="MARCHE", command=lambda: set_filtering_choice("start"), width=12)
auto_filter_button  = tb.Button(filter_frame, text="AUTO",   command=lambda: set_filtering_choice("auto") , width=12)

filter_label.pack(pady=10)
stop_filter_button.pack(pady=10)
start_filter_button.pack(pady=10)
auto_filter_button.pack(pady=10)

# Create a Frame for Cleaning stuff
clean_frame = Frame(tab1)
#clean_frame.pack(pady=50,padx=10)
clean_frame.grid(row=0,column=1,padx=10)

clean_label        = tb.Label(clean_frame,  text="ROBOT", anchor='center',font=('bold'),bootstyle="inverse",width=12)
stop_clean_button  = tb.Button(clean_frame, text="ARRET",  command=lambda: set_filtering_choice("stop") , width=12)
start_clean_button = tb.Button(clean_frame, text="MARCHE", command=lambda: set_filtering_choice("start"), width=12)
auto_clean_button  = tb.Button(clean_frame, text="AUTO",   command=lambda: set_filtering_choice("auto") , width=12)

clean_label.pack(pady=10)
stop_clean_button.pack(pady=10)
start_clean_button.pack(pady=10)
auto_clean_button.pack(pady=10)



vin_meter = tb.Meter(tab1, bootstyle="light",
        subtext="VIN",
        interactive=False,
        textright="V",
        #textleft="$"
        metertype="semi", # Can be semi
        stripethickness=20,
        metersize=metersize1,
        padding=20,
        amountused=0,
        amounttotal=20, #20Volts max
        subtextstyle="light"
        )

#vin_meter.grid(column=0,row=0)
root.mainloop()
