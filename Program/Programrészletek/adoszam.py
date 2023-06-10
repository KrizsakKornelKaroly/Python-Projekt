from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

def adokalkulacio():
    try:
        adotipusbeindex = adotipus.current()
        if adotipusbeindex == 0:
            afatipus = 1
        elif adotipusbeindex == 1:
            afatipus = 2
        elif adotipusbeindex == 2:
            afatipus = 3
        elif adotipusbeindex == 3:
            afatipus = 4
        elif adotipusbeindex == 4:
            afatipus = 5

        adoteruletbeindex = adoterulet.current()
        if adoteruletbeindex == 0:
            terulettipus = random.choice(["02", "22"])
        elif adoteruletbeindex == 1:
            terulettipus = random.choice(["03", "23"])
        elif adoteruletbeindex == 2:
            terulettipus = random.choice(["04", "24"])
        elif adoteruletbeindex == 3:
            terulettipus = random.choice(["05", "25"])    
        elif adoteruletbeindex == 4:
            terulettipus = random.choice(["06", "26"])
        elif adoteruletbeindex == 5:
            terulettipus = random.choice(["07", "27"])
        elif adoteruletbeindex == 6:
            terulettipus = random.choice(["08", "28"])
        elif adoteruletbeindex == 7:
            terulettipus = random.choice(["09", "29"])
        elif adoteruletbeindex == 8:
            terulettipus = random.choice(["10", "30"])
        elif adoteruletbeindex == 9:
            terulettipus = random.choice(["11", "31"])
        elif adoteruletbeindex == 10:
            terulettipus = random.choice(["12", "32"])
        elif adoteruletbeindex == 11:
            terulettipus = random.choice(["13", "33"]) 
        elif adoteruletbeindex == 12:
            terulettipus = random.choice(["14", "34"])
        elif adoteruletbeindex == 13:
            terulettipus = random.choice(["15", "35"])
        elif adoteruletbeindex == 14:
            terulettipus = random.choice(["16", "36"])
        elif adoteruletbeindex == 15:
            terulettipus = random.choice(["17", "37"])
        elif adoteruletbeindex == 16:
            terulettipus = random.choice(["18", "38"])
        elif adoteruletbeindex == 17:
            terulettipus = random.choice(["19", "39"])
        elif adoteruletbeindex == 18:
            terulettipus = random.choice(["20", "40"])
        elif adoteruletbeindex == 19:
            terulettipus = 41
        elif adoteruletbeindex == 20:
            terulettipus = 42
        elif adoteruletbeindex == 21:
            terulettipus = 43
        elif adoteruletbeindex == 22:
            terulettipus = 44
        elif adoteruletbeindex == 23:
            terulettipus = 51

        adostarter = random.randint(10000000,99999999)

        adoszamki = str(adostarter)+"-"+str(afatipus)+"-"+str(terulettipus)
        adoszam.config(text=adoszamki)
    except:
        adoszam.config(text="Hiba történt!")


adoablak = Tk()
adoablak.config(bg="#5FC861")
adoablak.title("Adószám-kalkulátor")

#Bekeres
adotipus_szov = Label(adoablak, text="ÁFA-kód:")
adoterulet_szov = Label(adoablak, text="Terület:")
adotipus = ttk.Combobox(
    state="readonly",
    values=["Alanyi adómentes",
             "Általános adózás", 
             "Egyszerűsített vállalkozói adó", 
             "ÁFA-kör - Csoportos adóalanyiság", 
             "ÁFA-kör - Csoport közös adószáma"],
    width=30,
)
adoterulet = ttk.Combobox(
    state="readonly",
    values=["Baranya", 
            "Bács-Kiskun", 
            "Békés", 
            "Borsod-Abaúj-Zemplén", 
            "Csongrád-Csanád", 
            "Fejér", 
            "Győr-Moson-Sopron", 
            "Hajdú-Bihar", 
            "Heves", 
            "Komárom-Esztergom", 
            "Nógrád", 
            "Pest", 
            "Somogy", 
            "Szabolcs-Szatmár-Bereg", 
            "Jász-Nagykun-Szolnok", 
            "Tolna", 
            "Vas", 
            "Veszprém", 
            "Zala", 
            "Észak-Budapest", 
            "Kelet-Budapest", 
            "Dél-Budapest", 
            "Kiemelt Adózók Adóigazgatósága", 
            "Kiemelt Ügyek Adóigazgatósága"],
    width=30
)

#Szamitas
adoszamitas = Button(adoablak, text="Számítás",bg="#359e18",fg="white", font="Arial 15", command=adokalkulacio)

#Kimenet
adoszam_szov = Label(adoablak, text="Adószám:")
adoszam = Label(adoablak)
#KILEP
adokilep = Button(adoablak, text="Kilépés", command=adoablak.destroy, bg="#359e18",fg="white", font="Arial 15")

#KEP
adocanvas = Canvas(adoablak, width=250, height=250)
adocanvas.grid(column=3, row=2, rowspan=10, padx=50, pady=20)
adoimage = (Image.open("Tervek\\Képek\\ado.jpg"))
atmeret_adoimage = adoimage.resize((250,250))
ujkep = ImageTk.PhotoImage(atmeret_adoimage)
adocanvas.create_image(1,1,anchor=NW, image=ujkep)

#LABEL
LabelSettings = {"bg":"#5FC861", "fg":"white", "font":("Arial", 15), "padx":"15"}
adotipus_szov.config(LabelSettings)
adoterulet_szov.config(LabelSettings)
adoszam_szov.config(LabelSettings)
adoszam.config(LabelSettings)

#GRID
adotipus_szov.grid(column=1, row=2, pady=10)
adotipus.grid(column=2, row=2, pady=10)
adoterulet_szov.grid(column=1, row=3, pady=10)
adoterulet.grid(column=2, row=3, pady=10)
adoszamitas.grid(column=2, row=4)
adoszam_szov.grid(column=1, row=5)
adoszam.grid(column=2, row=5)
adokilep.place(relx=0.03, rely=0.95, anchor=SW)

adoablak.minsize(650,300)
adoablak.maxsize(650,300)
adoablak.mainloop()