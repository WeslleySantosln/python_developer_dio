import pygame
import sys

# Inicializa o pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bola em um Retângulo")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurações da bola
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Posição inicial no centro
ball_speed_x, ball_speed_y = 4, 3  # Velocidade inicial

# Configurações do retângulo
rect_width, rect_height = WIDTH, HEIGHT

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)  # Preenche a tela com branco

    # Desenha o retângulo (borda)
    pygame.draw.rect(screen, BLACK, (0, 0, rect_width, rect_height), 2)

    # Desenha a bola
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Atualiza a posição da bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Verifica colisões com as bordas
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= rect_width:
        ball_speed_x = -ball_speed_x  # Inverte a direção horizontal
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= rect_height:
        ball_speed_y = -ball_speed_y  # Inverte a direção vertical

    # Eventos do pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros por segundo (FPS)
    clock.tick(60)

# Encerra o pygame
pygame.quit()
sys.exit()