
from random import *
from pygame import *
font.init()
font = font.SysFont('Arial',40)
score = 3.0
h = 0

window = display.set_mode((700,500))
display.set_caption('shoter')

background = transform.scale(image.load('galaxy.jpg'),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(70,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

game = True

class Rocket(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_d]and self.rect.x < 630:
            self.rect.x +=5
        if key_pressed[K_a]and self.rect.x >  0:
            self.rect.x -=5 
        if h == 1:
            self.kill()
    def fire(self):
        bullets = Bullet('bullet.png',rocket.rect.x ,self.rect.top,10)
        b.add(bullets)

class Monsters(GameSprite):
    def update(self):
        global score
        self.rect.y += self.speed     
        if self.rect.y > 500:
            score -= 1
            self.rect.y =-50
            self.rect.x = randint(80,620)
            

class Bullet(GameSprite):
    def update(self):
        
            
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
        if self.rect.y > 0:
            for i in range(1):
                self.rect.y = self.rect.y - 40


            
            

        




rocket = Rocket('rocket.png',320,400,10)

r = sprite.Group()

r.add(rocket)

b = sprite.Group()



m = sprite.Group()
for i in range (randint(2,5)):
    
    monsters = Monsters('ufo.png',randint(80,620),-10,randint(2,5))
    m.add(monsters)
    




finish = False



FPS = 60
clock = time.Clock()
while game:
    if not finish:
        ded = sprite.groupcollide(b,m,True,True)
        for d in ded:
            monsters = Monsters('ufo.png',randint(80,620),-10,randint(2,5))
            m.add(monsters)
            score = score + 0.50
        gg = sprite.groupcollide(m,r,True,True)
        for ggg in gg:
            h = 1
            rocket.reset()
            rocket.update()
            
            finish = True


        window.blit(background,(0,0))
        rocket.reset()
        rocket.update()
        m.update()
        m.draw(window)       
        if score < 0.1:
            score = 0

        scorerender = font.render('score: '+ str(score),True,(242,243,244))
        window.blit(scorerender,(30,20))
        b.update()
        b.draw(window)

        if score < 0.1:
            F = font.render('Не повезло, не повезло.',True,(243,243,244))
            
            window.blit(F,(150,150))
            
            finish = True

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                rocket.fire()
        

        


        
    clock.tick(FPS)
    display.update()
    
