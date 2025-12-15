
import winsound, random, os
from playsound import playsound
from tkinter import *

zongorabillentyu_szama = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
hang_neve_kereszt = ["A0", "A#0", "B0", "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A1", "A#1", "B1", "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6", "F6", "F#6", "G6", "G#6", "A6", "A#6", "B6", "C7", "C#7", "D7", "D#7", "E7", "F7", "F#7", "G7", "G#7", "A7", "A#7", "B7", "C8"]
hang_neve_be = ["A0", "Bb0", "B0", "C1", "Db1", "D1", "Eb1", "E1", "F1", "Gb1", "G1", "Ab1", "A1", "Bb1", "B1", "C2", "Db2", "D2", "Eb2", "E2", "F2", "Gb2", "G2", "Ab2", "A2", "Bb2", "B2", "C3", "Db3", "D3", "Eb3", "E3", "F3", "Gb3", "G3", "Ab3", "A3", "Bb3", "B3", "C4", "Db4", "D4", "Eb4", "E4", "F4", "Gb4", "G4", "Ab4", "A4", "Bb4", "B4", "C5", "Db5", "D5", "Eb5", "E5", "F5", "Gb5", "G5", "Ab5", "A5", "Bb5", "B5", "C6", "Db6", "D6", "Eb6", "E6", "F6", "Gb6", "G6", "Ab6", "A6", "Bb6", "B6", "C7", "Db7", "D7", "Eb7", "E7", "F7", "Gb7", "G7", "Ab7", "A7", "Bb7", "B7", "C8"]
frekvencia = [28, 29, 31, 33, 35, 37, 39, 41, 44, 46, 49, 52, 55, 58, 62, 65, 69, 73, 78, 82, 87, 93, 98, 104, 110, 117, 123, 131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247, 262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523, 554, 587, 622, 659, 698, 740, 784, 831, 880, 932, 988, 1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976, 2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951, 4186]
hangkoz_neve = ["0 - prím", "1 - kis szekund", "2 - nagy szekund", "3 - kis terc", "4 - nagy terc", "5 - tiszta kvart", "6 - bővített kvart = tritonus = szűkített kvint", "7 - tiszta kvint", "8 - kis szext", "9 - nagy szext", "10 - kis szeptim", "11 - nagy szeptim", "12 - oktáv", "13 - kis nóna", "14 - nagy nóna", "15 - kis decima", "16 - nagy decima", "17 - tiszta undecima", "18 - bővített undecima = szűkített duodecima", "19 - tiszta duodecima", "20 - kis tredecima", "21 - nagy tredecima"]

#Apáé
#most meg fogok probalni ellentmondast tenni bele
#abszolut_also = 25 #!!! A4-től két oktáv mindkét irányban; a minimum 1
#abszolut_felso = 73 #!!! A4-től két oktáv mindkét irányban; a maximum 88
#abszolut_index_lista = list(range(abszolut_also - 1, abszolut_felso))
#hangkoz_sz_elso_hang_also = 25 #!!! A4-től két oktáv mindkét irányban; a minimum 1
#hangkoz_sz_elso_hang_felso = 73 #!!! A4-től két oktáv mindkét irányban; a maximum 88
#hangkoz_sz_elso_hang_index_lista = list(range(hangkoz_sz_elso_hang_also - 1, hangkoz_sz_elso_hang_felso))
#hangkoz_sz_hangkoz_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] #!!! egy oktáv; a teljes sor [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

#Danié
abszolut_index_lista = [48, 50, 51, 53, 55, 56, 58, 60, 62, 63, 65, 67] #!!! A4 - E6, csak fehér billentyűk
hangkoz_sz_elso_hang_index_lista = [48, 50, 51, 53, 55, 56, 58, 60, 62, 63, 65, 67] #!!! A4 - E6, csak fehér billentyűk
hangkoz_sz_hangkoz_lista = [0, 4, 7, 12] #!!! prím, nagy terc, tiszta kvint, oktáv

hang_indexe = -1
elso_hang_indexe = -1
hangkoz = -1
hangkoz_iranya = -1
masodik_hang_indexe = -1

radio_hangkoz = []

fulhangolo = Tk()
fulhangolo.title("Fülhangoló")
fulhangolo.geometry("700x550")

gyakorlo = StringVar()
hangszer = StringVar()
zongorabillentyu_szama_abszolut = StringVar()
hang_neve_kereszt_abszolut = StringVar()
hang_neve_be_abszolut = StringVar()
hangkoz_hangkoz_sz = StringVar()

gyakorlo_text = ""
hangszer_text = ""
zongorabillentyu_szama_abszolut_text = ""
hang_neve_kereszt_abszolut_text = ""
hang_neve_be_abszolut_text = ""
hangkoz_hangkoz_sz_text = -1

tippelt = 0
talalt = 0
szazalek = 0

konyvtar = os.getcwd()


def ilyet():
    global gyakorlo_text, hangszer_text, hang_indexe, elso_hang_indexe, masodik_hang_indexe, hangkoz

    gyakorlo_text = gyakorlo.get()
    hangszer_text = hangszer.get()

    if gyakorlo_text == "abszolut":
       valaszto.pack_forget()

       hang_indexe = random.choice(abszolut_index_lista) 
       print(zongorabillentyu_szama[hang_indexe])

       entry_zongorabillentyu_szama_abszolut.place(x = 20, y = 70)
       entry_hang_neve_kereszt_abszolut.place(x = 185, y = 70)
       entry_hang_neve_be_abszolut.place(x = 365, y = 70)
       felirat_zongorabillentyu_szama_helyes_abszolut.place_forget()
       felirat_hang_neve_kereszt_helyes_abszolut.place_forget()
       felirat_hang_neve_be_helyes_abszolut.place_forget()
       felirat_jo_abszolut.place_forget()
       felirat_rossz_abszolut.place_forget()
       gomb_tippelek_abszolut.place(x = 130, y = 180)
       gomb_meg_egyet_abszolut.place_forget()

       tippelo_abszolut.pack(fill = "both", expand = True, padx = 10, pady = 10)
       if hangszer_text == "generalt":
          winsound.Beep(frekvencia[hang_indexe], 1000)
       else:
          playsound(konyvtar + "/zene/sounds/piano_" + str(zongorabillentyu_szama[hang_indexe]).rjust(2, "0") + ".mp3")
    else:
       valaszto.pack_forget()

       elso_hang_indexe = random.choice(hangkoz_sz_elso_hang_index_lista) 
       hangkoz = random.choice(hangkoz_sz_hangkoz_lista)
       hangkoz_iranya = random.randint(0, 1)
       masodik_hang_indexe = elso_hang_indexe + (-1) ** hangkoz_iranya * hangkoz

       print(zongorabillentyu_szama[elso_hang_indexe])
       print(hangkoz)

       for i in range(0, len(hangkoz_sz_hangkoz_lista)):
           radio_hangkoz[i].place(x = 15 + 150 * (i // 8), y = 40 + 30 * (i % 8))
       felirat_hangkoz_neve_helyes_hangkoz_sz.place_forget()
       felirat_jo_hangkoz_sz.place_forget()
       felirat_rossz_hangkoz_sz.place_forget()
       gomb_tippelek_hangkoz_sz.place(x = 130, y = 300)
       gomb_meg_egyet_hangkoz_sz.place_forget()

       tippelo_hangkoz_sz.pack(fill = "both", expand = True, padx = 10, pady = 10)

       if hangszer_text == "generalt":
          winsound.Beep(frekvencia[elso_hang_indexe], 1000)
          winsound.Beep(frekvencia[masodik_hang_indexe], 1000)
       else:
          playsound(konyvtar + "/zene/sounds/piano_" + str(zongorabillentyu_szama[elso_hang_indexe]).rjust(2, "0") + ".mp3")
          playsound(konyvtar + "/zene/sounds/piano_" + str(zongorabillentyu_szama[masodik_hang_indexe]).rjust(2, "0") + ".mp3")



def tippelek_abszolut():
    global hang_indexe, \
           felirat_zongorabillentyu_szama_helyes_abszolut, felirat_hang_neve_kereszt_helyes_abszolut, felirat_hang_neve_be_helyes_abszolut, \
           tippelt, talalt, szazalek

    zongorabillentyu_szama_abszolut_text = zongorabillentyu_szama_abszolut.get()
    hang_neve_kereszt_abszolut_text = hang_neve_kereszt_abszolut.get()
    hang_neve_be_abszolut_text = hang_neve_be_abszolut.get()

    if zongorabillentyu_szama_abszolut_text == "":
       zongorabillentyu_szama_abszolut_text = -100
    if hang_neve_kereszt_abszolut_text == "":
       hang_neve_kereszt_abszolut_text = "üres"
    if hang_neve_be_abszolut_text == "":
       hang_neve_be_abszolut_text = "üres"

    entry_zongorabillentyu_szama_abszolut.place_forget()
    entry_hang_neve_kereszt_abszolut.place_forget()
    entry_hang_neve_be_abszolut.place_forget()
    felirat_zongorabillentyu_szama_helyes_abszolut = Label(tippelo_abszolut, text = zongorabillentyu_szama[hang_indexe])
    felirat_zongorabillentyu_szama_helyes_abszolut.place(x = 20, y = 70)
    felirat_hang_neve_kereszt_helyes_abszolut = Label(tippelo_abszolut, text = hang_neve_kereszt[hang_indexe])
    felirat_hang_neve_kereszt_helyes_abszolut.place(x = 185, y = 70)
    felirat_hang_neve_be_helyes_abszolut = Label(tippelo_abszolut, text = hang_neve_be[hang_indexe])
    felirat_hang_neve_be_helyes_abszolut.place(x = 365, y = 70)

    if (  int(zongorabillentyu_szama_abszolut_text) == zongorabillentyu_szama[hang_indexe]
       or hang_neve_kereszt_abszolut_text.upper() == hang_neve_kereszt[hang_indexe].upper()
       or hang_neve_be_abszolut_text.upper() == hang_neve_be[hang_indexe].upper()):
       felirat_jo_abszolut.place(x = 15, y = 115)
       talalt = talalt + 1
    else:
       felirat_rossz_abszolut.place(x = 15, y = 115)

    gomb_tippelek_abszolut.place_forget()
    gomb_meg_egyet_abszolut.place(x = 130, y = 180)

    tippelt = tippelt + 1
    szazalek = round(talalt / tippelt * 100)

    felirat_tippelt_visszajelzo_abszolut.config(text = f"Tippelt: {tippelt}")
    felirat_talalt_visszajelzo_abszolut.config(text = f"Talált: {talalt}")
    felirat_szazalek_visszajelzo_abszolut.config(text = f"Találati arány: {szazalek} %")

    zongorabillentyu_szama_abszolut.set("")
    hang_neve_kereszt_abszolut.set("")
    hang_neve_be_abszolut.set("")

def tippelek_hangkoz_sz():
    global elso_hang_indexe, masodik_hang_indexe, hangkoz, \
           felirat_hangkoz_neve_helyes_hangkoz_sz, \
           tippelt, talalt, szazalek

    hangkoz_hangkoz_sz_text = hangkoz_hangkoz_sz.get()

    if hangkoz_hangkoz_sz_text == "":
       hangkoz_hangkoz_sz_text = -100

    for i in range(0, len(hangkoz_sz_hangkoz_lista)):
       radio_hangkoz[i].place_forget()
    
    felirat_hangkoz_neve_helyes_hangkoz_sz = Label(tippelo_hangkoz_sz, text = hangkoz_neve[hangkoz])
    felirat_hangkoz_neve_helyes_hangkoz_sz.place(x = 20, y = 70)

    if int(hangkoz_hangkoz_sz_text) == hangkoz:
       felirat_jo_hangkoz_sz.place(x = 15, y = 115)
       talalt = talalt + 1
    else:
       felirat_rossz_hangkoz_sz.place(x = 15, y = 115)

    gomb_tippelek_hangkoz_sz.place_forget()
    gomb_meg_egyet_hangkoz_sz.place(x = 130, y = 300)

    tippelt = tippelt + 1
    szazalek = round(talalt / tippelt * 100)

    felirat_tippelt_visszajelzo_hangkoz_sz.config(text = f"Tippelt: {tippelt}")
    felirat_talalt_visszajelzo_hangkoz_sz.config(text = f"Talált: {talalt}")
    felirat_szazalek_visszajelzo_hangkoz_sz.config(text = f"Találati arány: {szazalek} %")

    for i in range(0, len(hangkoz_sz_hangkoz_lista)):
       radio_hangkoz[i].place_forget()
    hangkoz_hangkoz_sz.set(None)

def jatsszd_ujra_abszolut():
       if hangszer_text == "generalt":
          winsound.Beep(frekvencia[hang_indexe], 1000)
       else:
          playsound(konyvtar + "/zene/sounds/piano_" + str(zongorabillentyu_szama[hang_indexe]) + ".mp3")

def jatsszd_ujra_hangkoz_sz():
       if hangszer_text == "generalt":
          winsound.Beep(frekvencia[elso_hang_indexe], 1000)
          winsound.Beep(frekvencia[masodik_hang_indexe], 1000)
       else:
          playsound(konyvtar + "/zene/sounds/piano_" + str(zongorabillentyu_szama[elso_hang_indexe]) + ".mp3")
          playsound(konyvtar + "/zene/sounds/piano_" + str(zongorabillentyu_szama[masodik_hang_indexe]) + ".mp3")

def inkabb_mast_gyakorlok_abszolut():
    global tippelt, talalt, szazalek
    tippelo_abszolut.pack_forget()
    tippelt = 0
    talalt = 0
    szazalek = 0
    valaszto.pack(fill = "both", expand = True, padx = 10, pady = 10)

def inkabb_mast_gyakorlok_hangkoz_sz():
    global tippelt, talalt, szazalek
    tippelo_hangkoz_sz.pack_forget()
    tippelt = 0
    talalt = 0
    szazalek = 0
    valaszto.pack(fill = "both", expand = True, padx = 10, pady = 10)

def kilepek():
    fulhangolo.quit()



#VALASZTO

valaszto = Frame(fulhangolo, padx = 30, pady = 30)

felirat_gyakorlas_valaszto = Label(valaszto, text = "Mit szeretnél gyakorolni?")
felirat_gyakorlas_valaszto.place(x = 5, y = 0)

radio_abszolut = Radiobutton(valaszto, text = "Abszolút hang", variable = gyakorlo, value = "abszolut", tristatevalue = "x")
radio_abszolut.place(x = 15, y = 30)

radio_hangkoz_sz = Radiobutton(valaszto, text = "Hangköz számokkal / betűkkel", variable = gyakorlo, value = "hangkoz_sz", tristatevalue = "x")
radio_hangkoz_sz.place(x = 15, y = 60)

#radio_hangkoz_k = Radiobutton(valaszto, text = "Hangköz kottával", variable = gyakorlo, value = "hangkoz_k", tristatevalue = "x")
#radio_hangkoz_k.place(x = 15, y = 90)

felirat_hangszer_valaszto = Label(valaszto, text = "Milyen hangokkal szeretnél gyakorolni?")
felirat_hangszer_valaszto.place(x = 5, y = 130)

radio_generalt = Radiobutton(valaszto, text = "Generált hang", variable = hangszer, value = "generalt", tristatevalue = "x")
radio_generalt.place(x = 15, y = 160)

radio_zongora = Radiobutton(valaszto, text = "Zongora", variable = hangszer, value = "zongora", tristatevalue = "x")
radio_zongora.place(x = 15, y = 190)

gomb_ilyet = Button(valaszto, text = "Ilyet!", padx = 10, command = ilyet)
gomb_ilyet.place(x = 15, y = 250)

gomb_kilepek = Button(valaszto, text = "Kilépek", padx = 10, command = kilepek)
gomb_kilepek.place(x = 100, y = 250)



#TIPPELO_ABSZOLUT

tippelo_abszolut = Frame(fulhangolo, padx = 30, pady = 30)

felirat_kerdes_abszolut = Label(tippelo_abszolut, text = "Milyen hangot hallasz?")
felirat_kerdes_abszolut.place(x = 5, y = 0)

felirat_zongorabillentyu_szama_abszolut = Label(tippelo_abszolut, text = "Zongorabillentyű száma:")
felirat_zongorabillentyu_szama_abszolut.place(x = 15, y = 40)

felirat_hang_neve_kereszt_abszolut = Label(tippelo_abszolut, text = "Hang neve kereszt jelöléssel:")
felirat_hang_neve_kereszt_abszolut.place(x = 180, y = 40)

felirat_hang_neve_be_abszolut = Label(tippelo_abszolut, text = "Hang neve bé jelöléssel:")
felirat_hang_neve_be_abszolut.place(x = 360, y = 40)

entry_zongorabillentyu_szama_abszolut = Entry(tippelo_abszolut, textvariable = zongorabillentyu_szama_abszolut)

entry_hang_neve_kereszt_abszolut = Entry(tippelo_abszolut, textvariable = hang_neve_kereszt_abszolut)

entry_hang_neve_be_abszolut = Entry(tippelo_abszolut, textvariable = hang_neve_be_abszolut)

felirat_zongorabillentyu_szama_helyes_abszolut = Label(tippelo_abszolut, text = zongorabillentyu_szama[elso_hang_indexe])

felirat_hang_neve_kereszt_helyes_abszolut = Label(tippelo_abszolut, text = hang_neve_kereszt[elso_hang_indexe])

felirat_hang_neve_be_helyes_abszolut = Label(tippelo_abszolut, text = hang_neve_be[elso_hang_indexe])

felirat_jo_abszolut = Label(tippelo_abszolut, text = "JUHÉJ!!!", font = ("Arial", 25))

felirat_rossz_abszolut = Label(tippelo_abszolut, text = "Majdnem.", font = ("Arial", 25))

gomb_jatsszd_ujra_abszolut = Button(tippelo_abszolut, text = "Játsszd újra!", padx = 10, command = jatsszd_ujra_abszolut)
gomb_jatsszd_ujra_abszolut.place(x = 15, y = 180)

gomb_tippelek_abszolut = Button(tippelo_abszolut, text = "Szerintem ez!", padx = 10, command = tippelek_abszolut)

gomb_meg_egyet_abszolut = Button(tippelo_abszolut, text = "Még egyet!", padx = 10, command = ilyet)

gomb_inkabb_mast_gyakorlok_abszolut = Button(tippelo_abszolut, text = "Inkább mást gyakorlok!", padx = 10, command = inkabb_mast_gyakorlok_abszolut)
gomb_inkabb_mast_gyakorlok_abszolut.place(x = 255, y = 180)

gomb_kilepek_abszolut = Button(tippelo_abszolut, text = "Kilépek", padx = 10, command = kilepek)
gomb_kilepek_abszolut.place(x = 435, y = 180)

felirat_tippelt_visszajelzo_abszolut = Label(tippelo_abszolut, text = f"Tippelt: {tippelt}")
felirat_tippelt_visszajelzo_abszolut.place(x = 5, y = 280)

felirat_talalt_visszajelzo_abszolut = Label(tippelo_abszolut, text = f"Talált: {talalt}")
felirat_talalt_visszajelzo_abszolut.place(x = 5, y = 300)

felirat_szazalek_visszajelzo_abszolut = Label(tippelo_abszolut, text = f"Találati arány: {szazalek} %")
felirat_szazalek_visszajelzo_abszolut.place(x = 5, y = 320)




#TIPPELO_HANGKOZ_SZ

tippelo_hangkoz_sz = Frame(fulhangolo, padx = 30, pady = 30)

felirat_kerdes_hangkoz_sz = Label(tippelo_hangkoz_sz, text = "Milyen hangközt hallasz?")
felirat_kerdes_hangkoz_sz.place(x = 5, y = 0)

for i in range(0, len(hangkoz_sz_hangkoz_lista)):
   radio_hangkoz.append(Radiobutton(tippelo_hangkoz_sz, text = hangkoz_neve[hangkoz_sz_hangkoz_lista[i]], variable = hangkoz_hangkoz_sz, value = hangkoz_sz_hangkoz_lista[i], tristatevalue = "x"))
   radio_hangkoz[i].place(x = 15 + 150 * (i // 8), y = 40 + 30 * (i % 8))

felirat_hangkoz_neve_helyes_hangkoz_sz = Label(tippelo_hangkoz_sz, text = hangkoz_neve[hangkoz_iranya * hangkoz])

felirat_jo_hangkoz_sz = Label(tippelo_hangkoz_sz, text = "JUHÉJ!!!", font = ("Arial", 25))

felirat_rossz_hangkoz_sz = Label(tippelo_hangkoz_sz, text = "Majdnem.", font = ("Arial", 25))

gomb_jatsszd_ujra_hangkoz_sz = Button(tippelo_hangkoz_sz, text = "Játsszd újra!", padx = 10, command = jatsszd_ujra_hangkoz_sz)
gomb_jatsszd_ujra_hangkoz_sz.place(x = 15, y = 300)

gomb_tippelek_hangkoz_sz = Button(tippelo_hangkoz_sz, text = "Szerintem ez!", padx = 10, command = tippelek_hangkoz_sz)

gomb_meg_egyet_hangkoz_sz = Button(tippelo_hangkoz_sz, text = "Még egyet!", padx = 10, command = ilyet)

gomb_inkabb_mast_gyakorlok_hangkoz_sz = Button(tippelo_hangkoz_sz, text = "Inkább mást gyakorlok!", padx = 10, command = inkabb_mast_gyakorlok_hangkoz_sz)
gomb_inkabb_mast_gyakorlok_hangkoz_sz.place(x = 255, y = 300)

gomb_kilepek_hangkoz_sz = Button(tippelo_hangkoz_sz, text = "Kilépek", padx = 10, command = kilepek)
gomb_kilepek_hangkoz_sz.place(x = 435, y = 300)

felirat_tippelt_visszajelzo_hangkoz_sz = Label(tippelo_hangkoz_sz, text = f"Tippelt: {tippelt}")
felirat_tippelt_visszajelzo_hangkoz_sz.place(x = 5, y = 400)

felirat_talalt_visszajelzo_hangkoz_sz = Label(tippelo_hangkoz_sz, text = f"Talált: {talalt}")
felirat_talalt_visszajelzo_hangkoz_sz.place(x = 5, y = 420)

felirat_szazalek_visszajelzo_hangkoz_sz = Label(tippelo_hangkoz_sz, text = f"Találati arány: {szazalek} %")
felirat_szazalek_visszajelzo_hangkoz_sz.place(x = 5, y = 440)



valaszto.pack(fill = "both", expand = True, padx = 10, pady = 10)



fulhangolo.mainloop()

