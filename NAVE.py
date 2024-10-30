import pygame
import random

# Começa o jogo
pygame.init()

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
amarelo_brilhante = (255, 255, 0)

# Dimensões da tela
largura = 800
altura = 600

# Configurações do jogo
largura_nave = 150
altura_nave = 150
velocidade = 5
estrelas_total = 8  # Número de estrelas
meteoros_total = 10  # Número de meteoros


# Carregar a imagem de Vitória
try:
    imagem_vitoria = pygame.image.load("vitoria.JPG")
    imagem_vitoria = pygame.transform.scale(imagem_vitoria, (largura, altura))
except pygame.error as e:
    print(f"Erro ao carregar a imagem de vitória: {e}")
    pygame.quit()
    quit()


# Classe para a nave


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            # Carregar a imagem da nave em vez de usar uma superfície
            self.image = pygame.image.load("shark.png").convert_alpha()
            # Ajuste o tamanho da imagem, se necessário
            self.image = pygame.transform.scale(self.image, (60, 75))
        except pygame.error as e:
            print(f"Erro ao carregar a imagem da nave: {e}")
            pygame.quit()
            quit()

        # Obtém o retângulo da imagem para a nave
        self.rect = self.image.get_rect()
        self.rect.x = largura // 2 - self.rect.width // 2
        self.rect.y = altura - self.rect.height - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= velocidade
        if keys[pygame.K_RIGHT]:
            self.rect.x += velocidade
        if keys[pygame.K_UP]:
            self.rect.y -= velocidade
        if keys[pygame.K_DOWN]:
            self.rect.y += velocidade

        # Impede a nave de sair da tela
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > largura - largura_nave:
            self.rect.x = largura - largura_nave
        if self.rect.y < 0:  # Impede a nave de sair do topo
            self.rect.y = 0
        if self.rect.y > altura - altura_nave:  # Impede a nave de sair da parte inferior
            self.rect.y = altura - altura_nave

# Classe para as estrelas


class Estrela(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            # Carregar a imagem da estrela
            self.image = pygame.image.load("peixe.png").convert_alpha()
            # Redimensionar a imagem da estrela, se necessário
            self.image = pygame.transform.scale(self.image, (30, 30))
        except pygame.error as e:
            print(f"Erro ao carregar a imagem da estrela: {e}")
            pygame.quit()
            quit()

        # Obtém o retângulo da imagem para a estrela
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura - self.rect.width)
        self.rect.y = random.randint(-100, -20)
        self.velocidade = random.randint(2, 5)

    def update(self):
        self.rect.y += self.velocidade
        # Redefine posição caso a estrela saia da tela
        if self.rect.y > altura:
            self.rect.y = random.randint(-100, -20)
            self.rect.x = random.randint(0, largura - self.rect.width)

# Classe para os meteoros


class Meteoro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            # Carregar a imagem do meteoro
            self.image = pygame.image.load("bomba.png").convert_alpha()
            # Tamanho do meteoro ajustado (tente outros tamanhos se necessário)
            self.image = pygame.transform.scale(self.image, (40, 40))
        except pygame.error as e:
            print(f"Erro ao carregar a imagem do meteoro: {e}")
            pygame.quit()
            quit()

        # Obtém o retângulo da imagem para o meteoro
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura - self.rect.width)
        self.rect.y = random.randint(-150, -30)
        self.velocidade = random.randint(3, 6)

    def update(self):
        self.rect.y += self.velocidade
        # Redefine posição caso o meteoro saia da tela
        if self.rect.y > altura:
            self.rect.y = random.randint(-150, -30)
            self.rect.x = random.randint(0, largura - self.rect.width)

# Função para exibir o menu inicial


def menu_inicial():
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("HUNGRY SHARK")
    # Carregar imagem de fundo do menu
    try:
        fundo_menu = pygame.image.load("mar.png")
        fundo_menu = pygame.transform.scale(fundo_menu, (largura, altura))
    except pygame.error as e:
        print(f"Erro ao carregar a imagem de fundo do menu: {e}")
        pygame.quit()
        quit()

    fonte = pygame.font.Font(None, 74)
    fonte_botao = pygame.font.Font(None, 50)
    rodando = True
    while rodando:
        # Desenha a imagem de fundo no menu
        tela.blit(fundo_menu, (0, 0))
        # Desenha título do menu em amarelo brilhante
        titulo = fonte.render("HUNGRY SHARK", True, amarelo_brilhante)
        tela.blit(titulo, (largura // 2 -
                  titulo.get_width() // 2, altura // 4 - 40))

        # Criação dos botões
        botao_jogar = pygame.Rect(
            largura // 2 - 100, altura // 2 - 50, 200, 60)
        botao_sair = pygame.Rect(largura // 2 - 100, altura // 2 + 50, 200, 60)
        pygame.draw.rect(tela, branco, botao_jogar)
        pygame.draw.rect(tela, branco, botao_sair)
        texto_jogar = fonte_botao.render("Jogar", True, preto)
        texto_sair = fonte_botao.render("Sair", True, preto)
        tela.blit(texto_jogar, (botao_jogar.x + botao_jogar.width // 2 - texto_jogar.get_width() // 2,
                                botao_jogar.y + botao_jogar.height // 2 - texto_jogar.get_height() // 2))
        tela.blit(texto_sair, (botao_sair.x + botao_sair.width // 2 - texto_sair.get_width() // 2,
                               botao_sair.y + botao_sair.height // 2 - texto_sair.get_height() // 2))

        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.collidepoint(evento.pos):
                    rodando = False  # Sai do menu para iniciar o jogo
                if botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    quit()


# Carregar a imagem de Game Over
try:
    game_over_image = pygame.image.load("gameover.jpg")
    game_over_image = pygame.transform.scale(
        game_over_image, (largura, altura))
except pygame.error as e:
    print(f"Erro ao carregar a imagem: {e}")
    pygame.quit()
    quit()


def main():
    menu_inicial()
    print("Iniciando o jogo...")
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("HUNGRY SHARK")

    # Carregar imagem de fundo do jogo
    try:
        fundo = pygame.image.load("mar.png")
        fundo = pygame.transform.scale(fundo, (largura, altura))
    except pygame.error as e:
        print(f"Erro ao carregar a imagem de fundo do jogo: {e}")
        pygame.quit()
        quit()

    # Cria uma instância da nave
    nave = Nave()

    # Cria grupos de sprites
    all_sprites = pygame.sprite.Group()
    estrelas = pygame.sprite.Group()
    meteoros = pygame.sprite.Group()

    # Adiciona a nave ao grupo de all_sprites
    all_sprites.add(nave)

    # Cria e adiciona estrelas
    for _ in range(estrelas_total):
        estrela = Estrela()
        all_sprites.add(estrela)
        estrelas.add(estrela)

    # Cria e adiciona meteoros
    for _ in range(meteoros_total):
        meteoro = Meteoro()
        all_sprites.add(meteoro)
        meteoros.add(meteoro)

    # Pontuação do jogador
    pontuacao = 0

    # Loop principal do jogo
    clock = pygame.time.Clock()
    rodando = True
    game_over = False
    venceu = False  # Flag para verificar se o jogador venceu

    while rodando:
        print("Loop do jogo...")
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        if not game_over and not venceu:
            # Atualiza a posição dos sprites
            all_sprites.update()

            # Verifica se a nave colidiu com alguma estrela
            colisoes_estrelas = pygame.sprite.spritecollide(
                nave, estrelas, True)
            for colisao in colisoes_estrelas:
                pontuacao += 1
                # Recria a estrela que foi coletada
                nova_estrela = Estrela()
                all_sprites.add(nova_estrela)
                estrelas.add(nova_estrela)
                if pontuacao >= 8:  # Condição de vitória
                    venceu = True  # O jogador venceu

            # Verifica se a nave colidiu com algum meteoro
            colisoes_meteoros = pygame.sprite.spritecollide(
                nave, meteoros, False)
            if colisoes_meteoros:
                game_over = True  # Termina o jogo se colidir com um meteoro

            # Desenha a imagem de fundo
            tela.blit(fundo, (0, 0))

            # Desenha todos os sprites
            all_sprites.draw(tela)

            # Desenha a pontuação na tela
            fonte = pygame.font.Font(None, 36)
            texto_pontuacao = fonte.render(
                f'Pontuação: {pontuacao}', True, branco)
            tela.blit(texto_pontuacao, (10, 10))

            # Atualiza a tela
            pygame.display.flip()
            clock.tick(60)
        elif venceu:
            tela.blit(imagem_vitoria, (0, 0))
            fonte_vitoria = pygame.font.Font(None, 74)
            texto_vitoria = fonte_vitoria.render(
                "VOCÊ VENCEU!", True, amarelo_brilhante)
            tela.blit(texto_vitoria, (largura // 2 -
                      texto_vitoria.get_width() // 2, altura // 2 - 40))

            # Criação do botão "Jogar Novamente"
            botao_reiniciar = pygame.Rect(
                largura // 2 - 100, altura // 2 + 50, 200, 60)
            pygame.draw.rect(tela, branco, botao_reiniciar)
            texto_reiniciar = fonte_vitoria.render(
                "Jogar Novamente", True, preto)
            # Define as dimensões do botão com base no tamanho do texto
            largura_botao = texto_reiniciar.get_width() + 40  # Margem horizontal extra
            altura_botao = texto_reiniciar.get_height() + 20  # Margem vertical extra
            botao_reiniciar = pygame.Rect(
                largura // 2 - largura_botao // 2, altura // 2 + 50, largura_botao, altura_botao)

            # Desenha o botão
            pygame.draw.rect(tela, branco, botao_reiniciar)
            tela.blit(texto_reiniciar, (botao_reiniciar.x + botao_reiniciar.width // 2 - texto_reiniciar.get_width() // 2,
                                        botao_reiniciar.y + botao_reiniciar.height // 2 - texto_reiniciar.get_height() // 2))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_reiniciar.collidepoint(evento.pos):
                    menu_inicial()  # Retorna ao menu inicial

        else:
            # Exibe mensagem de Game Over
            tela.fill(preto)
            tela.blit(game_over_image, (0, 0))
            fonte = pygame.font.Font(None, 74)
            texto_game_over = fonte.render("Game Over", True, branco)
            tela.blit(texto_game_over, (largura // 2 - texto_game_over.get_width() // 2,
                      altura // 2 - texto_game_over.get_height() // 2))

            # Criação do botão "Jogar Novamente"
            fonte_botao = pygame.font.Font(None, 50)
            texto_reiniciar = fonte_botao.render(
                "Jogar Novamente", True, preto)

            # Define as dimensões do botão com base no tamanho do texto
            largura_botao = texto_reiniciar.get_width() + 40  # Margem horizontal extra
            altura_botao = texto_reiniciar.get_height() + 20  # Margem vertical extra
            botao_reiniciar = pygame.Rect(
                largura // 2 - largura_botao // 2, altura // 2 + 50, largura_botao, altura_botao)

            # Desenha o botão
            pygame.draw.rect(tela, branco, botao_reiniciar)
            tela.blit(texto_reiniciar, (botao_reiniciar.x + botao_reiniciar.width // 2 - texto_reiniciar.get_width() // 2,
                                        botao_reiniciar.y + botao_reiniciar.height // 2 - texto_reiniciar.get_height() // 2))

            pygame.display.flip()

            # Verifica eventos para clicar no botão "Jogar Novamente"
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botao_reiniciar.collidepoint(evento.pos):
                        # Reinicia o jogo
                        main()

    pygame.quit()


if __name__ == "__main__":
    main()
    pygame.quit()
