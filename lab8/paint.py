import pygame
import sys
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple paint')

white = (255, 255, 255)
black = (0, 0 , 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

# Button class for creating clickable buttons
class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)  # Define button's position and size
        self.text = text  # Text that appears on the button
        self.color = color  # Button's color
        self.action = action  # Action to be performed when the button is clicked

    def draw(self, screen):
        # Draw the button rectangle
        pygame.draw.rect(screen, self.color, self.rect)
        # Render the text on the button
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 12))

    def check_action(self, event):
        # Check if the button was clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()  # Call the associated action when button is clicked

# Global variables for drawing state
drawing = False
brush_color = black  # Default color of the brush
current_shape = None  # Shape currently selected
start_pos = None  # Starting position for drawing shapes or lines
last_pos = None  # Last position for drawing lines

# Functions to change the brush color
def set_black():
    global brush_color
    brush_color = black

def set_green():
    global brush_color
    brush_color = green

def set_red():
    global brush_color
    brush_color = red

def set_blue():
    global brush_color
    brush_color = blue

def set_white():
    global brush_color
    brush_color = white

def clear_screen():
    screen.fill(white)

def exit_app():
    pygame.quit()
    sys.exit()

# Functions to set the current shape (circle, square, or line)
def set_circle():
    global current_shape
    current_shape = "circle"

def set_square():
    global current_shape
    current_shape = "square"

def set_line():
    global current_shape
    current_shape = None 

# Create buttons for the interface
buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Eraser', gray, set_white),
    Button(380, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(470, 10, 60, 30, 'Exit', gray, exit_app),
    Button(540, 10, 60, 30, 'Circle', gray, set_circle),  # Button to select circle drawing
    Button(610, 10, 60, 30, 'Square', gray, set_square),  # Button to select square drawing
    Button(680, 10, 60, 30, 'Line', gray, set_line)       # Button to select line drawing
]

clear_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = pygame.mouse.get_pos()  # Save the starting position of the mouse
                last_pos = start_pos  # Save the starting position for line drawing
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                start_pos = None  # Reset start position after releasing the mouse

        # Check button actions (for color and shape selections)
        for button in buttons:
            button.check_action(event)

    # If drawing is active, perform the drawing action
    if drawing and start_pos:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # If the current shape is a circle
        if current_shape == "circle":
            # Calculate radius based on the distance from the start point to the mouse position
            radius = int(math.hypot(mouse_x - start_pos[0], mouse_y - start_pos[1]))
            pygame.draw.circle(screen, brush_color, start_pos, radius)  # Draw the circle

        # If the current shape is a square
        elif current_shape == "square":
            # Calculate side length based on distance from the start point to the mouse position
            side = int(math.hypot(mouse_x - start_pos[0], mouse_y - start_pos[1]))
            # Draw the square with the center at the start position
            pygame.draw.rect(screen, brush_color, (start_pos[0] - side // 2, start_pos[1] - side // 2, side, side))

        # If the current shape is None (drawing lines)
        elif current_shape is None:
            pygame.draw.line(screen, brush_color, last_pos, (mouse_x, mouse_y), 3)  # Draw the line
            last_pos = (mouse_x, mouse_y)  # Update the last position for the next line segment

    # Draw the top panel with buttons
    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)  # Draw each button on the screen

    pygame.display.flip()  # Update the screen
