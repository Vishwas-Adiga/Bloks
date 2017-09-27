import pygame
pygame.init()

import sys

#if sys.version_info[0] < 3:
#    print("Python 3 or a more recent version is required.")


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
blue     = (   0, 105,  92)
teal     = (   0,  77,  64)

size = (900, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bloks")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    # --- Game logic should go here
    
    # --- Drawing code should go here
    
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    pygame.draw.rect(screen, blue, [0,0,900,490])
    pygame.draw.rect(screen, teal, [0,490,900,10])
    
    basicfont = pygame.font.SysFont(None, 100)
    loadingfont = pygame.font.SysFont(None, 20)
    text = basicfont.render('Bloks', True, (255, 255, 255), blue)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(text, textrect)
    
    loading_text = loadingfont.render('Loading', True, (255, 255, 255), blue)
    loading_textrect = text.get_rect()
    loading_textrect.centerx = screen.get_rect().centerx
    loading_textrect.centery = screen.get_rect().centery + 70
    screen.blit(loading_text, loading_textrect)
     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)