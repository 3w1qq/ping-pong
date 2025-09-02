import pygame as p

LIGHTPINK = (255, 182, 193)

win_width, win_height = 700, 500
window = p.display.set_mode((win_width, win_height))
window.fill(LIGHTPINK)
p.display.set_caption('Пинг понг')
timer = p.time.Clock()

run = True 

while run:
    events = p.event.get()
    for event in events:
        if event.type == p.QUIT:
            run = False

    p.display.update()
    timer.tick(60)
