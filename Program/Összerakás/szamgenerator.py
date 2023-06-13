from tkinter import *
from random import randint
from PIL import Image, ImageTk

def szamgenerator():
    start = szamgenerator_start.get()
    end = szamgenerator_end.get()

    try:
        start = int(start)
        end = int(end)

        if start <= end:
            number = randint(start, end)
            szamgenerator_kimenet.config(text=str(number))
        else:
            szamgenerator_kimenet.config(text="Hibás bemenet!")
    except ValueError:
        szamgenerator_kimenet.config(text="Hibás bemenet!")

szamgeneratorablak = Tk()
szamgeneratorablak.config(bg="#df5a67")
szamgeneratorablak.title("Random szám generátor")

# BEMENET
szamgenerator_start = Entry(szamgeneratorablak, width=20, font="Arial 15", bg="#ad3e49", fg="white")
szamgenerator_end = Entry(szamgeneratorablak, width=20, font="Arial 15", bg="#ad3e49", fg="white")
szamgenerator_startszov = Label(szamgeneratorablak, text="Kezdőérték:")
szamgenerator_endszov = Label(szamgeneratorablak, text="Végérték:")

# KIMENET
szamgenerator_kimenet_szov = Label(szamgeneratorablak, text="Végeredmény:")
szamgenerator_kimenet = Label(szamgeneratorablak)

# Számítás
szamgeneratorszamitas = Button(szamgeneratorablak, text="Számítás", bg="#ad3e49", fg="white", font="Arial 15", command=szamgenerator)
# Kilepes
szamgeneratorkilep = Button(szamgeneratorablak, text="Kilépés", command=szamgeneratorablak.destroy, bg="#ad3e49", fg="white", font="Arial 15")
# KÉP
szamgeneratorcanvas = Canvas(szamgeneratorablak, width=260, height=160)
szamgeneratorcanvas.grid(column=3, row=3, rowspan=10, padx=10, pady=15)
szamgeneratorimage = Image.open("Program\\Összerakás\\Képek\\szamgenerator.jpg")
atmeret_szamgeneratorimage = szamgeneratorimage.resize((260,160))
ujkep = ImageTk.PhotoImage(atmeret_szamgeneratorimage)
szamgeneratorcanvas.create_image(1, 1, anchor=NW, image=ujkep)

# LABELCONFIG
LabelSettings = {"bg": "#df5a67", "fg": "white", "font": ("Arial", 15), "padx": "8"}
szamgenerator_startszov.config(LabelSettings)
szamgenerator_endszov.config(LabelSettings)
szamgenerator_kimenet_szov.config(LabelSettings)
szamgenerator_kimenet.config(LabelSettings)

# GRID
szamgenerator_startszov.grid(column=1, row=2, pady=20)
szamgenerator_start.grid(column=2, row=2,pady=20)
szamgenerator_endszov.grid(column=1, row=3, pady=10)
szamgenerator_end.grid(column=2, row=3, pady=10)
szamgeneratorszamitas.grid(column=2, row=4)
szamgenerator_kimenet_szov.grid(column=1, row=5)
szamgenerator_kimenet.grid(column=2, row=5)
szamgeneratorkilep.place(relx=0.03, rely=0.95, anchor=SW)

szamgeneratorablak.minsize(650, 300)
szamgeneratorablak.maxsize(650, 300)
szamgeneratorablak.mainloop()
