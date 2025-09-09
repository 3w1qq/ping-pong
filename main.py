import pygame as p
from pygame.locals import *

p.init()

LIGHTPINK = (255, 182, 193)

win_width, win_height = 700, 500

window = p.display.set_mode((win_width, win_height))
window.fill(LIGHTPINK)
p.display.set_caption('Пинг понг')
timer = p.time.Clock()

class GameSprite(p.sprite.Sprite):
    def __init__(self, image_path, speed, x, y, width, height):
        p.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = p.transform.scale(p.image.load(image_path), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_left(self):
        keys_pressed = p.key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= self.speed
        elif keys_pressed[K_s]:
            self.rect.y += self.speed
    
    def move_right(self):
        keys_pressed = p.key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= self.speed
        elif keys_pressed[K_DOWN]:
            self.rect.y += self.speed

racket_left = Player('racket.png', 4, 0, 0, 50, 150)
racket_right = Player('racket.png', 4, win_width - 50, 0, 50, 150)

run = True 

while run:
    events = p.event.get()
    for event in events:
        if event.type == p.QUIT:
            run = False
    window.fill(LIGHTPINK)
    racket_left.draw()
    racket_right.draw()
    racket_right.move_right()
    racket_left.move_left()
    p.display.update()
    timer.tick(60)
