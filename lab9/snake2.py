import pygame
import sys
import random

pygame.init()

width, height = 500, 500
cell_size = 10
frame_count = 0
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Snake')

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = 'RIGHT'
change_to = direction

# New variable for food 1
food1_pos = [random.randrange(1, (width // cell_size)) * cell_size,
            random.randrange(1, (height // cell_size)) * cell_size]
food1_spawn = True

# New variable for food 2
food2_pos = [random.randrange(1, (width // cell_size)) * cell_size,
            random.randrange(1, (height // cell_size)) * cell_size]
food2_spawn = False
food2_ticks = 0

# Score and level counters
score = 0
level = 1
speed = 10

clock = pygame.time.Clock()

running = True
while running:
    # Manipulate the snake with keyboard
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

    # Border collision
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False

    # Collision with the snake's body
    if snake_pos in snake_body[1:]:
        running = False

    snake_body.insert(0, list(snake_pos))

    # Random appearing of food2
    frame_count += 1
    ap = 1
    if frame_count % 100 == 0 and food2_spawn == False:
        ap = random.randrange(1, 3)
    appear = ap == 2

    # If the snake eats food 1 
    if snake_pos == food1_pos:
        food1_spawn = False
        score += 1
        if score // level >= 5:
            level += 1
            speed += 2  

    # If the snake eats food 2
    elif snake_pos == food2_pos:
        food2_spawn = False
        score += random.randrange(2, 4)
        if score // level >= 5:
            level += 1
            speed += 2  
    else:
        snake_body.pop()

    # Generate new food1
    if not food1_spawn:
        food1_pos = [random.randrange(1, (width // cell_size)) * cell_size,
                    random.randrange(1, (height // cell_size)) * cell_size]
        food1_spawn = True

    # Generate new food2
    if appear and not food2_spawn:
        food2_pos = [random.randrange(1, (width // cell_size)) * cell_size,
                    random.randrange(1, (height // cell_size)) * cell_size]
        food2_spawn = True
        food2_ticks = 0

    # Timer of appearance of food2
    if food2_spawn:
        food2_ticks += 1
        if food2_ticks > 99:
            food2_spawn = False

    screen.fill(black)

    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
    
    # Draw food1
    pygame.draw.rect(screen, red, pygame.Rect(food1_pos[0], food1_pos[1], cell_size, cell_size))
    
    # Draw food2 only if it should spawn
    if food2_spawn:
        pygame.draw.rect(screen, yellow, pygame.Rect(food2_pos[0], food2_pos[1], cell_size, cell_size))

    # Display score and level
    font = pygame.font.SysFont('arial', 24)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    time_text = font.render(f'You have: {100-food2_ticks}sec', True, (255, 255, 255))
    level_text = font.render(f'Level: {level}', True, (255, 255, 255))
    screen.blit(score_text, [10, 10])
    screen.blit(level_text, [10, 40])
    if food2_spawn:
        screen.blit(time_text, [10, 70])

    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
sys.exit()