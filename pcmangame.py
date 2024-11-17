from p5 import *

# Dimensions de la fenêtre
WIDTH = 600
HEIGHT = 400

# Variables pour Pac-Man
pacman_x = 50
pacman_y = 300
pacman_diameter = 100
h = 0  # Angle de la bouche de Pac-Man
o = 1  # Direction de l'animation de la bouche
jump = False
velocity = 0
gravity = 1
jump_force = -15

# Variables pour le cactus
cactus_x = 500
cactus_y = 300
cactus_width = 20
cactus_height = 50
cactus_speed = 5

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
        self.speed = random_uniform(1, 3)

    def update(self):
        self.x -= self.speed
        if self.x < -self.cloud_size:
            self.x = WIDTH + self.cloud_size

    def display(self):
        no_stroke()
        fill(255, 255, 255, 220)
        ellipse((self.x, self.y), self.cloud_size, self.cloud_size * 0.6)

def setup():
    size(WIDTH, HEIGHT)  # Appelle la fonction size() pour définir la fenêtre
    title("Pac-Man Chrome")
    for _ in range(5):  # Création des nuages
        x = random_uniform(WIDTH, WIDTH * 2)
        y = random_uniform(HEIGHT / 2)
        cloud_size = random_uniform(80, 150)  # Utilisation de `cloud_size`
        clouds.append(Cloud(x, y, cloud_size))

def draw():
    global pacman_y, velocity, jump, cactus_x, score, game_over, h, o

    background(135, 206, 235)  # Ciel bleu clair

    # Affichage des nuages
    for cloud in clouds:
        cloud.update()
        cloud.display()

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

    # Dessin du cactus
    fill(0, 255, 0)
    rect((cactus_x, cactus_y), cactus_width, cactus_height)

    # Mouvement du cactus
    cactus_x -= cactus_speed
    if cactus_x < -cactus_width:
        cactus_x = WIDTH
        score += 1

    # Vérification de la collision
    if (pacman_x + pacman_diameter / 2 > cactus_x) and (pacman_x < cactus_x + cactus_width) and (pacman_y + pacman_diameter / 2 > cactus_y):
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
    global jump, velocity, game_over, pacman_y, velocity, cactus_x, score

    if key == ' ':
        if game_over:
            # Réinitialiser toutes les variables
            pacman_y = 300
            velocity = 0
            jump = False
            cactus_x = 500
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

if __name__ == '__main__':
    run()
