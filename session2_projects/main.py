import pygame
from player import Player
pygame.init()
screen_width = 800
screen_height = 600
FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Second Game")

clock = pygame.time.Clock()

background_image = pygame.image.load("./assets/background.png")
background_rect = background_image.get_rect(topleft=(0,0))

# pygame.mixer.music.load("assets/background.wav")
# pygame.mixer.music.set_volume(0.4)
# pygame.mixer.music.play(-1)

my_player = Player(100, 300)
moving_left, moving_right = (False, False)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            
            
            
    screen.blit(background_image, background_rect)  
    my_player.move(moving_left, moving_right)
    my_player.draw(screen)     
    pygame.display.update()
    clock.tick(FPS)