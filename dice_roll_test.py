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