import os,easygui
what = easygui.buttonbox("Wybierz opcje zasilania.","Opcje Zasilania",["Wyłącz opcje zasilania",
                                                                      "Włącz opcje zasilania"])
if what == "Włącz opcje zasilania":
    if easygui.buttonbox("Teraz włączysz wszystkie opcje zasilania. Jesteś pewien?",
                         "Pewien?",["Tak","Nie"])== "Tak":
        os.system("reg import of.reg")
elif what == "Wyłącz opcje zasilania":
    if easygui.buttonbox("Teraz wyłączysz wszystkie opcje zasilania. Jesteś pewien?",
                         "Pewien?",["Tak","Nie"])== "Tak":
        os.system("reg import nopeof.reg")
else:
    exit()
