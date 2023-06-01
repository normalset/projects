#todo aggiungere la modifica della dimensione al momento del puickup di un elemento

import pygame 
from sys import exit
import os
import math , random
os.chdir("D:/Code/projects-1/pyPhisics")

BG_COLOR = "Black"
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH , HEIGHT))
fruit_counter = 0
last_fruit_taken = 0
bomb_counter = 0
last_bomb_taken = 0

pygame.init()
pygame.display.set_caption("Physics Test")
clock = pygame.time.Clock()

#player
PLAYER = pygame.image.load("./alienBoolean.png").convert_alpha()
PLAYER = pygame.transform.rotozoom(PLAYER , 0 , 0.5)

player_rect = PLAYER.get_rect(center = (WIDTH/2 , HEIGHT/2))
x_grav = 0
y_grav = 0
moving_up = False
moving_down = False
moving_left = False
moving_right = False

#score
score = 0
font = pygame.font.Font(None , 50)
score_text = font.render(f'score: {score}' , None , "White").convert_alpha()
score_text_rect = score_text.get_rect(center = (WIDTH/2 , HEIGHT*0.2))

#fruits
fruits = []
class Fruit:
    def __init__(self):
        self.image = pygame.image.load('./fruit.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 950), random.randint(50, 950))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def reset(self):
        self.rect.center = (random.randint(50, 950), random.randint(50, 950))    


bombs = [] 
class Bomb:
    def __init__(self):
        self.image = pygame.image.load('./bomb.png')
        self.image = pygame.transform.rotozoom(self.image , 0 ,0.5)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 950), random.randint(50, 950))
        self.timer = 0
        self.when_placed = pygame.time.get_ticks()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update_timer(self):
        self.timer = int((pygame.time.get_ticks() - self.when_placed)/1000)

#fruit
# fruit_on = False
# fruit = pygame.image.load("./fruit.png").convert_alpha()
# fruit = pygame.transform.rotozoom(fruit , 0 , 0.5)
# fruit_rect = fruit.get_rect()
# fruit_taken = pygame.image.load("./fruit_take.png").convert_alpha()
# fruit_taken_surf = fruit_taken.get_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w and y_grav > 0:
        #         y_grav /=2
        #     elif event.key == pygame.K_s and y_grav < 0:
        #         y_grav /=2
        #     elif event.key == pygame.K_a and x_grav < 0:
        #         x_grav /=2
        #     elif event.key == pygame.K_d and x_grav > 0:
        #         x_grav /=2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_d:
                moving_right = True
         # Handle key up events
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_s:
                moving_down = False
            elif event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_d:
                moving_right = False
         # Update the player's position based on the movement keys
        if moving_up:
            y_grav -= 5
            print("moving up" , player_rect)
        if moving_down:
            y_grav += 5
            print("moving down" , player_rect)
        if moving_left:
            x_grav -= 5
            print("moving left" , player_rect)
        if moving_right:
            x_grav += 5
            print("moving right" , player_rect)
            
    #? Grav kicks in
    player_rect.x += x_grav
    player_rect.y += y_grav
    #? Gravity goes away
    if x_grav > 0 : x_grav *=0.9
    elif x_grav < 0 : x_grav *=0.9
    if y_grav > 0 : y_grav *=0.9
    elif y_grav < 0 : y_grav *=0.9

    #? collisions
    #top
    if player_rect.top <=0 : 
        player_rect.top = 0
        y_grav *= -1
    #bot
    if player_rect.bottom >= HEIGHT : 
        player_rect.bottom = HEIGHT
        y_grav *= -1
    #left
    if player_rect.left <= 0 : 
        player_rect.left = 0
        x_grav *= -1
    #right
    if player_rect.right >= WIDTH : 
        player_rect.right = WIDTH
        x_grav *= -1
    
    screen.fill(BG_COLOR)
    screen.blit(PLAYER , player_rect)
    
    #display score
    if (not player_rect.colliderect(score_text_rect))and(not (any(fruit.rect.colliderect(score_text_rect) for fruit in fruits)))and(not (any(bomb.rect.colliderect(score_text_rect) for bomb in bombs))): 
        screen.blit(score_text , score_text_rect)

    #! Fruit Logic

    for fruit in fruits:
        fruit.draw(screen)

    if (len(fruits) < 5) and fruit_counter > 1 :
        fruits.append(Fruit())
        last_fruit_taken = int(pygame.time.get_ticks()/1000)

        #fruit_rect.center = (random.randint( 50 , 950 ) , random.randint( 50 , 950 )) 
    
    for fruit in fruits:
        if player_rect.colliderect(fruit.rect) :
            score += 1
            score_text = font.render(f'score: {score}' , None , "White").convert_alpha()
            last_fruit_taken = int(pygame.time.get_ticks()/1000)
            fruit_counter = int(pygame.time.get_ticks()/1000) - last_fruit_taken
            #place fruit out of bounds
            fruits.remove(fruit)
            print(score)
        
    #! Bomb Logic
    for bomb in bombs:
        bomb.draw(screen)
        bomb.update_timer()

    if (len(bombs) < 5) and bomb_counter > 5 :
        bombs.append(Bomb())
        last_bomb_taken = int(pygame.time.get_ticks()/1000)

        #fruit_rect.center = (random.randint( 50 , 950 ) , random.randint( 50 , 950 )) 
    
    for bomb in bombs:
        if player_rect.colliderect(bomb.rect) :
            score -= 1
            score_text = font.render(f'score: {score}' , None , "White").convert_alpha()
            last_fruit_taken = int(pygame.time.get_ticks()/1000)
            # remove bomb
            bombs.remove(bomb)
            print(score)
        if bomb.timer > 5 : bombs.remove(bomb)

    fruit_counter = int(pygame.time.get_ticks()/1000) - last_fruit_taken
    bomb_counter = int(pygame.time.get_ticks()/1000) - last_bomb_taken
    pygame.display.update()
    clock.tick(60)