import pygame 
import sys
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("My Ball")
clock = pygame.time.Clock()

back_surface = pygame.Surface((800, 400))
back_surface.fill('white')

ball_x = 400
ball_y = 200
ball_speed = 20
ball_radius = 25

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(back_surface,(0, 0))
    pygame.draw.circle(screen, 'red', (ball_x, ball_y), 25)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= ball_speed  
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < 800:
        ball_x += ball_speed  
    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius < 400:
        ball_y += ball_speed

    pygame.display.update()
    clock.tick(60)