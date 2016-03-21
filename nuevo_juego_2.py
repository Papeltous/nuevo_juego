import pygame, sys, time
from pygame.locals import *

pygame.init()
pygame.display.set_caption('ventana de prueva')

windowcolor = (0, 0, 0)
TEXTCOLOR = (255, 255, 255)

#funcions creation
#--------------------------------------------------------------------------------------------

def terminate():
    pygame.quit()
    sys.exit()


def Draw_Text(text, font, surface, x, y):
    objtext = font.render(text, 1, TEXTCOLOR)
    rectext = objtext.get_rect()
    rectext.topleft = (x, y)
    surface.blit(objtext, rectext)

def munitionHasHitAlien1(MunitionRect, enemies):
    for e in enemies:
        if MunitionRect.colliderect(e['rect']):
            print("toco!")
            return True
        return False

def munitionHasHitAlien2(MunitionRect, enemies_2):
    for e in enemies_2:
        if MunitionRect.colliderect(e['rect']):
            return True
        return False

def munitionHasHitAlien3(MunitionRect, enemies_3):
    for e in enemies_3:
        if MunitionRect.colliderect(e['rect']):
            return True
        return False

def munitionHasHitAlien4(MunitionRect, enemies_4):
    for e in enemies_4:
        if MunitionRect.colliderect(e['rect']):
            return True
        return False

def munitionHasHitAlien5(MunitionRect, enemies_5):
    for e in enemies_5:
        if MunitionRect.colliderect(e['rect']):
            return True
        return False

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return

#--------------------------------------------------------------------------------------------

#sprites creation
#--------------------------------------------------------------------------------------------

munition = pygame.image.load('munition.png')
MunitionRect = munition.get_rect

spaceship = pygame.image.load('spaceship.png')
ShipRect = spaceship.get_rect

enemy_1_1 = pygame.image.load('enemy1.png')
enemy_1_2 = pygame.image.load('enemy1_2.png')
enemy1_actual = enemy_1_1
enemy_1Rect = enemy1_actual.get_rect

enemy_2 = pygame.image.load('enemy.png')
enemy_2_2 = pygame.image.load('enemy2_2.png')
enemy2_actual = enemy_2
enemy_2Rect = enemy2_actual.get_rect

enemy_3 = pygame.image.load('enemy3.png')
enemy_3_2 = pygame.image.load('enemy3_1.png')
enemy3_actual = enemy_3
enemy_3Rect = enemy3_actual.get_rect

random_boss = pygame.image.load('random_enemy.png')

Init_image = pygame.image.load('Init_image.png')

#--------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------

#variables' creation
#--------------------------------------------------------------------------------------------

left = False

n0 = False

counter = -1

munition_on = False
movement_left = False
movement_right = False

window_x = 600
window_y = 400

#enemys first row
#---------------------------------------------

position_x_enemy_1a_row = window_x / 12

position_y_enemy_1a_row = 20



position_x_spaceship = window_x / 2
position_y_spaceship = window_y - 10

munition_x = position_x_spaceship + 6
munition_y = position_y_spaceship

counter_3 = 0

counter_2 = 0

counter_4 = 0

counter_2_0 = True

window = pygame.display.set_mode((window_x, window_y))
Reloj = pygame.time.Clock()
FPS = 40

font = pygame.font.SysFont(None, 24)

Init = False





Draw_Text('Space invaders.', font, window, (window_x / 3), (window_y / 3))
Draw_Text('Press a key to start the game.', font, window, (window_x / 3) - 30, (window_y / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


#---------------------------------------------------------------------------------------------

#the game's loop
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:

    while True:
        window.fill(windowcolor)
        counter_3 += 1

        

        if counter_3 / 5 == int(counter_3 / 5):

            counter_4 = counter_4 + 1

            if counter == 0:
                n0 = True
            if counter == 1:
                n0 = False

            if counter == 2:
                counter = -1

            if counter_4 / 40 == int(counter_4 / 40):
                position_y_enemy_1a_row = position_y_enemy_1a_row + 5

            counter = counter + 1

            if counter_2 == -20:
                counter_2_0 = True

            if counter_2 == 20:
                counter_2_0 = False


            if counter_2_0 == True:
                counter_2 = counter_2 + 1
            
            if counter_2_0 == False:
                counter_2 = counter_2 - 1

            position_x_enemy_1a_row = position_x_enemy_1a_row + 1

        for nº_alien_in_row in range(1,13):
            position_x_enemy_1a_row = window_x/13 * nº_alien_in_row
            position_x_enemy_1a_row = position_x_enemy_1a_row + counter_2
 
            if n0 == True:
                window.blit(enemy_1_1, (position_x_enemy_1a_row, position_y_enemy_1a_row))

            if n0 == False:
                window.blit(enemy_1_2, (position_x_enemy_1a_row, position_y_enemy_1a_row))

		
		
		
		
        if munition_on == False:
            munition_x = position_x_spaceship + 6
            munition_y = position_y_spaceship

        for event in pygame.event.get():

#spaceship's movement
#-----------------------------------------------------------------------------------------------------------
            if event.type == KEYDOWN:
                if event.key == ord('a') or event.key == K_LEFT:
                    movement_left = True
                    movement_right = False

                elif event.key == ord('d') or event.key == K_RIGHT:
                    movement_right = True
                    movement_left = False

                if event.key == K_ESCAPE:
                    terminate()

                
            if event.type == KEYUP:
                if event.key == ord('a') or event.key == K_LEFT:
                    movement_left = False

                elif event.key == ord ('d') or event.key == K_RIGHT:
                    movement_right = False

                if event.key == K_SPACE:
                    window.blit(munition, (munition_x, munition_y))
                    munition_on = True
                    munition_y = 390
                    munition_x = position_x_spaceship + 6

        if movement_left == True:
            position_x_spaceship = position_x_spaceship - 2

        if movement_right == True:
            position_x_spaceship = position_x_spaceship + 2
#-------------------------------------------------------------------------------------------------------------  

#sprites prints
#-------------------------------------------------------------------------------------------------------------
        
        if munition_on  == True:
            window.blit(munition, (munition_x, munition_y))
            munition_y = munition_y - 5

            if munition_y == 0:
                munition_on = False

        window.blit(spaceship, (position_x_spaceship, position_y_spaceship))

#-------------------------------------------------------------------------------------------------------------

        pygame.display.update()
        Reloj.tick(FPS)