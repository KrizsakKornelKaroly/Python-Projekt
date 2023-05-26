from tkinter import *

hengerablak = Tk()
hengerablak.title("Henger felszíne és térfogata")
hengersugar = Entry(hengerablak)
hengermagassag = Entry(hengerablak)
hengersugarszov = Label(hengerablak, text="Sugár: ")
hengermagassagszov = Label(hengerablak, text="Magasság: ")
hengerszamitas = Button(hengerablak, text="Számítás")
hengerfelszinszov = Label(hengerablak, text="Felszín: ")
hengerterfogatszov = Label(hengerablak, text="Térfogat: ")
hengerfelszinki = Label(hengerablak)
hengerterfogatki = Label(hengerablak)
hengerkilep = Button(hengerablak, text="Kilépés", command=hengerablak.destroy)

hengersugarszov.grid(column=1, row=2)
hengersugar.grid(column=2, row=2)
hengermagassagszov.grid(column=1, row=3)
hengermagassag.grid(column=2, row=3)
hengerszamitas.grid(column=1, row=4, columnspan=2, sticky=CENTER)
hengerfelszinszov.grid(column=1, row=5)
hengerfelszinki.grid(column=2, row=5)
hengerterfogatszov.grid(column=1, row=6)
hengerterfogatki.grid(column=2, row=6)
hengerkilep.grid(column=1, row=10)

hengerablak.mainloop()
    