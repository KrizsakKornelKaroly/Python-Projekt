from tkinter import *
from tkinter import ttk

ablak = Tk()
ablak.configure(bg='#eb942a')
ablak.title('Raktárprogram')
ablak.geometry("600x300")
menubar = Menu(ablak)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Geometriai számítások', menu = file)
file.add_command(label ='Háromszög',command = None)
file.add_command(label ='Henger',command = None)
file.add_command(label ='Kocka',command = None)
file.add_command(label ='Kör',command = None)
file.add_command(label ='Négyzet',command = None)
file.add_command(label ='Pitagorasz',command = None)

file1 = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Matematikai számítások', menu = file1)
file1.add_command(label ='Százalékszámítás',command = None)
file1.add_command(label ='Átlagszámítás',command = None)
file1.add_command(label ='Másodfokú-egyenletkalkulátor',command = None)
file1.add_command(label ='Számgenerátor',command = None)
file1.add_command(label ='Négyzet',command = None)
file1.add_command(label ='Pitagorasz',command = None)

file2 = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Pénzügyi számítások', menu = file2)
file2.add_command(label ='Borravaló',command = None)
file2.add_command(label ='Kamat-kalkulátor',command = None)
file2.add_command(label ='Adószám-generátor',command = None)
ablak.config(menu=menubar)

file3 = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Kilépés', menu = file3, command= ablak.destroy)
file3.add_separator()
file3.add_command(label ='Kilépés', command = ablak.destroy)

cim=Label(ablak,text="Üdvözöllek az Univerzális Kalkulátor \nAlkalmazásban!")
cim.config(bg="#eb942a", fg="white",font="Arial 17", padx=10)
cim.pack()

kesz=Label(ablak,text="Az alkalmazást készítették: Krizsák Kornél, Péter Dávid, Pálinkás Andor")
kesz.config(bg="#eb942a", fg="white",font="Arial 13", padx=10)
kesz.pack(side=BOTTOM)




ablak.mainloop()