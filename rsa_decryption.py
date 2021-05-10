import math
from tkinter import *
from tkinter import messagebox

def rsa_dec():
    root = Tk()

    root.title("RSA ALGORITHM")

    canvas = Canvas(root, height=400, width=700, bg="#A3E4D7")
    canvas.pack()

    frame = Frame(root, bg="#D0ECE7")
    frame.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

    def act():
            p['state'] = 'normal'
            p.delete(0,END)
            q['state'] = 'normal'
            q.delete(0,END)
            ct_e['state'] = 'normal'
            ct_e.delete(0,END)
            pk.config(text="")
            prk.config(text="")
            pt_e['state'] = 'normal'
            pt_e.delete(0, END)
            myButton1['state'] = 'normal'

    def dis():
        p['state'] = 'readonly'
        q['state'] = 'readonly'
        ct_e['state'] = 'readonly'
        pt_e['state'] = 'readonly'
        myButton1['state'] = 'disabled'

    def prime_check(a):
        if(a==2):
            return True
        elif((a<2) or ((a%2)==0)):
            return False
        elif(a>2):
            for i in range(2,a):
                if not(a%i):
                    return False
        return True

    def egcd(e,r):
        while(r!=0):
            e,r=r,e%r
        return e

    def eugcd(e,r):
        for i in range(1,r):
            while(e!=0):
                a,b=r//e,r%e
                if(b!=0):
                    print("%d = %d*(%d) + %d"%(r,a,e,b))
                r=e
                e=b

    def eea(a,b):
        if(a%b==0):
            return(b,0,1)
        else:
            gcd,s,t = eea(b,a%b)
            s = s-((a//b) * t)
            print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
            return(gcd,t,s)

    def mult_inv(e,r):
        gcd,s,_=eea(e,r)
        if(gcd!=1):
            return None
        else:
            if(s<0):
                print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
            elif(s>0):
                print("s=%d."%(s))
            return s%r

    def encrypt(pub_key,n_text):
        e,n=pub_key
        x=[]
        m=0
        for i in n_text:
            if(i.isupper()):
                m = ord(i)-65
                c=(m**e)%n
                x.append(c)
            elif(i.islower()):               
                m= ord(i)-97
                c=(m**e)%n
                x.append(c)
            elif(i.isspace()):
                spc=400
                x.append(spc)
        return x

    def decrypt(priv_key,c_text):
        d,n=priv_key
        txt=c_text.split(',')
        x=''
        m=0
        for i in txt:
            if(i==400):
                x+=' '
            else:
                m=(int(i)**d)%n
                m+=97
                c=chr(m)
                x+=c
        return x

    def rsa_algo():
        if p.get().isdigit() and q.get().isdigit() and ct_e.get():
            check_p = prime_check(int(p.get()))
            check_q = prime_check(int(q.get()))
            def check_data():
                if(((check_p==False) or (check_q==False))):
                    messagebox.showinfo("error", "Please enter Prime value only!!")
                    p.delete(0, END)
                    q.delete(0, END)
                    return False
                else:
                    return True

            if check_data() == True:
                n = int(p.get()) * int(q.get())
                phi= (int(p.get())-1)*(int(q.get())-1)
                for i in range(1,1000):
                    if(egcd(i,phi)==1):
                        e=i
                eugcd(e,phi)
                d = mult_inv(e,phi)
                public = (e,n)
                private = (d,n)
                pk.config(text="{}".format(public))
                prk.config(text="{}".format(private))
                pt_e.insert(0, "{}".format(decrypt(private,ct_e.get())))
                dis()
        elif p.get().isdigit()==False or q.get().isdigit()==False:
            messagebox.showinfo("error", "Please enter only Integers in p and q entries!!")
        else:
            messagebox.showinfo("error", "Please enter Chiper Text with(,) for Decryption")

    label0 = Label(frame, text="RSA Algorithm for Decryption", bg="#D0ECE7", font=("Tahoma", 20, "bold"))
    label0.pack(padx=10)

    label = Label(frame, text="Enter Prime number as p and q: ", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    label.pack(padx=10)
    label.place(x=10, y=70)

    label_p = Label(frame, text="p: ", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    label_p.pack(side=LEFT, padx=10)
    label_p.place(x=350, y=70)

    p = Entry(frame, width=10, font=("Tahoma", 14, "normal"))
    p.pack()
    p.place(x=380, y=75)

    label_q = Label(frame, text="q: ", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    label_q.pack(side=LEFT, padx=10)
    label_q.place(x=500, y=70)

    q = Entry(frame, width=10, font=("Tahoma", 14, "normal"))
    q.pack()
    q.place(x=530, y=75)

    labelAB = Label(frame, text="Calculated Public and Private Keys: ", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    labelAB.pack(padx=10)
    labelAB.place(x=10, y=130)

    label_pk = Label(frame, text="Public Key: ", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    label_pk.pack(side=LEFT, padx=10)
    label_pk.place(x=100, y=170)

    pk = Label(frame, font=("Tahoma", 14, "normal"), bg='#D0ECE7')
    pk.pack()
    pk.place(x=210, y=170)

    label_prk = Label(frame, text="Private Key: ", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    label_prk.pack(side=LEFT, padx=10)
    label_prk.place(x=350, y=170)

    prk = Label(frame, font=("Tahoma", 14, "normal"), bg='#D0ECE7')
    prk.pack()
    prk.place(x=460, y=170)

    ct = Label(frame, text="Enter Chiper Text for decryption with (,):", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    ct.pack(padx=10)
    ct.place(x=10, y=220)

    ct_e = Entry(frame, width=27, font=("Tahoma", 14, "normal"))
    ct_e.pack()
    ct_e.place(x=360, y=223)

    pt = Label(frame, text="Plain Text after decryption:", bg="#D0ECE7", font=("Tahoma", 14, "normal"))
    pt.pack(padx=10)
    pt.place(x=10, y=263)

    pt_e = Entry(frame, width=27, font=("Tahoma", 14, "normal"))
    pt_e.pack()
    pt_e.place(x=360, y=263)

    myButton1 = Button(frame, text="Decrypt", font=("calibri", 15,'bold'), bg='#A3E4D7', width=12, command=rsa_algo)
    myButton2 = Button(frame, text="Reload", font=("calibri", 15,'bold'), bg='#A3E4D7', width=12, command=act)

    myButton1.pack(padx=80)
    myButton1.place(x=200, y=325)
    myButton2.pack(padx=80)
    myButton2.place(x=375, y=325)

    root.resizable(False, False)
    root.mainloop()