from tkinter import *
from PIL import Image, ImageTk
kockaablak = Tk()
kockaablak.config(bg="#6a92ef")
kockaablak.title("Kocka felszíne és térfogata")

def kocka_szamitas():
    elhossz = kockael.get()
    try:
        elhossz = float(elhossz)
        terfogat = elhossz ** 3
        felszin = 6 * (elhossz ** 2)
        kockafelszin_kimenet.config(text=str(felszin))
        kockaterfogat_kimenet.config(text=str(terfogat))
    except ValueError:
        kockafelszin_kimenet.config(text="Hibás adat")
        kockaterfogat_kimenet.config(text="Hibás adat")

kockael_szoveg = Label(kockaablak, text="Élhossz: ", bg="#6a92ef", fg="white", font="Arial 15")
kockael = Entry(kockaablak, width=20, font="Arial 15", bg="#4162b0", fg="white")

kockafelszin_szoveg = Label(kockaablak, text="Felszín: ", bg="#6a92ef", fg="white", font="Arial 15")
kockaterfogat_szoveg = Label(kockaablak, text="Térfogat: ", bg="#6a92ef", fg="white", font="Arial 15")
kockafelszin_kimenet = Label(kockaablak, bg="#6a92ef", fg="white", font="Arial 15")
kockaterfogat_kimenet = Label(kockaablak, bg="#6a92ef", fg="white", font="Arial 15")


kockaszamitas = Button(kockaablak, text="Számítás", bg="#4162b0", fg="white", font="Arial 15", command=kocka_szamitas)
kockakimenetlep = Button(kockaablak, text="Kilépés", command=kockaablak.destroy, bg="#4162b0", fg="white", font="Arial 15")


#photo
kockacanvas = Canvas(kockaablak, width=250, height=250)
kockacanvas.grid(column=3, row=1, rowspan=10, padx=20, pady=20)
kockaimage = Image.open("Tervek\\Képek\\kocka.jpg")
atmeret_kockaimage = kockaimage.resize((250,250))
ujkep = ImageTk.PhotoImage(atmeret_kockaimage)
kockacanvas.create_image(1, 1, anchor=NW, image=ujkep)

kocka_filler1=Label(kockaablak, bg="#6a92ef")
kocka_filler1.grid(column=1,row=1)
kockael_szoveg.grid(column=1, row=4, padx=8, pady=10)
kockael.grid(column=2, row=4, pady=10)
kockafelszin_szoveg.grid(column=1, row=6, padx=8, pady=10)
kockaterfogat_szoveg.grid(column=1, row=7, padx=8, pady=10)
kockafelszin_kimenet.grid(column=2, row=6)
kockaterfogat_kimenet.grid(column=2, row=7)
kockaszamitas.grid(column=2, row=5)
kockakimenetlep.grid(column=1, row=9)

LabelSettings = {"bg": "#6a92ef", "fg": "white", "font": ("Arial", 15)}
kockafelszin_szoveg.config(LabelSettings)
kockaterfogat_szoveg.config(LabelSettings)

kockaablak.minsize(650, 300)
kockaablak.maxsize(650, 300)

kockaablak.mainloop()