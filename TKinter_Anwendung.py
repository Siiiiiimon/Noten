import tkinter as tk
from tkinter import *
import random

window = tk.Tk()

window.title("Turnierplaner")

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)


    window.geometry('%dx%d+%d+%d' % (width, height, x, y))




def main():
    center_window(window, 800, 800)
    global teilnehmer
    teilnehmer = []
    teilnehmerabfrage()

def teilnehmerabfrage():
    global teilnehmer_eingeben, teilnehmer_bestätigen, teilnehmer_aufnehmen,hinzugefügte_teilnehmer_anzahl, liste_teilnehmer_widget, liste_teilnehmer_beschreibung, leeres_label1

    teilnehmerabfrage_label = tk.Label(text="""Bitte gib einen Namen ein und drücke den 'Teilnehmen' Knopf um den eingebenen Teilnehmer mitspielen zu lassen,
wenn alle Namen der Teilnehmer eingetragen wurden, drücke den 'Spiele berechnen' Knopf.

Es müssen mindestens 4 Spieler eingetragen werden und es dürfen höchstens 16 Spieler eingetragen werden.\n""")
    teilnehmerabfrage_label.pack()

    teilnehmer_eingeben = tk.Entry()
    teilnehmer_eingeben.pack()

    leeres_label1 = tk.Label(text="")
    leeres_label1.pack()

    teilnehmer_aufnehmen = tk.Button(text="Teilnehmen", command=teilnehmer_hinzufügen, width=20)
    teilnehmer_aufnehmen.pack()


    hinzugefügte_teilnehmer_anzahl = tk.Label(text="")
    hinzugefügte_teilnehmer_anzahl.pack()

    teilnehmer_bestätigen = tk.Button(text="Spiele berechnen", command=spiele_berechnen_knopf, width=20)

    liste_teilnehmer_widget = tk.Listbox()

    liste_teilnehmer_beschreibung = tk.Label(text="Hier ist eine Liste aller aktuellen Teilnehmer:\n")





def teilnehmer_hinzufügen():
    teilnehmer.append(teilnehmer_eingeben.get())

    liste_teilnehmer_widget.insert(tk.END, teilnehmer_eingeben.get())
    liste_teilnehmer_widget_size = liste_teilnehmer_widget.size()
    liste_teilnehmer_widget.config(height=liste_teilnehmer_widget_size)
    liste_teilnehmer_beschreibung.pack()
    liste_teilnehmer_widget.pack()


    teilnehmer_eingeben.delete(0, END)

    if len(teilnehmer) < 4:
        hinzugefügte_teilnehmer_anzahl.config(text=f"""\n{teilnehmer[-1]} ist Teilnehmer {len(teilnehmer)}/16. 

Es fehlen noch mindestens {4 - len(teilnehmer)} zum Starten!""")
    if len(teilnehmer) == 4:
        leeres_label2 = tk.Label(text="")
        leeres_label2.pack()
        teilnehmer_bestätigen.pack()
        hinzugefügte_teilnehmer_anzahl.config(text=f"""\n{teilnehmer[-1]} ist Teilnehmer {len(teilnehmer)}/16.

Jetzt kann gestartet werden!""")
    if len(teilnehmer) > 4:
        hinzugefügte_teilnehmer_anzahl.config(text=f"""\n{teilnehmer[-1]} ist Teilnehmer {len(teilnehmer)}/16.

Es kann gestartet werden!""")
    if len(teilnehmer) == 16:
        teilnehmer_eingeben.pack_forget()
        teilnehmer_aufnehmen.pack_forget()
        leeres_label1.forget()
        hinzugefügte_teilnehmer_anzahl.config(text=f"""\n{teilnehmer[-1]} ist Teilnehmer {len(teilnehmer)}/16.

Die Maximale Anzahl an Teilnehmern von 16 wurde erreicht!

Starte jetzt das Programm in dem du auf den 'Spiele berechnen' Knopf drückst""")

def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list

def alles_schließen():
    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()



def spiele_berechnen_knopf():
    alles_schließen()
    anzahl_teilnehmer = tk.Label(text=f"""Es gibt {len(teilnehmer)} Teilnehmer.
Hier ist eine Liste aller Teilnehmer:\n""")
    anzahl_teilnehmer.pack()
    liste_teilnehmer_widget.pack()
    sortierten_spiele = tk.Label(text=f"\nHier sind die sortierten Spiele:\n")
    sortierten_spiele.pack()

    main_berechnung()

def spiele_berechnen():
    spiele_berechnung = list(teilnehmer)
    spiele = []
    anzahl_schleifendurchläufe = len(teilnehmer)
    while anzahl_schleifendurchläufe > 0:
        a = 0
        b = 1
        for i in spiele_berechnung:
            if b >= len(spiele_berechnung):
                break
            spiele.append(f"{spiele_berechnung[a]} vs {spiele_berechnung[b]}")
            b += 1

        del spiele_berechnung[0]
        anzahl_schleifendurchläufe -= 1
    return spiele


def zufall_spiel_erstellen(übrigen_spiele, teilnehmer):
    global teilnehmer_1, teilnehmer_2
    teilnehmer_1 = random.randint(0, len(teilnehmer)-1)
    teilnehmer_2 = random.randint(0, len(teilnehmer)-1)
    if teilnehmer_2 < teilnehmer_1:
        teilnehmer_1_tausch = teilnehmer_1
        teilnehmer_2_tausch = teilnehmer_2
        teilnehmer_2 = teilnehmer_1_tausch
        teilnehmer_1 = teilnehmer_2_tausch
    spiel = f"{teilnehmer[teilnehmer_1]} vs {teilnehmer[teilnehmer_2]}"
    if spiel in übrigen_spiele:
        return spiel
    else:
        spiel = ""
        return spiel

def berechnen_spiele(teilnehmer):
    global teilnehmer_1, teilnehmer_1_vorher, teilnehmer_2, teilnehmer_2_vorher, spiele
    spiel = ""
    übrigen_spiele = list(spiele)
    while spiel not in spiele:
        spiel = zufall_spiel_erstellen(spiele, teilnehmer)
        if spiel != "":
            if übrigen_spiele != [] and spiel in übrigen_spiele:
                übrigen_spiele.remove(spiel)
        if teilnehmer_1 == teilnehmer_1_vorher or teilnehmer_1 == teilnehmer_2_vorher:
            spiel = ""
            if übrigen_spiele == []:
                spiel = zufall_spiel_erstellen(übrigen_spiele, teilnehmer)
        if teilnehmer_2 == teilnehmer_1_vorher or teilnehmer_2 == teilnehmer_2_vorher:
            spiel = ""
            if übrigen_spiele == []:
                spiel = zufall_spiel_erstellen(spiele, teilnehmer)

    teilnehmer_1_vorher = teilnehmer_1
    teilnehmer_2_vorher = teilnehmer_2
    spiele.remove(spiel)
    return spiel

def main_berechnung():
    global spiele
    spiele = spiele_berechnen()
    global teilnehmer_1, teilnehmer_2, teilnehmer_2_vorher, teilnehmer_1_vorher
    teilnehmer_1 = 0
    teilnehmer_1_vorher = 0
    teilnehmer_2 = 0
    teilnehmer_2_vorher = 0
    spiele_reihenfolge_schleife = len(spiele)
    spiele_reihenfolge = []

    while spiele_reihenfolge_schleife > 0:
        spiele_reihenfolge.append(berechnen_spiele(teilnehmer))
        spiele_reihenfolge_schleife -= 1


    liste_sortierte_spiele = tk.Listbox()
    for element in spiele_reihenfolge:
        liste_sortierte_spiele.insert(tk.END, element)
    liste_sortierte_spiele.pack()

    neu_starten_label = tk.Label(text="\nWenn du noch ein Turnier planes willst, drücke aud den 'Neu Starten' Knopf!\n")
    neu_starten_label.pack()

    neu_starten_knopf = tk.Button(text="Neu Starten", command=neu_starten_knopf_def)
    neu_starten_knopf.pack()

def neu_starten_knopf_def():
    alles_schließen()
    main()




main()

window.mainloop()