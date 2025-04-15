import pygame

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    



    pygame.display.update()