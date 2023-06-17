from pygame import *

win_width = 600
win_height = 500
title = 'Ping-Pong'
back = (127, 127, 127)

window = display.set_mode((win_width, win_height))
display.set_caption(title)
window.fill(back)

racket_width = 10
racket_height = 70

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,  player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 430:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
f1 = font.Font(None, 30)
l_lose = f1.render('Левый игрок проиграл!', True, (125, 0, 0))
r_lose = f1.render('Правый игрок проиграл!', True, (125, 0, 0))

speedx = 3
speedy = 3

l_player = Player('sprite2.jpeg', 30, 200, racket_width, racket_height, 7)
r_player = Player('sprite2.jpeg', 580, 200, racket_width, racket_height, 7)
ball = GameSprite('ball.jpeg', 200, 200, 50, 50, 8)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)
        l_player.update_l()
        r_player.update_r()
        ball.rect.x += speedx
        ball.rect.y += speedy

        if sprite.collide_rect(l_player, ball) or sprite.collide_rect(r_player, ball):
            speedx *= -1
        if ball.rect.y < 0 or ball.rect.y > 450:
            speedy *= -1
        if ball.rect.x > 550:
            finish = True
            window.blit(r_lose, (200, 200))
        if ball.rect.x < 0:
            finish = True
            window.blit(l_lose, (200, 200))

        r_player.reset()
        l_player.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
