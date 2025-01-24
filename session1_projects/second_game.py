import pygame
pygame.init()
WIDTH = 800
HEIGTH = 600

screen = pygame.display.set_mode((WIDTH, HEIGTH))
player_rect = pygame.Rect(10, 10, 50, 50)
y_direction = 1
x_direction = 1
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player_rect.x += 2 * x_direction
    player_rect.y += 2 * y_direction
    if player_rect.y >= HEIGTH:
        y_direction *= -1
    if player_rect.x >= WIDTH:
        x_direction *= -1
        
        
    pygame.draw.rect(screen,  "red", player_rect)
    pygame.display.update()