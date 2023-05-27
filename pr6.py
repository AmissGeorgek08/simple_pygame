#import
from pygame import *

font.init()

#sprite class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#window
window = display.set_mode((700, 500))
display.set_caption("Sussy Baka")
background = transform.scale(image.load("background_.jpg"), (700, 500))
sprite1 = GameSprite(player_image="sus1.jpg", player_x=100, player_y=100, player_speed=5)
sprite2 = GameSprite(player_image="sus2.jpg", player_x=500, player_y=200, player_speed=5)
clock = time.Clock()

#background music
mixer.init()
mixer.music.load('fire.mp3')
mixer.music.play()
fire_sound = mixer.Sound('fire.mp3')

game = True
collision = False

#game loop
while game:

    #when sprites don't collide:
    if collision == False:

        #blits
        window.blit(background,(0, 0))
        window.blit(sprite1.image,(sprite1.rect.x, sprite1.rect.y))
        window.blit(sprite2.image,(sprite2.rect.x, sprite2.rect.y))

        #controls
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and sprite1.rect.x > 0:
            sprite1.rect.x -= 10
        if keys_pressed[K_d] and sprite1.rect.x < 600:
            sprite1.rect.x += 10
        if keys_pressed[K_w] and sprite1.rect.y > 0:
            sprite1.rect.y -= 10
        if keys_pressed[K_s] and sprite1.rect.y < 400:
            sprite1.rect.y += 10
        if keys_pressed[K_LEFT] and sprite2.rect.x > 0:
            sprite2.rect.x -= 10
        if keys_pressed[K_RIGHT] and sprite2.rect.x < 600:
            sprite2.rect.x += 10
        if keys_pressed[K_UP] and sprite2.rect.y > 0:
            sprite2.rect.y -= 10
        if keys_pressed[K_DOWN] and sprite2.rect.y < 400:
            sprite2.rect.y += 10

    #when sprites collide:
    if sprite.collide_rect(sprite1, sprite2):
        collision = True
        white = (255, 255, 255)
        black = (0, 0, 0)
        x3 = 700
        y3 = 500
        font1 = font.Font('C:/Users/User/Desktop/Files/Φροντιστήριο/Algorithmics/VSCode/sussy baka/arial.ttf', 50)
        text = font1.render('P1 WINS!!!', True, white, black)
        textRect = text.get_rect()
        textRect.center = (x3 // 2, y3 // 2)
        window.blit(text, textRect)

    for e in event.get():
            if e.type == QUIT:
                game = False

    #screen update and fps
    display.update()
    clock.tick(60)