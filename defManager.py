def mousePosition():
    """Returns mouse position"""
    return pygame.mouse.get_pos()

def drawEnemy(enemy_list, index, index_speed, enemy_xspeed, enemy_yspeed, position):
    """Draws enemy given list, speed at which it draws it, x and y speed, and position"""
    position[0] = position[0] + enemy_xspeed
    position[1] = position[1] + enemy_yspeed
    index[0] = index[0] + index_speed
    if int(index[0]) == len(enemy_list):
        index[0] = 0
    if type(index[0]) == int:
        screen.blit(enemy_list[index[0]], position)
    else:
        screen.blit(enemy_list[int(index[0])], position)

def drawMenu(list, index, index_speed, position):
    """Draws menu background as a sprite"""
    index[0] = index[0] + index_speed
    if int(index[0]) == len(list):
        index[0] = 0
    if type(index[0]) == int:
        screen.blit(list[index[0]], position)
    else:
        screen.blit(list[int(index[0])], position)

def menuSFX():
    """Plays background music"""
    pygame.mixer.music.load('sfx/menu_sfx.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

def menuButton(button1, button2, button3, button4):
    """Draws buttons for menu screen"""
    screen.blit(button1, [0,0] )
    screen.blit(button2, [0,0] )
    screen.blit(button3, [0,0] )
    screen.blit(button4, [0,0] )

def resetEnemy(enemy_list, x1, x2, y1, y2):
    """Sets new x and y given range for enemy in enemy list"""
    enemy_list[i][0] = random.randint(x1, x2) # Sets new x of enemy
    enemy_list[i][1] = random.randint(y1, y2) # Sets new y of enemy

