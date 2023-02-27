import pygame
from random import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 1280
is_running = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Barnsley Fern")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

def translate(point, old_min, old_max, new_min, new_max):
    return (point - old_min) * (new_max - new_min) / (old_max - old_min) + new_min

def draw_point(x, y) -> None:
    rect = pygame.Rect(translate(x, -2.1820, 2.6558, 0, SCREEN_WIDTH), translate(y, 0, 9.9983, SCREEN_HEIGHT, 0), 1, 1)
    pygame.draw.rect(screen, (0, 255, 0), rect)

def get_next_point(x, y):
    num = random()
    if num < 0.1:
        # Takes any point and moves it onto a line at the center
        # Makes the stem
        new_x = 0
        new_y = 0.16 * y
    elif num < 0.86:
        # Takes a point and moves it up and a little to the right
        # Makes more ferns as you go up and to the right
        new_x = 0.85 * x + 0.04 * y
        new_y = -0.04 * x + 0.85 * y + 1.6
    elif num < 0.93:
        # Rotates a point to the left
        # Crates leaves on the left
        new_x = 0.2 * x + -0.26 * y
        new_y = 0.23 * x + 0.22 * y + 1.6
    else:
        # Flips a point to the right
        # Creates leaves on the right
        new_x = -0.15 * x + 0.28 * y
        new_y = 0.26 * x + 0.24 * y + 0.44
    return new_x, new_y


x, y = 0, 0
screen.fill((0, 0, 0))

while is_running:
    for _ in range(500):
        draw_point(x, y)
        x, y = get_next_point(x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()

pygame.quit()