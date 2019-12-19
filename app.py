# importando a lib do pygame
import pygame
# inicindo pygame
pygame.init()

# variavéis para movimentação do objeto
# devem ser declaradas antes do loop do jogo
x= 400
y = 300
velocidade = 15
# definindo imagens de fundo e imagem do objeto
fundo = pygame.image.load('imagens/bosque.png')
mercenario_direita = pygame.image.load('imagens/mercenario-direita.png')
mercenario_esquerda = pygame.image.load('imagens/mercenario-esquerda.png')
mercenario_pos = mercenario_direita

# definindo janela e salvando em uma variável
janela = pygame.display.set_mode((800,600))
# definindo nome que aparece na janela
pygame.display.set_caption("POC do PyGame")

# definindo loop para que a janela não feche até que o usuário faça manualmente
# aparentemente o jogo deve ser desenvolvido dentro desse loop 
janela_aberta = True
while janela_aberta:
    # estipulando delay de atualização da tela. Aparentemente essa atualização não pode ser muito rápida
    pygame.time.delay(50)

    # for que pega todos os eventos do pygame, incluindo o evento de fechar janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        
        # trecho para trocar foto do personagem de acordo com sua direção
        # usei o mesmo trecho que estipula dos comando de movimentação do teclado
        # por estar dentro do 'for' de eventos, se comporta de forma diferente do trecho de movimentação
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]:
            mercenario_pos = mercenario_direita
        if comandos[pygame.K_LEFT]:
            mercenario_pos = mercenario_esquerda
        
    # Estipulando comandos para movimentação com teclado. Deve estar fora do 'for' para
    # permitir que o objeto se movimento ao manter o botão pressionado
    '''
    O eixo x,y començam no canto superior esquerdo da tela. Com isso, decremente y para subir
    e incremente y para descer, já que o objeto está no meio da tela. 
    Para esquerda: decremente x. Para direita: incremente x. 
    '''
    
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade

    # comando para preencher a tela com o fundo, evitando que o objeto deixe rastros
    janela.blit(fundo, (0, 0))
    # desenhando objeto na tela
    # os parâmetros são: variável com imagem do objeto; posição na tela
    janela.blit(mercenario_pos, (x, y))
    # realizando o update na tela para mostrar objeto
    pygame.display.update()

pygame.quit()