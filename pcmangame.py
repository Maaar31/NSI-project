from p5 import *  


WIDTH = 600
HEIGHT = 400


pacman_x = 50
pacman_y = 300
pacman_diameter = 100
h = 0  
o = 1  


jump = False
velocity = 0
gravity = 1
jump_force = -15


cactus_x = 500
cactus_y = 300
cactus_width = 20
cactus_height = 50
cactus_speed = 5


score = 0
game_over = False

def setup():
    size(WIDTH, HEIGHT)  
    title("Pac-Man Chrome")  

def draw():
    global pacman_y, velocity, jump, cactus_x, score, game_over, h, o

    background(0)  
    
    
    stroke(255)
    line((0, 350), (WIDTH, 350))

    
    draw_pacman(pacman_x, pacman_y)

    
    if jump:
        pacman_y += velocity
        velocity += gravity
        if pacman_y >= 300:
            pacman_y = 300  
            jump = False
            velocity = 0

    
    fill(0, 255, 0)
    rect((cactus_x, cactus_y), cactus_width, cactus_height)

    
    cactus_x -= cactus_speed
    if cactus_x < -cactus_width:  
        cactus_x = WIDTH  
        score += 1  

    
    if (pacman_x + pacman_diameter / 2 > cactus_x) and (pacman_x < cactus_x + cactus_width) and (pacman_y + pacman_diameter / 2 > cactus_y):
        game_over = True  

    
    fill(255)
    text(f'Score: {score}', (10, 30))

    
    if game_over:
        fill(255, 0, 0)
        text('Game Over', (200, 200))
        no_loop()  

def key_pressed():
    global jump, velocity
    if key == ' ' and not jump:  
        jump = True
        velocity = jump_force  

def draw_pacman(x, y):
    global h, o

    no_stroke()
    fill(255, 255, 0)  # Pac-Man jaune
    
    
    start_angle = radians(h)
    stop_angle = radians(360 - h)
    
    arc((x, y), pacman_diameter, pacman_diameter, start_angle, stop_angle)  

    
    h += o  
    if h >= 45 or h <= 0:  
        o *= -1  

run()
