from p5 import *
import random

# Dimensions de la fenêtre
WIDTH = 600
HEIGHT = 400

# Liste pour les nuages et les cactus
clouds = []
cacti = []

# Variables pour Pac-Man
pacman_x = 60
pacman_y = 300
pacman_diameter = 100
h = 0  # Angle de la bouche de Pac-Man
o = 1  # Direction de l'animation de la bouche
jump = False
velocity = 0
gravity = 0.6  # Gravité ajustée
jump_force = -12  # Force du saut ajustée

# Variables pour le fantôme
ghost_x = 500
ghost_y = 300
ghost_width = 60
ghost_speed = 6  # Vitesse du fantôme augmentée

# Variables d'état du jeu
score = 0
game_over = False

# Liste pour les nuages
clouds = []

class Cloud:
    def __init__(self, x, y, cloud_size):
        self.x = x
        self.y = y
        self.cloud_size = cloud_size
        self.speed = random.uniform(1, 3)

    def update(self):
        self.x -= self.speed
        if self.x < -self.cloud_size:
            self.x = WIDTH + self.cloud_size

    def display(self):
        no_stroke()
        fill(255, 255, 255, 220)
        ellipse(self.x, self.y, self.cloud_size, self.cloud_size * 0.6)

class Cactus:
    def __init__(self, x, y, cactus_height):
        self.x = x
        self.y = y
        self.cactus_height = cactus_height
        self.speed = random.uniform(1, 3)

    def update(self):
        self.x -= self.speed
        if self.x < -self.cactus_height:
            self.x = WIDTH + self.cactus_height

    def display(self):
        no_stroke()
        fill(34, 139, 34)  # Couleur verte pour le cactus
        rect(self.x, self.y, 20, self.cactus_height)  # Un cactus basique en rectangle

def setup():
    size(WIDTH, HEIGHT)  # Appelle la fonction size() pour définir la fenêtre
    title("Pac-Man Chrome")
    
    # Création des nuages
    for _ in range(5):
        x = random.uniform(WIDTH, WIDTH * 2)
        y = random.uniform(0, HEIGHT / 2)  # Correction ici
        cloud_size = random.uniform(80, 150)
        clouds.append(Cloud(x, y, cloud_size))
    
    # Création des cactus
    for _ in range(3):  # Par exemple, trois cactus
        x = random.uniform(WIDTH, WIDTH * 2)
        y = HEIGHT - random.uniform(50, 100)  # Les mettre au sol
        cactus_height = random.uniform(40, 70)  # Hauteur
        cacti.append(Cactus(x, y, cactus_height))

def draw():
    global pacman_y, velocity, jump, ghost_x, score, game_over, h, o

    background(135, 206, 235)  # Couleur de fond bleu ciel
    
    # Mise à jour et affichage des nuages
    for cloud in clouds:
        cloud.update()
        cloud.display()
    
    # Mise à jour et affichage des cactus
    for cactus in cacti:
        cactus.update()
        cactus.display()

    # Sol
    stroke(255)
    line((0, 350), (WIDTH, 350))

    # Dessin de Pac-Man
    draw_pacman(pacman_x, pacman_y)

    # Saut de Pac-Man
    if jump:
        pacman_y += velocity
        velocity += gravity
        if pacman_y >= 300:
            pacman_y = 300
            jump = False
            velocity = 0

    # Dessin du fantôme
    draw_ghost(ghost_x, ghost_y)

    # Mouvement du fantôme
    ghost_x -= ghost_speed
    if ghost_x < -ghost_width:
        ghost_x = WIDTH
        score += 1

    # Vérification de la collision entre Pac-Man et le fantôme
    if (pacman_x + pacman_diameter / 2 > ghost_x - 20) and (pacman_x - pacman_diameter / 2 < ghost_x + ghost_width / 2) and (pacman_y + pacman_diameter / 2 > ghost_y):
        game_over = True

    # Affichage du score
    fill(255)
    text(f'Score: {score}', (10, 30))

    # État "Game Over"
    if game_over:
        fill(255, 0, 0)
        text('Game Over', (WIDTH // 2 - 50, HEIGHT // 2))
        no_loop()

def key_pressed():
    global jump, velocity, game_over, pacman_y, velocity, ghost_x, score

    if key == ' ':
        if game_over:
            # Réinitialiser toutes les variables
            pacman_y = 300
            velocity = 0
            jump = False
            ghost_x = 500
            score = 0
            game_over = False
            loop()  # Redémarrer le dessin
        elif not jump:
            # Pac-Man saute
            jump = True
            velocity = jump_force

def draw_pacman(x, y):
    global h, o

    no_stroke()
    fill(255, 255, 0)
    start_angle = radians(h)
    stop_angle = radians(360 - h)
    arc((x, y), pacman_diameter, pacman_diameter, start_angle, stop_angle)

    # Animation de la bouche de Pac-Man
    h += o
    if h >= 45 or h <= 0:
        o *= -1

def draw_ghost(x, y):
    # Base du fantôme
    no_stroke()
    fill(255, 0, 255)
    circle(x, y, ghost_width)
    no_stroke()
    fill(255, 0, 255)
    rect((x - 30), y, 60, 40)  # Taille du rect ajustée pour correspondre à la largeur du cercle

    # Les "pattes"
    for i in range(0, 4):
        no_stroke()
        fill(255, 0, 255)
        circle((x - 22) + (15 * i), (y + 41), 16)  # Les pattes sont ajustées

    # Yeux
    no_stroke()
    fill(255)
    ellipse((x - 22), y, 18, 28)
    fill(255)
    ellipse((x + 8), y, 18, 28)

    # Pupilles
    no_stroke()
    fill(0)
    ellipse((x - 25), y, 14, 16)
    fill(0)
    ellipse((x + 5), y, 14, 16)

if __name__ == '__main__':
    run()
