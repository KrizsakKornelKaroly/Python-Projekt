from tkinter import *
from PIL import Image, ImageTk
import math

korablak=Tk()
korablak.config(bg="#6a92ef")
korablak.title("Kör kerülete és területe")
korsugszov=Label(korablak,text="Sugár:", bg="#6a92ef", fg="white", font="Arial 15")
korsugszov.grid(row=1, column=1)
korkerszov=Label(korablak,text="Kerület:", bg="#6a92ef", fg="white", font="Arial 15")
korkerszov.grid(row=3, column=1)
korterszov=Label(korablak,text="Terület:", bg="#6a92ef", fg="white", font="Arial 15")
korterszov.grid(row=4, column=1)

korablak.minsize(650,300)
korablak.maxsize(650,300)
korablak.mainloop()