# Import modules & config required to run the game with full functionality
import pygame
#import pygame
import math
import os
import time
import random

# This allows the game client to launch at a certain location within the user's screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (25,35)
execfile ("defManager.py")

# Set colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

# Initializes pygame, clock, and cursor
pygame.init()
clock = pygame.time.Clock()
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

done = False
# Set booleans for each screen in game
menu_Shown = True
game_Shown = False
settings_Shown = False
credits_Shown = False
end_Shown = False

# Set screen, icon, and load static images
size = (900, 675)
screen = pygame.display.set_mode(size) # Set screen + screen size
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon) # Set icon
pygame.display.set_caption("Fire Fight")
game_background = pygame.image.load("img/gamebackground2.png").convert() # Game background image
menu_logo = pygame.image.load("img/logo.png")
play_button = pygame.image.load("img/playbutton.png")
settings_button = pygame.image.load("img/settingsbutton.png")
credits_button = pygame.image.load("img/creditsbutton.png")
quit_button = pygame.image.load("img/quitbutton.png")
play_button_press = pygame.image.load("img/playbuttonpress.png")
settings_button_press = pygame.image.load("img/settingsbuttonpress.png")
credits_button_press = pygame.image.load("img/creditsbuttonpress.png")
quit_button_press = pygame.image.load("img/quitbuttonpress.png")
castle = pygame.image.load("img/gamesprites/castlenew.png")
health_bar = pygame.image.load("img/healthbar.png")
credit_name = pygame.image.load("img/credit.png")
back_button = pygame.image.load("img/back.png")
back_button_press = pygame.image.load("img/backpressed.png")
end = pygame.image.load("img/scorepage.png")

# Set empty lists for animated sprites/backgrounds and index variables
menu_images = []
menu_i = [0]

werewolf_walk_sprites = []
werewolf_attack_sprites = []
werewolf_walk_list = []
werewolf_attack_list = []
werewolf_i = [0]

skeleton_walk_sprites = []
skeleton_attack_sprites = []
skeleton_walk_list = []
skeleton_attack_list = []
skeleton_i = [0]

raven_walk_sprites = []
raven_walk_list = []
raven_attack_list = []
raven_i = [0]

# Load image sprites and append to their appropriate lists
for i in range(33, 37):
    werewolf_walk_sprites.append(pygame.image.load("img/gamesprites/"+str(i)+".png"))
for i in range(23, 29):
    werewolf_attack_sprites.append(pygame.image.load("img/gamesprites/"+str(i)+".png"))
for i in range(14, 19):
    raven_walk_sprites.append(pygame.image.load("img/gamesprites/"+str(i)+".png"))
for i in range(29, 33):
    skeleton_walk_sprites.append(pygame.image.load("img/gamesprites/"+str(i)+".png"))
for i in range(37,41):
    skeleton_attack_sprites.append(pygame.image.load("img/gamesprites/"+str(i)+".png"))
for i in range(1, 9):
    menu_images.append(pygame.image.load("img/newmenubackground/menu ("+str(i)+").png"))
    #menu_image_resize = pygame.transform.scale(menu_image_fetch, (900,675))
    #menu_images.append(menu_image_resize)

# Set starting position for each enemy, set number of WALKING enemies
for i in range(18): # Number of walking werewolfs
    xx = random.randrange(-1800, -50)
    yy = random.randrange(250, 525)
    werewolf_walk_list.append([xx, yy])

for i in range(5): # Number of walking ravens
    xx = random.randrange(-1800, -50)
    yy = random.randrange(200, 250)
    raven_walk_list.append([xx, yy])

for i in range(15): # Number of walking skeletors
    xx = random.randrange(-1800, -50)
    yy = random.randrange(250, 525)
    skeleton_walk_list.append([xx, yy])

# Set starting variables
mouseClick = [0,0]
health = 10000 # Starting health
step = 0
splash = 5 # Set splash radius for damaging enemies
score = 0 # Starting score
score_label = "Score:"

# Play background music
menuSFX()

##################################################################################################################################
# MAIN LOOP
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.constants.USEREVENT and menu_Shown == True:
            pygame.mixer.music.play()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseClick = mousePosition()

    mouse = mousePosition()
##################################################################################################################################
    # MAIN MENU LOOP
    if menu_Shown:
        # Draws menu background, menu logo
        drawMenu(menu_images, menu_i, 0.8, [-25,0])
        screen.blit(menu_logo, [0,0] )

        # Calculates whether mouse is HOVERING over button, blits darkened button if true
        if 43+165 > mouse[0] > 43 and 431+42 > mouse[1] > 431: # Play button hover
            menuButton(play_button_press, settings_button, credits_button, quit_button)
        elif 40+194 > mouse[0] > 40 and 492+25 > mouse[1] > 492: # Settings button hover
            menuButton(play_button, settings_button_press, credits_button, quit_button)
        elif 40+168 > mouse[0] > 40 and 535+25 > mouse[1] > 535: # Credits button hover
            menuButton(play_button, settings_button, credits_button_press, quit_button)
        elif 41+95 > mouse[0] > 41 and 578+32 > mouse[1] > 578: # Quit button hover
            menuButton(play_button, settings_button, credits_button, quit_button_press)
        else:
            menuButton(play_button, settings_button, credits_button, quit_button)

        # Calculates whether mouse CLICKED on button, opens appropriate screen if true
        if 43+165 > mouseClick[0] > 43 and 431+42 > mouseClick[1] > 431: # Play button click
            pygame.mixer.music.stop()
            menu_Shown = False
            game_Shown = True

        elif 40+168 > mouseClick[0] > 40 and 535+25 > mouseClick[1] > 535: # Credits button click
            credits_Shown = True
            menu_Shown = False
        elif 41+95 > mouseClick[0] > 41 and 578+32 > mouseClick[1] > 578: # Quit button click
            done = True
##################################################################################################################################
    # SETTINGS LOOP
    if settings_Shown:
        screen.fill(WHITE)
        drawMenu(menu_images, menu_i, 0.27, [-25,0])
        if 706+168 > mouse[0] > 706 and 606+42 > mouse[1] > 606: # Back button hover
            screen.blit(back_button_press, [0,0])
        else:
            screen.blit(back_button, [0,0])
        if 706+168 > mouseClick[0] > 706 and 606+42 > mouseClick[1] > 606:
            settings_Shown = False
            menu_Shown = True
##################################################################################################################################
    # CREDITS LOOP
    if credits_Shown:
        screen.fill(RED)
        drawMenu(menu_images, menu_i, 0.27, [-25,0])
        if 706+168 > mouse[0] > 706 and 606+42 > mouse[1] > 606: # Back button hover
            screen.blit(back_button_press, [0,0])
        else:
            screen.blit(back_button, [0,0])
        screen.blit(credit_name, [0,0] )
        if 706+168 > mouseClick[0] > 706 and 606+42 > mouseClick[1] > 606:
            credits_Shown = False
            menu_Shown = True
##################################################################################################################################
    # MAIN GAME LOOP
    if game_Shown:
        # Draws background and empty health bar
        screen.blit(game_background, [0,0])
        screen.blit(health_bar, [0,0])

        # Draws FPS counter
        font = pygame.font.Font(None,30)
        fps_counter = clock.get_fps()
        fps = font.render(format(fps_counter,".0f"), True,GREEN)
        screen.blit(fps, [0,0] )
        score_counter = font.render(format(score,".0f"), True,WHITE)
        score_blit_label = font.render(format(score_label), True,WHITE)
        screen.blit(score_counter, [750,22] )
        screen.blit(score_blit_label, [650,20] )

#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
        # Werewolf walking loop
        for i in range(len(werewolf_walk_list)):
            drawEnemy(werewolf_walk_sprites, werewolf_i, 0.008, 2, 0, werewolf_walk_list[i])
            werewolf_walk_x = werewolf_walk_list[i][0]
            werewolf_walk_y = werewolf_walk_list[i][1]
            # Resets enemy when at castle, appens to attack list, resets if clicked on
            if werewolf_walk_x > 810:
                resetEnemy(werewolf_walk_list, -1800, -50, 250, 525)
                werewolf_attack_list.append([810, werewolf_walk_y])
            elif werewolf_walk_x+35+splash > mouseClick[0] > werewolf_walk_x-splash and werewolf_walk_y+44+splash > mouseClick[1] > werewolf_walk_y-splash: # Hitbox for werewolf walking
                resetEnemy(werewolf_walk_list, -1800, -50, 250, 525)
                score += 1
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
        enemy_attacking_Num = 0 # Fixes bug where health bar drops with no enemies, sets back to zero each tick
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
        # Werewolf attacking loop
        for i in range(len(werewolf_attack_list)):
            drawEnemy(werewolf_attack_sprites, werewolf_i, 0, 0, 0, werewolf_attack_list[i])
            werewolf_attack_x = 810
            werewolf_attack_y = werewolf_attack_list[i][1]
            # Resets enemy if clicked on
            if werewolf_attack_x+40+splash > mouseClick[0] > werewolf_attack_x-splash and werewolf_attack_y+54+splash > mouseClick[1] > werewolf_attack_y-splash: # Hitbox for werewolf attacking
                resetEnemy(werewolf_attack_list, -50, -50, 0, 0)
                score += 1
            # If werewolf enemy is at x=810, add it's damage multiplier to enemies attacking
            if werewolf_attack_list[i][0] == 810:
                enemy_attacking_Num += 7
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
        # Raven walking loop
        for i in range(len(raven_walk_list)):
            # Calculates y position to make raven move up and down
            yPos = -1 * math.sin(step) * 2
            step += 0.01
            drawEnemy(raven_walk_sprites, raven_i, 0.03, 2.5, yPos, raven_walk_list[i])
            raven_walk_x = raven_walk_list[i][0]
            raven_walk_y = raven_walk_list[i][1]

            # Resets enemy when at castle, appens to attack list, resets if clicked on
            if raven_walk_x > 810:
                resetEnemy(raven_walk_list, -1800, -50, 200, 250)
                raven_attack_list.append([810, raven_walk_y])
            elif raven_walk_x+32+splash > mouseClick[0] > raven_walk_x-splash and raven_walk_y+42+splash > mouseClick[1] > raven_walk_y+5-splash: # Hitbox for walking raven
                resetEnemy(raven_walk_list, -1800, -50, 200, 250)
                score += 1
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
        # Raven attacking loop
        for i in range(len(raven_attack_list)):
            drawEnemy(raven_walk_sprites, raven_i, 0, 0, 0, raven_attack_list[i])
            raven_attack_x = 810
            raven_attack_y = raven_attack_list[i][1]

            # Resets enemy if clicked on
            if raven_attack_x+32+splash > mouseClick[0] > raven_attack_x-splash and raven_attack_y+42+splash > mouseClick[1] > raven_attack_y-splash: # Hitbox for attacking
                resetEnemy(raven_attack_list, -1800, -50, 200, 250) # Reset if clicked on
                score += 1
            # If raven enemy is at x=810, add it's damage multiplier to enemies attacking
            if raven_attack_list[i][0] == 810:
                enemy_attacking_Num += 4
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
        # Skeleton walking loop
        for i in range(len(skeleton_walk_list)):
            drawEnemy(skeleton_walk_sprites, skeleton_i, 0.008, 3.5, 0, skeleton_walk_list[i])
            skeleton_walk_x = skeleton_walk_list[i][0]
            skeleton_walk_y = skeleton_walk_list[i][1]
            # Resets enemy when at castle, appens to attack list, resets if clicked on
            if skeleton_walk_x > 820:
                resetEnemy(skeleton_walk_list, -1800, -50, 250, 525)
                skeleton_attack_list.append([820, skeleton_walk_y])
            elif skeleton_walk_x+35+splash > mouseClick[0] > skeleton_walk_x-splash and skeleton_walk_y+44+splash > mouseClick[1] > skeleton_walk_y-splash: # Hitbox for skeleton walking
                resetEnemy(skeleton_walk_list, -1800, -50, 250, 525)
                score += 1
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
        # Skeleton attacking loop
        for i in range(len(skeleton_attack_list)):
            drawEnemy(skeleton_attack_sprites, skeleton_i, 0, 0, 0, skeleton_attack_list[i])
            skeleton_attack_x = 820
            skeleton_attack_y = skeleton_attack_list[i][1]
            # Resets enemy if clicked on
            if skeleton_attack_x+40+splash > mouseClick[0] > skeleton_attack_x-splash and skeleton_attack_y+54+splash > mouseClick[1] > skeleton_attack_y-splash: # Hitbox for skeleton attacking
                resetEnemy(skeleton_attack_list, -50, -50, 0, 0)
                score += 1
            # If skeleton enemy is at x=820, add it's damage multiplier to enemies attacking
            if skeleton_attack_list[i][0] == 820:
                enemy_attacking_Num += 5
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
        # Calculate health by subtracting the enemies attacking variable, # of enemies multiplied by their damage multipliers
        health = health - enemy_attacking_Num
        # Draws health bar depending on health
        health_bar_x = (health / 10000.0) * 266
        if health > 0: # Fixes health bar going into negatives
            pygame.draw.rect(screen,RED,[17,13,health_bar_x,23],0)
        # Fixes glitch where you could shoot ahead of enemy and it dying when walking over mouse click
        mouseClick = [0, 0]

        screen.blit(castle, [847, 160]) # Draw castle

        if health <= 0:
            game_Shown = False
            menu_Shown = False
            end_Shown = True
##################################################################################################################################
    if end_Shown:
        drawMenu(menu_images, menu_i, 0.27, [-25,0])
        if 706+168 > mouse[0] > 706 and 606+42 > mouse[1] > 606: # Back button hover
            screen.blit(back_button_press, [0,0])
        else:
            screen.blit(back_button, [0,0])
        if 706+168 > mouseClick[0] > 706 and 606+42 > mouseClick[1] > 606:
            end_Shown = False
            menu_Shown = True

            # Resets game
            health = 10000
            score = 0
            for i in range(len(werewolf_walk_list)):
                resetEnemy(werewolf_walk_list, -1800, -50, 250, 525)
            werewolf_attack_list = []

            for i in range(len(raven_walk_list)):
                resetEnemy(raven_walk_list, -1800, -50, 200, 250)
            raven_attack_list = []

            for i in range(len(skeleton_walk_list)):
                resetEnemy(skeleton_walk_list, -1800, -50, 250, 525)
            skeleton_attack_list = []

        # Draws score to screen
        screen.blit(end, [0,0] )
        end_font = pygame.font.Font(None,170)
        final_score = end_font.render(format(score,".0f"), True, WHITE)
        screen.blit(final_score, [580, 290])

##################################################################################################################################
    pygame.display.flip()
    clock.tick(60)
##################################################################################################################################


pygame.quit()
