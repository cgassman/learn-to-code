import tkinter as tk
import json

General = open("Noteenn.json", "r", encoding="utf-8")
General.close()

Result=0

root = tk.Tk()
root.config(height=700,width=1244, bg="#282828")

frame=tk.Frame(root, bg="#282828")
frame.place(relwidth=0.5, relheight=0.647, relx=0, rely=0)

Result=0

def sPhysik():
    Noten  = General["Physik_Noten"]
    Datum = General["Physik_Datum"]
    Thema = General["Physik_Thema"]

    Noten_qount = len(Noten)

    total = 0

    for ele in range(0, len(Noten)): 
        total = total + Noten[ele]
    try:
        Result = total / Noten_qount
    except:
        Result=None

    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)

def sDeutsch():
    Noten  = General["Deutsch_Noten"]
    Datum = General["Deutsch_Datum"]
    Thema = General["Deutsch_Thema"]

    Noten_qount = len(Noten)

    total = 0

    for ele in range(0, len(Noten)): 
        total = total + Noten[ele]
    try:
        Result = total / Noten_qount
    except:
        Result=None

    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)

def sFrench():
    Noten  = General["Franz_Noten"]
    Datum = General["Franz_Datum"]
    Thema = General["Franz_Thema"]

    Noten_qount = len(Noten)

    total = 0

    for ele in range(0, len(Noten)): 
        total = total + Noten[ele]
    try:
        Result = total / Noten_qount
    except:
        Result = None

    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)

def sGG():
    Noten  = General["GG_Noten"]
    Datum = General["GG_Datum"]
    Thema = General["GG_Thema"]

    Noten_qount = len(Noten)

    total = 0

    for ele in range(0, len(Noten)): 
        total = total + Noten[ele]
    try:
        Result = total / Noten_qount
    except:
        Result = None

    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)

def sMathe():

    

    Noten  = General["Mathe_Noten"]

    Datum = General["Mathe_Datum"]

    Thema = General["Mathe_Thema"]



    Noten_qount = len(Noten)

    total = 0

    for ele in range(0, len(Noten)): 

        total = total + Noten[ele]



    try:

        Result = total / Noten_qount

    except:

        Result = None



    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")

    Schnitt.config(height=2,width=16)

    Schnitt.grid(column=2,row=1)

def sMusik():

    Noten  = General["Musik_Noten"]

    Datum = General["Musik_Datum"]

    Thema = General["Musik_Thema"]



    Noten_qount = len(Noten)

    total = 0

    for ele in range(0, len(Noten)): 

        total = total + Noten[ele]

    try:

        

        Result = total / Noten_qount

    except:

        Result = None

    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")

    Schnitt.config(height=2,width=16)

    Schnitt.grid(column=2,row=1)

    

def sBG():

    Noten  = General["BG_Noten"]

    Datum = General["BG_Datum"]

    Thema = General["BG_Thema"]



    Noten_qount = len(Noten)

    total = 0

    for ele in range(0, len(Noten)): 

        total = total + Noten[ele]

    try:

        Result = total / Noten_qount

    except:

        Result = None



    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")

    Schnitt.config(height=2,width=16)

    Schnitt.grid(column=2,row=1)

    

def sTurnen():

    Noten  = General["Turnen_Noten"]

    Datum = General["Turnen_Datum"]

    Thema = General["Turnen_Thema"]



    Noten_qount = len(Noten)

    total = 0

    for ele in range(0, len(Noten)): 

        total = total + Noten[ele]



    try:

        Result = total / Noten_qount

    except:

        Result = None



    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")

    Schnitt.config(height=2,width=16)

    Schnitt.grid(column=2,row=1) 

def sGS():

    Noten  = General["GS_Noten"]

    Datum = General["GS_Datum"]

    Thema = General["GS_Thema"]



    Noten_qount = len(Noten)

    total = 0

    for ele in range(0, len(Noten)): 

        total = total + Noten[ele]

    try:

        Result = total / Noten_qount



    except:

        Result = None





    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")

    Schnitt.config(height=2,width=16)

    Schnitt.grid(column=2,row=1)        

def sEnglisch():

    Noten  = General["Englisch_Noten"]

    Datum = General["Englisch_Datum"]

    Thema = General["Englisch_Thema"]



    Noten_qount = len(Noten)

    total = 0

    for ele in range(0, len(Noten)): 

        total = total + Noten[ele]



    try:

    

        Result = total / Noten_qount



    except:

        Result = None



    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")

    Schnitt.config(height=2,width=16)

    Schnitt.grid(column=2,row=1)    

def neue_Note():

    global newWindow

    newWindow=tk.Toplevel()

    newWindow.config(bg="#282828")







    Fachl = tk.Label(newWindow, text="Fach",bg="#282828", fg="white")

    Fachl.grid(column=0,row=0)



    global Fach

    Fach = tk.StringVar()

    Fach.set("Bitte Auswählen")

    Fachmenu = tk.OptionMenu(newWindow, Fach, "Physik", "Deutsch", "Franz", "GG","Mathe", "Musik", "BG", "BuS", "GS", "Englisch")

    Fachmenu.config(width=14,bg="#282828", fg="white")

    Fachmenu.grid(column=1,row=0)







    Note= tk.Label(newWindow, text="Note: ",bg="#282828", fg="white")

    Note.grid(column=0, row=1)

    

    global Notee

    Noteestr=""

    Notee = tk.Entry(newWindow, textvariable=Noteestr,bg="#282828", fg="white")

    Notee.grid(column=1, row=1)







    DatumL = tk.Label(newWindow, text="Datum: (TT/MM)",bg="#282828", fg="white")

    DatumL.grid(column=0,row=4)



    global Datum

    global Datumstr

    Datumstr = ""

    Datum = tk.Entry(newWindow, textvariable=Datumstr,bg="#282828", fg="white")

    Datum.grid(column=1,row=4)





    global Thema

    Themastr = ""

    Thema = tk.Entry(newWindow, textvariable=Datumstr,bg="#282828", fg = "white")

    Thema.grid(column=1, row= 5)



    ThemaL = tk.Label(newWindow, text="Thema:", bg="#282828", fg="white")

    ThemaL.grid(column=0, row=5)



    

    Button=tk.Button(newWindow, text="Finished", command=Finished, bg="#282828", fg="white")

    Button.grid(column=0,row=6)



    

    

        





    

        

def Finished():



    #Get data from Entry/Drop down Menu

    Fachstr= Fach.get()

    Datumstr = Datum.get()

    Noteestr =  Notee.get()

    Themastr = Thema.get()

    

    FachundNote = Fachstr+"/"+Noteestr+"\n"

    print(Fachstr)

    print(Noteestr)

    print(Datumstr)

    print(Themastr)



    #General.write(Deutsch_Noten)



    with open("Noteenn.json","a") as f:

        json.dump("{}: {}".format("Deutsch_Noten",Noteestr),f)











    newWindow.withdraw()







        

 



  









newGrade= tk.Button(frame, text="neue Note", fg="white", bg="#404040", command=neue_Note)

newGrade.config(height=2,width=16)

newGrade.grid(column=0, row=11)









Physik = tk.Button(frame, text="Physik", fg="white", bg="#404040", command=sPhysik)

Physik.config(height=2,width=16)

Physik.grid(column=0, row=1)



Deutsch = tk.Button(frame, text="Deutsch", fg="white", bg="#404040", command=sDeutsch)

Deutsch.config(height=2,width=16)

Deutsch.grid(column=0, row=2)



French = tk.Button(frame, text="French", fg="white", bg="#404040", command=sFrench)

French.config(height=2,width=16)

French.grid(column=0, row=3)



GG = tk.Button(frame, text="GG", fg="white", bg="#404040", command= sGG)

GG.config(height=2,width=16)

GG.grid(column=0,row=4)



Mathe = tk.Button(frame, text="Mathe", fg="white", bg="#404040", command= sMathe)

Mathe.config(height=2,width=16)

Mathe.grid(column=0,row=5)



Musik = tk.Button(frame, text="Musik", fg="white", bg="#404040", command = sMusik)

Musik.config(height=2,width=16)

Musik.grid(column=0,row=6)



BG = tk.Button(frame, text="BG", fg="white", bg="#404040", command = sBG)

BG.config(height=2,width=16)

BG.grid(column=0,row=7)



Turnen = tk.Button(frame, text="Turnen", fg="white", bg="#404040", command = sTurnen)

Turnen.config(height=2,width=16)

Turnen.grid(column=0,row=8)



GS = tk.Button(frame, text="GS", fg="white", bg="#404040", command= sGS)

GS.config(height=2,width=16)

GS.grid(column=0,row=9)



Englisch = tk.Button(frame, text="Englisch", fg="white", bg="#404040", command = sEnglisch)

Englisch.config(height=2,width=16)

Englisch.grid(column=0,row=10)



root.mainloop()









