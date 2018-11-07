import pygame
import os
import assets.fonts.FontsManager as Fonts
import assets.ColoursManager as Colours

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

def show():
    screen = pygame.display.set_mode([400, 200], pygame.NOFRAME)
    pygame.display.set_caption("Bloks")

    titleText = Fonts.productSansRegular(50).render('Bloks', True, Colours.WHITE)
    titleTextBox = titleText.get_rect()
    titleTextBox.center  = (100, 80)

    loadingText = Fonts.productSansRegular(16).render('Loading...', True, Colours.WHITE)
    loadingTextBox = loadingText.get_rect()
    loadingTextBox.center = (85, 120)

    versionText = Fonts.productSansRegular(10).render('Version 1.0', True, Colours.GREY_100)
    versionTextBox = versionText.get_rect()
    versionTextBox.center = (370, 190)

    clock = pygame.time.Clock()
    screen.fill(Colours.PRIMARY_900)
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    screen.blit(titleText, titleTextBox)
    screen.blit(loadingText, loadingTextBox)
    screen.blit(versionText, versionTextBox)
    pygame.display.flip()
    pygame.time.wait(5000)
    clock.tick(60)
    pygame.display.quit()
