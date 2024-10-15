from p5 import *                            # importe la librairie p5

WIDTH = 800                                 # la longueur de l'écran est de 800
HEIGHT = 600                                # la largeur de l'écran est de 600

h = 0                                       # la bouche de pacman est fermée au départ
o = 1                                       # son ouverture est positive au départ

def setup() :
    createCanvas(WIDTH, HEIGHT) 
    background(0)
    

def draw() :
    background(0)                           # fond d'écran noir
    global h, o                             # importe les variables h et o dans draw()
    
    def pacmanBasic():
        noStroke()                          # pas de bordure
        fill(255, 255, 0)                   # remplir en jaune
        arc(400, 300, 100, 100, radians(h),radians( h * (-1)))  # ouvre / fermer la bouche en fonction de h
        
    def pacmanMulticolor():
        a = random(32, 256)                 # a est un nombre entre 32 et 255
        b = random(32, 256)                 # b est un nombre entre 32 et 255
        c = random(32, 129)                 # c est un nombre entre 32 et 128
        noStroke()
        fill(a,b,c)                         # la couleur de pacman change aléatoirement
        arc(200, 300, 100, 100, radians(h), radians( h * (-1)))
        
    def pacmanPhantom():
        g = random(16, 129)                 # g est un nombre entre 16 et 128
        noStroke()
        noSmooth()
        fill(g)                             # la nuance de gris de pacman change aléatoirement 
        arc(600, 300, 100, 100, radians(h), radians( h * (-1)))


    h = h + o                               # on agrandit/rétrécit sa bouche en fonction du signe de o
    if h >= 45 or h <= 0:                   # si sa bouche est trop grande ou négative
        o = o * (-1)                        # on inverse sont mouvement 
        
# appel des fonctions 

    pacmanBasic()
    pacmanMulticolor()
    pacmanPhantom()

        
run()