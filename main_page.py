import sys
sys.path.append('..')

from scripts.deffie_hellmen_encryption import *
from scripts.deffie_hellmen_decryption import *
from scripts.rsa_encryption import *
from scripts.rsa_decryption import *

from tkinter import *
from tkinter import messagebox
from random import randint

def home_display():

	root1 = Tk()

	root1.title("Encoder - Decoder System")	

	def f1():
		root1.destroy()
		encryption()

	def f2():
		root1.destroy()
		decryption()

	def f3():
		root1.destroy()
		key_exchange()	

	canvas = Canvas(root1, height=150, width=400, bg="#A3E4D7")
	canvas.pack()

	frame = Frame(root1, bg="#D0ECE7")
	frame.place(relwidth=0.95, relheight=0.8, relx=0.025, rely=0.1)

	label = Label(frame, text="Encoder - Decoder System", bg="#D0ECE7", font=("Tahoma", 20, "bold"))
	label.pack()

	myButton1 = Button(frame, text="Encryption", font=("calibri", 15,'bold'), bg='#A3E4D7', command=f1)
	myButton2 = Button(frame, text="Decryption", font=("calibri", 15,'bold'), bg='#A3E4D7', command=f2)

	myButton1.pack()
	myButton1.place(x=50, y=60)
	myButton2.pack()
	myButton2.place(x=200, y=60)

	root1.resizable(False, False)
	root1.mainloop() 

def decryption():
	root3 = Tk()
	root3.title("Decryption")

	def f1():
		root3.destroy()
		home_display()

	def ff1():
		deff_hell_dec()

	def ff2():
		rsa_dec()

	canvas = Canvas(root3, height=250, width=400, bg="#A3E4D7")
	canvas.pack()

	frame = Frame(root3, bg="#D0ECE7")
	frame.place(relwidth=0.90, relheight=0.90, relx=0.05, rely=0.04)

	label = Label(frame, text="Decryption System", bg="#D0ECE7", font=("Tahoma", 20, "bold"))
	label.pack()

	label1 = Label(frame, text="Select Key generation option:", bg="#D0ECE7", font=("Tahoma", 13, "normal"), padx=20)
	label1.place(x=5, y=50)

	var = IntVar()

	R1 = Radiobutton(frame, text="Deffi-Hellmen Algorithm", variable=var, value=1, font=("Tahoma", 12, "normal"), bg="#D0ECE7", command=ff1)
	R1.place(x=60, y=80)

	R2 = Radiobutton(frame, text="RSA Algorithm", variable=var, value=2, font=("Tahoma", 12, "normal"), bg="#D0ECE7", command=ff2)
	R2.place(x=60, y=110)

	myButton2 = Button(frame, text="Back", font=("calibri", 15,'bold'), bg='#A3E4D7', padx=20, command=f1)

	myButton2.place(x=150, y=170)

	root3.resizable(False, False)
	root3.mainloop()

def encryption():
	root3 = Tk()
	root3.title("Encryption")

	def f1():
		root3.destroy()
		home_display()

	def ff1():
		deff_hell_enc()

	def ff2():
		rsa_enc()

	canvas = Canvas(root3, height=250, width=400, bg="#A3E4D7")
	canvas.pack()

	frame = Frame(root3, bg="#D0ECE7")
	frame.place(relwidth=0.90, relheight=0.90, relx=0.05, rely=0.04)

	label = Label(frame, text="Encryption System", bg="#D0ECE7", font=("Tahoma", 20, "bold"))
	label.pack()

	label1 = Label(frame, text="Select Key generation option:", bg="#D0ECE7", font=("Tahoma", 13, "normal"), padx=20)
	label1.place(x=5, y=50)

	var = IntVar()

	R1 = Radiobutton(frame, text="Deffi-Hellmen Algorithm", variable=var, value=1, font=("Tahoma", 12, "normal"), bg="#D0ECE7", command=ff1)
	R1.place(x=60, y=80)

	R2 = Radiobutton(frame, text="RSA Algorithm", variable=var, value=2, font=("Tahoma", 12, "normal"), bg="#D0ECE7", command=ff2)
	R2.place(x=60, y=110)

	myButton2 = Button(frame, text="Back", font=("calibri", 15,'bold'), bg='#A3E4D7', padx=20, command=f1)

	myButton2.place(x=150, y=170)

	root3.resizable(False, False)
	root3.mainloop()