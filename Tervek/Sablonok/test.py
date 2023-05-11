from tkinter import *
from tkinter import ttk
ablak = Tk()
ablak.configure(bg='#5FC861')
ablak.title('')
ablak.geometry("600x300")
#afadrop = OptionMenu(ablak,"Alanyi adómentes", "Általános adózás", "Egyszerűsített vállalkozói adó", "ÁFA-kör - Csoportos adóalanyiság", "ÁFA-kör - Csoport közös adószáma")
#afadrop.pack()
afadrop = ttk.Combobox(
    state="readonly",
    values=["Alanyi adómentes", "Általános adózás", "Egyszerűsített vállalkozói adó", "ÁFA-kör - Csoportos adóalanyiság", "ÁFA-kör - Csoport közös adószáma"],
    width=30,
)
terulet = ttk.Combobox(
    state="readonly",
    values=["Baranya", "Bács-Kiskun", "Békés", "Borsod-Abaúj-Zemplén", "Csongrád-Csanád", "Fejér", "Győr-Moson-Sopron", "Hajdú-Bihar", "Heves", "Komárom-Esztergom", "Nógrád", "Pest", "Somogy", "Szabolcs-Szatmár-Bereg", "Jász-Nagykun-Szolnok", "Tolna", "Vas", "Veszprém", "Zala", "Észak-Budapest", "Kelet-Budapest", "Dél-Budapest", "Kiemelt Adózók Adóigazgatósága", "Kiemelt Ügyek Adóigazgatósága"],
    width=30
)
terulet.pack()
afadrop.config(background="#359e18")
afadrop.pack()
#tests = Label(ablak, text="Teszt", fg='white', bg='#5FC861')
gomb1 = Button(ablak, text="Hozzáadás",fg='white', bg='#359e18')
gomb2 = Button(ablak, text="Hozzáadás",fg='white', bg='#4162b0')
gomb3 = Button(ablak, text="Hozzáadás",fg='white', bg='#ad3e49')
gomb1.pack()
gomb2.pack()
gomb3.pack()

#testm = Entry(ablak, fg='white', bg='#4162b0')
#testm.pack()
#testg.pack()
#tests.pack()
ablak.mainloop() 