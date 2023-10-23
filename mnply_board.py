import pygame as py


py.init()


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000


screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), py.RESIZABLE)


def board():
    '''
    py.draw.rect(screen, (175, 225, 175), (100, 50, 910, 910))
    py.draw.rect(screen, (0, 0 , 0), (100, 50, 140, 140), 2)
    run = 0
    for i in range(9):
        width = 70
        py.draw.rect(screen, (0, 0, 0), (100, 190+(width * run), 140, 70), 2)
        run = run + 1
    py.draw.rect(screen, (0, 0 , 0), (100, 820, 140, 140), 2)
    run = 0
    for i in range(9):
        width = 70
        py.draw.rect(screen, (0, 0, 0), (240+(width*run), 820, 70, 140), 2)
        run = run + 1
    py.draw.rect(screen, (0, 0, 0), (870, 820, 140, 140), 2)
    run = 0
    for i in range(9):
        width = 70
        py.draw.rect(screen, (0, 0, 0), (870, 750-(width*run), 140, 70), 2)
        run = run + 1
    py.draw.rect(screen, (0, 0, 0), (870, 50, 140, 140), 2)
    run = 0
    for i in range(9):
        width = 70
        py.draw.rect(screen, (0, 0, 0), (240+(width*run), 50, 70, 140), 2)
        run = run + 1
    monopolyIMG = py.image.load('monopolycenter.gif')
    #screen.blit(monopolyIMG, (0, 0))
    mply_scale = py.transform.scale(monopolyIMG, (monopolyIMG.get_width()*0.875, monopolyIMG.get_height()*0.875))
    screen.blit(mply_scale, (140, 210))

    chance_card = py.image.load('chance_card.png')
    screen.blit(chance_card, (500, 490))
    commchest = py.image.load("communitychest.png")
    #commchest_scale = py.transform.scale (commchest,(commchest.get_width()*0.875, commchest.get_height()*0.875))
    screen.blit(commchest, (195, 180))
    '''
    full_board = py.image.load("Streets.png")
    screen.blit(full_board, (-88, 20))
run = True
while run:
    screen.fill((255, 255, 255))
    board()


    for event in py.event.get():
        if event.type == py.QUIT:
            run = False


    py.display.update()


py.quit()


