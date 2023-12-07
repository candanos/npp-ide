from tkinter import *
from tkinter import messagebox  

#reportName = ""
def listboxSelect(event):
	widget = event.widget
	selection=widget.curselection()
	value = widget.get(selection[0])
	global reportName
	reportName = value

def submit(reportName):
	print("lambda" + reportName)
	
master = Tk()
master.geometry("500x300")
frame = Frame(master)
frame.pack()
label = Label(master,text = "Name")
label.place(x = 10, y = 10)  
listbox = Listbox(master, width = 30)
listbox.place(x = 10, y = 50)
listbox.insert(END, "01-BCVALTAB Mutabakat.")
listbox.insert(END, "02-Next Faiz Tarihi.")
listbox.insert(END, "03-Tahakkuk Sayilari.")
listbox.insert(END, "04-BFZKMTAH Mutabakat.")
listbox.insert(END, "05-Son Faiz Tarihi.")
listbox.insert(END, "06-Reeskont Tutarlari.")
listbox.bind('<<ListboxSelect>>',listboxSelect)
button1 = Button(master, text = "Submit", command=lambda: submit(reportName))
button1.place(x = 10, y = 250)

master.mainloop()
