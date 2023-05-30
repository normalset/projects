import pygame
from sys import exit
import math
import os
os.chdir("D:\Code\projects-1\pyfractals")

print('hello world')

WIDTH = 800
HEIGHT = 800

pygame.init()
pygame.display.set_caption("Fractals")
counter = 0
screen = pygame.display.set_mode((HEIGHT , WIDTH))
screen_rect = screen.get_rect(center = (HEIGHT/2 , WIDTH/2))

len = 10
dir = -1
start_point = screen_rect.center

def draw(start , len , dir): #start(x,y) dir  0=u 1=d 2=l 3=r 
    global start_point
    
    if dir == 0:
        pygame.draw.line(screen, 'White', start, (start[0] , start[1] - len), 2)
        start_point = (start[0] , start[1] - len)
    elif dir == 1:
        pygame.draw.line(screen, 'White', start, (start[0] - len , start[1]), 2)
        start_point = (start[0] - len , start[1])
    elif dir == 2:
        pygame.draw.line(screen, 'White', start, (start[0] , start[1] + len), 2)
        start_point = (start[0] , start[1] + len)
    elif dir == 3:
        pygame.draw.line(screen, 'White', start, (start[0] + len, start[1]), 2)
        start_point = (start[0] + len, start[1])
    


while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            len += 10
            dir += 1
            if dir == 5 : dir = 0 
            draw(start_point , len , dir)
            draw(start_point , len , dir)
    

    pygame.display.update()
