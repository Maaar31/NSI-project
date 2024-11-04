from p5 import *
def setup():
    size(1200,400)

class Cloud:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = random_uniform(1, 3)  # vitesse aléatoire pour chaque nuage

    def update(self):
        # Déplace le nuage vers la gauche avec differente vitesse
        self.x -= self.speed
        if self.x < -self.size:
            self.x = width + self.size

    def display(self):  # fonction déssinant les nuages
        no_stroke()
        fill(255, 255, 255, 220)  
        ellipse((self.x, self.y), self.size, self.size * 0.6)

clouds = [] # stocker les nuages

def setup():
    # Crée des nuages avec des positions et tailles aléatoires
    for _ in range(5):
        x = random_uniform(width, width * 2)  
        y = random_uniform(height / 2)  
        size = random_uniform(80, 150) 
        clouds.append(Cloud(x, y, size))

def draw():
    background(135, 206, 235)
    for cloud in clouds:      
        cloud.update()
        cloud.display()

if __name__ == '__main__':   #c'est pour pas que le code s'arette 
    run()
