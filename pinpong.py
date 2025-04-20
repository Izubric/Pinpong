from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_q] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_wight - 150:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_p] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < win_wight - 150:
            self.rect.y += self.speed


back = (186, 148, 242)
win_wight = 600
win_hight = 500
window = display.set_mode((win_wight, win_hight))
img_hero = 'rocketka.png'

window.fill(back)


game = True
finish = False
clock = time.Clock()
FPS = 60

roketka1 = Player('roketka.png', 0, 200, 5, 100, 150)
roketka2 = Player('roketka.png', 500, 200, 5, 100, 150)
bal = GameSprite('bal2.png', 200, 200, 15, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        roketka1.update_l()
        roketka2.update_r()
        bal.rect.x += speed_x
        bal.rect.y += speed_y

        if sprite.collide_rect(roketka1, bal) or sprite.collide_rect(roketka2, bal):
            speed_x *= -1
        if bal.rect.y > win_hight-50 or bal.rect.y < 0:
            speed_y *= -1
        if bal.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if bal.rect.x > win_wight:
            finish = True
            window.blit(lose2, (200, 200))

        roketka1.reset()
        roketka2.reset()
        bal.reset()
    
    display.update()
    clock.tick(FPS)