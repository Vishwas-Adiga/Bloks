import pygame
from tkinter import *
import sys
import os

pygame.init()

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




size = (900,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bloks")
pygame.mouse.set_cursor(*pygame.cursors.diamond)


# Define the font and it's size
largeText = pygame.font.Font('freesansbold.ttf', 100)



class textObjects():
    '''To create a class with which we can display the text on a surface with ease'''

    def __init__(self,text,xCord,yCord,font):
        self.textOnSurface = text
        self.x = xCord
        self.y = yCord
        self.displayFont = font

    def create(self, colour, bg, surface):
        text = self.displayFont.render(self.textOnSurface, True, colour, WHITE)
        text_rectSize = text.get_rect()
        text_rect = pygame.draw.rect(surface, bg, (self.x,self.y,text_rectSize[0],text_rectSize[1])  )
        surface.blit(text,text_rect)
        pygame.display.flip()



# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rectangle = pygame.rect.Rect(176, 134, 200, 30)
main = pygame.rect.Rect(0,0,900,490)

rectangle_draging = False

ForeverSurf = pygame.image.load('Forever.png')
ForeverSurf_rect = ForeverSurf.get_rect()
asurf = pygame.image.load('dum.png')
asurf_rect = asurf.get_rect()


popup = pygame.rect.Rect(0, 0,asurf_rect[0] , asurf_rect[1])
popup2 = pygame.rect.Rect(20, 20, ForeverSurf_rect[0], ForeverSurf_rect[1])




# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #popup = pygame.rect.Rect(0, 0, 0, 0)  this is a bug I guess
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y
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

    test = textObjects('hello', 300, 300, largeText)
    test.create(blue,WHITE,screen)

    pygame.draw.rect(screen, WHITE, main)
    pygame.draw.rect(screen, teal, [0,490,900,10])
    
    pygame.draw.rect(screen, BROWN, rectangle)
    pygame.draw.rect(screen, WHITE, popup)
    screen.blit(asurf, popup)
    screen.blit(ForeverSurf, popup2)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()