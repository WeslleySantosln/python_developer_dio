import pygame

# Inicializa o pygame
pygame.init()

# Define as dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Bola Quicando no Retângulo")

# Define as cores
cor_branca = (255, 255, 255)
cor_azul = (0, 0, 255)
cor_preta = (0, 0, 0)

# Define as propriedades do retângulo
retangulo_x = 100
retangulo_y = 100
retangulo_largura = largura_tela - 200 # Deixa margem nas laterais
retangulo_altura = altura_tela - 200  # Deixa margem superior e inferior
retangulo_cor = cor_branca

# Define as propriedades da bola
bola_raio = 30
bola_x = largura_tela // 2
bola_y = altura_tela // 2
bola_velocidade_x = 5
bola_velocidade_y = 5
bola_cor = cor_azul

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Move a bola
    bola_x += bola_velocidade_x
    bola_y += bola_velocidade_y

    # Detecta colisões com as bordas do retângulo
    if bola_x + bola_raio > retangulo_x + retangulo_largura:
        bola_x = retangulo_x + retangulo_largura - bola_raio # Evita que a bola saia do retângulo
        bola_velocidade_x = -bola_velocidade_x # Inverte a direção horizontal
    elif bola_x - bola_raio < retangulo_x:
        bola_x = retangulo_x + bola_raio # Evita que a bola saia do retângulo
        bola_velocidade_x = -bola_velocidade_x # Inverte a direção horizontal

    if bola_y + bola_raio > retangulo_y + retangulo_altura:
        bola_y = retangulo_y + retangulo_altura - bola_raio # Evita que a bola saia do retângulo
        bola_velocidade_y = -bola_velocidade_y # Inverte a direção vertical
    elif bola_y - bola_raio < retangulo_y:
        bola_y = retangulo_y + bola_raio # Evita que a bola saia do retângulo
        bola_velocidade_y = -bola_velocidade_y # Inverte a direção vertical

    # Limpa a tela
    tela.fill(cor_preta)

    # Desenha o retângulo
    pygame.draw.rect(tela, retangulo_cor, (retangulo_x, retangulo_y, retangulo_largura, retangulo_altura), 2) # O '2' desenha apenas a borda

    # Desenha a bola
    pygame.draw.circle(tela, bola_cor, (int(bola_x), int(bola_y)), bola_raio)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a velocidade do jogo (opcional)
    pygame.time.delay(20) # Reduz a velocidade para 20 milissegundos (mais lento)

pygame.quit()