import pygame
import random

pygame.init()
pygame.display.set_caption("Snake")
largura, altura = 320, 320
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

tamanho_item = 20
teclas = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

def gerar_item():
    item_x = round(random.randrange(0, largura - tamanho_item) / 20.0) * 20.0
    item_y = round(random.randrange(0, altura - tamanho_item) / 20.0) * 20.0

    return item_x, item_y

def desenhar_item(tamanho, x, y):
    pygame.draw.rect(tela, "green", [x, y, tamanho, tamanho])

def desenhar_personagem(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, "black", [pixel[0], pixel[1], tamanho, tamanho])

def selecionar_velocidade(velocidade_x, velocidade_y, tecla, direcao):

    if tecla == pygame.K_DOWN and direcao != pygame.K_UP:
        velocidade_x = 0
        velocidade_y = tamanho_item
        direcao = pygame.K_DOWN
    elif tecla == pygame.K_UP and direcao != pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = -tamanho_item
        direcao = pygame.K_UP
    elif tecla == pygame.K_RIGHT and direcao != pygame.K_LEFT:
        velocidade_x = tamanho_item
        velocidade_y = 0
        direcao = pygame.K_RIGHT
    elif tecla == pygame.K_LEFT and direcao != pygame.K_RIGHT:
        velocidade_x = -tamanho_item
        velocidade_y = 0
        direcao = pygame.K_LEFT
    else:
        velocidade_x = velocidade_x
        velocidade_y = velocidade_y
        direcao = direcao

    return velocidade_x, velocidade_y, direcao

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Arial", 18)
    texto = fonte.render(f"Pontos: {pontuacao}", False, "black")
    tela.blit(texto, [1, 1])

def rodar_jogo():
    fim_jogo = False

    pontuacao = 0

    pixels = []
    tamanho_personagem = 1

    x = largura / 2
    y = altura / 2

    direcao = 0
    velocidade_x = 0
    velocidade_y = 0

    item_x, item_y = gerar_item()

    while not fim_jogo:
        tela.fill("white")

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN and evento.key in teclas:
                velocidade_x, velocidade_y, direcao = selecionar_velocidade(velocidade_x, velocidade_y, evento.key, direcao)

        # desenhar item
        desenhar_item(tamanho_item, item_x, item_y)

        # colisão com a borda
        if x < 0 or y < 0 or x >= largura or y >= altura:
            fim_jogo = True

        # atualizando posição
        x += velocidade_x
        y += velocidade_y

        # desenhar personagem
        pixels.append([x, y])
        if len(pixels) > tamanho_personagem:
            del pixels[0]
        
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_personagem(tamanho_item, pixels)

        # desenhar pontuação
        desenhar_pontuacao(pontuacao)

        # update
        pygame.display.update()

        # gera novo item
        if x == item_x and y == item_y:
            item_x, item_y = gerar_item()
            pontuacao += 1
            tamanho_personagem += 1

        clock.tick(10)

rodar_jogo()