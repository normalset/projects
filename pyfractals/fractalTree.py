import pygame , random , math , os , time
from sys import exit
os.chdir("D:\Code\projects-1\pyfractals")


print('hello world')

WIDTH = 1000
HEIGHT = 1000

random.seed(time.time())
file_name = 'screenshot'

pygame.init()
pygame.display.set_caption("Tree Fractals")
counter = 0
screen = pygame.display.set_mode((HEIGHT , WIDTH))
screen_rect = screen.get_rect(center = (HEIGHT/2 , WIDTH/2))
clock = pygame.time.Clock()

len = 300
dir = -1
angle = 0
start_point = screen_rect.center


r=g=b=255
def drawAngle(start , len , angle):
    global start_point ,r,g,b
    dir = math.radians(angle)
    end = (start[0] + math.cos(dir)*len , start[1] + math.sin(dir)*len)
    
    #pygame.draw.line(screen, 'White', start, end, 2)
    pygame.draw.line(screen, (r,g,b) , start, end, 2)
    
    print(start , end , len , (angle , dir) , r,g,b)
    start_point = end

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
    
          if counter > 500 : exit()
          
          len /= 2
          if angle > 360 : angle = 0
          drawAngle(start_point , len , angle + 180)

    pygame.display.update()
    
    if start_point[0] > 1000 or start_point[1] > 1000 :
        if counter < 500 and counter%5 == 0 :
            # file_path = f'{file_name}-{str(time.time())}.png'
            # pygame.image.save(screen, file_path)
            screen.fill((0, 0, 0))
        
        counter += 1
        start_point = (WIDTH/2 , HEIGHT/2)
        len = 1
    
