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
    def __init__(self, x, y, width, height, color, jail):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.jail = jail






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
         
player1 = player(888, 843, 35, 35, (255, 0, 0), 0)
player2 = player(888, 897, 35, 35, (0, 255, 0), 0)
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
while run:
    screen.fill((255, 255, 255))
    board()


    if stamp == False:
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
            if (player1.jail == 0):
                if (188 < player1.x <= 888) and (player1.y == 843):#bottom right to bottom left
                    player1.x -= (70*dice_sum)
                    if player1.x < 188:#if going around bottom left corner
                        player1.y -= 188 - player1.x
                        player1.x = 188
                elif (player1.x == 188) and (143 < player1.y <= 843):#bottom left to top left
                    player1.y -= (70*dice_sum)
                    if player1.y < 143:#if going around top left corner
                        player1.x += 143 - player1.y
                        player1.y = 143
                elif (188 <= player1.x < 888) and (player1.y == 143):#top left to top right
                    player1.x += (70*dice_sum)
                    if player1.x > 888:#if going around top right corner
                        player1.y += player1.x - 888
                        player1.x = 888
                elif (player1.x == 888) and (143 <= player1.y < 843):#top right to bottom right
                    player1.y += (70*dice_sum)
                    if player1.y > 843:#if going around bottom right corner
                        player1.x -= player1.y - 843
                        player1.y = 843
                player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail)
                turn += 1#making it next person's turn
            else:
                turn += 1 #next person's turn
        else:
            if (player2.jail == 0):
                if (188 < player2.x <= 888) and (840 <= player2.y <= 960):#bottom right to bottom left
                    player2.x -= (70*dice_sum)
                    if player2.x < 188:#if going around bottom left corner
                        player2.y = 843
                        player2.y -= 188 - player2.x
                        player2.x = 118
                    if (100 <= player2.x <= 240) and (820 <= player2.y <= 960):#if reaching bottom left corner
                        player2.x = 118
                        player2.y = 843
                elif (100 <= player2.x <= 240) and (197 < player2.y <= 897):#bottom left to top left
                    player2.y -= (70*dice_sum)
                    if player2.y < 143:#if going around top left corner
                        player2.x = 188
                        player2.x += 143 - player2.y
                        player2.y = 73
                    if (100 <= player2.x <= 240)and (50 <= player2.y <= 190):#if reaching top left corner
                        player2.x = 188
                        player2.y = 73
                elif (118 <= player2.x < 888) and (50 <= player2.y <= 190):#top left to top right
                    player2.x += (70*dice_sum)
                    if player2.x > 888:#if going around top right corner
                        player2.y = 143
                        player2.y += player2.x - 888
                        player2.x = 958
                    if (870 <= player2.x <= 1010) and (50 <= player2.y <= 290):#if reaching top right corner
                        player2.x = 958
                        player2.y = 143
                elif (870 <= player2.x <= 1010) and (143 <= player2.y < 897):#top right to bottom right
                    player2.y += (70*dice_sum)
                    if player2.y > 843:#if going around bottom right corner
                        player2.x = 888
                        player2.x -= player2.y - 843
                        player2.y = 897
                    if (870 <= player2.x <= 1010) and (820 <= player2.y <= 960):#if reaching bottom right corner
                        player2.x = 888
                        player2.y = 897
                player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail)
                turn += 1#making it next person's turn
            else:
                turn += 1#making it next person's turn


        if (870 < player1.x < 1010) and (50< player1.y <190):
            player1.jail = 1
            player1.x = 188
            player1.y = 843
            player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail)
        if (870 < player2.x < 1010) and (50< player2.y <190):
            player2.jail = 1
            player2.x = 118
            player2.y = 843
            player2 = player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail)
           
       


    if endturn.draw(screen):
        end_turn = 0
        if (player1.jail != 0) and (turn & 2 == 0):
            if (player1.jail == 1):
                player1.jail += 1        
            if (player1.jail == 5):
                player1.jail = 0
            else:
                if N == A:
                    player1.jail = 0
                else:
                    player1.jail += 1
       
        if (player2.jail != 0) and (turn % 2 == 1):
            if (player2.jail == 1):
                player2.jail += 1
            if (player2.jail == 5):
                player2.jail = 0
            else:  
                if N == A:
                    player2.jail = 0
                else:
                    player2.jail += 1




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