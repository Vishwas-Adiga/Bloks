import pygame
import sys
import os
from win32api import GetSystemMetrics


pygame.init()
pygame.font.init()

#declaration of colour palette
BLACK          = (   0,   0,   0)
WHITE          = ( 255, 255, 255)
GREY           = ( 224, 224, 224)
GREY_LIGHT     = ( 238, 238, 238)
GREY_DARK     =  ( 117, 117, 117)

ALPHA = (255,255,255,255)

RED                 = ( 255,   0,   0)

PRIMARY             = (   0, 188, 212)
PRIMARY_DARK        = (   0, 151, 167)
PRIMARY_DEEP_DARK   = (   0, 131, 143)

#default fonts
Dubai_small   = pygame.font.SysFont('Dubai', 20)
Dubai_med   = pygame.font.SysFont('Dubai', 30)
Dubai_large = pygame.font.SysFont('Dubai', 60)


#screen details
width, height = GetSystemMetrics(0),GetSystemMetrics(1)
size = (width,height)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption("Bloks")
#pygame.mouse.set_cursor(*pygame.cursors.arrow)
thickarrow_strings = ( "xX                      ",
          "X.X                     ",
          "X..X                    ",
          "X...X                   ",
          "X....X                  ",
          "X.....X                 ",
          "X......X                ",
          "X.......X               ",
          "X........X              ",
          "X.........X             ",
          "X......XXXXX            ",
          "X...X..X                ",
          "X..XX..X                ",
          "X.X XX..X               ",
          "XX   X..X               ",
          "X     X..X              ",
          "      X..X              ",
          "       X..X             ",
          "       X..X             ",
          "        XX              ",
          "                        ",
          "                        ",
          "                        ",
          "                        ")

datatuple, masktuple = pygame.cursors.compile( thickarrow_strings,
                                  black='.', white='X', xor='o' )
pygame.mouse.set_cursor( (24,24), (0,0), datatuple, masktuple )

#boxes
bar_recent_files = pygame.rect.Rect(0, 0, width/4.0, height)
bar_title = pygame.rect.Rect(width/4.0,0,width,100)

btn_quit = pygame.rect.Rect(width-100,0,80,30)

btn_new_project = pygame.rect.Rect(width/4+60,160,180,180)
btn_open_project = pygame.rect.Rect(width/4+300,160,180,180)

box_no_recents = pygame.rect.Rect(0,0,210,210)

#images
img_close = pygame.image.load('close.png').convert_alpha()

img_new_project = pygame.image.load('Images/menu_new_project/menu_new_project.png').convert_alpha()
img_new_project_hover = pygame.image.load('Images/menu_new_project/menu_new_project_hover.png').convert_alpha()
img_new_project_click = pygame.image.load('Images/menu_new_project/menu_new_project_click.png').convert_alpha()

img_open_project = pygame.image.load('Images/menu_open_project/menu_open_project.png').convert_alpha()
img_open_project_hover = pygame.image.load('Images/menu_open_project/menu_open_project_hover.png').convert_alpha()
img_open_project_click = pygame.image.load('Images/menu_open_project/menu_open_project_click.png').convert_alpha()

img_no_recents = pygame.image.load('no_recents.png').convert_alpha()

#text
txt_title = Dubai_large.render('Bloks', True, WHITE)
txt_recent = Dubai_med.render('Recent', True, GREY_DARK)
txt_no_recents = Dubai_small.render('No recent files', True, GREY_DARK)


# Loop until the user clicks the close button.
done = False

#Other variables
btn_quit_hover = PRIMARY_DARK
no_recents = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #left click
            if event.button == 1:
                if btn_quit.collidepoint(event.pos):
                    #if click on exit btn
                    done = True
                    pygame.QUIT
                elif btn_new_project.collidepoint(event.pos):
                    img_new_project_current = img_new_project_click
                elif btn_open_project.collidepoint(event.pos):
                    img_open_project_current = img_open_project_click
        elif event.type == pygame.MOUSEMOTION:
            if btn_quit.collidepoint(event.pos):
                btn_quit_hover = PRIMARY_DEEP_DARK
            else:
                btn_quit_hover = PRIMARY_DARK
            
            if btn_new_project.collidepoint(event.pos):
                img_new_project_current = img_new_project_hover
            else:
                img_new_project_current = img_new_project
                
            if btn_open_project.collidepoint(event.pos):
                img_open_project_current = img_open_project_hover
            else:
                img_open_project_current = img_open_project
    
    # --- Drawing code should go here
    
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREY_LIGHT, bar_recent_files)
    pygame.draw.rect(screen, PRIMARY, bar_title)
    
    pygame.draw.rect(screen, ALPHA, btn_new_project)
    pygame.draw.rect(screen, ALPHA, btn_open_project)
    
    screen.blit(img_new_project_current,btn_new_project)
    screen.blit(img_open_project_current,btn_open_project)
        
    pygame.draw.rect(screen, btn_quit_hover, btn_quit)
    pygame.draw.line(screen, PRIMARY_DARK, (width/4.0,100),(width,100))
    pygame.draw.line(screen, GREY, (width/4.0,100),(width/4.0,height))
    
    
    close_box = screen.blit(img_close,(btn_quit.left+30,7))
    
    screen.blit(txt_title,(width/4+30,5))
    screen.blit(txt_recent,(30,15))
    
    if no_recents:
        pygame.draw.rect(screen, GREY_LIGHT, box_no_recents)
        box_no_recents.center = bar_recent_files.center
        screen.blit(img_no_recents,box_no_recents)
        screen.blit(txt_no_recents,(box_no_recents.left+40,box_no_recents.bottom+15))
    

 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()