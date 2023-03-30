from tkinter import*
import tkinter as tk
import tkinter.ttk as ttk


ekran = Tk()
ekran.geometry("600x500+400+150")


mesai = Entry()
mesai.grid(row = 0,column = 1)


mesailabel = Label(text = "Mesai Saatinizi Giriniz = ")
mesailabel.grid(row = 0,column = 0)

prim = Entry()
prim.grid(row = 1,column = 1)

primlabel = Label(text = "Aylık Prim Miktarınızı Giriniz = ")
primlabel.grid(row = 1,column = 0)

kkas = Scale(ekran, from_ = 0, to = 100, length = 200, tickinterval = 40)
kkas.grid(row = 2,column = 1)

kkaslabel = Label(text = "Üye Yaptığınız Kredi Kartı Kullanıcı Sayısı = ")
kkaslabel.grid(row = 2,column = 0)

kks = Scale(ekran, from_ = 0, to = 50, length = 150, tickinterval = 25, orient = HORIZONTAL)
kks.grid(row = 3,column = 1)

kkslabel = Label(text = "Kredi Kullandırma Sayınızı Giriniz = ")
kkslabel.grid(row = 3,column = 0)


def hesapla():
    global maas
    global sonmaas

    maas = (int(mesai.get())*50) + (int(prim.get()*1)) + (int(kkas.get()*20)) + (int(kks.get()*50))
    if int(kks.get()) >20:
        maas = (maas + 1000)
    maaslabel["text"] = maas

    sonmaas = 6000 + (maas - (maas * 17/100))
    sonmaaslabel["text"] = sonmaas


cizgilabel = Label(text = "-------------------------------")
cizgilabel.grid(row = 4,column = 1)

cizgilabel2 = Label(text = "-------------------------------")
cizgilabel2.grid(row = 4,column = 0)

maaslabel = Label(text = "")
maaslabel.grid(row = 5,column = 1)

maaslabel2 = Label(text = "Aylık Hakedişiniz = ")
maaslabel2.grid(row = 5,column = 0)

sonmaaslabel = Label(text = "")
sonmaaslabel.grid(row = 6,column = 1)

sonmaaslabel2 = Label(text = "Alacağınız Maaş Ücreti = ")
sonmaaslabel2.grid(row = 6,column = 0)

buton = Button(text = "HESAPLA", command = hesapla)
buton.grid(row = 7,column = 1)


mainloop()