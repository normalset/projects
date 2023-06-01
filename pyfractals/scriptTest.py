import pygame , random , math , os , time
from sys import exit
os.chdir("D:\Code\projects-1\pyfractals")


print('hello world')

WIDTH = 1000
HEIGHT = 1000

random.seed(time.time())
file_name = 'screenshot'

pygame.init()
pygame.display.set_caption("Fractals")
counter = 0
screen = pygame.display.set_mode((HEIGHT , WIDTH))
screen_rect = screen.get_rect(center = (HEIGHT/2 , WIDTH/2))
clock = pygame.time.Clock()

len = 1
dir = -1
angle = 0
start_point = screen_rect.center

# def drawCard(start , len , dir): #start(x,y) dir  0=u 1=d 2=l 3=r 
#     global start_point
    
#     if math.floor(dir) == 0:
#         pygame.draw.line(screen, 'White', start, (start[0] , start[1] - len), 2)
#         start_point = (start[0] , start[1] - len)
#     elif math.floor(dir) == 1:
#         pygame.draw.line(screen, 'White', start, (start[0] - len , start[1]), 2)
#         start_point = (start[0] - len , start[1])
#     elif math.floor(dir) == 2:
#         pygame.draw.line(screen, 'White', start, (start[0] , start[1] + len), 2)
#         start_point = (start[0] , start[1] + len)
#     elif math.floor(dir) == 3:
#         pygame.draw.line(screen, 'White', start, (start[0] + len, start[1]), 2)
#         start_point = (start[0] + len, start[1])
r=g=b=100  
def drawAngle(start , len , angle):
    global start_point ,r,g,b
    dir = math.radians(angle)
    end = (start[0] + math.cos(dir)*len , start[1] + math.sin(dir)*len)
    
    #pygame.draw.line(screen, 'White', start, end, 2)
    pygame.draw.line(screen, (r,g,b) , start, end, 2)
    r=g=b=(b+1)%256
    print(start , end , len , (angle , dir) , r,g,b)
    start_point = end

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEBUTTONDOWN:
    
    if counter > 500 : exit()
    # Rotazione NSWE
    # len += 1
    # dir = random.randint(0,3)
    # if dir >= 5 : dir = 0 
    # drawCard(start_point , len , dir)
    
    len += 1
    angle = random.randint(0,359)
    if angle > 360 : angle = 0
    drawAngle(start_point , len , angle)

    pygame.display.update()
    
    if start_point[0] > 1000 or start_point[1] > 1000 :
        if counter < 500 and counter%5 == 0 :
            file_path = f'{file_name}-{str(time.time())}.png'
            pygame.image.save(screen, file_path)
            screen.fill((0, 0, 0))
        
        counter += 1
        start_point = (WIDTH/2 , HEIGHT/2)
        len = 1
    
