from random import randint
from tkinter import *
from tkinter import messagebox

def deff_hell_enc():
    root = Tk()

    root.title("Deffie-Hellmen Algorithm")

    canvas = Canvas(root, height=400, width=700, bg="#A3E4D7")
    canvas.pack()

    frame = Frame(root, bg="#D0ECE7")
    frame.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

    def act():
        P['state'] = 'normal'
        P.delete(0,END)
        G['state'] = 'normal'
        G.delete(0,END)
        A['state'] = 'normal'
        A.delete(0,END)
        B['state'] = 'normal'
        B.delete(0,END)
        pt_e['state'] = 'normal'
        pt_e.delete(0,END)
        Ka.config(text="")
        Kb.config(text="")
        ct_e['state'] = 'normal'
        ct_e.delete(0,END)
        myButton1['state'] = 'normal'

    def dis():
        P['state'] = 'readonly'
        G['state'] = 'readonly'
        A['state'] = 'readonly'
        B['state'] = 'readonly'
        pt_e['state'] = 'readonly'
        ct_e['state'] = 'readonly'
        myButton1['state'] = 'disabled'

    def encryption(msg, k, p):
        x = ''
        for i in msg:
            if(i.isupper()):
                m = ord(i)-65
                c = (m+k) % p
                c+=65
                x += chr(c)
            elif(i.islower()):               
                m = ord(i)-97
                c = (m+k) % p
                c+=97
                x += chr(c)
            elif(i.isspace()):
                x += " "
        ct_e.insert(0, "{}".format(x))

    def calculate_key():
        p = int(P.get())
        g = int(G.get())
        a = int(A.get())
        x = int(pow(g,a,p))
        b = int(B.get())
        y = int(pow(g,b,p))
        ka = int(pow(y,a,p))
        kb = int(pow(x,b,p))
        Ka.config(text=ka)
        Kb.config(text=kb)
        encryption(pt_e.get(), ka, p)
        dis()

    def pt_check():
        if pt_e.get().isalpha():
            return True
        else:
            return False

    def G_value():
        if G.get().isdigit():
            n = int(G.get())
            if n > 0 and n < int(P.get()):
                if A.get().isdigit():
                    if B.get().isdigit():
                        if pt_check() == True:
                            calculate_key()
                        else:
                            messagebox.showerror("Error", "Please enter Plain Text as a Alphabets only!!")
                            return False
                    else:
                        messagebox.showerror("Error", "Please enter Integers in B only!!")
                        return False
                else:
                    messagebox.showerror("Error", "Please enter Integers in A only!!") 
                    return False 
            else:
                messagebox.showerror("Error", "G should be between 0 < G < P!!\nPlease select Correct One!!")
                G.delete(0,END)
                return False
        else:
            messagebox.showerror("Error", "Please enter Integers in G only!!")
            return False

    def prime():
        if P.get().isdigit():
            n = int(P.get())
            if n > 1:
                for i in range(2, int(n/2)+1):
                    # If num is divisible by any number between
                    # 2 and n / 2, it is not prime
                    if (n % i) == 0:
                        messagebox.showerror("Error", "P is not a Prime Number!!\nPlease select Prime Number!!")
                        P.delete(0,END)
                        break
                    else:
                        G_value()
                        break
            else:
                messagebox.showerror("Error", "P is not a Prime Number!!\nPlease select Prime Number!!")
                P.delete(0,END)
        else:
            messagebox.showerror("Error", "Please enter Integers in P only!!")
            return False

    label0 = Label(frame, text="Deffie-Hellmen Algorithm for Encryption", bg="#D0ECE7", font=("Tahoma", 20, "bold"))
    label0.pack(padx=10)

    label = Label(frame, text="Enter Public Keys P and G: ", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    label.pack(padx=10)
    label.place(x=10, y=70)

    label_P = Label(frame, text="P: ", bg="#D0ECE7", font=("Tahoma", 16, "normal"))
    label_P.pack(side=LEFT, padx=10)
    label_P.place(x=350, y=70)

    P = Entry(frame, width=10, font=("Tahoma", 16, "normal"))
    P.pack()
    P.place(x=380, y=70)

    label_G = Label(frame, text="G: ", bg="#D0ECE7", font=("Tahoma", 16, "normal"))
    label_G.pack(side=LEFT, padx=10)
    label_G.place(x=500, y=70)

    G = Entry(frame, width=10, font=("Tahoma", 16, "normal"))
    G.pack()
    G.place(x=530, y=70)

    labelA = Label(frame, text="Enter Private Keys of A and B: ", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    labelA.pack(padx=10)
    labelA.place(x=10, y=110)

    label_A = Label(frame, text="A: ", bg="#D0ECE7", font=("Tahoma", 16, "normal"))
    label_A.pack(side=LEFT, padx=10)
    label_A.place(x=350, y=110)

    A = Entry(frame, width=10, font=("Tahoma", 16, "normal"))
    A.pack()
    A.place(x=380, y=110)

    label_B = Label(frame, text="B: ", bg="#D0ECE7", font=("Tahoma", 16, "normal"))
    label_B.pack(side=LEFT, padx=10)
    label_B.place(x=500, y=110)

    B = Entry(frame, width=10, font=("Tahoma", 16, "normal"))
    B.pack()
    B.place(x=530, y=110)

    labelAB = Label(frame, text="Calculated Secret Keys of A and B: ", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    labelAB.pack(padx=10)
    labelAB.place(x=10, y=150)

    label_KA = Label(frame, text="Ka: ", bg="#D0ECE7", font=("Tahoma", 16, "normal"))
    label_KA.pack(side=LEFT, padx=10)
    label_KA.place(x=340, y=150)

    Ka = Label(frame, font=("Tahoma", 16, "normal"), bg='#D0ECE7')
    Ka.pack()
    Ka.place(x=380, y=150)

    label_KB = Label(frame, text="Kb: ", bg="#D0ECE7", font=("Tahoma", 16, "normal"))
    label_KB.pack(side=LEFT, padx=10)
    label_KB.place(x=489, y=150)

    Kb = Label(frame, font=("Tahoma", 16, "normal"), bg='#D0ECE7')
    Kb.pack()
    Kb.place(x=530, y=150)

    pt = Label(frame, text="Enter Plain Text for encryption:", bg="#D0ECE7", font=("Tahoma", 16, "normal"))
    pt.pack(padx=10)
    pt.place(x=10, y=210)

    pt_e = Entry(frame, width=27, font=("Tahoma", 16, "normal"))
    pt_e.pack()
    pt_e.place(x=340, y=213)

    ct = Label(frame, text="Cipher Text after encryption:", bg="#D0ECE7", font=("Tahoma", 16, "normal"))
    ct.pack(padx=10)
    ct.place(x=10, y=250)

    ct_e = Entry(frame, width=27, font=("Tahoma", 16, "normal"))
    ct_e.pack()
    ct_e.place(x=340, y=253)

    myButton1 = Button(frame, text="Encrypt", font=("calibri", 15,'bold'), bg='#A3E4D7', width=8, command=prime)
    myButton2 = Button(frame, text="Reload", font=("calibri", 15,'bold'), bg='#A3E4D7', width=8, command=act)

    myButton1.pack(padx=80)
    myButton1.place(x=190, y=320)
    myButton2.pack(padx=80)
    myButton2.place(x=380, y=320)

    root.resizable(False, False)
    root.mainloop()

