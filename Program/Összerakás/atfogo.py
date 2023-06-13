from tkinter import *
from PIL import Image, ImageTk
import math

def atfogo():
    atfogo_a_be = atfogo_a.get()
    atfogo_b_be = atfogo_b.get()
    try:
        atfogo_a_be = int(atfogo_a_be)
        atfogo_b_be = int(atfogo_b_be)
        atfogo_eredmeny = round(math.sqrt(atfogo_a_be**2 + atfogo_b_be**2),2)
        atfogo_kimenet.config(text=atfogo_eredmeny)
    except:
        atfogo_kimenet.config(text="Hibás bemenet!")

atfogoablak = Tk()
atfogoablak.config(bg="#6A91EF")
atfogoablak.title("Átfogószámítás - Pitagorasz-tétel")
#bemenet
atfogo_a = Entry(atfogoablak, width=20, font="Arial 15", bg="#4162b0",fg="white")
atfogo_b = Entry(atfogoablak, width=20, font="Arial 15", bg="#4162b0",fg="white")
atfogo_a_szov = Label(atfogoablak, text="a oldal: ",)
atfogo_b_szov = Label(atfogoablak, text="b oldal: ")
#kimenet
atfogo_kimenet_szov = Label(atfogoablak, text="Átfogó: ")
atfogo_kimenet = Label(atfogoablak)
#szamitas
atfogoszamitas = Button(atfogoablak, text="Számítás",bg="#4162b0",fg="white", font="Arial 15", command=atfogo)
#kilepes
atfogokilep = Button(atfogoablak, text="Kilépés", command=atfogoablak.destroy, bg="#4162b0",fg="white", font="Arial 15")
#KEP
atfogocanvas = Canvas(atfogoablak, width=250, height=250)
atfogocanvas.grid(column=3, row=2, rowspan=10, padx=25, pady=15)
atfogoimage = (Image.open("Program\\Összerakás\\Képek\\pitagorasz.png"))
atmeret_atfogoimage = atfogoimage.resize((250,250))
ujkep = ImageTk.PhotoImage(atmeret_atfogoimage)
atfogocanvas.create_image(1,1,anchor=NW, image=ujkep)

#LABELCONFIG
LabelSettings = {"bg":"#6A91EF", "fg":"white", "font":("Arial", 15), "padx":"10"}
atfogo_a_szov.config(LabelSettings)
atfogo_b_szov.config(LabelSettings)
atfogo_kimenet.config(LabelSettings)
atfogo_kimenet_szov.config(LabelSettings)

#GRID
atfogo_a_szov.grid(column=1, row=2,  pady=10, padx=8)
atfogo_a.grid(column=2, row=2,  pady=10)
atfogo_b_szov.grid(column=1, row=3)
atfogo_b.grid(column=2, row=3)
atfogoszamitas.grid(column=2, row=4)
atfogo_kimenet_szov.grid(column=1, row=5)
atfogo_kimenet.grid(column=2, row=5)
atfogokilep.place(relx=0.03, rely=0.95, anchor=SW)


atfogoablak.minsize(650,300)
atfogoablak.maxsize(650,300)
atfogoablak.mainloop()