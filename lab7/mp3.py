import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Music Player")

KEYS = {
    pygame.K_UP: 'play', 
    pygame.K_DOWN: 'stop',
    pygame.K_RIGHT: 'next',
    pygame.K_LEFT: 'previous',
}

playlist = ["track1.mp3", "track2.mp3", "track3.mp3"]
current_track_index = 0

def play_track(track_index):
    track = playlist[track_index]
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()
    print(f"Playing: {track}")

def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(playlist)
    play_track(current_track_index)

def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(playlist)
    play_track(current_track_index)

play_track(current_track_index)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not pygame.mixer.music.get_busy():
                    play_track(current_track_index)
            elif event.key == pygame.K_DOWN:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT: 
                previous_track()

    pygame.display.update()

pygame.quit()
