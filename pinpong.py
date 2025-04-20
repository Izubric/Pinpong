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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_wight - 150:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_wight - 150:
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

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        roketka1.update_l()
        roketka2.update_r()

        roketka1.reset()
        roketka2.reset()
    
    display.update()
    clock.tick(FPS)