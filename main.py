import tkinter as tk
from tkinter import *



zulässige_noten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

window = tk.Tk()

window.title("Turnierplaner")

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)


    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

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




def main():
    global entry, listbox_noten, bestätigen, fehlermeldung, liste_beschreibung,letze_entfernen, noten
    noten = []
    center_window(window, 800, 400)

    noten_eingeben_label = tk.Label(text="""Bitte gib deine Noten von 0-15 hier ein
Drücke 'Hinzufügen' um die Note hinzuzufügen oder 'Ausrechnen' um den Durschnitt aller hinzugefügten Noten zu errechnen.\n""")
    noten_eingeben_label.pack()

    entry = tk.Entry()
    entry.pack()

    leeres_label1 = tk.Label(text="")
    leeres_label1.pack()

    hinzufügen_knopf = tk.Button(text="Hinzufügen", command=knopf_hinzufügen_def)
    hinzufügen_knopf.pack()

    fehlermeldung = tk.Label(text="")
    fehlermeldung.pack()

    liste_beschreibung = tk.Label(text="")
    liste_beschreibung.pack()


    bestätigen = tk.Button(text="Ausrechnen", command=rechnen)
    listbox_noten = tk.Listbox()

    letze_entfernen = tk.Button(text="letze Note entfernen", command=letze_entfernen)

def knopf_hinzufügen_def():
    eingabe = entry.get()
    entry.delete(0, END)
    try:
        note = int(eingabe)
    except ValueError:
        fehlermeldung.config(fg="red", text="Dies ist keine gütlige Eingabe!")
        note = ""
    if note in zulässige_noten:
        noten.append(note)
        letze_entfernen.pack()
        fehlermeldung.config(text="")
        liste_beschreibung.config(text=f"""Du hast {len(noten)} Noten eingegeben.
Hier ist eine Liste aller eingetragenen Noten: \n""")
        liste_beschreibung.pack()
        listbox_noten.insert(tk.END, note)
        listbox_noten_size = listbox_noten.size()
        listbox_noten.config(height=listbox_noten_size)
        listbox_noten.pack()
        leeres_label2 = tk.Label(text="")
        leeres_label2.pack()
        bestätigen.pack()


    else:
        fehlermeldung.config(fg="red", text="Dies ist keine gütlige Eingabe!")

def letze_entfernen():
    listbox_noten.delete(tk.END)
    listbox_noten_size = listbox_noten.size()
    listbox_noten.config(height=listbox_noten_size)
    listbox_noten.pack()
    noten.remove(noten[-1])
    liste_beschreibung.config(text=f"""Du hast {len(noten)} Noten eingegeben.
Hier ist eine Liste aller eingetragenen Noten: \n""")



def rechnen():
    alles_schließen()

    liste_beschreibung1 = tk.Label(text=f"""Du hast {len(noten)} Noten eingegeben.
Hier ist eine Liste aller eingetragenen Noten: \n""")
    liste_beschreibung1.pack()

    listbox1 = tk.Listbox()
    for note in noten:
        listbox1.insert(tk.END, note)
        listbox1_size = listbox1.size()
        listbox1.config(height=listbox1_size)
        listbox1.pack()

    gesamt = 0
    for note in noten:
        gesamt += note

    durschnitt = gesamt / len(noten)
    durschnitt = round(durschnitt, 3)

    durschnitt_noten_text = tk.Label(text=f"\nDer Durschnitt der von dir eingegebenen Noten ist : {durschnitt}\n")
    durschnitt_noten_text.pack()

    neu_starten_knopf = tk.Button(text="Neu Starten", command=neu_starten_knopf_def)
    neu_starten_knopf.pack()

def neu_starten_knopf_def():
    alles_schließen()
    main()


main()

window.mainloop()