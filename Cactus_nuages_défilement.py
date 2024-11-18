import random

# Liste pour les nuages et les cactus
clouds = []
cacti = []

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
        y = random.uniform(HEIGHT / 2)
        cloud_size = random.uniform(80, 150)
        clouds.append(Cloud(x, y, cloud_size))
    
    # Création des cactus
    for _ in range(3):  # Par exemple, trois cactus
        x = random.uniform(WIDTH, WIDTH * 2)
        y = HEIGHT - random.uniform(50, 100)  # Les mettres aux sol
        cactus_height = random.uniform(40, 70)  #hauteur
        cacti.append(Cactus(x, y, cactus_height))

def draw():
    background(135, 206, 235)  # Couleur de fond bleu ciel
    
    # Mise à jour et affichage des nuages
    for cloud in clouds:
        cloud.update()
        cloud.display()
    
    # Mise à jour et affichage des cactus
    for cactus in cacti:
        cactus.update()
        cactus.display()

# Exemple de dimensions de la fenêtre (modifiable selon besoin)
WIDTH = 800
HEIGHT = 600
