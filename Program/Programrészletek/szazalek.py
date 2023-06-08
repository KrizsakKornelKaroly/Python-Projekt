from tkinter import *
from PIL import Image, ImageTk

szazalekablak = Tk()
szazalekablak.config(bg="#df5a67")
szazalekablak.title("Átlagszámítás")

#BEMENET
szazalek_lab = Entry(szazalekablak, width=20, font="Arial 15", bg="#ad3e49",fg="white")
szazalek_ertek = Entry(szazalekablak, width=20, font="Arial 15", bg="#ad3e49",fg="white")
szazalek_lab_szov = Label(szazalekablak, text="Százalékláb: ",)
szazalek_ertek_szov = Label(szazalekablak, text="Százalékérték: ")

#KIMENET
szazalek_kimenet_szov = Label(szazalekablak, text="Végeredmény: ")
szazalek_kimenet = Label(szazalekablak)

#Szamitas
szazalekszamitas = Button(szazalekablak, text="Számítás",bg="#ad3e49",fg="white", font="Arial 15", command=None)
#Kilepes
szazalekkilep = Button(szazalekablak, text="Kilépés", command=szazalekablak.destroy, bg="#ad3e49",fg="white", font="Arial 15")
#KEP
szazalekcanvas = Canvas(szazalekablak, width=250, height=250)
szazalekcanvas.grid(column=3, row=2, rowspan=10, padx=10, pady=15)
szazalekimage = (Image.open("Tervek\\Képek\\szazalekszamitas.jpg"))
atmeret_szazalekimage = szazalekimage.resize((250,250))
ujkep = ImageTk.PhotoImage(atmeret_szazalekimage)
szazalekcanvas.create_image(1,1,anchor=NW, image=ujkep)

#LABELCONFIG
LabelSettings = {"bg":"#df5a67", "fg":"white", "font":("Arial", 15), "padx":"8"}
szazalek_lab_szov.config(LabelSettings)
szazalek_ertek_szov.config(LabelSettings)
szazalek_kimenet_szov.config(LabelSettings)
szazalek_kimenet.config(LabelSettings)

#GRID
szazalek_lab_szov.grid(column=1, row=2, pady=10)
szazalek_lab.grid(column=2, row=2, pady=10)
szazalek_ertek_szov.grid(column=1, row=3)
szazalek_ertek.grid(column=2, row=3)
szazalekszamitas.grid(column=2, row=4)
szazalek_kimenet_szov.grid(column=1, row=5)
szazalek_kimenet.grid(column=2, row=5)
szazalekkilep.place(relx=0.03, rely=0.95, anchor=SW)

szazalekablak.minsize(650,300)
szazalekablak.maxsize(650,300)
szazalekablak.mainloop()