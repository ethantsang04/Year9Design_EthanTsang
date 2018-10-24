#imports tkinter module to python so we can use it
from tkinter import *
#Tk makes window
master = Tk()

def return_entry(en):
	content = entry.get()
	print(content)
	
Label(master, text="Input: ").grid(row=0, sticky=W)

entry = Entry(master)
entry.grid(row=0, column=1)

entry.bind('<Return>', return_entry)

#keeps window open
mainloop()