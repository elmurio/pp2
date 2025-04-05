import pygame
import sys
import random

pygame.init()

width, height = 500, 500
cell_size = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Snake')

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = 'RIGHT'
change_to = direction

#New variable for food
food_pos = [random.randrange(1, (width // cell_size)) * cell_size,
            random.randrange(1, (height // cell_size)) * cell_size]
food_spawn = True

#Score and level counters
score = 0
level = 1
speed = 10

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
    
    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size

    #Border collision
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False

    #Collision with the snake's body
    if snake_pos in snake_body[1:]:
        running = False

    snake_body.insert(0, list(snake_pos))

    #If the snake eats food
    if snake_pos == food_pos:
        food_spawn = False
        score += 1
        #Increase level and speed
        if score % 3 == 0:
            level += 1
            speed += 2  
    else:
        snake_body.pop()

    #Generate new food
    if not food_spawn:
        food_pos = [random.randrange(1, (width // cell_size)) * cell_size,
                    random.randrange(1, (height // cell_size)) * cell_size]
        food_spawn = True

    screen.fill(black)

    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
    
    #Draw food
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

    #Display score and level
    font = pygame.font.SysFont('arial', 24)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    level_text = font.render(f'Level: {level}', True, (255, 255, 255))
    screen.blit(score_text, [10, 10])
    screen.blit(level_text, [10, 40])

    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
sys.exit()
