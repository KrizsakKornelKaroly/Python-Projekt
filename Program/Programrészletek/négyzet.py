from tkinter import *
#	Négyzet (Kerület & Terület)
#   Tartalmazni fogja a négyzet oldalának bemeneti mezőjét. Két label mezőbe kiírja a két kimeneti értéket. 
#   Egy bemeneti mező, egy kimeneti label és egy gomb.

negyzetablak=Tk()
negyzetablak.title("Négyzet kerülete és területe")
negyzetoldalhosszszov= Label(negyzetablak,text="Oldalhossz: ")
negyzetoldalhossz= Entry(negyzetablak)
negyzetszamitas= Button(negyzetablak, text="Számítás")

negyzetkeruletszov= Label(negyzetablak,text="Kerület: ")
negyzetteruletszov= Label(negyzetablak,text="Terület: ")

negyzetkerulet= Label(negyzetablak)
negyzetterulet= Label(negyzetablak)
negyzetkilep= Button(negyzetablak, command=negyzetablak.destroy)

negyzetablak.mainloop()


