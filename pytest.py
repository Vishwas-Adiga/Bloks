import pygame
pygame.init()

import sys
import os

#if sys.version_info[0] < 3:
#    print("Python 3 or a more recent version is required.")


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
blue     = (   0, 105,  92)
teal     = (   0,  77,  64)
BROWN = (230,81,0)
GREY = (224,224,224)

size = (900, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bloks")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rectangle = pygame.rect.Rect(176, 134, 200, 30)
main = pygame.rect.Rect(0,0,900,490)
popup = pygame.rect.Rect(0, 0, 0, 0)
rectangle_draging = False

asurf = pygame.image.load('dum.png')
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #popup = pygame.rect.Rect(0, 0, 0, 0)
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y
            elif event.button == 3:
                mouse_x, mouse_y = event.pos
                popup = pygame.rect.Rect(mouse_x, mouse_y, 100, 300)
            elif event.button == 2:
                mouse_x, mouse_y = event.pos
                screen.scroll(10,10)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y
    # --- Game logic should go here
    
    # --- Drawing code should go here
    
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    pygame.draw.rect(screen, WHITE, main)
    pygame.draw.rect(screen, teal, [0,490,900,10])
    
    pygame.draw.rect(screen, BROWN, rectangle)
    pygame.draw.rect(screen, WHITE, popup)
    screen.blit(asurf, popup)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)