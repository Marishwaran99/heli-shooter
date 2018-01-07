import pygame,time,random
pygame.init()
pygame.mixer.init()
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
dw=500
dh=500
screen=pygame.display.set_mode([dw,dh])
pygame.display.set_caption(" Shooter")
clock=pygame.time.Clock()
bg=pygame.image.load("bg.png")
def msg(txt,size,color,x,y):
    font=pygame.font.SysFont("comicsansms",size,bold=1)
    txtsurf=font.render(txt,True,color)
    txtrect=txtsurf.get_rect()
    txtrect.x=x
    txtrect.y=y
    screen.blit(txtsurf,txtrect)
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y): 
        super().__init__()
        self.i1=pygame.image.load("copter.png")
        self.i1=pygame.transform.scale(self.i1,[60,50]) 
        self.i2=pygame.image.load("copter1.png")
        self.i2=pygame.transform.scale(self.i2,[60,50])
        self.i3=pygame.image.load("crash.png")
        self.image=self.i1
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vx=0
        self.vy=0
        self.last_shot=pygame.time.get_ticks()
        self.last=pygame.time.get_ticks()
        self.shot_delay=1000
    def shoot(self):
        now=pygame.time.get_ticks()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if now-self.last_shot>self.shot_delay:
                self.last_shot=now
                bullet=Bullet(self.rect.centerx,self.rect.top,10,0)
                all_sprites.add(bullet)
                bullets.add(bullet)
        if keys[pygame.K_LSHIFT]:
            if now-self.last_shot>self.shot_delay:
                self.last_shot=now
                bullet=Bullet(self.rect.centerx,self.rect.bottom,0,10)
                all_sprites.add(bullet)
                bullets.add(bullet)    
    def update(self):
       n=pygame.time.get_ticks()
       if n-self.last>100:
            self.last=n
            self.image=self.i2
       else:     
        self.image=self.i1
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
    def __init__(self,x,y,vx,vy):
        super().__init__()
        self.image=pygame.image.load("b.png")     
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vx=vx
        self.vy=vy
    def update(self):
        self.rect.x+=self.vx
        self.rect.y+=self.vy
        if self.rect.right>dw+10:
            self.kill()       
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.i1=pygame.image.load("loon.png")
        self.i1=pygame.transform.scale(self.i1,[30,50])       
        self.image=self.i1        
        self.rect=self.image.get_rect()
        x=500
        y=random.randrange(50,270)
        self.rect.x=x
        self.rect.y=y
        self.shot_delay=500
        self.last=pygame.time.get_ticks()
    def update(self):         
        if self.rect.right<=0:
          self.rect.x=500
          self.rect.y=random.randrange(30,250)
          self.vx=random.randrange(-6,-1)
        self.rect.x+=-3
        
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("cloud.png")
        self.image=pygame.transform.scale(self.image,(200,100))
        self.rect=self.image.get_rect()
        self.rect.x=500
        self.rect.y=random.randrange(40,200)
        self.vx=-1
    def update(self):
        self.rect.x+=self.vx
        if self.rect.x<-200:
            self.rect.x=500
class Ebullet(pygame.sprite.Sprite):
    def __init__(self,x,y,vx,vy):
        super().__init__()
        self.image=pygame.image.load("b.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vx=vx
        self.vy=vy
    def update(self):
        if self.rect.right<0:
            self.kill()
        self.rect.x+=self.vx
        self.rect.y+=self.vy
class Boat(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.image=pygame.image.load("boat.png")
        self.image=pygame.transform.scale(self.image,[60,50])
        self.rect=self.image.get_rect()
        self.rect.x=500
        self.rect.y=300
        self.vx=0
        self.vy=0
        self.last_shot=pygame.time.get_ticks()
        self.shot_delay=400
        self.vx=-0.5
        self.vy=0
    def update(self):       
        self.rect.x+=self.vx
        if self.rect.left<=0:
           self.kill()
           mobgen()
        now=pygame.time.get_ticks()
        if now-self.last_shot>600:
            self.last_shot=now            
            ebullet=Ebullet(self.rect.centerx,self.rect.top,-10,-10)
            all_sprites.add(ebullet)
            ebullets.add(ebullet)      
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("ship.png")
        self.image=pygame.transform.scale(self.image,(70,50))
        self.rect=self.image.get_rect()
        self.rect.x=600
        self.rect.y=random.randrange(50,250)
        self.vx=0
    def update(self):
        self.rect.x+=-10
        if self.rect.x<-50:
            self.kill()
            mobgen()
class Ecopter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.i1=pygame.image.load("ecopter.png")
        self.i1=pygame.transform.scale(self.i1,[60,50])
        self.i2=pygame.image.load("ecopter1.png")
        self.i2=pygame.transform.scale(self.i2,[60,50])
        self.image=self.i1
        self.rect=self.image.get_rect()
        self.rect.x=510
        self.rect.y=random.randrange(50,250)
        self.last=pygame.time.get_ticks()
        self.lanim=pygame.time.get_ticks()
        self.vx=0
        self.vy=0
    def shoot(self):
        now=pygame.time.get_ticks()
        if now-self.last>600:
            self.last=now
            ebullet=Ebullet(self.rect.centerx,self.rect.top,-10,0)
            all_sprites.add(ebullet)
            ebullets.add(ebullet)
    def  update(self):
        n=pygame.time.get_ticks()
        if n-self.lanim>100:
            self.lanim=n
            self.image=self.i2
        else:           
           self.image=self.i1    
        if self.rect.x<=510 and self.rect.x>350:
            self.vx=-2            
        self.rect.x+=self.vx
        self.rect.y+=self.vy
        self.shoot()
def drawlives(x,y,lives):
    for a in range(lives):
        i=pygame.image.load("copter.png")
        i=pygame.transform.scale(i,(30,25))
        irect=i.get_rect()
        irect.x=x+40*a+10
        irect.y=y
        screen.blit(i,irect)    
def newmob():   
        mob=Mob()
        mobs.add(mob)
        all_sprites.add(mob)
def newboat():   
    boat=Boat()
    all_sprites.add(boat)
    boats.add(boat)
def newecopter():    
    ecopter=Ecopter()
    all_sprites.add(ecopter)
    ecopters.add(ecopter)    
def newship():
    ship=Ship()
    if ship.rect.x>500:
        msg("!",100,Red,480,ship.rect.y)
        pygame.display.update()
    all_sprites.add(ship)
    ships.add(ship)    
def mobgen():
    i=random.random()
    if i>0.3 and i<0.5:
        newship()
    if i>0.6 and i<0.7:
        newecopter()
    if i>0.80 and i<0.85:
        newship()
def start():
    global hi_score,score
    screen.blit(bg,(0,0))
    i=pygame.image.load("cloud.png")
    irect=i.get_rect()
    irect.x=250
    irect.y=250
    msg("Heli Shooter",50,Red,100,150)
    if score>hi_score:
        hscore=open("highscore.txt","w")
        hscore.write(str(score))
        hscore.close()
    msg("High Score:-"+str(hi_score),20,Red,170,50)
    msg("Press Enter to Start",30,Red,100,300)
    pygame.display.update()
    wait=True
    while wait:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                   wait=0           
        
def pause():
    screen.blit(bg,[0,0])

    msg("Paused",50,Red,170,220)    
    pygame.display.update()    
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
def Score():
    global intro,score,hscore
    gover=True
    if  score>hi_score:
        hscore=open("highscore.txt","w")        
        hscore.write(str(score))
        hscore.close()
    while gover:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    gover=False
                elif event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        msg("High Score :"+str(hi_score),25,Blue,160,100)
        msg("Press Enter to Play Again ",25,Blue,100,175) 
        msg("Game Over",30,Red,180,250)
        pygame.display.flip()      
score=0
run=True
intro=True
over=False
hscore=open("highscore.txt","r")
hi_score=int(hscore.read())
while run:
    hscore=open("highscore.txt","r")
    hi_score=int(hscore.read())
    clock.tick(50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
                player.shoot()               
                if event.key==pygame.K_RETURN:
                    pause()
    if intro:
        all_sprites=pygame.sprite.Group()
        cloud=Cloud()
        start()
        player=Player(200,100)
        mobs=pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        boats=pygame.sprite.Group()
        ebullets=pygame.sprite.Group()
        ships=pygame.sprite.Group()
        ecopters=pygame.sprite.Group()
        all_sprites.add(cloud)
        all_sprites.add(player)
        mob=Mob()
        mobs.add(mob)
        all_sprites.add(mob)
        boat=Boat()
        boats.add(boat)
        all_sprites.add(boat)
        score=0
        lives=3
        intro=False
    if over:
        Score()
        all_sprites=pygame.sprite.Group()
        cloud=Cloud()
        player=Player(200,100)
        mobs=pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        boats=pygame.sprite.Group()
        ebullets=pygame.sprite.Group()
        ships=pygame.sprite.Group()
        ecopters=pygame.sprite.Group()
        all_sprites.add(cloud)
        all_sprites.add(player)
        mob=Mob()
        mobs.add(mob)
        all_sprites.add(mob)
        boat=Boat()
        boats.add(boat)
        all_sprites.add(boat)
        score=0
        lives=3
        over=False    
    all_sprites.update()
    last_shot=pygame.time.get_ticks()
    hits=pygame.sprite.groupcollide(mobs,bullets,True,True)
    if hits:
            score+=10
            newmob()
            mobgen()
    hits1=pygame.sprite.spritecollide(player,mobs,True)
    if hits1:
        lives-=1
        newmob()
    hits2=pygame.sprite.groupcollide(boats,bullets,True,True)
    if hits2:
        score+=30
        mobgen()
    hits4=pygame.sprite.spritecollide(player,ebullets,True)
    if hits4:
        lives-=1
    hits5=pygame.sprite.groupcollide(bullets,ships,True,True)
    if hits5:
        score+=50
        mobgen()
    hits6=pygame.sprite.spritecollide(player,ships,True)
    if hits6:
        lives-=1
        newmob()
        mobgen()
    hits7=pygame.sprite.groupcollide(bullets,ecopters,True,True)
    if hits7:
        score+=40
        mobgen()
    hits8=pygame.sprite.spritecollide(player,ecopters,True)
    if hits8:
        lives-=1
        newmob()
        mobgen()
    hits9=pygame.sprite.spritecollide(player,boats,True)
    if hits9:
        lives-=1
        mobgen()
        newmob()
    screen.blit(bg,(0,0))
    all_sprites.draw(screen)
    msg("Score:"+str(score),20,Red,220,15)
    drawlives(10,10,lives)
    if lives<=0:
        player.image=player.i3
        over=1
    pygame.display.flip()
pygame.quit()
quit()
