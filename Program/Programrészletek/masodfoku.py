from tkinter import *

masodfoku_ablak = Tk()
masodfoku_ablak.config(bg="#df5a67")
masodfoku_ablak.title("Másodfokú egyenlet kalkulátor")

def masodfoku_szamitas():
    try:
        a = float(masodfoku_a_entry.get())
        b = float(masodfoku_b_entry.get())
        c = float(masodfoku_c_entry.get())
        masodfoku_diszkriminans = b ** 2 - 4 * a * c

        if masodfoku_diszkriminans < 0:
            masodfoku_eredmeny_label.config(text="Hiba: Nincs valós megoldás!")
        else:
            masodfoku_x1 = (-b + (masodfoku_diszkriminans ** 0.5)) / (2 * a)
            masodfoku_x2 = (-b - (masodfoku_diszkriminans ** 0.5)) / (2 * a)
            masodfoku_eredmeny_label.config(text=f"X1={masodfoku_x1}\nX2={masodfoku_x2}")
    except:
        masodfoku_eredmeny_label.config(text="Hiba: Érvénytelen bemenet!")

masodfoku_a_label = Label(masodfoku_ablak, text="A:", bg="#df5a67", fg="white", font="Arial 15")
masodfoku_b_label = Label(masodfoku_ablak, text="B:", bg="#df5a67", fg="white", font="Arial 15")
masodfoku_c_label = Label(masodfoku_ablak, text="C:", bg="#df5a67", fg="white", font="Arial 15")
masodfoku_eredmeny_cimke = Label(masodfoku_ablak, text="Végeredmény:", bg="#df5a67", fg="white", font="Arial 15")

masodfoku_a_entry = Entry(masodfoku_ablak, width=10, font="Arial 15", bg="#ad3e49")
masodfoku_b_entry = Entry(masodfoku_ablak, width=10, font="Arial 15", bg="#ad3e49")
masodfoku_c_entry = Entry(masodfoku_ablak, width=10, font="Arial 15", bg="#ad3e49")
masodfoku_eredmeny_label = Label(masodfoku_ablak, bg="#df5a67", fg="white", font="Arial 10")

masodfoku_szamitas_gomb = Button(masodfoku_ablak, text="Számítás", bg="#ad3e49", fg="white", font="Arial 10", command=masodfoku_szamitas)
masodfoku_kilepes_gomb = Button(masodfoku_ablak, text="Kilépés", command=masodfoku_ablak.destroy, bg="#ad3e49", fg="white", font="Arial 10")

masodfoku_image = PhotoImage(file="Tervek\\Képek\\masodfoku.png" ) 
masodfoku_image_label = Label(masodfoku_ablak, image=masodfoku_image)

masodfoku_a_label.grid(row=0, column=0,columnspan=2)
masodfoku_a_entry.grid(row=0, column=1, padx=10, pady=10)

masodfoku_b_label.grid(row=1, column=0,columnspan=2)
masodfoku_b_entry.grid(row=1, column=1, padx=10, pady=10)

masodfoku_c_label.grid(row=2, column=0,columnspan=2)
masodfoku_c_entry.grid(row=2, column=1, padx=10, pady=10)

masodfoku_eredmeny_cimke.grid(row=4, column=0, padx=5, pady=5)
masodfoku_eredmeny_label.grid(row=4, column=1, padx=5, pady=5)
masodfoku_szamitas_gomb.grid(row=3, columnspan=2, padx=10, pady=10)
masodfoku_kilepes_gomb.grid(row=5, columnspan=1, padx=10, pady=10)

masodfoku_image_label.grid(rowspan=5,row=0, column=2, padx=10, pady=10)
masodfoku_ablak.minsize(600, 300)
masodfoku_ablak.maxsize(600, 300)
masodfoku_ablak.mainloop()
