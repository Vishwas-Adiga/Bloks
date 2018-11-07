import pygame
import os
import assets.fonts.FontsManager as Fonts
import assets.ColoursManager as Colours


os.environ['SDL_VIDEO_CENTERED'] = '0'
def show():
    pygame.init()
    screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
    
    screen = pygame.display.set_mode([screenWidth, screenHeight], pygame.RESIZABLE)
    pygame.display.set_caption("Bloks")

    titleBar = pygame.Rect(0, 0, screenWidth, 100)

    titleText = Fonts.productSansRegular(50).render('Bloks', True, Colours.PRIMARY_500)
    titleTextBox = titleText.get_rect()
    titleTextBox.center  = (100, 80)

    loadingText = Fonts.productSansRegular(16).render('Loading...', True, Colours.WHITE)
    loadingTextBox = loadingText.get_rect()
    loadingTextBox.center = (85, 120)

    versionText = Fonts.productSansRegular(10).render('Version 1.0', True, Colours.GREY_100)
    versionTextBox = versionText.get_rect()
    versionTextBox.center = (370, 190)

    clock = pygame.time.Clock()
    done = False

    while(not done):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
            if event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
        screen.fill(Colours.PRIMARY_500)
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        pygame.draw.rect(screen, Colours.WHITE, titleBar)
        pygame.display.flip()
        clock.tick(60)
