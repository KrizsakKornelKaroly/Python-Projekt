from tkinter import *
from PIL import Image, ImageTk
import math
masodfoku_ablak = Tk()
masodfoku_ablak.config(bg="#df5a67")
masodfoku_ablak.title("Másodfokú egyenlet kalkulátor")

def masodfoku_szamitas():
    try:
        a = float(masodfoku_a_entry.get())
        b = float(masodfoku_b_entry.get())
        c = float(masodfoku_c_entry.get())
        masodfoku_diszkriminans = (b**2)-4*a*c

        if masodfoku_diszkriminans < 0:
            masodfoku_eredmeny_label.config(text="Hiba: Nincs valós megoldás!")
        else:
            masodfoku_x1 = round(((b*(-1))+math.sqrt(masodfoku_diszkriminans))/(2*a),2)
            masodfoku_x2 = round(((b*(-1))-math.sqrt(masodfoku_diszkriminans))/(2*a),2)
            masodfoku_eredmeny_label.config(text=f"X1={masodfoku_x1}\nX2={masodfoku_x2}")
    except:
        masodfoku_eredmeny_label.config(text="Hiba: Érvénytelen bemenet!")




masodfoku_a_label = Label(masodfoku_ablak, text="A:", bg="#df5a67", fg="white", font="Arial 15")
masodfoku_b_label = Label(masodfoku_ablak, text="B:", bg="#df5a67", fg="white", font="Arial 15")
masodfoku_c_label = Label(masodfoku_ablak, text="C:", bg="#df5a67", fg="white", font="Arial 15")
masodfoku_eredmeny_cimke = Label(masodfoku_ablak, text="Végeredmény:", bg="#df5a67", fg="white", font="Arial 15")

masodfoku_a_entry = Entry(masodfoku_ablak, width=20, font="Arial 15", bg="#ad3e49", fg="white")
masodfoku_b_entry = Entry(masodfoku_ablak, width=20, font="Arial 15", bg="#ad3e49", fg="white")
masodfoku_c_entry = Entry(masodfoku_ablak, width=20, font="Arial 15", bg="#ad3e49", fg="white")
masodfoku_eredmeny_label = Label(masodfoku_ablak, bg="#df5a67", fg="white", font="Arial 15")

masodfoku_szamitas_gomb = Button(masodfoku_ablak, text="Számítás", bg="#ad3e49", fg="white", font="Arial 15", command=masodfoku_szamitas)
masodfoku_kilepes_gomb = Button(masodfoku_ablak, text="Kilépés", command=masodfoku_ablak.destroy, bg="#ad3e49", fg="white", font="Arial 15")

masodfoku_a_label.grid(row=0, column=1, padx=5, pady=10)
masodfoku_a_entry.grid(row=0, column=2, padx=5, pady=10)

masodfoku_b_label.grid(row=1, column=1, padx=5, pady=10)
masodfoku_b_entry.grid(row=1, column=2, padx=5, pady=10)

masodfoku_c_label.grid(row=2, column=1, padx=5, pady=10)
masodfoku_c_entry.grid(row=2, column=2, padx=5, pady=10)

masodfokucanvas = Canvas(masodfoku_ablak, width=250, height=180)
masodfokucanvas.grid(column=3, row=1, rowspan=10, padx=10, pady=10)
masodfokuimage = Image.open("Tervek\\Képek\\masodfoku.jpg")
atmeret_masodfokuimage = masodfokuimage.resize((250,180))
ujkep = ImageTk.PhotoImage(atmeret_masodfokuimage)
masodfokucanvas.create_image(1, 1, anchor=NW, image=ujkep)
masodfoku_eredmeny_cimke.grid(row=4, column=1, padx=5, pady=5)
masodfoku_eredmeny_label.grid(row=4, column=2, padx=5, pady=5)
masodfoku_szamitas_gomb.grid(row=3, column=2, pady=5)
masodfoku_kilepes_gomb.place(relx=0.03, rely=0.95, anchor=SW)

masodfoku_ablak.minsize(650, 300)
masodfoku_ablak.maxsize(650, 300)
masodfoku_ablak.mainloop()
