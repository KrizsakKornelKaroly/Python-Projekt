from tkinter import *
from PIL import Image, ImageTk
import math

def szamit():
    try:
        haromszogA=float(haromszoga1.get())
        haromszogB=float(haromszogb1.get())
        haromszogC=float(haromszogc1.get())
        haromszogker1=(haromszogA+haromszogB+haromszogC)
        haromszogker.config(text=haromszogker1)
        haromszogS=haromszogker1/2
        haromszogter1=round(math.sqrt(haromszogS*(haromszogS-haromszogA)*(haromszogS-haromszogB)*(haromszogS-haromszogC)),2)
        haromszogter.config(text=haromszogter1)
    except:
        haromszogter.config(text="Hibás bemenet!")
        haromszogker.config(text="Hibás bemenet!")

haromszogablak=Tk()

haromszogablak.config(bg="#6a92ef")
haromszogablak.title("Háromszög kerülete és területe")
haromszogker=Label(haromszogablak,text="Kerület:", bg="#6a92ef", fg="white", font="Arial 15", padx=15)
haromszogker.grid(row=6, column=1)
haromszogter=Label(haromszogablak,text="Terület:", bg="#6a92ef", fg="white", font="Arial 15", padx=15)
haromszogter.grid(row=7, column=1)
haromszogszamitas = Button(haromszogablak, text="Számítás", bg="#4162b0", fg="white", font="Arial 15", command=szamit)
haromszogszamitas.grid(row=5, column=2)
haromszogki = Button(haromszogablak, text="Kilépés", command=haromszogablak.destroy, bg="#4162b0", fg="white", font="Arial 15")
haromszogki.place(relx=0.03, rely=0.96, anchor=SW)
haromszogker=Label(haromszogablak, bg="#6a92ef", fg="white", font="Arial 15")
haromszogker.grid(row=6, column=2)
haromszogter=Label(haromszogablak, bg="#6a92ef", fg="white", font="Arial 15")
haromszogter.grid(row=7, column=2)
haromszogcanvas = Canvas(haromszogablak, width=250, height=250)
haromszogcanvas.grid(column=3, row=2, rowspan=10, padx=40, pady=20)
haromszogimage = (Image.open("Program\\Összerakás\\Képek\\haromszog.jpg"))
atmeret_haromszogimage = haromszogimage.resize((250,250))
ujkep = ImageTk.PhotoImage(atmeret_haromszogimage)
haromszogcanvas.create_image(1,1,anchor=NW, image=ujkep)

haromszoga=Label(haromszogablak,text="\"a\" oldal:" , bg="#6a92ef", fg="white", font="Arial 15", padx=15, pady=2)
haromszoga.grid(row=2, column=1)
haromszoga1 = Entry(haromszogablak, width=20, font="Arial 15", bg="#4162b0", fg="white")
haromszoga1.grid(row=2, column=2)

haromszogb=Label(haromszogablak,text="\"b\" oldal:", bg="#6a92ef", fg="white", font="Arial 15", padx=15, pady=2)
haromszogb.grid(row=3, column=1)
haromszogb1 = Entry(haromszogablak, width=20, font="Arial 15", bg="#4162b0", fg="white")
haromszogb1.grid(row=3, column=2)

haromszogc=Label(haromszogablak,text="\"c\" oldal:", bg="#6a92ef", fg="white", font="Arial 15", padx=15, pady=2)
haromszogc.grid(row=4, column=1)
haromszogc1 = Entry(haromszogablak, width=20, font="Arial 15", bg="#4162b0", fg="white")
haromszogc1.grid(row=4, column=2)

haromszogablak.minsize(650,300)
haromszogablak.maxsize(650,300)
haromszogablak.mainloop()