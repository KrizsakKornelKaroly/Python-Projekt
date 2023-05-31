#Kocka (Térfogat, felszín)
#Bekéri a kocka élének hosszát, majd ezek alapján kiszámítja a két értéket, két label mezőben kiírja azt.
#Egy bemeneti mező, két kimeneti label, egy gomb.
from tkinter import *

kockaablak=Tk()
kockaablak.config(bg="blue")
kockaablak.title("Kocka felszíne és térfogata")
kockaelhosszszov= Label(kockaablak,text="Élhossz: ")
kockaelhossz= Entry(kockaablak)
kockaszamitas= Button(kockaablak, text="Számítás")

kockafelszinszov= Label(kockaablak,text="Felszín: ")
kockaterfogatszov= Label(kockaablak,text="Térfogat: ")

kockafelszin= Label(kockaablak)
kockaterfogat= Label(kockaablak)
kockakilep= Button(kockaablak, command=kockaablak.destroy)
kockaablak.minsize(600,300)
kockaablak.maxsize(600,300)
kockaablak.mainloop()