import pygame

class Background:
    def __init__(self):
        self.background_images = [
            "terrenos/yer.png",
            "terrenos/yer.png",
            "terrenos/bloc.png",
            "terrenos/tres.png",
            "terrenos/inicio.png"
        ]
        self.current_background_index = 0

    def update_background(self, score, width, height):
        if score >= 24:
            self.current_background_index = 4
        elif score >= 16:
            self.current_background_index = 3
        elif score >= 8:
            self.current_background_index = 2
        elif score >= 1:
            self.current_background_index = 1
        else:
            self.current_background_index = 0
        return pygame.transform.scale(pygame.image.load(self.background_images[self.current_background_index]), (width, height))

class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rect_x, self.rect_y = self.width // 2, self.height // 2
        self.rect_width = 50
        self.rect_height = 50
        self.rect_color = (255, 0, 0)
        self.game_over = True
        self.score = 0
        self.start_time = None
