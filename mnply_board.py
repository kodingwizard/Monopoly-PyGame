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
    #monopolyIMG = py.image.load('monopolycenter.gif')
    #screen.blit(monopolyIMG, (0, 0))
    #mply_scale = py.transform.scale(monopolyIMG, (monopolyIMG.get_width()*0.875, monopolyIMG.get_height()*0.875))
    #screen.blit(mply_scale, (140, 210))

    #chance_card = py.image.load('chance_card.png')
    #screen.blit(chance_card, (500, 490))
    #commchest = py.image.load("communitychest.png")
    #commchest_scale = py.transform.scale (commchest,(commchest.get_width()*0.875, commchest.get_height()*0.875))
    #screen.blit(commchest, (195, 180))
    '''
    full_board = py.image.load("Streets.png")
    full_board_scale = py.transform.scale(full_board, (full_board.get_width()*1, full_board.get_height()*0.99))
    screen.blit(full_board_scale, (-88, 50))

class player(): 
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.jail = 0



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
         
player1posx = 888
player2posx = 888
player1posy = 843
player2posy = 897
player1 = player(player1posx, player1posy, 35, 35, (255, 0, 0))
player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
font = py.font.Font('freesansbold.ttf', 32)
dice_button_text = font.render("Roll the Dice", True, (0, 0, 0), (215, 215, 215))
dbt_Rect = py.draw.rect(screen, (215, 215, 215), (1050, 330, 140, 140))
dicebutton = button(1050, 300, 200, 100, (215, 215, 215))
endturn = button(1050, 500, 200, 100, (215, 215, 215))
etb_rect = py.draw.rect(screen, (215, 215, 215), (1050, 530, 140, 140))
etb_text = font.render("End Turn", True, (0, 0, 0), (215, 215, 215))




turn = 1
stamp = False
run = True
end_turn = 0
jailcheckerp1 = 0
jailcheckerp2 = 0
while run:
    screen.fill((255, 255, 255))
    board()


    player1.draw(screen)
    player2.draw(screen)


    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
       

    if dicebutton.draw(screen) and (end_turn == 0):
        diceroll()
        dicetext()
        stamp = True
        end_turn = 1
        if (turn % 2 == 1):#see if it is player one's turn
            if (jailcheckerp1 == 0):
                if (188 < player1posx <= 888) and (player1posy == 843):#bottom right to bottom left
                    player1posx -= (70*dice_sum)
                    if player1posx < 188:#if going around bottom left corner
                        player1posy -= 188 - player1posx
                        player1posx = 188
                        player1 = player(player1posx, player1posy, 35, 35, (255, 0, 0))
                    else:#normal movement
                        player1 = player(player1posx, player1posy, 35, 35, (255, 0, 0))
                elif (player1posx == 188) and (143 < player1posy <= 843):#bottom left to top left
                    player1posy -= (70*dice_sum)
                    if player1posy < 143:#if going around top left corner
                        player1posx += 143 - player1posy
                        player1posy = 143
                        player1 = player(player1posx, player1posy, 35, 35, (255, 0, 0))
                    else:#normal movement
                        player1 = player(player1posx, player1posy, 35, 35, (255, 0, 0))
                elif (188 <= player1posx < 888) and (player1posy == 143):#top left to top right
                    player1posx += (70*dice_sum)
                    if player1posx > 888:#if going around top right corner
                        player1posy += player1posx - 888
                        player1posx = 888
                        player1 = player(player1posx, player1posy, 35, 35, (255, 0, 0))
                    else:#normal movement
                        player1 = player(player1posx, player1posy, 35, 35, (255, 0, 0))
                elif (player1posx == 888) and (143 <= player1posy < 843):#top right to bottom right
                    player1posy += (70*dice_sum)
                    if player1posy > 843:#if going around bottom right corner
                        player1posx -= player1posy - 843
                        player1posy = 843
                        player1 = player(player1posx, player1posy, 35, 35, (255, 0, 0))
                    else:#normal movement
                        player1 = player(player1posx, player1posy, 35, 35, (255, 0, 0))
                turn += 1#making it next person's turn
            else:
                turn += 1 #next person's turn
        else:
            if (jailcheckerp2 == 0):
                if (188 < player2posx <= 888) and (840 <= player2posy <= 960):#bottom right to bottom left
                    player2posx -= (70*dice_sum)
                    if player2posx < 188:#if going around bottom left corner
                        player2posy = 843
                        player2posy -= 188 - player2posx
                        player2posx = 118
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                    if (100 <= player2posx <= 240) and (820 <= player2posy <= 960):#if reaching bottom left corner
                        player2posx = 118
                        player2posy = 843
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                    else: #normal movement
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                elif (100 <= player2posx <= 240) and (197 < player2posy <= 897):#bottom left to top left
                    player2posy -= (70*dice_sum)
                    if player2posy < 143:#if going around top left corner
                        player2posx = 188
                        player2posx += 143 - player2posy
                        player2posy = 73
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                    if (100 <= player2posx <= 240)and (50 <= player2posy <= 190):#if reaching top left corner
                        player2posx = 188
                        player2posy = 73
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                    else:#normal movement
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                elif (118 <= player2posx < 888) and (50 <= player2posy <= 190):#top left to top right
                    player2posx += (70*dice_sum)
                    if player2posx > 888:#if going around top right corner
                        player2posy = 143
                        player2posy += player2posx - 888
                        player2posx = 958
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                    if (870 <= player2posx <= 1010) and (50 <= player2posy <= 290):#if reaching top right corner
                        player2posx = 958
                        player2posy = 143
                        player2 = player(player2posx, player2posy, 35, 35,(0, 255, 0))
                    else:
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                elif (870 <= player2posx <= 1010) and (143 <= player2posy < 897):#top right to bottom right
                    player2posy += (70*dice_sum)
                    if player2posy > 843:#if going around bottom right corner
                        player2posx = 888
                        player2posx -= player2posy - 843
                        player2posy = 897
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                    if (870 <= player2posx <= 1010) and (820 <= player2posy <= 960):#if reaching bottom right corner
                        player2posx = 888
                        player2posy = 897
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                    else:#normal movement
                        player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
                turn += 1#making it next person's turn
            else:
                turn += 1#making it next person's turn
        #print(jailcheckerp1)
        #print(jailcheckerp2)

        if (870 < player1posx < 1010) and (50< player1posy <190):
            jailcheckerp1 = 1
            player1posx = 188
            player1posy = 843
            player1 = player(player1posx, player2posx, 35, 35, (255, 0, 0))
        if (870 < player2posx < 1010) and (50< player2posy <190):
            jailcheckerp2 = 1
            player2posx = 118
            player2posy = 843
            player2 = player(player2posx, player2posy, 35, 35, (0, 255, 0))
        

    if endturn.draw(screen):
        end_turn = 0
        if (jailcheckerp1 != 0) and (turn & 2 == 0):
            if (jailcheckerp1 == 1):
                jailcheckerp1 += 1         
            if (jailcheckerp1 == 5):
                jailcheckerp1 = 0
            else:
                if N == A:
                    jailcheckerp1 = 0
                else:
                    jailcheckerp1 += 1
        
        if (jailcheckerp2 != 0) and (turn % 2 == 1):
            if (jailcheckerp2 == 1):
                jailcheckerp2 += 1
            if (jailcheckerp2 == 5):
                jailcheckerp2 = 0
            else:   
                if N == A:
                    jailcheckerp2 = 0
                else:
                    jailcheckerp2 += 1


    if stamp == True:
        screen.blit(text, textRect)
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
    screen.blit(dice_button_text, dbt_Rect)
    screen.blit(etb_text, etb_rect)

    player1.draw(screen)
    player2.draw(screen)
    py.display.update()




py.quit()


