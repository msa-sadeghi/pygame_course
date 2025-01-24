import pygame
pygame.init()
WIDTH = 800
HEIGTH = 600
clock = pygame.time.Clock()
FPS = 60
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
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= 5
    if keys[pygame.K_DOWN] and player_rect.bottom < HEIGTH:
        player_rect.y += 5
    
    
    screen.fill((0,0,0))    
    pygame.draw.rect(screen,  "red", player_rect)
    pygame.display.update()
    clock.tick(FPS)