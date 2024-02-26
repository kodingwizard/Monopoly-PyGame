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
    def __init__(self, x, y, width, height, color, jail, money, jailfree, orbit):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.jail = jail
        self.money = money
        self.jailfree = jailfree
        self.orbit = orbit

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

def playerinfo():
    global font1, p1text, p1textRect, p1text1, p1textRect1, p2text, p2textRect, p2text1, p2textRect1
    font1 = py.font.Font('freesansbold.ttf', 16)
    p1text = font1.render("Player 1's Money: " + str(player1.money), True, (0, 0, 0), (255, 255, 255))
    p1textRect = py.draw.rect(screen, (255,255,255), (1040, 700, 140, 140))
    p1text1 = font1.render("Player 1's Jail Free Cards: " + str(player1.jailfree), True, (0, 0, 0), (255, 255, 255))
    p1textRect1 = py.draw.rect(screen, (255,255,255), (1040, 750, 140, 140))
    p2text = font1.render("Player 2's Money: " + str(player2.money), True, (0, 0, 0), (255, 255, 255))
    p2textRect = py.draw.rect(screen, (255,255,255), (1040, 800, 140, 140))
    p2text1 = font1.render("Player 2's Jail Free Cards: " + str(player2.jailfree), True, (0, 0, 0), (255, 255, 255))
    p2textRect1 = py.draw.rect(screen, (255,255,255), (1040, 850, 140, 140))
    



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
         
player1 = player(888, 843, 35, 35, (255, 0, 0), 0, 1500, 0, 0)
player2 = player(888, 897, 35, 35, (0, 255, 0), 0, 1500, 0, 0)
font = py.font.Font('freesansbold.ttf', 32)
dice_button_text = font.render("Roll the Dice", True, (0, 0, 0), (215, 215, 215))
dbt_Rect = py.draw.rect(screen, (215, 215, 215), (1050, 330, 140, 140))
dicebutton = button(1050, 300, 200, 100, (215, 215, 215))
endturn = button(1050, 500, 200, 100, (215, 215, 215))
etb_rect = py.draw.rect(screen, (215, 215, 215), (1050, 530, 140, 140))
etb_text = font.render("End Turn", True, (0, 0, 0), (215, 215, 215))
font1 = py.font.Font('freesansbold.ttf', 16)
p1text = font1.render("Player 1's Money: " + str(player1.money), True, (0, 0, 0), (255, 255, 255))
p1textRect = py.draw.rect(screen, (255,255,255), (1040, 700, 140, 140))
p1text1 = font1.render("Player 1's Jail Free Cards: " + str(player1.jailfree), True, (0, 0, 0), (255, 255, 255))
p1textRect1 = py.draw.rect(screen, (255,255,255), (1040, 750, 140, 140))
p2text = font1.render("Player 2's Money: " + str(player2.money), True, (0, 0, 0), (255, 255, 255))
p2textRect = py.draw.rect(screen, (255,255,255), (1040, 800, 140, 140))
p2text1 = font1.render("Player 2's Jail Free Cards: " + str(player2.jailfree), True, (0, 0, 0), (255, 255, 255))
p2textRect1 = py.draw.rect(screen, (255,255,255), (1040, 850, 140, 140))


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
            player1.orbit += dice_sum * 70
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
                player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
                turn += 1#making it next person's turn
            else:
                turn += 1 #next person's turn
        else:
            player2.orbit += dice_sum * 70
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
                player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)
                turn += 1#making it next person's turn
            else:
                turn += 1#making it next person's turn

            if (870 < player1.x < 1010) and (50< player1.y <190):
                player1.jail = 1
                player1.x = 188
                player1.y = 843
                player1.orbit = 700
                player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
            if (870 < player2.x < 1010) and (50< player2.y <190):
                player2.jail = 1
                player2.x = 118
                player2.y = 843
                player2.orbit = 700
                player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)
        
        if player1.orbit >= 2800:
            player1.money += 200
            player1.orbit = (888 - player1.x) + (843 - player1.y)
            player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
        if player2.orbit >= 2800:
            player2.money += 200
            player2.orbit = (888 - player2.x) + (843 - player2.y)
            player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)


    from communitycard import * 
    comcardp1()
    comcardp2()
    from chancecard import *
    chancecardp1()
    chancecardp2()

    def p1buttons(purchase, revamp, rent, mecontrol, theycontrol):
        font = py.font.Font('freesansbold.ttf', 24)
        if theycontrol != 0:
            player1.money -= rent * theycontrol
            player2.money += rent * theycontrol
        else:
            if mecontrol == 0:
                buyButton = button(400, 800, 100, 30, (0, 255, 0))
                buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 800, 100, 30))
                buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= purchase
                    global end_turn
                    end_turn = 2
                    mecontrol += 1
                screen.blit(buy, buy_rect)
            if mecontrol != 0:
                upgradeButton = button(400, 800, 100, 30, (0, 255, 0))
                upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 800, 100, 30))
                upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
                if upgradeButton.draw(screen) and (mecontrol < 5):
                    player2.money -= revamp
                    mecontrol += 1
                    end_turn = 2
                screen.blit(upgrade, upgrade_rect)
            closeButton = button(620, 800, 100, 30, (255, 0, 0))
            close_rect = py.draw.rect(screen, (0, 255, 0), (620, 800, 100, 30))
            close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
            screen.blit(close, close_rect)
            if closeButton.draw(screen):
                end_turn = 2
            screen.blit(close, close_rect)

    def p2buttons(buynum, upgradenum, tribute, meown, theyown):
        font = py.font.Font('freesansbold.ttf', 24)
        if theyown != 0:
            player2.money -= tribute * theyown
            player1.money += tribute * theyown
        else:
            if meown == 0:
                buyButton = button(400, 800, 100, 30, (0, 255, 0))
                buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 800, 100, 30))
                buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= buynum
                    global end_turn
                    end_turn = 2
                    meown += 1
                screen.blit(buy, buy_rect)
            if meown != 0:
                upgradeButton = button(400, 800, 100, 30, (0, 255, 0))
                upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 800, 100, 30))
                upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
                if upgradeButton.draw(screen) and (meown < 5):
                    player2.money -= upgradenum
                    meown += 1
                    end_turn = 2
                screen.blit(upgrade, upgrade_rect)
            closeButton = button(620, 800, 100, 30, (255, 0, 0))
            close_rect = py.draw.rect(screen, (0, 255, 0), (620, 800, 100, 30))
            close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
            screen.blit(close, close_rect)
            if closeButton.draw(screen):
                end_turn = 2
            screen.blit(close, close_rect)

    from propertycards import *
    propcardsp1()
    propcardsp2()

#win condition
    if player1.money <= 0:
        font = py.font.Font('freesansbold.ttf', 24)
        wintext1_rect = py.draw.rect(screen, (0, 0, 0), (0, 0, 2000, 2000))
        wintext1 = font.render("Player 2 wins!", True, (255, 255, 255), (0, 0, 0))
        screen.blit(wintext1, wintext1_rect)

    elif player2.money <= 0:
        font = py.font.Font('freesansbold.ttf', 24)
        wintext2_rect = py.draw.rect(screen, (0, 0, 0), (0, 0, 2000, 2000))
        wintext2 = font.render("Player 1 wins!", True, (255, 255, 255), (0, 0, 0))
        screen.blit(wintext2, wintext2_rect)

     

    if endturn.draw(screen):
        print(end_turn)
        end_turn = 0
        if (player1.jail != 0) and (turn & 2 == 0):
            if (player1.jail == 1):
                if (player1.jailfree != 0):
                    font = py.font.Font('freesansbold.ttf', 32)
                    jailfreetext = font.render("Use JAILFREECARD", True, (0, 0, 0), (215, 215, 215))
                    jf_Rect = py.draw.rect(screen, (215, 215, 215), (325, 375, 200, 60))
                    jailfreebutton = button(325, 375, 200, 60, (215, 215, 215))
                    if jailfreebutton.draw(screen):
                        player1.jail = 0
                        player1.jailfree -= 1
                    screen.blit(jailfreetext, jf_Rect)
                else:
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
                if (player1.jailfree != 0):
                    font = py.font.Font('freesansbold.ttf', 32)
                    jailfreetext = font.render("Use JAILFREECARD", True, (0, 0, 0), (215, 215, 215))
                    jf_Rect = py.draw.rect(screen, (215, 215, 215), (325, 375, 200, 60))
                    jailfreebutton = button(325, 375, 200, 60, (215, 215, 215))
                    if jailfreebutton.draw(screen):
                        player2.jail = 0
                        player2.jailfree -= 1
                    screen.blit(jailfreetext, jf_Rect)
                else:
                    player2.jail += 1    
                player2.jail += 1
            if (player2.jail == 5):
                player2.jail = 0
            else:  
                if N == A:
                    player2.jail = 0
                else:
                    player2.jail += 1
        print(player1.money)
        print(player2.money)


    if stamp == True:
        screen.blit(text, textRect)
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
    screen.blit(dice_button_text, dbt_Rect)
    screen.blit(etb_text, etb_rect)
    playerinfo()
    screen.blit(p1text, p1textRect)
    screen.blit(p1text1, p1textRect1)
    screen.blit(p2text, p2textRect)
    screen.blit(p2text1, p2textRect1)


    player1.draw(screen)
    player2.draw(screen)
    py.display.update()


py.quit()