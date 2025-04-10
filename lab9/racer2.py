import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
DARK_YELLOW = (240, 190, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ENEMY_SPEED = 5
ENEMY_SPEED2 = 2
COINS_SPEED = 5
SCORE = 0
collected_coins = 0

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Road image
background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Yellow coim class
class YellowCoin(pygame.sprite.Sprite):  
    def __init__(self):
        super().__init__()
        self.value = 1
        self.color = YELLOW
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, COINS_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Dark Yellow coin class
class DarkYellowCoin(pygame.sprite.Sprite):  
    def __init__(self):
        super().__init__()
        self.value = random.randrange(2,5)
        self.color = DARK_YELLOW
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, COINS_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Creating objects
P1 = Player()
E1 = Enemy()
yellow_coin = YellowCoin()
dark_yellow_coin = DarkYellowCoin()

# Creating gorups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(yellow_coin, dark_yellow_coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, yellow_coin, dark_yellow_coin)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    # Display score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Display coin counter 
    coin_count = font_small.render(f"Coins: {collected_coins}", True, BLACK)
    DISPLAYSURF.blit(coin_count, (SCREEN_WIDTH - 100, 10))

    # Display objects
    for entity in all_sprites:
        if entity == dark_yellow_coin and SCORE <= 3:
            continue
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check for collisions with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check for collisions with coins
    coin_hit_list = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coin_hit_list:
        collected_coins += coin.value
        # Creating new coins
        if random.random() < 0.9:
            new_coin = YellowCoin()
        else:
            new_coin = DarkYellowCoin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    #Increase of eneies speed
    if collected_coins // ENEMY_SPEED2 > 1:
        ENEMY_SPEED += 1
        ENEMY_SPEED2 += 5
    
    pygame.display.update()
    FramePerSec.tick(FPS)