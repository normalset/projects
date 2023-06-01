import pygame 
from sys import exit
import os
import math
os.chdir("D:\Code\projects-1\pygameTest")

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}' , False , (64,64,64))
    score_rect = score_surf.get_rect(center = (400 , 50))
    screen.blit(score_surf,score_rect)
    return current_time


pygame.init()
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('./font/Pixeltype.ttf' , 50)

start_time = 0
game_active = False
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH , HEIGHT))
score = 0

#test surfs
sky_surf = pygame.image.load('./graphics/Sky.png').convert()
ground_surf = pygame.image.load('./graphics/ground.png').convert()

# score_surf = test_font.render('My game' , False , (64,64,64))
# score_rect = score_surf.get_rect(center = (WIDTH / 2, HEIGHT *0.2))

snail_surf = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600 , 300))

player_surf = pygame.image.load('./graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#intro screen
player_stand = pygame.image.load("./graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (WIDTH/2 , HEIGHT/2))

intro_text = test_font.render("PIXL/Runner - Press space to start and jump!" , False , "White")
intro_text_rect = intro_text.get_rect(center = (WIDTH/2 , HEIGHT/5))

                                   
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active: 
            # if event.type == pygame.MOUSEMOTION:
            #     if player_rect.collidepoint(event.pos) : print('mouse collision detected')

            score = display_score()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity -= 20
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE : 
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)
                

    if game_active :           
        screen.blit(ground_surf, (0 , 300))
        screen.blit(sky_surf, (0,0))

        #rect(surface , color, thing to draw , line WIDTH , border radius, )
        # pygame.draw.rect(screen , '#c0e8ec' , score_rect , 10 , 10)
        # pygame.draw.rect(screen , '#c0e8ec' , score_rect)
        # screen.blit(score_surf , score_rect)
        score = display_score()
        

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
    else:         
        score_message = test_font.render(f'Your Score was: {score}' , False , "White")
        score_message_rect = score_message.get_rect(center = (WIDTH/2 , HEIGHT * 0.8))
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        
        if score == 0 : screen.blit(intro_text , intro_text_rect)
        else : screen.blit(score_message , score_message_rect)
            

    pygame.display.update()
    clock.tick(60)
    
