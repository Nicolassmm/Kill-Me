import pygame
import random

def create_new_rectangle(rect, width, height):
    rect.rect_x = random.randint(0, width - rect.rect_width)
    rect.rect_y = random.randint(0, height - rect.rect_height)
    rect.rect_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def reset_game(rect, current_background_index):
    rect.game_over = False
    rect.score = 0
    rect.start_time = pygame.time.get_ticks()  # Agrega esta línea para actualizar start_time
    create_new_rectangle(rect, rect.width, rect.height)
    current_background_index = 0


def load_highest_score():
    try:
        with open("highest_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def save_highest_score(score):
    with open("highest_score.txt", "w") as file:
        file.write(str(score))
