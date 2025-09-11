import pygame as p
from pygame.locals import *

p.init()

LIGHTBLUE = (70, 130, 180)
GREEN = (0, 100, 0)

win_width, win_height = 700, 500

window = p.display.set_mode((win_width, win_height))
window.fill(LIGHTBLUE)
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

racket_left = Player('./images/racket.png', 4, 0, 0, 50, 150)
racket_right = Player('./images/racket.png', 4, win_width - 50, 0, 50, 150)
ball = GameSprite('./images/ball.png', 5, win_width / 2, 50, 50, 50)

run = True 
finish = False
speed_x = 2
speed_y = 2

while run:
    events = p.event.get()
    for event in events:
        if event.type == p.QUIT:
            run = False
    if not finish:
        window.fill(LIGHTBLUE)
        ball.draw()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if ball.rect.colliderect(racket_right):
            speed_x *= -1
        elif ball.rect.y >= win_height - 50:
            speed_y *= -1
        elif ball.rect.y <= 0:
            speed_y *= -1
        elif ball.rect.colliderect(racket_left):
            speed_x *= -1
        
        if ball.rect.x <= 0:
            win_left = p.font.Font(None, 75).render('SECOND PLAYER WIN!', True, GREEN)
            window.blit(win_left, (75, 200))
            finish = True
        elif ball.rect.x >= win_width:
            win_right = p.font.Font(None, 75).render('FIRST PLAYER WIN!', True, GREEN)
            window.blit(win_right, (100, 200))
            finish = True

        racket_left.draw()
        racket_right.draw()
        racket_right.move_right()
        racket_left.move_left()
    p.display.update()
    timer.tick(60)
