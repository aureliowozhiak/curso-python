import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definição das dimensões da tela
WIDTH = 800
HEIGHT = 600

# Criação da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Simples")

# Variáveis do jogo
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_radius = 20

# Variaveis moedas
moedas = []
for i in range(10):
    moedas.append([random.randint(0, WIDTH), random.randint(0, HEIGHT)])

for moeda in moedas:
    pygame.draw.circle(screen, (255, 255, 0), moeda, 10)

# Loop principal do jogo
running = True
while running:
    # Eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica do jogo WASD
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= 0.2
    if keys[pygame.K_s]:
        player_y += 0.2
    if keys[pygame.K_a]:
        player_x -= 0.2
    if keys[pygame.K_d]:
        player_x += 0.2

    if player_x < 0:
        player_x = 0
    elif player_x > WIDTH:
        player_x = WIDTH
    
    if player_y < 0:
        player_y = 0
    elif player_y > HEIGHT:
        player_y = HEIGHT

    for moeda in moedas:
        if (player_x - moeda[0])**2 + (player_y - moeda[1])**2 < player_radius**2:
            moedas.remove(moeda)
            moedas.append([random.randint(0, WIDTH), random.randint(0, HEIGHT)])
        
    # Renderização do jogo
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (player_x, player_y), player_radius)
    for moeda in moedas:
        pygame.draw.circle(screen, (255, 255, 0), moeda, 10)

    # Atualização da tela
    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()