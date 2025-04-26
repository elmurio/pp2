import pygame
import sys
import random
import json
import psycopg2
from psycopg2 import sql
from datetime import datetime

# Конфигурация подключения к PostgreSQL
DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '634548mmm',
    'host': 'localhost',
    'port': '5432'
}

# Определение уровней
LEVELS = {
    1: {"speed": 10, "walls": [], "description": "No walls, basic speed"},
    2: {"speed": 12, "walls": [[200, 200, 100, 10], [300, 300, 100, 10]], "description": "Two central walls"},
    3: {"speed": 15, "walls": [[100, 100, 10, 300], [400, 100, 10, 300]], "description": "Vertical barriers"}
}

def init_db():
    """Инициализация базы данных и создание таблиц"""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Создание таблицы users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(50) PRIMARY KEY,
            current_level INTEGER DEFAULT 1
        )
    """)
    
    # Создание таблицы scores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) REFERENCES users(username),
            score INTEGER,
            level INTEGER,
            score_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Создание таблицы game_states
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_states (
            username VARCHAR(50) PRIMARY KEY REFERENCES users(username),
            game_state JSONB
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

def save_user(username, level):
    """Сохраняет пользователя и его уровень"""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO users (username, current_level)
        VALUES (%s, %s)
        ON CONFLICT (username) DO UPDATE
        SET current_level = EXCLUDED.current_level
    """, (username, level))
    
    conn.commit()
    cursor.close()
    conn.close()

def get_user_level(username):
    """Получает текущий уровень пользователя"""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("SELECT current_level FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return result[0] if result else 1

def save_score(username, score, level):
    """Сохраняет результат игры"""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Вставка нового результата
    cursor.execute("""
        INSERT INTO scores (username, score, level)
        VALUES (%s, %s, %s)
    """, (username, score, level))
    
    # Удаление старых результатов, если их больше 10
    cursor.execute("""
        DELETE FROM scores
        WHERE id NOT IN (
            SELECT id FROM scores
            ORDER BY score DESC
            LIMIT 10
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

def save_game_state(username, state):
    """Сохраняет текущее состояние игры"""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO game_states (username, game_state)
        VALUES (%s, %s)
        ON CONFLICT (username) DO UPDATE
        SET game_state = EXCLUDED.game_state
    """, (username, json.dumps(state)))
    
    conn.commit()
    cursor.close()
    conn.close()

def get_high_scores():
    """Возвращает топ-10 результатов"""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT username, score, level, score_date
        FROM scores
        ORDER BY score DESC
        LIMIT 10
    """)
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return [{"username": r[0], "score": r[1], "level": r[2], "date": r[3]} for r in results]

# Инициализация базы данных при запуске
init_db()
# Ввод имени пользователя
username = input("Enter your username: ").strip() or "Player"
current_level = get_user_level(username)
print(f"Welcome {username}! Your current level: {current_level}")

# Инициализация Pygame
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
white = (255, 255, 255)

# Инициализация игры
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = 'RIGHT'
change_to = direction

food1_pos = [random.randrange(1, (width // cell_size)) * cell_size,
             random.randrange(1, (height // cell_size)) * cell_size]
food1_spawn = True

food2_pos = [random.randrange(1, (width // cell_size)) * cell_size,
             random.randrange(1, (height // cell_size)) * cell_size]
food2_spawn = False
food2_ticks = 0

score = 0
level = current_level
speed = LEVELS[level]["speed"]
walls = LEVELS[level]["walls"]

clock = pygame.time.Clock()
paused = False

running = True
while running:
    # Управление
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Пауза
                paused = not paused
                if paused:
                    # Сохранение состояния
                    state = {
                        "snake_pos": snake_pos,
                        "snake_body": snake_body,
                        "direction": direction,
                        "food1_pos": food1_pos,
                        "food1_spawn": food1_spawn,
                        "food2_pos": food2_pos,
                        "food2_spawn": food2_spawn,
                        "food2_ticks": food2_ticks,
                        "score": score,
                        "level": level
                    }
                    save_game_state(username, state)
                    save_score(username, score, level)
                    print("Game paused and state saved.")
            if not paused:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'

    if paused:
        font = pygame.font.SysFont('arial', 48)
        pause_text = font.render("Paused", True, white)
        screen.blit(pause_text, (width // 2 - 60, height // 2 - 20))
        pygame.display.flip()
        continue

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size

    # Проверка столкновения с границами
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False

    # Проверка столкновения с телом
    if snake_pos in snake_body[1:]:
        running = False

    # Проверка столкновения со стенами
    snake_rect = pygame.Rect(snake_pos[0], snake_pos[1], cell_size, cell_size)
    for wall in walls:
        wall_rect = pygame.Rect(wall[0], wall[1], wall[2], wall[3])
        if snake_rect.colliderect(wall_rect):
            running = False

    snake_body.insert(0, list(snake_pos))

    # Логика еды
    frame_count += 1
    ap = 1
    if frame_count % 100 == 0 and not food2_spawn:
        ap = random.randrange(1, 3)
    appear = ap == 2

    if snake_pos == food1_pos:
        food1_spawn = False
        score += 1
        if score // level >= 5 and level < max(LEVELS.keys()):
            level += 1
            speed = LEVELS[level]["speed"]
            walls = LEVELS[level]["walls"]
            save_user(username, level)  # Обновление уровня пользователя

    elif snake_pos == food2_pos:
        food2_spawn = False
        score += random.randrange(2, 4)
        if score // level >= 5 and level < max(LEVELS.keys()):
            level += 1
            speed = LEVELS[level]["speed"]
            walls = LEVELS[level]["walls"]
            save_user(username, level)
    else:
        snake_body.pop()

    if not food1_spawn:
        food1_pos = [random.randrange(1, (width // cell_size)) * cell_size,
                     random.randrange(1, (height // cell_size)) * cell_size]
        food1_spawn = True

    if appear and not food2_spawn:
        food2_pos = [random.randrange(1, (width // cell_size)) * cell_size,
                     random.randrange(1, (height // cell_size)) * cell_size]
        food2_spawn = True
        food2_ticks = 0

    if food2_spawn:
        food2_ticks += 1
        if food2_ticks > 99:
            food2_spawn = False

    # Отрисовка
    screen.fill(black)

    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))

    pygame.draw.rect(screen, red, pygame.Rect(food1_pos[0], food1_pos[1], cell_size, cell_size))

    if food2_spawn:
        pygame.draw.rect(screen, yellow, pygame.Rect(food2_pos[0], food2_pos[1], cell_size, cell_size))

    # Отрисовка стен
    for wall in walls:
        pygame.draw.rect(screen, white, pygame.Rect(wall[0], wall[1], wall[2], wall[3]))

    # Отображение информации
    font = pygame.font.SysFont('arial', 24)
    score_text = font.render(f'Score: {score}', True, white)
    level_text = font.render(f'Level: {level} ({LEVELS[level]["description"]})', True, white)
    time_text = font.render(f'You have: {100-food2_ticks}', True, white)
    screen.blit(score_text, [10, 10])
    screen.blit(level_text, [10, 40])
    if food2_spawn:
        screen.blit(time_text, [10, 70])

    pygame.display.flip()

    clock.tick(speed)

# Сохранение финального результата
save_score(username, score, level)
save_user(username, level)
print("Game Over!")
print("High Scores:", get_high_scores())

pygame.quit()
sys.exit()
