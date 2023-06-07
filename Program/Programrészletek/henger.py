from tkinter import *

hengerablak = Tk()
hengerablak.config(bg="#5FC861")
hengerablak.title("Henger felszíne és térfogata")
#bemenet
hengersugar = Entry(hengerablak, width=20, font="Arial 15", bg="#359e18",fg="white")
hengermagassag = Entry(hengerablak, width=20, font="Arial 15", bg="#359e18",fg="white")
hengersugarszov = Label(hengerablak, text="Sugár: ",)
hengermagassagszov = Label(hengerablak, text="Magasság: ")
#szamitas
hengerszamitas = Button(hengerablak, text="Számítás",bg="#359e18",fg="white", font="Arial 15")
#kimenet
hengerfelszinszov = Label(hengerablak, text="Felszín: ")
hengerterfogatszov = Label(hengerablak, text="Térfogat: ")
hengerfelszinki = Label(hengerablak)
hengerterfogatki = Label(hengerablak)
#EXITc
hengerkilep = Button(hengerablak, text="Kilépés", command=hengerablak.destroy, bg="#359e18",fg="white", font="Arial 15")

#LABELCONFIG
LabelSettings = {"bg":"#5FC861", "fg":"white", "font":("Arial", 15)}
hengersugarszov.config(LabelSettings)
hengermagassagszov.config(LabelSettings)
hengerfelszinszov.config(LabelSettings)
hengerterfogatszov.config(LabelSettings)
hengerfelszinki.config(LabelSettings)
hengerterfogatki.config(LabelSettings)

#GRIDALIGNMENT
hengersugarszov.grid(column=1, row=2,  pady=10, padx=8)
hengersugar.grid(column=2, row=2,  pady=10)
hengermagassagszov.grid(column=1, row=3, pady=10, padx=8)
hengermagassag.grid(column=2, row=3, pady=10)
hengerszamitas.grid(column=1, row=4, columnspan=2)
hengerfelszinszov.grid(column=1, row=5, padx=8, pady=10)
hengerfelszinki.grid(column=2, row=5, pady=10)
hengerterfogatszov.grid(column=1, row=6, padx=8, pady=10)
hengerterfogatki.grid(column=2, row=6, pady=10)
hengerkilep.place(relx=0.03, rely=0.95, anchor=SW)
hengerablak.minsize(600,300)
hengerablak.maxsize(600,300)

hengerablak.mainloop()
    