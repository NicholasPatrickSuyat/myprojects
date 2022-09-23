import pygame
import random

pygame.init()

size = width, height = 600, 600
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
colors = ["Red", "Blue", "Green"]

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
rgb = [r,g,b]
randcolor = random.randrange(0,255)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Click and drag to draw")

keep_going = True
mousedown = False
radius = 5

while keep_going != False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going  = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
            
    if mousedown:
        spot = pygame.mouse.get_pos() 
        if pygame.mouse.get_pressed()[0]: 
            button_color = rgb[0]
        elif pygame.mouse.get_pressed()[1]:
            button_color = rgb[1]
        elif pygame.mouse.get_pressed()[2]:
            button_color = rgb[2]
        pygame.draw.circle(screen, button_color, spot, radius)      
    pygame.display.update()
pygame.quit()