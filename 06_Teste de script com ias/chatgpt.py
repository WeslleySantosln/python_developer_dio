import pygame
import sys

# Inicializa o pygame
pygame.init()

# Definir as cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definir o tamanho da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bola dentro do retângulo")

# Definir a bola
ball_radius = 20
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 4
ball_speed_y = 0
gravity = 0.5

# Definir o retângulo (dimensões da tela)
rect_x = 0
rect_y = 0
rect_width = screen_width
rect_height = screen_height

# Relógio para controlar a taxa de atualização
clock = pygame.time.Clock()

# Loop principal
while True:
    screen.fill(WHITE)  # Preenche o fundo com a cor branca
    
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar a posição da bola com base na velocidade
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Aplicar a gravidade
    ball_speed_y += gravity
    
    # Verificar colisões com as paredes (simulação das leis da física)
    if ball_x - ball_radius <= rect_x or ball_x + ball_radius >= rect_width:
        ball_speed_x = -ball_speed_x  # Inverte a direção horizontal (quica)
    
    if ball_y - ball_radius <= rect_y:  # Colisão com a parte superior
        ball_speed_y = -ball_speed_y  # Inverte a direção vertical (quica)
    elif ball_y + ball_radius >= rect_height:  # Colisão com a parte inferior
        ball_speed_y = -ball_speed_y * 0.9  # Quica, mas perde um pouco de energia (diminui a velocidade)

    # Desenhar a bola
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    # Atualizar a tela
    pygame.display.flip()
    
    # Controlar a taxa de atualização (60 FPS)
    clock.tick(60)
