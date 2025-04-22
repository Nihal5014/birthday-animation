import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600
TITLE = 'Birthday animatioins'

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

run = True
bg1 = pygame.image.load('confetti.jpg')
bg2 = pygame.image.load('cake.jpg')
bg3 = pygame.image.load('birthday_backround.jpg')
while run == True:
    screen.blit(bg1,(0,0))
    font = pygame.font.SysFont("calibiri",22)
    text = font.render('Happy Birthday to you!',True,"black")
    screen.blit(text,(75,75))
    pygame.display.update()
    pygame.time.delay(3000)
    
    screen.blit(bg2,(0,0))
    font = pygame.font.SysFont("times new roman",32)
    text = font.render('Have a wonderful day',True,"orange")
    screen.blit(text,(75,75))
    pygame.display.update()
    pygame.time.delay(3000)

    screen.blit(bg3,(0,0))
    font = pygame.font.SysFont("arial",32)
    text = font.render('May your year be filled with joy',True,"purple")
    screen.blit(text,(150,175))
    pygame.display.update()
    pygame.time.delay(3000)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    



    pygame.display.update()