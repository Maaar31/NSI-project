import winsound
import random
from p5 import *

# Dimensions de la fenêtre
WIDTH = 600  # Largeur de la fenêtre
HEIGHT = 400  # Hauteur de la fenêtre

# Variables pour le fond (accélération progressive)
background_speed_multiplier = 1  # Multiplicateur de vitesse pour le déplacement du fond
background_acceleration = 0.01  # Valeur d'accélération de la vitesse du fond

# Listes pour les objets mobiles (nuages et cactus)
clouds = []  # Liste des nuages (éléments de décor)
cacti = []  # Liste des cactus (obstacles)

# Variables pour Pac-Man
pacman_x = 60  # Position horizontale de Pac-Man
pacman_y = 300  # Position verticale de Pac-Man
pacman_diameter = 100  # Diamètre de Pac-Man
h = 0  # Angle actuel de la bouche de Pac-Man (animation)
o = 1  # Direction d'animation de la bouche (ouverture/fermeture)
jump = False  # Indique si Pac-Man est en train de sauter
velocity = 0  # Vitesse verticale de Pac-Man
gravity = 0.6  # Force de gravité qui agit sur Pac-Man
jump_force = -12  # Force du saut appliquée à Pac-Man

# Variables pour le fantôme
ghost_x = 500  # Position horizontale du fantôme
ghost_y = 300  # Position verticale du fantôme
ghost_width = 60  # Largeur du fantôme
ghost_speed = 6  # Vitesse de déplacement du fantôme

# Variables d'état du jeu
score = 0  # Score actuel du joueur
game_over = False  # Indique si le jeu est terminé

# Classe pour gérer les nuages 
class Cloud:
    def __init__(self, x, y, cloud_size):
        # Initialisation des propriétés du nuage
        self.x = x  # Position horizontale
        self.y = y  # Position verticale
        self.cloud_size = cloud_size  # Taille du nuage
        self.base_speed = random.uniform(1, 3)  # Vitesse de déplacement aléatoire

    def update(self):
        # Mise à jour de la position du nuage en fonction de la vitesse
        global background_speed_multiplier
        self.x -= self.base_speed * background_speed_multiplier  # Déplacement vers la gauche
        if self.x < -self.cloud_size:  # Si le nuage sort de l'écran, il réapparaît à droite
            self.x = WIDTH + self.cloud_size

    def display(self):
        # Affichage du nuage 
        no_stroke()
        fill(255, 255, 255, 220)  # Couleur blanche 
        ellipse(self.x, self.y, self.cloud_size, self.cloud_size * 0.6)

# Classe pour gérer les cactus 
class Cactus:
    def __init__(self, x, y, cactus_height):
        # Initialisation des propriétés du cactus
        self.x = x  # Position horizontale
        self.y = y  # Position verticale
        self.cactus_height = cactus_height  # Hauteur du cactus
        self.base_speed = random.uniform(1, 3)  # Vitesse de déplacement aléatoire
        self.arm_angle = 0  # Angle initial des bras du cactus 

    def update(self):
        # Mise à jour de la position et de l'oscillation des bras du cactus
        global background_speed_multiplier
        self.x -= self.base_speed * background_speed_multiplier  # Déplacement vers la gauche
        if self.x < -self.cactus_height:  # Si le cactus sort de l'écran, il réapparaît à droite
            self.x = WIDTH + self.cactus_height

        # Mise à jour de l'angle des bras 
        self.arm_angle = sin(frame_count * 0.1) * 20

    def display(self):
        # Affichage du cactus 
        no_stroke()
        fill(34, 139, 34)  # Couleur verte pour le cactus

        # Corps principal
        rect(self.x, self.y, 20, self.cactus_height)

        # Bras gauche 
        with push_matrix():
            translate(self.x + 10, self.y + self.cactus_height / 2)
            rotate(radians(self.arm_angle))
            rect(-40, -5, 30, 10)

        # Bras droit 
        with push_matrix():
            translate(self.x + 10, self.y + self.cactus_height / 2)
            rotate(radians(-self.arm_angle))
            rect(10, -5, 30, 10)

# Fonction pour jouer la musique de fond
def play_background_music():
    # Boucle infinie pour rejouer la musique
    while True:
        winsound.PlaySound("music.wav", winsound.SND_FILENAME)  # Chargement et lecture du fichier audio

def setup():
    # Configuration initiale de la fenêtre et des objets du jeu
    size(WIDTH, HEIGHT)
    title("Pac-Man Chrome")  # Titre de la fenêtre

    # Création des nuages
    for _ in range(5):  # Génère 5 nuages
        x = random.uniform(WIDTH, WIDTH * 2)  # Position horizontale aléatoire hors de l'écran
        y = random.uniform(0, HEIGHT / 2)  # Position verticale aléatoire
        cloud_size = random.uniform(80, 150)  # Taille aléatoire
        clouds.append(Cloud(x, y, cloud_size))

    # Création des cactus
    for _ in range(3):  # Génère 3 cactus
        x = random.uniform(WIDTH, WIDTH * 2)  # Position horizontale aléatoire hors de l'écran
        y = HEIGHT - random.uniform(50, 100)  # Position verticale
        cactus_height = random.uniform(40, 70)  # Hauteur aléatoire
        cacti.append(Cactus(x, y, cactus_height))

    # Lancer la musique de fond dans un thread séparé
    from threading import Thread
    music_thread = Thread(target=play_background_music)
    music_thread.daemon = True  # Le thread s'arrêtera automatiquement à la fermeture du programme
    music_thread.start()

def draw():
    # Fonction appelée à chaque frame pour mettre à jour et dessiner le jeu
    global pacman_y, velocity, jump, ghost_x, score, game_over, h, o, background_speed_multiplier

    background(135, 206, 235)  # Couleur de fond bleu ciel

    # Augmentation progressive de la vitesse du fond
    background_speed_multiplier += background_acceleration

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
    line((0, 350), (WIDTH, 350))  # Ligne blanche représentant le sol

    # Dessin de Pac-Man
    draw_pacman(pacman_x, pacman_y)

    # Saut de Pac-Man
    if jump:
        pacman_y += velocity  # Mise à jour de la position verticale
        velocity += gravity  # Application de la gravité
        if pacman_y >= 300:  # Réinitialisation une fois que Pac-Man touche le sol
            pacman_y = 300
            jump = False
            velocity = 0

    # Dessin du fantôme
    draw_ghost(ghost_x, ghost_y)

    # Mouvement du fantôme
    ghost_x -= ghost_speed
    if ghost_x < -ghost_width:  # Réinitialisation si le fantôme sort de l'écran
        ghost_x = WIDTH
        score += 1  # Augmentation du score

    # Vérification de la collision entre Pac-Man et le fantôme
    if (pacman_x + pacman_diameter / 2 > ghost_x - 20) and \
       (pacman_x - pacman_diameter / 2 < ghost_x + ghost_width / 2) and \
       (pacman_y + pacman_diameter / 2 > ghost_y):
        game_over = True  # Fin du jeu en cas de collision

    # Affichage du score
    fill(255)
    text(f'Score: {score}', (10, 30))

    # État "Game Over"
    if game_over:
        fill(255, 0, 0)
        text('Game Over', (WIDTH // 2 - 50, HEIGHT // 2))  # Message de fin au centre
        no_loop()  # Arrêt de la boucle du jeu

def key_pressed():
    # Gestion des entrées clavier
    global jump, velocity, game_over, pacman_y, ghost_x, score

    if key == ' ':  # Touche espace
        if game_over:
            # Réinitialisation du jeu
            pacman_y = 300
            velocity = 0
            jump = False
            ghost_x = 500
            score = 0
            game_over = False
            loop()  # Redémarrage de la boucle
        elif not jump:
            jump = True  # Lancer le saut
            velocity = jump_force  # Appliquer la force de saut

def draw_pacman(x, y):
    # Dessin de Pac-Man avec animation de la bouche
    global h, o

    fill(255, 255, 0)  # Couleur jaune pour Pac-Man
    angle = radians(30 + h)  # Angle d'ouverture de la bouche
    arc((x, y), pacman_diameter, pacman_diameter, angle, TWO_PI - angle)  # Corps de Pac-Man

    h += o  # Mise à jour de l'angle d'ouverture
    if h >= 15 or h <= 0:  # Inversion du mouvement à certaines limites
        o *= -1

def draw_ghost(x, y):
    # Dessin du fantôme
    fill(255, 0, 0)  # Couleur rouge pour le fantôme
    rect((x - 20, y - 40), 40, 40)  # Corps rectangulaire
    ellipse((x, y - 40), 40, 40)  # Tête ronde

    # Yeux
    fill(255)
    ellipse((x - 10, y - 35), 10, 10)  # Oeil gauche
    ellipse((x + 10, y - 35), 10, 10)  # Oeil droit
    fill(0)
    ellipse((x - 10, y - 35), 5, 5)  # Pupille gauche
    ellipse((x + 10, y - 35), 5, 5)  # Pupille droite
if __name__ == "__main__":
    run()
