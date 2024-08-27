import paramiko
import sys
from tkinter import *
import ttkbootstrap as tb
from collections import OrderedDict
import threading


metersize1 = 150


root = tb.Window(themename="superhero")
root.title("Mon Appli")
root.geometry('1000x500')
my_notebook = tb.Notebook(root)
my_notebook.grid()

tab1 = tb.Frame(my_notebook)
tab2 = tb.Frame(my_notebook)

my_notebook.add(tab1, text="  Cockpit  ")
my_notebook.add(tab2, text="  Battery  ")

style = tb.Style()
style.configure('TNotebook.Tab', font=('URW Gothic L','35','bold'), padding=[50, 50])

b1 = tb.Button(tab1, text="TEST")

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

vin_meter.grid(column=0,row=0)
b1.grid(column=1,row=0)

root.mainloop()
