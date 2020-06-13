from tkinter import *
class App():
	def __init__(self):
		window = Tk()
		window.title('extensive search')
		Label(window, text = "A min/max=").grid(row = 1, column = 1, sticky = E)
		Label(window, text = "B min/max=").grid(row = 2, column = 1, sticky = E)
		Label(window, text ="An min/max=").grid(row = 3, column = 1, sticky = E)
		Label(window, text =   "GroupID=").grid(row = 4, column = 1, sticky = E)
		Label(window, text =   "Howmany=").grid(row = 5, column = 1, sticky = E)
		

		self.A_min = StringVar()
		Entry(window, textvariable = self.A_min, justify = RIGHT).grid(row = 1, column = 2)
		self.A_max = StringVar()
		Entry(window, textvariable = self.A_max, justify = RIGHT).grid(row = 1, column = 3)
		self.B_min = StringVar()
		Entry(window, textvariable = self.B_min, justify = RIGHT).grid(row = 2, column = 2)
		self.B_max = StringVar()
		Entry(window, textvariable = self.B_max, justify = RIGHT).grid(row = 2, column = 3)
		self.An_min = StringVar()
		Entry(window, textvariable = self.An_min, justify = RIGHT).grid(row = 3, column = 2)
		self.An_max = StringVar()
		Entry(window, textvariable = self.An_max, justify = RIGHT).grid(row = 3, column = 3)
		self.Group_ID = StringVar()
		Entry(window, textvariable = self.Group_ID, justify = RIGHT).grid(row = 4, column = 3)
		self.Howmany = StringVar()
		Entry(window, textvariable = self.Howmany, justify = RIGHT).grid(row = 5, column = 3)

		Button(window, text = 'SEARCH', command = self.value).grid(row = 6, column = 3)	
		window.mainloop()
	def value(self):
		global maxa,mina,maxb,minb,maxan,minan,GroupID,Howmany
		maxa = self.A_max.get()
		mina = self.A_min.get() 
		maxb = self.B_max.get() 
		minb = self.B_min.get()
		maxan = self.An_max.get()
		minan = self.An_min.get()
		GroupID = self.Group_ID.get()
		Howmany = self.Howmany.get()
#		return maxa,mina,maxb,minb,maxan,minan,GroupID,Howmany
	def get_A(self):
		return (float(mina), float(maxa))
	def get_B(self):
		return (float(minb), float(maxb))
	def get_An(self):
		return (float(minan), float(maxan))
	def get_G(self):
		return (int(GroupID))
	def get_H(self):
		return [ int(i) for i in Howmany.split()]









