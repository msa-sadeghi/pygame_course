from pygame.sprite import Sprite
import pygame
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.images = []
        for i in range(1,5):
            img = pygame.image.load(f"./assets/guy{i}.png")
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = 5
        self.flip = False
        
    def draw(self, screen):
        img = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(img, self.rect)
    
    def move(self, moving_left, moving_right):
        dx = 0
        if moving_left:
            dx -= self.speed
            self.flip = True
        if moving_right:
            dx += self.speed
            self.flip = False
            
        self.rect.x += dx
        
    def animation(self):
        pass