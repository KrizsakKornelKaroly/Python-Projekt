from tkinter import *
from PIL import Image, ImageTk

atlagszamlista = []

def hozzaad():
    try:
        atlagbuffer = atlagertek.get()
        atlagbuffer = int(atlagbuffer)
        atlagszamlista.append(atlagbuffer)
        atlagertek.delete(0, END)
        atlagstatus = str(len(atlagszamlista)) + " elemet tartalmaz!"
        atlagkimenet.config(text=atlagstatus)
    except:
        atlagkimenet.config(text="Hibás bemenet!")
        atlagertek.delete(0, END)

def szamit():
    try:
        atlagszamhossz = len(atlagszamlista)
        atlagcounter = 0
        for i in atlagszamlista:
            atlagcounter = atlagcounter + i
        atlagveg = atlagcounter/atlagszamhossz
        atlagvegki = round(atlagveg, 2),"-" ,"Elemszám:",atlagszamhossz
        atlagkimenet.config(text=atlagvegki)
        atlagszamlista.clear()
    except ZeroDivisionError:
        atlagkimenet.config(text="Adj meg számot!")

atlagablak = Tk()
atlagablak.config(bg="#df5a67")
atlagablak.title("Átlagkalkulátor")

#bemenet
atlagertek_szov = Label(atlagablak, text="Érték: " )
atlagertek = Entry(atlagablak, width=20, font="Arial 15", bg="#ad3e49",fg="white")

#Gombok
atlagszamitas = Button(atlagablak, text="Számítás", bg="#ad3e49", fg="white", font="Arial 15", command=szamit)
atlaghozzaad = Button(atlagablak, text="Hozzáadás", bg="#ad3e49", fg="white", font="Arial 15", command=hozzaad)
atlagkilep = Button(atlagablak, text="Kilépés", command=atlagablak.destroy, bg="#ad3e49", fg="white", font="Arial 15")

#kimenet
atlagkimenet_szov = Label(atlagablak, text="Átlag:")
atlagkimenet = Label(atlagablak)

#LABELCONF
LabelSettings = {"bg":"#df5a67", "fg":"white", "font":("Arial", 15), "padx":"15", "pady":"10"}
atlagertek_szov.config(LabelSettings)
atlagkimenet_szov.config(LabelSettings)
atlagkimenet.config(LabelSettings)

#KEP
atlagcanvas = Canvas(atlagablak, width=250, height=250)
atlagcanvas.grid(column=3, row=2, rowspan=10, padx=50, pady=20)
atlagimage = (Image.open("Program\\Összerakás\\Képek\\atlagszamitas.jpg"))
atmeret_atlagimage = atlagimage.resize((250,250))
ujkep = ImageTk.PhotoImage(atmeret_atlagimage)
atlagcanvas.create_image(1,1,anchor=NW, image=ujkep)

#GRID
atlagertek_szov.grid(column=1, row=2, pady=10)
atlagertek.grid(column=2, row=2, pady=10)
atlagszamitas.grid(column=2, row=3, sticky=W, pady=10)
atlaghozzaad.grid(column=2, row=3, sticky=E, pady=10)
atlagkimenet_szov.grid(column=1, row=4, pady=10)
atlagkimenet.grid(column=2, row=4, pady=10)
atlagkilep.place(relx=0.03, rely=0.95, anchor=SW)

atlagablak.minsize(650,300)
atlagablak.maxsize(650,300)
atlagablak.mainloop()
