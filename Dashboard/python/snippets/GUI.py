from tkinter import Tk, Label, Button, Entry, Canvas

class NakitAkisHesaplamaGUI:
	def __init__(self, master):
		self.master = master
		
		master.title("GetToken")

		self.w = Canvas(master, width=200, height=200)
		self.w.config(bg='white')
		self.w.pack()

		self.label = Label(master, text="GetToken")
		self.label.pack()
		
		self.entry = Entry(master)
		self.entry.pack()

		self.greet_button = Button(master, text="Send", command=self.greet)
		self.greet_button.pack()
		
		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()

	def greet(self): 
		x = self.entry.get()
		print(x)
		print("Sending Request...")

root = Tk()
my_gui = NakitAkisHesaplamaGUI(root)
root.mainloop()