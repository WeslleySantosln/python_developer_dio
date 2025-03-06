import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bola no Retângulo")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Parâmetros da bola
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5  # Velocidade horizontal
ball_speed_y = 3  # Velocidade vertical
gravity = 0.2     # Simulação de gravidade

# Parâmetros do retângulo (bordas)
rect_margin = 50
rect_left = rect_margin
rect_right = WIDTH - rect_margin
rect_top = rect_margin
rect_bottom = HEIGHT - rect_margin

# Loop principal
clock = pygame.time.Clock()

while True:
    # Verifica eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Aplica gravidade à velocidade vertical
    ball_speed_y += gravity

    # Atualiza a posição da bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Verifica colisão com as bordas do retângulo
    # Colisão com as laterais (esquerda e direita)
    if ball_x - ball_radius < rect_left:
        ball_x = rect_left + ball_radius
        ball_speed_x = -ball_speed_x * 0.8  # Reduz velocidade (atrito)
    elif ball_x + ball_radius > rect_right:
        ball_x = rect_right - ball_radius
        ball_speed_x = -ball_speed_x * 0.8

    # Colisão com o topo e fundo
    if ball_y - ball_radius < rect_top:
        ball_y = rect_top + ball_radius
        ball_speed_y = -ball_speed_y * 0.8
    elif ball_y + ball_radius > rect_bottom:
        ball_y = rect_bottom - ball_radius
        ball_speed_y = -ball_speed_y * 0.8  # Quica com perda de energia

    # Limpa a tela
    screen.fill(BLACK)

    # Desenha o retângulo
    pygame.draw.rect(screen, WHITE, (rect_left, rect_top, 
                                    rect_right - rect_left, 
                                    rect_bottom - rect_top), 2)

    # Desenha a bola
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros
    clock.tick(60)