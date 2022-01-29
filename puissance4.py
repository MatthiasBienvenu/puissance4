from tkinter import *

joueur = 1

window = Tk()
window.minsize(720, 480)
window.geometry('1280x720')
window.configure(bg = '#AFB3F7')
window.title("Puissance 4")

menubar = Menu(window)

couleurs = Menu(menubar, tearoff=0)
couleurJ1 = Menu(menubar, tearoff=0)
couleurJ2 = Menu(menubar, tearoff=0)

taille = Menu(menubar, tearoff=0)
hauteur = Menu(taille, tearoff=0)
largeur = Menu(taille, tearoff=0)

regle = Menu(menubar, tearoff=0)
pions_a_aligner = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Couleurs", menu=couleurs)
couleurs.add_cascade(label="Joueur 1", menu=couleurJ1)
couleurs.add_cascade(label="Joueur 2", menu=couleurJ2)

menubar.add_cascade(label="Taille", menu=taille)
taille.add_cascade(label="Largeur", menu=largeur)
taille.add_cascade(label="Hauteur", menu=hauteur)

menubar.add_cascade(label="Règle", menu=regle)
regle.add_cascade(label="Pions à aligner", menu=pions_a_aligner)

CouleurJ1 = StringVar()
CouleurJ2 = StringVar()

Largeur = IntVar()
Hauteur = IntVar()

cap = IntVar()

def pion(event):
    x = event.x//100
    global joueur
    
    if Grille[x+1][1]!=0:
            messagebox.showinfo(title="", message="La colonne choisie est pleine")
    else:
        for i in range (len(Grille[x])):
            if  Grille[x+1][-i-2] == 0:
                Grille[x+1][-i-2] = joueur
                break
        y = Hauteur.get()-1-i
        if joueur == 1:
            zone_jeu.create_oval(x*100+10, y*100+10, x*100+90, y*100+90, fill=CouleurJ1.get())
            check(x+1, (-i-2))
            joueur = 2
        else:
            zone_jeu.create_oval(x*100+10, y*100+10, x*100+90, y*100+90, fill=CouleurJ2.get())
            check(x+1, (-i-2))
            joueur = 1

zone_jeu = Canvas(window)
Grille = []
def grille():
    global zone_jeu, Grille, L1, L2
    zone_jeu.destroy()
    zone_jeu = Canvas(window, width = 100*Largeur.get()-5, height = 100*Hauteur.get(), bg = 'white')
    zone_jeu.pack(expand = YES)
    zone_jeu.bind('<Button-1>', pion)
    Grille = [["!" for k in range(Hauteur.get()+2)]] + [["!"]+[0 for Y in range(Hauteur.get())]+["!"] for X in range(Largeur.get())] + [["!" for k in range(Hauteur.get()+2)]]
    
    L1 = [(x+1, 1) for x in range(Largeur.get())] + [(1, y+1) for y in range(Hauteur.get())]
    L1.remove((1, 1))
    
    L2 = [(x+1, 1) for x in range(Largeur.get())] + [(Largeur.get(), y+1) for y in range(Hauteur.get())]
    L2.remove((Largeur.get(), 1))

couleursFr = ["jaune","rouge","orange","olive","vert foncé","vert clair","turquoise","cyan","bleu foncé","bleu royal","bleu ciel","violet medium","indigo","orchidée","violet","magenta","rose","rose profond","cramoisi","blanc","noir"]
couleursEn = ["yellow","red","orange","olive","green","lime","turquoise","cyan","darkblue","royalblue","lightskyblue","mediumpurple","indigo","mediumorchid","purple","magenta","pink","deeppink","crimson","white","black"]

for larg in range(4, 16):
    largeur.add_radiobutton(label=str(larg), variable=Largeur, value=larg, command=grille)
for haut in range(4, 16):
    hauteur.add_radiobutton(label=str(haut), variable=Hauteur, value=haut, command=grille)

for colFr, colEn  in zip(couleursFr, couleursEn):
    couleurJ1.add_radiobutton(label=colFr, variable=CouleurJ1, value=colEn, command=grille)
for colFr, colEn  in zip(couleursFr, couleursEn):
    couleurJ2.add_radiobutton(label=colFr, variable=CouleurJ2, value=colEn, command=grille)

for n in range(3, 11):
    pions_a_aligner.add_radiobutton(label=str(n), variable=cap, value=n, command=grille)

hauteur.invoke(2)
largeur.invoke(3)

couleurJ1.invoke(0)
couleurJ2.invoke(1)

pions_a_aligner.invoke(1)

grille()


def check(x, y):
    nb = 0
    
    #ligne -
    for x1 in range(len(Grille)):
        if Grille[x1][y] == joueur:
            nb += 1
        else:
            nb = 0
        if nb == cap.get():
            win()
    
    #colonne |
    for y1 in range(len(Grille[0])):
        if Grille[x][y1] == joueur:
            nb += 1
        else:
            nb = 0
        if nb == cap.get():
            win()
    
    #diagonale \
    for x0, y0 in L1:
        x1 = x0
        y1 = y0
        for k in range(min([Hauteur.get(), Largeur.get()])):
            if Grille[x1][y1] == "!":
                nb = 0
                break
            elif Grille[x1][y1] == joueur:
                nb += 1
            else:
                nb = 0
            if nb == cap.get():
                win()
            x1 += 1
            y1 += 1
    
    #diagonale /
    for x0, y0 in L2:
        x1 = x0
        y1 = y0
        for k in range(min([Hauteur.get(), Largeur.get()])):
            if Grille[x1][y1] == "!":
                break
            elif Grille[x1][y1] == joueur:
                nb += 1
            else:
                nb = 0
            if nb == cap.get():
                win()
            x1 += -1
            y1 += 1

def win():
    global joueur
    if joueur == 1:    
        messagebox.showinfo(title="", message=f"victoire du joueur 1\navec les pions de couleur {couleursFr[couleursEn.index(CouleurJ1.get())]}")
        joueur = 2
        grille()
    else:
        messagebox.showinfo(title="", message=f"victoire du joueur 2\navec les pions de couleur {couleursFr[couleursEn.index(CouleurJ2.get())]}")
        joueur = 1
        grille()

window.config(menu=menubar)
window.mainloop()