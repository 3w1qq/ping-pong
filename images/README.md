# Ping pong
Это симулятор игры в пинг-понг, написанный на языке Python.

При написании проекта я использовала библиотеку PyGame.

Это игра на двоих, цель игры заключается в том, чтобы не пропустить мячик и отбить его

![Скриншот](https://raw.githubusercontent.com/3w1qq/ping-pong/56a31963a2ba978e3e708d3e4b70f3a288328938/ping%20pong%20screenshot%20.png)

### Пример кода:

```python
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
```