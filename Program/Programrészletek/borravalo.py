from tkinter import *
from PIL import Image, ImageTk
import math

def bor_szamitas():
    try:
        borossz=float(bore.get())
        borvalo=float(bore1.get())
        borvalo0=borvalo/100
        borveg=borossz*borvalo0
        borvegossz=borossz+borveg
        borvaloszov.config(text=borveg)
        borvegeszov.config(text=borvegossz)


    except:
        borvaloszov.config(text="Hibás bemenet!")
        borvegeszov.config(text="Hibás bemenet!")




borablak=Tk()

borablak.config(bg="#6a92ef")
borablak.title("Kör kerülete és területe")
borsugszov=Label(borablak,text="Összege:", bg="#6a92ef", fg="white", font="Arial 15", padx=15, pady=15)
borsugszov.grid(row=2, column=1)
bore = Entry(borablak, width=20, font="Arial 15", bg="#4162b0", fg="white")
bore.grid(row=2, column=2)
borsugszov1=Label(borablak,text="Borravaló(%):", bg="#6a92ef", fg="white", font="Arial 15", padx=15, pady=15)
borsugszov1.grid(row=3, column=1)
bore1 = Entry(borablak, width=20, font="Arial 15", bg="#4162b0", fg="white")
bore1.grid(row=3, column=2)
borvegeszov=Label(borablak,text="Végösszege:", bg="#6a92ef", fg="white", font="Arial 15", padx=15)
borvegeszov.grid(row=5, column=1)
borvaloszov=Label(borablak,text="Borravaló:", bg="#6a92ef", fg="white", font="Arial 15", padx=15)
borvaloszov.grid(row=6, column=1)
borszamitas = Button(borablak, text="Számítás", bg="#4162b0", fg="white", font="Arial 15", command=bor_szamitas)
borszamitas.grid(row=4, column=2)
borki = Button(borablak, text="Kilépés", command=borablak.destroy, bg="#4162b0", fg="white", font="Arial 15")
borki.place(relx=0.03, rely=0.95, anchor=SW)
borvaloszov=Label(borablak, bg="#6a92ef", fg="white", font="Arial 15")
borvaloszov.grid(row=6, column=2)
borvegeszov=Label(borablak, bg="#6a92ef", fg="white", font="Arial 15")
borvegeszov.grid(row=5, column=2)
borcanvas = Canvas(borablak, width=250, height=250)
borcanvas.grid(column=3, row=2, rowspan=10, padx=40, pady=20)
borimage = (Image.open("Tervek\\Képek\\borravalo.jpg"))
atmeret_borimage = borimage.resize((250,250))
ujkep = ImageTk.PhotoImage(atmeret_borimage)
borcanvas.create_image(1,1,anchor=NW, image=ujkep)

borablak.minsize(650,300)
borablak.maxsize(650,300)
borablak.mainloop()