from tkinter import *
from PIL import Image, ImageTk
import math

def kor_szamitas():
    korsug=float(korel.get())
    korter=(korsug**2)*math.pi
    korterszov=Label(korablak,text=korter, bg="#6a92ef", fg="white", font="Arial 15")
    korterszov.grid(row=5, column=2)
    korker=2*korsug*math.pi
    korkerszov=Label(korablak,text=korker, bg="#6a92ef", fg="white", font="Arial 15")
    korkerszov.grid(row=4, column=2)




korablak=Tk()

kor_filler1=Label(korablak, bg="#6a92ef")
kor_filler1.grid(column=1,row=1)
korablak.config(bg="#6a92ef")
korablak.title("Kör kerülete és területe")
korsugszov=Label(korablak,text="Sugár:", bg="#6a92ef", fg="white", font="Arial 15")
korsugszov.grid(row=2, column=1)
korel = Entry(korablak, width=20, font="Arial 15", bg="#4162b0", fg="white")
korel.grid(row=2, column=2)
korkerszov=Label(korablak,text="Kerület:", bg="#6a92ef", fg="white", font="Arial 15")
korkerszov.grid(row=4, column=1)
korterszov=Label(korablak,text="Terület:", bg="#6a92ef", fg="white", font="Arial 15")
korterszov.grid(row=5, column=1)
korszamitas = Button(korablak, text="Számítás", bg="#4162b0", fg="white", font="Arial 10", command=kor_szamitas)
korszamitas.grid(row=3, column=2)
korki = Button(korablak, text="Kilépés", command=korablak.destroy, bg="#4162b0", fg="white", font="Arial 10")
korki.grid(column=1, row=9)

kocka_image1 = PhotoImage(file="Tervek\\Képek\\kor.png" ) 
kocka_image=kocka_image1.resize(height=5, width=5)
kocka_image_label = Label(korablak, image=kocka_image)
kocka_image_label.grid(rowspan=10,row=5, column=3)

korablak.minsize(650,300)
korablak.maxsize(650,300)
korablak.mainloop()