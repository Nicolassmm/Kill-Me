#creeria que si quieres que el juego funcione, debes de descargarlo, mas primero prueva en git hub, deproto sale bien (～￣▽￣)～
import pygame
import os
from clases import Background, Button, Rectangle
from funciones import create_new_rectangle, reset_game, load_highest_score, save_highest_score


# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
width, height = 800, 500
screen = pygame.display.set_mode((width, height))

# Título de la ventana esta parte realemnte es un tanto insignificante, ya que no se suele leer ese pedacito de la ventana
##igual lo voy a dejar así, como que le da personalidad
pygame.display.set_caption("kill me")

##ruta  para que el programa me pille la canción
ruta_cancion = os.path.join(r"musica\jo.mp3")

# que empiece a reproducir la canción que ya lo hice buscar anteriormente
pygame.mixer.music.load(ruta_cancion)
pygame.mixer.music.play(-1)  # El argumento -1 indica que la canción se reproducirá en bucle

# Reloj para controlar el tiempo
clock = pygame.time.Clock()

# Variables del juego
background = Background()  # Crear una instancia de la clase Background
rect = Rectangle(width, height)
start_time = None
rect.game_over = True
rect.score = 0
font = pygame.font.Font(None, 36)

# Variables para la pantalla de inicio
start_screen = True
start_button = Button(width // 2 - 100, height // 2 - 25, 200, 50)
start_button_color = (0, 255, 0)

# Bucle principal del juego
reset_game(rect, background)

# Carga el puntaje más alto al inicio
highest_score = load_highest_score()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_highest_score(highest_score)  # Guarda el puntaje más alto antes de salir
            pygame.quit()
            quit()
        if start_screen:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    reset_game(rect, background)  # Usar background
                    start_screen = False
                    rect.score = 0  # Restablece el puntaje al comenzar
        elif rect.game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    reset_game(rect, background)  # Usar background
                    start_screen = True

    if not start_screen:
        if not rect.game_over:
            screen.blit(background.update_background(rect.score, width, height), (0, 0))  # Cambia el fondo

            pygame.draw.rect(screen, rect.rect_color, (rect.rect_x, rect.rect_y, rect.rect_width, rect.rect_height))

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if rect.rect_x <= mouse_x <= rect.rect_x + rect.rect_width and rect.rect_y <= mouse_y <= rect.rect_y + rect.rect_height:
                if pygame.mouse.get_pressed()[0]:
                    create_new_rectangle(rect, width, height)
                    rect.score += 1

            current_time = pygame.time.get_ticks()
            time_elapsed = (current_time - rect.start_time) / 1000 if rect.start_time is not None else 0
            time_remaining = max(0, 10 - time_elapsed)  # Limita el tiempo a 10 segundos

            text = font.render(f"Tiempo restante: {time_remaining:.2f}s", True, (255, 255, 255))
            screen.blit(text, (10, 10))
            score_text = font.render(f"Puntaje: {rect.score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 50))

            if time_remaining <= 0:
                rect.game_over = True

        if rect.game_over:
            text = font.render("Game Over", True, (255, 0, 0))
            screen.blit(text, (width // 2 - 60, height // 2))

            pygame.draw.rect(screen, start_button_color, start_button.rect)
            start_text = font.render("Reiniciar", True, (0, 0, 0))
            screen.blit(start_text, (width // 2 - 40, height // 2 - 10))

            if rect.score > highest_score:
                highest_score = rect.score
                save_highest_score(highest_score)

    if start_screen:
        screen.blit(background.update_background(rect.score, width, height), (0, 0))  # sirve para ambiar el fondo
        pygame.draw.rect(screen, start_button_color, start_button.rect)
        start_text = font.render("Comenzar", True, (0, 0, 0))
        screen.blit(start_text, (width // 2 - 40, height // 2 - 10))
        highest_score_text = font.render(f"Mejor Puntaje: {highest_score}", True, (255, 255, 255))
        screen.blit(highest_score_text, (width - 200, 10))

    pygame.display.update()
    clock.tick(60)
