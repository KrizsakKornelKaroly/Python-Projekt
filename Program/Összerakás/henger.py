from tkinter import *
from PIL import Image, ImageTk
from math import *

def henger():
    hengersugarbe = hengersugar.get()
    hengermagassagbe = hengermagassag.get()
    try:
        hengersugarbe = int(hengersugarbe)
        hengermagassagbe = int(hengermagassagbe)
        hengerfelszin = round(2*(hengersugarbe**2)*pi + 2*hengersugarbe*pi*hengermagassagbe),"cm\u00b2"
        hengerterfogat = round(hengersugarbe**2 * pi * hengermagassagbe),"cm\u00b3"
        hengerfelszinki.config(text=hengerfelszin)
        hengerterfogatki.config(text=hengerterfogat)
    except:
        hengerfelszinki.config(text="Hibás bemenet!")
        hengerterfogatki.config(text="Hibás bemenet!")

hengerablak = Tk()
hengerablak.config(bg="#6A91EF")
hengerablak.title("Henger felszíne és térfogata")
#bemenet
hengersugar = Entry(hengerablak, width=20, font="Arial 15", bg="#4162b0",fg="white")
hengermagassag = Entry(hengerablak, width=20, font="Arial 15", bg="#4162b0",fg="white")
hengersugarszov = Label(hengerablak, text="Sugár: ",)
hengermagassagszov = Label(hengerablak, text="Magasság: ")
#szamitas
hengerszamitas = Button(hengerablak, text="Számítás",bg="#4162b0",fg="white", font="Arial 15", command=henger)
#kimenet
hengerfelszinszov = Label(hengerablak, text="Felszín: ")
hengerterfogatszov = Label(hengerablak, text="Térfogat: ")
hengerfelszinki = Label(hengerablak)
hengerterfogatki = Label(hengerablak)
#EXITc
hengerkilep = Button(hengerablak, text="Kilépés", command=hengerablak.destroy, bg="#4162b0",fg="white", font="Arial 15")

#KEP
hengercanvas = Canvas(hengerablak, width=250, height=250)
hengercanvas.grid(column=3, row=2, rowspan=10, padx=25, pady=15)
hengerimage = (Image.open("Program\\Összerakás\\Képek\\henger.jpg"))
atmeret_hengerimage = hengerimage.resize((250,250))
ujkep = ImageTk.PhotoImage(atmeret_hengerimage)
hengercanvas.create_image(1,1,anchor=NW, image=ujkep)

#LABELCONFIG
LabelSettings = {"bg":"#6A91EF", "fg":"white", "font":("Arial", 15)}
hengersugarszov.config(LabelSettings)
hengermagassagszov.config(LabelSettings)
hengerfelszinszov.config(LabelSettings)
hengerterfogatszov.config(LabelSettings)
hengerfelszinki.config(LabelSettings)
hengerterfogatki.config(LabelSettings)

#GRIDALIGNMENT
hengersugarszov.grid(column=1, row=2,  pady=10, padx=8)
hengersugar.grid(column=2, row=2,  pady=10)
hengermagassagszov.grid(column=1, row=3, pady=10, padx=8)
hengermagassag.grid(column=2, row=3, pady=10)
hengerszamitas.grid(column=2, row=4)
hengerfelszinszov.grid(column=1, row=5)
hengerfelszinki.grid(column=2, row=5)
hengerterfogatszov.grid(column=1, row=6)
hengerterfogatki.grid(column=2, row=6)
hengerkilep.place(relx=0.03, rely=0.95, anchor=SW)
hengerablak.minsize(650,300)
hengerablak.maxsize(650,300)

hengerablak.mainloop()
    