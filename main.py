import tkinter as tk

# Personnages (Allan)

Goku = {"Nom": "Goku", "clickValue": 2, "myMaxHP": 25, "myMaxKi": 10}
 # Formes de Goku
GokuSS = {"Nom": "Goku (SS)", "clickValue": 20, "myMaxHP": 25, "myMaxKi": 10}
GokuSS2 = {"Nom": "Goku (SS2)", "clickValue": 2, "myMaxHP": 25, "myMaxKi": 10}
GokuSS3 = {"Nom": "Goku (SS3)", "clickValue": 2, "myMaxHP": 25, "myMaxKi": 10}
GokuSSB = {"Nom": "Goku (SSB)", "clickValue": 2, "myMaxHP": 25, "myMaxKi": 10}
GokuUI = {"Nom": "Goku (UI)", "clickValue": 2, "myMaxHP": 25, "myMaxKi": 10}
Vegito = {"Nom": "Vegito", "clickValue": 2, "myMaxHP": 25, "myMaxKi": 10}

Vegeta = {"Nom": "Vegeta", "clickValue": 1, "myMaxHP": 40, "myMaxKi": 10}
 # Formes de Vegeta
VegetaSS = {"Nom": "Vegeta (SS)", "clickValue": 1, "myMaxHP": 40, "myMaxKi": 10}
VegetaSS2 = {"Nom": "Vegeta (SS2)", "clickValue": 1, "myMaxHP": 40, "myMaxKi": 10}
VegetaMajin = {"Nom": "Majin Vegeta", "clickValue": 1, "myMaxHP": 40, "myMaxKi": 10}
VegetaSS3 = {"Nom": "Vegeta (SS3)", "clickValue": 1, "myMaxHP": 40, "myMaxKi": 10}
VegetaSSB = {"Nom": "Vegeta (SSB)", "clickValue": 1, "myMaxHP": 40, "myMaxKi": 10}
Gogeta = {"Nom": "Gogeta", "clickValue": 1, "myMaxHP": 40, "myMaxKi": 10}

Trunks = {"Nom": "Trunks", "clickValue": 1, "myMaxHP": 25, "myMaxKi": 20}
 # Formes de Trunks
TrunksSS = {"Nom": "Trunks (SS)", "clickValue": 1, "myMaxHP": 25, "myMaxKi": 20}
TrunksRage = {"Nom": "Trunks (SS Enragé)", "clickValue": 1, "myMaxHP": 25, "myMaxKi": 20}
TrunksHope = {"Nom": "Trunks (Epée de l'Espoir)", "clickValue": 1, "myMaxHP": 25, "myMaxKi": 20}

myChara = Goku

### Arc : Saiyan, Namek, Cyborgs, Cell, Buu, BOG, FNF, U6vU7, FT, startTOP, endTOP
# Ennemis (Allan)

SBM = {"Nom": "Saibamen", "Dmg": 1}
Soldier = {"Nom": "Soldat de Frieza", "Dmg": 2}
Robot = {"Nom": "Robot", "Dmg": 3}
CellJR = {"Nom": "Cell Jr", "Dmg": 4}
MajinGuy = {"Nom": "Spopovitch", "Dmg": 5}
Beerus = {"Nom": "Beerus", "Dmg": 6}
Soldier2 = {"Nom": "Guerrier de Frieza", "Dmg": 7}
Botamo = {"Nom": "Botamo", "Dmg": 8}
Black = {"Nom": "Black", "Dmg": 9}
Bergamo = {"Nom": "Bergamo", "Dmg": 10}
Ribrianne = {"Nom": "Ribrianne", "Dmg": 11}

ennemies = [SBM, Soldier, Robot, CellJR, MajinGuy, Beerus, Soldier2, Botamo, Black, Bergamo, Ribrianne]

Nappa = {"Nom": "Nappa", "Dmg": 2}
Ginyu = {"Nom": "Ginyu", "Dmg": 4}
C17 = {"Nom": "C17", "Dmg": 6}
Cell = {"Nom": "Cell", "Dmg": 8}
MajinVegeta = {"Nom": "Majin Vegeta", "Dmg": 10}
VegetaRage = {"Nom": "Vegeta (Enragé)", "Dmg": 12}
Frieza2 = {"Nom": "Frieza (Entraîné)", "Dmg": 14}
Kyabe = {"Nom": "Kyabe (SS)", "Dmg": 16}
BlackZam = {"Nom": "Black (SSR) & Zamasu", "Dmg": 18}
Frost = {"Nom": "Frost", "Dmg": 20}
Toppo = {"Nom": "Toppo", "Dmg": 22}

minibosses = [Nappa, Ginyu, C17, Cell, MajinVegeta, VegetaRage, Frieza2, Kyabe, BlackZam, Frost, Toppo]

VegetApe = {"Nom": "Vegeta (Gorille)", "Dmg": 3}
Frieza = {"Nom": "Frieza", "Dmg": 6}
C18 = {"Nom": "C18", "Dmg": 9}
CellP = {"Nom": "Cell (Parfait)", "Dmg": 12}
KidBuu = {"Nom": "Buu enfant", "Dmg": 15}
BeerusRage = {"Nom": "Beerus (Enragé)", "Dmg": 18}
GFrieza = {"Nom": "Golden Frieza", "Dmg": 21}
Hit = {"Nom": "Hit", "Dmg": 24}
MGZ = {"Nom": "Zamasu fusionné", "Dmg": 27}
Kefla = {"Nom": "Kefla", "Dmg": 30}
Jiren = {"Nom": "Jiren", "Dmg": 33}

bosses = [VegetApe, Frieza, C18, CellP, KidBuu, BeerusRage, GFrieza, Hit, MGZ, Kefla, Jiren]

# Variables (Allan)

ennemyChara = SBM
clickValue = myChara["clickValue"]
myHP = myChara["myMaxHP"]
myMaxHP = myChara["myMaxHP"]
ennemyHP = 10
ennemyMaxHP = 10
money = 0

# Nouvelles variables (Allan)

myKi = myChara["myMaxKi"]
myMaxKi = myChara["myMaxKi"]

ennemyCount=1
ennemyMaxCount=10
stage=1

# Fonction du clic (Allan)

def click():
    global myHP, myMaxHP, ennemyHP, ennemyMaxHP, ennemyChara, money, ennemyCount, ennemyMaxCount, stage
    ennemyHP = ennemyHP - clickValue
    ennemyHP_Zone.configure(text=str(ennemyHP) + "/" + str(ennemyMaxHP))
    
    logs.configure(state="normal")
    logs.insert(tk.END, "\n" + "Vous avez infligé " + str(clickValue) + " dégats à " + str(ennemyChara["Nom"]) + " !")
    logs.configure(state="disabled")
    logs.see(tk.END)

    myHP = myHP # - ennemyChara["Dmg"]
    logs.configure(state="normal")
    logs.insert(tk.END, "\n" + "Vous avez subi " + str(ennemyChara["Dmg"]) + " dégats" + " !")
    logs.configure(state="disabled")
    logs.see(tk.END)
    myHP_Zone.configure(text=str(round(myHP)) + "/" + str(myMaxHP))

    if myHP < 1:
        ennemyHP = ennemyMaxHP
        ennemyHP_Zone.configure(text=str(ennemyHP) + "/" + str(ennemyMaxHP))
        ennemyCount = 1
        stage_Zone.configure(text="Stage " + str(stage) + " - Ennemi " + str(ennemyCount) + "/" + str(ennemyMaxCount))
        myHP = myMaxHP
        myHP_Zone.configure(text=str(round(myHP)) + "/" + str(myMaxHP))
    
    if ennemyHP < 1:
        ennemyHP = ennemyMaxHP
        ennemyHP_Zone.configure(text=str(ennemyHP) + "/" + str(ennemyMaxHP))
        ennemyCount = ennemyCount + 1

        logs.configure(state="normal")
        logs.insert(tk.END, "\n\n" + "[Vous êtes passé à l'ennemi numéro " + str(ennemyCount) + "]")
        logs.configure(state="disabled")
        
        if ennemyCount > ennemyMaxCount:
            stage = stage + 1
            ennemyCount = 1
            ennemyMaxCount = 10
            ennemyMaxHP = ((stage * 0.5) + (ennemyMaxHP * 0.75))
            ennemyHP = ennemyMaxHP
            ennemyChara = ennemies[stage - 1]
            money = (money + ((stage / 5) * 25) * ennemyMaxHP)
            
            logs.configure(state="normal")
            logs.insert(tk.END, "\n" + "Vous êtes passé au stage " + str(stage) + " !")
            logs.delete('1.0', tk.END)
            logs.configure(state="disabled")
        if ennemyCount == 5:
            ennemyChara = minibosses[stage - 1]
            ennemyMaxHP = ((stage * 2.5) + ennemyMaxHP)
            ennemyHP = ennemyMaxHP
            ennemyName_Zone.configure(text="Mini BOSS" + " \n " + str(ennemyChara["Nom"]), fg="red", font=("Open Sans", "10", "bold"))
            ennemyPic.configure(file="chara/" + str(ennemyChara["Nom"]) + ".png")
            logs.configure(state="normal")
            logs.insert(tk.END, "\n" + "Vous voilà face au Mini BOSS, " + str(ennemyChara["Nom"]) + " !")
            logs.configure(state="disabled")
        if ennemyCount == 6:
            ennemyChara = ennemies[stage - 1]
            ennemyMaxHP = ((stage * 0.5) + (ennemyMaxHP * 0.75))
            ennemyHP = ennemyMaxHP
        if ennemyCount == 10:
            ennemyChara = bosses[stage - 1]
            ennemyMaxHP = ((stage * 5) + ennemyMaxHP)
            ennemyHP = ennemyMaxHP
            
            ennemyName_Zone.configure(text="BOSS" + " \n " + str(ennemyChara["Nom"]), fg="red", font=("Open Sans", "10", "bold"))
            ennemyPic.configure(file="chara/" + str(ennemyChara["Nom"]) + ".png")
            logs.configure(state="normal")
            logs.insert(tk.END, "\n" + "Vous voilà face au BOSS, " + str(ennemyChara["Nom"]) + " !")
            logs.configure(state="disabled")
        else:
            money = (money + ((stage / 5) * 10) * ennemyMaxHP)
            ennemyName_Zone.configure(text=str(ennemyChara["Nom"]), fg="black", font=("Open Sans", "10"))
            ennemyPic.configure(file="chara/" + str(ennemyChara["Nom"]) + ".png")
            
            logs.configure(state="normal")
            logs.insert(tk.END, "\n")
            logs.configure(state="disabled")

        money_Zone.configure(text="Zenny = " + str(round(money)))
        
        ennemyHP = round(ennemyHP)
        ennemyMaxHP = round(ennemyMaxHP)
        ennemyHP_Zone.configure(text=str(ennemyHP) + "/" + str(ennemyMaxHP))
        stage_Zone.configure(text="Stage " + str(stage) + " - Ennemi " + str(ennemyCount) + "/" + str(ennemyMaxCount))

# Partie Tkinter - Combat (Allan)

window = tk.Tk()
window.title("DB Clicker")

stage_Zone = tk.Label(window, text="Stage " + str(stage) + " - Ennemi " + str(ennemyCount) + "/" + str(ennemyMaxCount), font=("Open Sans", "10", "bold"))
stage_Zone.grid(row=1, column=1, columnspan=2)

ennemyPic = tk.PhotoImage(file="chara/" + str(ennemyChara["Nom"]) + ".png")
ennemyPic_Zone = tk.Label(window, image=ennemyPic)
ennemyPic_Zone.grid(row=2, rowspan=2, column=2, padx=20, pady=10)

ennemyHP_Zone = tk.Label(window, text=str(ennemyHP) + "/" + str(ennemyMaxHP), font=("Open Sans", "10", "bold"), fg="white", bg="red", relief="groove", width=13) 
ennemyHP_Zone.grid(row=2, column=1, padx=20)

ennemyName_Zone = tk.Label(window, text=str(ennemyChara["Nom"]), font=("Open Sans", "10"))
ennemyName_Zone.grid(row=3, column=1, sticky="ne")

myPic = tk.PhotoImage(file="chara/" + str(myChara["Nom"]) + ".png")
myPic_Zone = tk.Label(window, image=myPic)
myPic_Zone.grid(row=4, rowspan=2, column=1, padx=20, pady=10)

myName_Zone = tk.Label(window, text=myChara["Nom"], font=("Open Sans", "10"))
myName_Zone.grid(row=4, column=2, sticky="sw")

myHP_Zone = tk.Label(window, text=str(myHP) + "/" + str(myMaxHP), font=("Open Sans", "10", "bold"), fg="white", bg="green", relief="groove", width=13)
myHP_Zone.grid(row=5, column=2, padx=20)

click_Zone = tk.Button(window, height=2, width=20, text="COMBATTRE !", font=("Open Sans", "11", "bold"), fg="white", bg="orange", relief="groove", activeforeground="orange", activebackground="white", command=click)
click_Zone.grid(row=6, column=1, columnspan=2)

myMove_Zone = tk.Button(window, width=10, text="Aucune", font=("Open Sans", "9", "bold"), fg="white", bg="purple", relief="groove", state="disabled")
myMove_Zone.grid(row=7, column=1, columnspan=2) 

myKi_Zone = tk.Label(window, text=str(myKi) + "/" + str(myMaxKi), font=("Open Sans", "10", "bold"), fg="white", bg="blue", relief="groove", width=18)
myKi_Zone.grid(row=8, column=1, columnspan=2)

money_Zone= tk.Label(window, text="Zenny = " + str(round(money)), font=("Open Sans", "9", "bold"))
money_Zone.grid(row=9, column=1, columnspan=2)

# Partie Tkinter - Logs (Allan)

events_Zone = tk.LabelFrame(window, text="Evénements", labelanchor="n", font=("Open Sans", "10", "bold"))
events_Zone.grid(row=1, rowspan=9, column=4, padx=20)

logs = tk.Text(events_Zone, width=50, font=("Courier New", "9"))
scroll = tk.Scrollbar(events_Zone, command=logs.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
logs.insert(tk.END, "Bienvenue !")
logs.configure(yscrollcommand=scroll.set, state="disabled")
logs.pack(side="left")

window.mainloop()
