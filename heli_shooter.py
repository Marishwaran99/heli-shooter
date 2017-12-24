import pygame,time,random
pygame.init()
Aqua =( 0, 255, 255)
Black= ( 0, 0, 0)
Blue =( 0, 0, 255)
Fuchsia= (255, 0, 255)
Gray= (128, 128, 128)
Green= ( 0, 128, 0)
Lime= ( 0, 255, 0)
Maroon= (128, 0, 0)
NavyBlue= ( 0, 0, 128)
Olive =(128, 128, 0)
Purple =(128, 0, 128)
Red= (255, 0, 0)
Silver =(192, 192, 192)
Teal =( 0, 128, 128)
White= (255, 255, 255)
Yellow =(255, 255, 0)
screen=pygame.display.set_mode([400,400])
pygame.display.set_caption(" Shooter")
clock=pygame.time.Clock()
bg=pygame.image.load("bg.png")
def msg(txt,size,color,x,y):
    font=pygame.font.SysFont("bold",size)
    txtsurf=font.render(txt,True,color)
    txtrect=txtsurf.get_rect()
    txtrect.center=x,y
    screen.blit(txtsurf,txtrect)
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y): 
        super().__init__()
        self.image=pygame.image.load("copter.png")
        self.image=pygame.transform.scale(self.image,[60,50])
 
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vx=0
        self.vy=0
        self.last_shot=pygame.time.get_ticks()
        self.shot_delay=1000
    def shoot(self):
        now=pygame.time.get_ticks()
        if now-self.last_shot>self.shot_delay:
            self.last_shot=now
            bullet=Bullet(self.rect.centerx,self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            
    def update(self):
       self.vx,self.vy=0,0
       keys=pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
           self.vx=-5
       elif keys[pygame.K_RIGHT]:
           self.vx=5
       elif keys[pygame.K_UP]:
           self.vy=-5
       elif keys[pygame.K_DOWN]:
           self.vy=5
           
       self.rect.x+=self.vx
       self.rect.y+=self.vy
       if self.rect.right>=400:
           self.rect.right=400
       if self.rect.left<=0:
          self.rect.left=0
       if self.rect.bottom>=400:
           self.rect.bottom=400
       if self.rect.top<=0:
          self.rect.top=0   
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("bullet.png").convert_alpha()
        self.image.set_colorkey(White)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def update(self):
        self.rect.x+=random.randrange(3,6)
        if self.rect.right>400+10:
            self.kill()
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.i1=pygame.image.load("loon.png")
        self.i1=pygame.transform.scale(self.i1,[30,50])
        self.i2=pygame.image.load("ecopter.png")
        self.i2=pygame.transform.scale(self.i2,[50,30])
        self.image=self.i1
        
        self.rect=self.image.get_rect()
        x=400
        y=random.randrange(50,350)
        self.rect.x=x
        self.rect.y=y
        self.last=pygame.time.get_ticks()
    def update(self):
        
        if self.rect.left<=0:
          self.rect.x=370
          self.rect.y=random.randrange(30,370)
          self.vx=random.randrange(-6,-1)
          now=pygame.time.get_ticks()
          if now-self.last>1000:
            self.image=self.i2
            now=self.last
        self.rect.x+=-2  
def newmob():
   
        mob=Mob()
        mobs.add(mob)
        all_sprites.add(mob)
   
def start():
    screen.fill(White)
    msg("Heli Shoot",50,Red,200,100)
    msg("Press Enter to Play",30,Red,200,200)
    msg("Press Escape to Exit",30,Red,200,300)
    
    wait=True
    while wait:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    wait=False
                elif event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        pygame.display.update()
                  
score=0
run=True
intro=True
while run:
    clock.tick(50)
    if intro:
        start()
        
        all_sprites=pygame.sprite.Group()

        player=Player(200,100)
        mobs=pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        all_sprites.add(player)
        mob=Mob()
        mobs.add(mob)
        all_sprites.add(mob)
        intro=False
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player.shoot()
    all_sprites.update()
    hits=pygame.sprite.groupcollide(mobs,bullets,True,True)
    if hits:
        score+=1

        newmob()
    hits1=pygame.sprite.spritecollide(player,mobs,True)
    if hits1:
        score-=1
        newmob()
    screen.fill(White)    
    
    
    screen.blit(bg,[0,0]) 
    all_sprites.draw(screen)
    msg("Score:"+str(score),40,Red,60,30)
    pygame.display.flip()
pygame.quit()
quit()
