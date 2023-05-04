from tkinter import *
from ttkthemes import ThemedTk
ablak = Tk()
ablak.configure(bg='#5FC861')
ablak.title('')
ablak.geometry("600x300")
afadrop = ["Alanyi adómentes", "Általános adózás", "Egyszerűsített vállalkozói adó", "ÁFA-kör - Csoportos adóalanyiság", "ÁFA-kör - Csoport közös adószáma"]
tests = Label(ablak, text="Teszt", fg='white', bg='#5FC861')
testg = Button(ablak, text="Teszt",fg='white', bg='#359e18')
testg.pack()
tests.pack()
ablak.mainloop() 