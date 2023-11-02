import pygame as py
import random

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

class player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)


    def draw(self, win):
        py.draw.rect(win, self.color, self.rect)

def diceroll():

	Diceroll = [ ]
	for i in range (1):
		global N
		N = random.randint(1,6)
		global A
		A = random.randint(1,6)

		Diceroll.append(N)
		Diceroll.append(A)
	print(Diceroll)
	global dice_sum
	dice_sum = N + A
	print("Total: %s" %dice_sum)
	if dice_sum < 10:
		print("yay no taxes")

	else:
		print("rip taxes")
diceroll()


def dicetext():      
    global font, text, textRect, text1, textRect1, text2, textRect2, text3, textRect3
    font = py.font.Font('freesansbold.ttf', 32)
    text = font.render(str(N), True, (0, 0, 0), (255, 255, 255))
    textRect = py.draw.rect(screen, (255,255,255), (1160, 50, 140, 140))
    text1 = font.render(str(A), True, (0, 0, 0), (255, 255, 255))
    textRect1 = py.draw.rect(screen, (255,255,255), (1100, 50, 140, 140))
    text2 = font.render('Total: ' + str(dice_sum), True, (0, 0, 0), (255, 255, 255))
    textRect2 = py.draw.rect(screen, (255,255,255), (1050, 150, 140, 140))
    if dice_sum < 10:
        text3 = font.render('yay no taxes', True, (0, 0, 0), (255, 255, 255))
        textRect3 = py.draw.rect(screen, (255,255,255), (1050, 200, 140, 100))
    else:
        text3 = font.render('rip taxes', True, (0, 0, 0), (255, 255, 255))
        textRect3 = py.draw.rect(screen, (255,255,255), (1050, 200, 140, 100))

class button():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.clicked = False

    def draw(self, win):
        action = False
        py.draw.rect(win, self.color, self.rect)
        posx, posy = py.mouse.get_pos()
        click = py.mouse.get_pressed()
        if (self.x < posx < self.x+200) and (self.y < posy < self.y+200):
            if (click[0] == 1) and (self.clicked == False):
                self.clicked = True
                action = True
            if click[0] == 0:
                self.clicked = False


        return action
         
player1posx = 923
player2posx = 923
player1posy = 843
player2posy = 897
player1 = player(player1posx, player1posy, 35, 35, (255, 0, 0))
player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
font = py.font.Font('freesansbold.ttf', 32)
dice_button_text = font.render("Roll the Dice", True, (0, 0, 0), (215, 215, 215))
dbt_Rect = py.draw.rect(screen, (215, 215, 215), (1050, 330, 140, 140))
dicebutton = button(1050, 300, 200, 100, (215, 215, 215))




stamp = False
run = True
while run:
    screen.fill((255, 255, 255))
    board()


    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        
    player1.draw(screen)
    player2.draw(screen)
    
    if dicebutton.draw(screen):
        diceroll()
        dicetext()
        stamp = True
           

    if stamp == True:
        screen.blit(text, textRect)
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
    screen.blit(dice_button_text, dbt_Rect)
    py.display.update()



py.quit()


