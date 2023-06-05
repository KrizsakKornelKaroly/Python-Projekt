from tkinter import *

negyzetablak = Tk()
negyzetablak.config(bg="#6a92ef")
negyzetablak.title("Négyzet kerülete és területe")

def negyzet_szamitas():
    oldalhossz = float(negyzetoldal.get())
    kerulet = 4 * oldalhossz
    terulet = oldalhossz ** 2
    negyzetkerulet_kimenet.config(text=str(kerulet))
    negyzetterulet_kimenet.config(text=str(terulet))

negyzetoldal_szoveg = Label(negyzetablak, text="Oldalhossz: ", bg="#6a92ef", fg="white", font="Arial 15")
negyzetoldal = Entry(negyzetablak, width=20, font="Arial 15", bg="#4162b0", fg="white")

negyzetkerulet_szoveg = Label(negyzetablak, text="Kerület: ", bg="#6a92ef", fg="white", font="Arial 15")
negyzetterulet_szoveg = Label(negyzetablak, text="Terület: ", bg="#6a92ef", fg="white", font="Arial 15")
negyzetkerulet_kimenet = Label(negyzetablak, bg="#6a92ef", fg="white", font="Arial 15")
negyzetterulet_kimenet = Label(negyzetablak, bg="#6a92ef", fg="white", font="Arial 15")


negyzetszamitas = Button(negyzetablak, text="Számítás", bg="#4162b0", fg="white", font="Arial 10", command=negyzet_szamitas)
negyzetkimenetlep = Button(negyzetablak, text="Kilépés", command=negyzetablak.destroy, bg="#4162b0", fg="white", font="Arial 10")


negyzet_image = PhotoImage(file="Tervek\\Képek\\negyzet.png" ) 
negyzet_image_label = Label(negyzetablak, image=negyzet_image)


negyzet_filler1=Label(negyzetablak, bg="#6a92ef")
negyzet_filler1.grid(column=1,row=1)
negyzetoldal_szoveg.grid(column=1, row=4, padx=8, pady=10)
negyzetoldal.grid(column=2, row=4, pady=10)
negyzetkerulet_szoveg.grid(column=1, row=6, padx=8, pady=10)
negyzetterulet_szoveg.grid(column=1, row=7, padx=8, pady=10)
negyzetkerulet_kimenet.grid(column=2, row=6)
negyzetterulet_kimenet.grid(column=2, row=7)
negyzetszamitas.grid(column=2, row=5)
negyzetkimenetlep.grid(column=1, row=9)

negyzet_image_label.grid(rowspan=5,row=5, column=3)

LabelSettings = {"bg": "#6a92ef", "fg": "white", "font": ("Arial", 15)}
negyzetkerulet_szoveg.config(LabelSettings)
negyzetterulet_szoveg.config(LabelSettings)

negyzetablak.minsize(600, 300)
negyzetablak.maxsize(600, 300)

negyzetablak.mainloop()