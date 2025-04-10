import pygame
import sys
import math

pygame.init()

width, height = 1000, 600
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

# Functions to set the current shape
def set_circle():
    global current_shape
    current_shape = "circle"

def set_square():
    global current_shape
    current_shape = "square"

def set_line():
    global current_shape
    current_shape = None 

def set_rectangle():
    global current_shape
    current_shape = "rectangle"

def set_right_triangle():
    global current_shape
    current_shape = "right_triangle"

def set_equilateral_triangle():
    global current_shape
    current_shape = "equilateral_triangle"

def set_rhombus():
    global current_shape
    current_shape = "rhombus"

# Create buttons for the interface
buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(280, 10, 60, 30, 'Eraser', gray, set_white),
    Button(360, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(430, 10, 60, 30, 'Circle', gray, set_circle),    # Button to select circle drawing
    Button(500, 10, 60, 30, 'Square', gray, set_square),    # Button to select square drawing
    Button(570, 10, 60, 30, 'Line', gray, set_line),    # Button to select line drawing
    Button(630, 10, 80, 30, 'Rect', gray, set_rectangle),   # Button to select rectangle drawing
    Button(700, 10, 80, 30, 'R-Tri', gray, set_right_triangle), # Button to select right triangle drawing
    Button(770, 10, 80, 30, 'E-Tri', gray, set_equilateral_triangle),   # Button to select equilateral triangle drawing
    Button(830, 10, 80, 30, 'Rhombus', gray, set_rhombus),  # Button to select rhombus drawing
    Button(935, 10, 60, 30, 'Exit', gray, exit_app)       
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

        if current_shape == "circle":
            # Calculate radius based on the distance from the start point to the mouse position
            radius = int(math.hypot(mouse_x - start_pos[0], mouse_y - start_pos[1]))
            pygame.draw.circle(screen, brush_color, start_pos, radius)  # Draw the circle

        elif current_shape == "square":
            # Calculate side length based on distance from the start point to the mouse position
            side = int(math.hypot(mouse_x - start_pos[0], mouse_y - start_pos[1]))
            # Draw the square with the center at the start position
            pygame.draw.rect(screen, brush_color, (start_pos[0] - side // 2, start_pos[1] - side // 2, side, side))

        # If the current shape is None (drawing lines)
        elif current_shape is None:
            pygame.draw.line(screen, brush_color, last_pos, (mouse_x, mouse_y), 3)  # Draw the line
            last_pos = (mouse_x, mouse_y)  # Update the last position for the next line segment

        elif current_shape == "rectangle":
            # Calculate height and width based on distance from the start point to the mouse position
            rect = pygame.Rect(min(start_pos[0], mouse_x), min(start_pos[1], mouse_y),
                               abs(mouse_x - start_pos[0]), abs(mouse_y - start_pos[1]))
            # Draw the rectangle with the left-top angle at the start position
            pygame.draw.rect(screen, brush_color, rect)

        elif current_shape == "right_triangle":
            # Right triangle with start point, vertical drop, and diagonal to mouse
            points = [start_pos, (start_pos[0], mouse_y), (mouse_x, mouse_y)]
            pygame.draw.polygon(screen, brush_color, points)

        elif current_shape == "equilateral_triangle":
            # Equilateral triangle pointing up from start_pos
            side = abs(mouse_x - start_pos[0])
            height = (math.sqrt(3) / 2) * side
            top_point = start_pos
            left_point = (start_pos[0] - side / 2, start_pos[1] + height)
            right_point = (start_pos[0] + side / 2, start_pos[1] + height)
            pygame.draw.polygon(screen, brush_color, [top_point, left_point, right_point])

        elif current_shape == "rhombus":
            # Rhombus centered at start_pos, stretched by mouse drag
            dx = mouse_x - start_pos[0]
            dy = mouse_y - start_pos[1]
            points = [
                (start_pos[0], start_pos[1] - dy),
                (start_pos[0] + dx, start_pos[1]),
                (start_pos[0], start_pos[1] + dy),
                (start_pos[0] - dx, start_pos[1])
            ]
            pygame.draw.polygon(screen, brush_color, points)



    # Draw the top panel with buttons
    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)  # Draw each button on the screen

    pygame.display.flip()