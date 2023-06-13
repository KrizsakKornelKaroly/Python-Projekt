from tkinter import *
from PIL import Image, ImageTk
import math

def kor_szamitas():
    try:
        korsug=float(korel.get())
        korter=round((korsug**2)*math.pi,2),"cm\u00b2"
        korker=round(2*korsug*math.pi,2),"cm"
        korterszov.config(text=korter)
        korkerszov.config(text=korker)
    except:
        korterszov.config(text="Hibás bemenet!")
        korkerszov.config(text="Hibás bemenet!")




korablak=Tk()

korablak.config(bg="#6a92ef")
korablak.title("Kör kerülete és területe")
korsugszov=Label(korablak,text="Sugár:", bg="#6a92ef", fg="white", font="Arial 15", padx=15, pady=15)
korsugszov.grid(row=2, column=1)
korel = Entry(korablak, width=20, font="Arial 15", bg="#4162b0", fg="white")
korel.grid(row=2, column=2)
korkerszov=Label(korablak,text="Kerület:", bg="#6a92ef", fg="white", font="Arial 15", padx=15)
korkerszov.grid(row=4, column=1)
korterszov=Label(korablak,text="Terület:", bg="#6a92ef", fg="white", font="Arial 15", padx=15)
korterszov.grid(row=5, column=1)
korszamitas = Button(korablak, text="Számítás", bg="#4162b0", fg="white", font="Arial 15", command=kor_szamitas)
korszamitas.grid(row=3, column=2)
korki = Button(korablak, text="Kilépés", command=korablak.destroy, bg="#4162b0", fg="white", font="Arial 15")
korki.place(relx=0.03, rely=0.95, anchor=SW)
korterszov=Label(korablak, bg="#6a92ef", fg="white", font="Arial 15")
korterszov.grid(row=5, column=2)
korkerszov=Label(korablak, bg="#6a92ef", fg="white", font="Arial 15")
korkerszov.grid(row=4, column=2)
korcanvas = Canvas(korablak, width=250, height=250)
korcanvas.grid(column=3, row=2, rowspan=10, padx=40, pady=20)
korimage = (Image.open("Program\\Összerakás\\Képek\\kor.png"))
atmeret_korimage = korimage.resize((250,250))
ujkep = ImageTk.PhotoImage(atmeret_korimage)
korcanvas.create_image(1,1,anchor=NW, image=ujkep)

korablak.minsize(650,300)
korablak.maxsize(650,300)
korablak.mainloop()