from tkinter import *
from ttkthemes import ThemedTk
ablak = Tk()
ablak.configure(bg='#5FC861')
ablak.title('')
ablak.geometry("600x300")
afadrop = ["Alanyi adómentes", "Általános adózás", "Egyszerűsített vállalkozói adó", "ÁFA-kör - Csoportos adóalanyiság", "ÁFA-kör - Csoport közös adószáma"]
#tests = Label(ablak, text="Teszt", fg='white', bg='#5FC861')
gomb1 = Button(ablak, text="Számítás",fg='white', bg='#359e18')
gomb2 = Button(ablak, text="Számítás",fg='white', bg='#4162b0')
gomb3 = Button(ablak, text="Számítás",fg='white', bg='#ad3e49')
gomb1.pack()
gomb2.pack()
gomb3.pack()

#testm = Entry(ablak, fg='white', bg='#4162b0')
#testm.pack()
#testg.pack()
#tests.pack()
ablak.mainloop() 