import pygame
pygame.init()
WIDTH = 800
HEIGTH = 600

# screen = pygame.display.set_mode((WIDTH, HEIGTH))
screen = pygame.display.set_mode()
pygame.display.set_caption("my game")
martin_img = pygame.image.load("martin.png")

pygame.display.set_icon(martin_img)
# my_font = pygame.font.SysFont("arial", 24)
my_font = pygame.font.Font("./mtfont.otf", 24)
hello_image = my_font.render("Hello", True, "purple")
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.draw.rect(screen, (255, 0,255), (10, 20, 50, 50), 5)
    pygame.draw.circle(screen, "green", (100, 100), 70, 3)
    pygame.draw.ellipse(screen, "green", (200, 120, 100, 200), 3)
    pygame.draw.line(screen, "white", (200,  220), (400, 220))
    screen.blit(hello_image, (300, 300))
    pygame.display.update()