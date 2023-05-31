from tkinter import *

hengerablak = Tk()
hengerablak.config(bg="#5FC861")
hengerablak.title("Henger felszíne és térfogata")
#-be
hengersugar = Entry(hengerablak, width=20, font="Arial 15", bg="#359e18",fg="white")
hengermagassag = Entry(hengerablak, width=20, font="Arial 15", bg="#359e18",fg="white")
#S
hengersugarszov = Label(hengerablak, text="Sugár: ",)
hengermagassagszov = Label(hengerablak, text="Magasság: ", bg="#5FC861",fg="white", font="Arial 15")
hengerszamitas = Button(hengerablak, text="Számítás",bg="#359e18",fg="white", font="Arial 15")
hengerfelszinszov = Label(hengerablak, text="Felszín: ", bg="#5FC861",fg="white", font="Arial 15")
hengerterfogatszov = Label(hengerablak, text="Térfogat: ", bg="#5FC861",fg="white", font="Arial 15")
hengerfelszinki = Label(hengerablak , bg="#5FC861",fg="white", font="Arial 15")
hengerterfogatki = Label(hengerablak , bg="#5FC861",fg="white", font="Arial 15")
hengerkilep = Button(hengerablak, text="Kilépés", command=hengerablak.destroy, bg="#359e18",fg="white", font="Arial 15")

LabelSettings = {"bg":"#5FC861", "fg":"white", "font":("Arial", 15)}
hengersugarszov.config(LabelSettings)

hengersugarszov.grid(column=1, row=2,  pady=10, padx=8)
hengersugar.grid(column=2, row=2,  pady=10)
hengermagassagszov.grid(column=1, row=3, pady=10, padx=8)
hengermagassag.grid(column=2, row=3, pady=10)
hengerszamitas.grid(column=1, row=4, columnspan=2)
hengerfelszinszov.grid(column=1, row=5, padx=8)
hengerfelszinki.grid(column=2, row=5)
hengerterfogatszov.grid(column=1, row=6, padx=8)
hengerterfogatki.grid(column=2, row=6)
hengerkilep.grid(column=1, row=10)
hengerablak.minsize(600,300)
hengerablak.maxsize(600,300)

hengerablak.mainloop()
    