from pygame import *
from random import randint





class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self,player_image,  player_x, player_y,  size_x, size_y, player_speed):
        super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = "right"
    def reset(self): 
         window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x  -= self.speed
        if keys[K_RIGHT] and self.rect.x <635:
            self.rect.x  += self.speed

    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top,20,40 ,- 15)
        bullets.add(bullet)



lost = 0
class Enemy(GameSprite):
     def update(self):
         self.rect.y += self.speed
         global lost
         if self.rect.y > 500:
             self.rect.x = randint(80,620)
             self.rect.y = 0
             lost = lost + 1
        



class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()




bullets = sprite.Group()

monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy("ufo.png", randint(80,620), -40,80,50, randint(1,3))
    monsters.add(monster)

player = Player("rocket.png", 10, 400, 50, 100, 15)
# enemy = Enemy("ufo.png",100,100,5,100,50)





window = display.set_mode((700, 500))
display.set_caption("Догонялки")
#задай фон сцены
background = transform.scale(image.load("galaxy.jpg"), (700, 500))    
game = True
finish = False
clock = time.Clock()
FPS = 60
score = 0
font.init()
font2 = font.SysFont("impact", 36)
while game:
    for e in event.get():    #обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()       




    if finish != True:
        window.blit(background,(0, 0))
        player.reset()
        player.update()
        # enemy.reset()
        # enemy.update()



   

        text = font2.render("Счет:" + str(score),1, (255,255,255))
        window.blit(text,(10,20))
    
    
    
    
    
    
        text_lose = font2.render("Пропущено:"+ str(lost),1,(255,255,255))
        window.blit(text_lose,(10,50))
            
        
        
        monsters.update()
        
        bullets.update()





        
        monsters.draw(window)



        collides = sprite.groupcollide(monsters,bullets, True, True)
        for c in collides:

            score = score + 1
            monster = Enemy ("ufo.png", randint(80,620), -40,80,50, randint(1,5))
            monsters.add (monster)


        if sprite.spritecollide (player, monsters, False) or lost >= 10:
            finish = True


        if score >= 10:
            finish = True







        bullets.draw(window)
        


        display.update()
    clock.tick(60)
   