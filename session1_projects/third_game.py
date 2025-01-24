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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= 5
            if event.key == pygame.K_RIGHT:
                player_rect.x += 5
            if event.key == pygame.K_UP:
                player_rect.y -= 5
            if event.key == pygame.K_DOWN:
                player_rect.y += 5
    
    
    screen.fill((0,0,0))    
    pygame.draw.rect(screen,  "red", player_rect)
    pygame.display.update()