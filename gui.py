import os
import math
import tkinter

from tkinter import ttk

mainWindow = tkinter.Tk()
row_max = 10
col_max = 10
maxValue = 100


def progress(currentValue):
    progressbar["value"] = currentValue


progressbar = ttk.Progressbar(
    mainWindow, orient="horizontal", length=300, mode="determinate")
progressbar.grid(row=0, column=0, columnspan=3)

currentValue = 0
progressbar["value"] = currentValue
progressbar["maximum"] = maxValue
divisions = 10

dir_path = os.path.dirname(os.path.realpath(__file__))
#icon_path = dir_path + r'/favicon.ico'
mainWindow.title("Grid Demo")
# mainWindow.iconbitmap(icon_path)
mainWindow.geometry('640x480')
for i in range(divisions):
    currentValue = currentValue+10
    progressbar.after(500, progress(currentValue))
    progressbar.update()  # Force an update of the GUI
progressbar.grid_forget()

label = tkinter.Label(mainWindow, text="Instrument List Processor")
label.grid(row=0, column=0, columnspan=math.floor(col_max/2))


mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)


fileList = tkinter.Listbox(mainWindow)
label1 = tkinter.Label(mainWindow, text="Please select instrument list")
label1.grid(row=0, column=0, columnspan=1)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir(dir_path):  # '/Windows/System32'
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(
    mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# frame for the radio buttons
optionFrame = tkinter.LabelFrame(
    mainWindow, text="File Details For Processing")
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(0)
# Radio buttons
radio1 = tkinter.Radiobutton(
    optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(
    optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(
    optionFrame, text="Timestamp", value=3, variable=rbValue)
radio4 = tkinter.Radiobutton(
    optionFrame, text="Location", value=4, variable=rbValue)
radio5 = tkinter.Radiobutton(
    optionFrame, text="Number", value=5, variable=rbValue)


radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')
radio4.grid(row=3, column=0, sticky='w')
radio5.grid(row=4, column=0, sticky='w')

mainWindow.mainloop()

print(rbValue.get())
