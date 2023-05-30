import pygame 
from sys import exit
import os
import math
os.chdir("D:/Code/Projects/pygameTest")

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render((f'{math.floor(current_time/1000)}') , False , (64,64,64))
    score_rect = score_surf.get_rect(center = (400 , 50))
    screen.blit(score_surf,score_rect)


pygame.init()
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('./font/Pixeltype.ttf' , 50)

start_time = 0
game_active = True
width = 800
height = 400
screen = pygame.display.set_mode((width , height))

#test surfs
sky_surf = pygame.image.load('./graphics/Sky.png').convert()
ground_surf = pygame.image.load('./graphics/ground.png').convert()

# score_surf = test_font.render('My game' , False , (64,64,64))
# score_rect = score_surf.get_rect(center = (width / 2, height *0.2))

snail_surf = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600 , 300))

player_surf = pygame.image.load('./graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0
                                   
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active: 
            # if event.type == pygame.MOUSEMOTION:
            #     if player_rect.collidepoint(event.pos) : print('mouse collision detected')
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity -= 20
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE : 
                game_active = True
                snail_rect.left = 800
                start_time = pygame.time.get_ticks()
                

    if game_active :           
        screen.blit(ground_surf, (0 , 300))
        screen.blit(sky_surf, (0,0))

        #rect(surface , color, thing to draw , line width , border radius, )
        # pygame.draw.rect(screen , '#c0e8ec' , score_rect , 10 , 10)
        # pygame.draw.rect(screen , '#c0e8ec' , score_rect)
        # screen.blit(score_surf , score_rect)
        display_score()
        

        screen.blit(snail_surf, snail_rect)
        snail_rect.x -= 5
        if snail_rect.right <= 0 : snail_rect.left = 800
        screen.blit(player_surf, player_rect)
        
        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300 : player_rect.bottom = 300
        screen.blit(player_surf , player_rect)

        #collisions
        if player_rect.colliderect(snail_rect) : game_active = False
    else: screen.fill('Black')

    pygame.display.update()
    clock.tick(60)
    
    