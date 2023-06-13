from tkinter import *
from PIL import Image, ImageTk
import math

def szamit():
    try:
        kamatA=float(kamata1.get())
        kamatB=float(kamatb1.get())
        kamatC=float(kamatc1.get())
        kamat1=((kamatB*kamatC)/100)+1
        kamat2=kamatA*kamat1
        kamatker.config(text=kamat2)
    except:
        kamatker.config(text="Hibás bemenet!")

kamatablak=Tk()

kamatablak.config(bg="#6a92ef")
kamatablak.title("Kamat")
kamatker=Label(kamatablak,text="Összeg:", bg="#6a92ef", fg="white", font="Arial 15", padx=15)
kamatker.grid(row=6, column=1)
kamatszamitas = Button(kamatablak, text="Számítás", bg="#4162b0", fg="white", font="Arial 15", command=szamit)
kamatszamitas.grid(row=5, column=2)
kamatki = Button(kamatablak, text="Kilépés", command=kamatablak.destroy, bg="#4162b0", fg="white", font="Arial 15")
kamatki.place(relx=0.03, rely=0.96, anchor=SW)
kamatker=Label(kamatablak, bg="#6a92ef", fg="white", font="Arial 15")
kamatker.grid(row=6, column=2)
kamatcanvas = Canvas(kamatablak, width=250, height=250)
kamatcanvas.grid(column=3, row=2, rowspan=10, padx=8, pady=20)
kamatimage = (Image.open("Tervek\\Képek\\kamat.jpg"))
atmeret_kamatimage = kamatimage.resize((250,250))
ujkep = ImageTk.PhotoImage(atmeret_kamatimage)
kamatcanvas.create_image(1,1,anchor=NW, image=ujkep)

kamata=Label(kamatablak,text="Pénzösszeg:" , bg="#6a92ef", fg="white", font="Arial 15", padx=10, pady=2)
kamata.grid(row=2, column=1)
kamata1 = Entry(kamatablak, width=20, font="Arial 15", bg="#4162b0", fg="white")
kamata1.grid(row=2, column=2)

kamatb=Label(kamatablak,text="Kamat(év):", bg="#6a92ef", fg="white", font="Arial 15", padx=10, pady=2)
kamatb.grid(row=3, column=1)
kamatb1 = Entry(kamatablak, width=20, font="Arial 15", bg="#4162b0", fg="white")
kamatb1.grid(row=3, column=2)

kamatc=Label(kamatablak,text="Futamidő(év):", bg="#6a92ef", fg="white", font="Arial 15", padx=10, pady=2)
kamatc.grid(row=4, column=1)
kamatc1 = Entry(kamatablak, width=20, font="Arial 15", bg="#4162b0", fg="white")
kamatc1.grid(row=4, column=2)

kamatablak.minsize(650,300)
kamatablak.maxsize(650,300)
kamatablak.mainloop()