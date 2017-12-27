import pygame
import random

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


def msg(txt, size, color, x, y):
    font = pygame.font.SysFont("comicsansms", size)
    txtsurf = font.render(txt, True, color)
    txtrect = txtsurf.get_rect()
    txtrect.center = x, y
    screen.blit(txtsurf, txtrect)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("copter.png")
        self.image = pygame.transform.scale(self.image, [60, 50])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0
        self.last_shot = pygame.time.get_ticks()
        self.shot_delay = 1000

    def shoot(self):
        now = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if now - self.last_shot > self.shot_delay:
                self.last_shot = now
                bullet = Bullet(self.rect.centerx, self.rect.top, 10, 0)
                all_sprites.add(bullet)
                bullets.add(bullet)

        if keys[pygame.K_LSHIFT]:
            if now - self.last_shot > self.shot_delay:
                self.last_shot = now
                bullet = Bullet(self.rect.centerx, self.rect.bottom, 0, 10)
                all_sprites.add(bullet)
                bullets.add(bullet)

    def update(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vx = -5
        elif keys[pygame.K_RIGHT]:
            self.vx = 5
        elif keys[pygame.K_UP]:
            self.vy = -5
        elif keys[pygame.K_DOWN]:
            self.vy = 5

        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.right >= 400:
            self.rect.right = 400
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
        if self.rect.top <= 0:
            self.rect.top = 0


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        super().__init__()
        self.image = pygame.image.load("bullet.png")
        self.image.convert_alpha()
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.right > 400 + 10:
            self.kill()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.i1 = pygame.image.load("loon.png")
        self.i1 = pygame.transform.scale(self.i1, [30, 50])

        self.image = self.i1

        self.rect = self.image.get_rect()
        x = 400
        y = random.randrange(50, 270)
        self.rect.x = x
        self.rect.y = y
        self.shot_delay = 500
        self.last = pygame.time.get_ticks()

    def update(self):
        if self.rect.right <= 0:
            self.rect.x = 370
            self.rect.y = random.randrange(30, 250)
            self.vx = random.randrange(-6, -1)

        self.rect.x += -2


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cloud.png")
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 40
        self.vx = -2

    def update(self):
        self.rect.x += self.vx
        if self.rect.x < -200:
            self.rect.x = 400


class Ebullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert_alpha()
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        if self.rect.right < 0:
            self.kill()
        self.rect.x += self.vx
        self.rect.y += self.vy


class Boat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("boat.png")
        self.image = pygame.transform.scale(self.image, [60, 50])

        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 300
        self.vx = 0
        self.vy = 0
        self.last_shot = pygame.time.get_ticks()
        self.shot_delay = 400
        self.vx = -0.5
        self.vy = 0

    def update(self):
        self.rect.x += self.vx
        if self.rect.left <= 0:
            self.kill()
            mobgen()

        now = pygame.time.get_ticks()
        if now - self.last_shot > 600:
            self.last_shot = now

            ebullet = Ebullet(self.rect.centerx, self.rect.top, -10, -10)
            all_sprites.add(ebullet)
            ebullets.add(ebullet)


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = random.randrange(50, 250)
        self.vx = 0

    def update(self):
        self.rect.x += -8
        if self.rect.x < -50:
            self.kill()
            mobgen()


class Ecopter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ecopter.png")
        self.image = pygame.transform.scale(self.image, [60, 50])
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = random.randrange(50, 250)
        self.vx = -7
        self.last = pygame.time.get_ticks()

    def update(self):
        self.vy = random.randrange(-3, 3)
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.x < 0:
            self.kill()
            mobgen()

        now = pygame.time.get_ticks()
        if now - self.last > 600:
            self.last = now
            ebullet = Ebullet(self.rect.centerx, self.rect.top, -10, 0)
            all_sprites.add(ebullet)
            ebullets.add(ebullet)


def newmob():
    mob = Mob()
    mobs.add(mob)
    all_sprites.add(mob)


def newboat():
    boat = Boat()
    all_sprites.add(boat)
    boats.add(boat)


def newecopter():
    ecopter = Ecopter()
    all_sprites.add(ecopter)
    ecopters.add(ecopter)


def newship():
    msg("!", 100, RED, 380, 200)
    pygame.display.update()
    ship = Ship()
    all_sprites.add(ship)
    ships.add(ship)


def mobgen():
    i = random.choice([1, 2, 3, 4])
    if i == 1:
        newmob()
    if i == 2:
        newboat()
    if i == 3:
        newship()
    if i == 4:
        newecopter()


def start():
    global hi_score, score

    screen.fill(WHITE)
    msg("Heli Shooter", 50, RED, 200, 100)

    if score > hi_score:
        hscore = open("highscore.txt", "w")
        hscore.write(str(score))
        hscore.close()

    msg("High Score:-" + str(hi_score), 20, RED, 200, 50)

    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        c = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 150 + 70 > c[0] > 150 and 160 + 40 > c[1] > 160:
            msg("Start", 30, BLUE, 180, 180)
            if click[0] == 1:
                wait = 0
        else:
            msg("Start", 30, RED, 180, 180)

        if 160 + 60 > c[0] > 160 and 230 + 40 > c[1] > 230:
            msg("Exit", 30, BLUE, 180, 240)
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            msg("Exit", 30, RED, 180, 240)

        pygame.display.update()


def pause():
    screen.blit(bg, [0, 0])
    msg("Paused", 50, RED, 200, 100)
    pygame.display.update()

    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    wait = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


def Score():
    global intro, score, hscore
    gover = True

    if score > hi_score:
        hscore = open("highscore.txt", "w")
        hscore.write(str(score))
        hscore.close()

    while gover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:

                    gover = False
                elif event.key == pygame.K_r:
                    gover = False
                    intro = True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        msg("High Score :" + str(hi_score), 25, BLUE, 200, 50)
        msg("Game Over", 30, RED, 200, 100)
        msg("Your Score :" + str(score), 25, BLUE, 200, 200)
        pygame.display.flip()


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([400, 400])
pygame.display.set_caption(" Shooter")
clock = pygame.time.Clock()
bg = pygame.image.load("bg.png")

score = 0
hscore = open("highscore.txt", "r")
hi_score = int(hscore.read())

run = True
intro = True
over = False

while run:
    clock.tick(50)

    if intro:
        all_sprites = pygame.sprite.Group()
        cloud = Cloud()
        start()
        player = Player(200, 100)
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        boats = pygame.sprite.Group()
        ebullets = pygame.sprite.Group()
        ships = pygame.sprite.Group()
        ecopters = pygame.sprite.Group()
        all_sprites.add(cloud)
        all_sprites.add(player)
        mob = Mob()
        mobs.add(mob)
        all_sprites.add(mob)
        boat = Boat()
        boats.add(boat)
        all_sprites.add(boat)
        score = 0
        intro = False

    if over:
        all_sprites = pygame.sprite.Group()
        cloud = Cloud()
        player = Player(200, 100)
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        boats = pygame.sprite.Group()
        ebullets = pygame.sprite.Group()
        ships = pygame.sprite.Group()
        ecopters = pygame.sprite.Group()
        all_sprites.add(cloud)
        all_sprites.add(player)
        mob = Mob()
        mobs.add(mob)
        all_sprites.add(mob)
        boat = Boat()
        boats.add(boat)
        all_sprites.add(boat)
        over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            player.shoot()
            if event.key == pygame.K_RETURN:
                pause()

    all_sprites.update()
    last_shot = pygame.time.get_ticks()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    if hits:
        score += 1
        mobgen()

    hits1 = pygame.sprite.spritecollide(player, mobs, True)
    if hits1:
        Score()
        mobgen()

    hits2 = pygame.sprite.groupcollide(boats, bullets, True, True)
    if hits2:
        score += 3
        mobgen()

    hits4 = pygame.sprite.spritecollide(player, ebullets, True)
    if hits4:
        Score()
        over = True

    hits5 = pygame.sprite.groupcollide(bullets, ships, True, True)
    if hits5:
        score += 10
        mobgen()

    hits6 = pygame.sprite.spritecollide(player, ships, False)
    if hits6:
        Score()
        over = True

    hits7 = pygame.sprite.groupcollide(bullets, ecopters, True, True)
    if hits7:
        score += 5
        mobgen()

    hits8 = pygame.sprite.spritecollide(player, ecopters, False)
    if hits8:
        Score()
        over = True

    screen.fill(WHITE)
    screen.blit(bg, [0, 0])
    all_sprites.draw(screen)
    msg("Score:" + str(score), 30, RED, 60, 30)
    pygame.display.flip()

pygame.quit()
quit()
