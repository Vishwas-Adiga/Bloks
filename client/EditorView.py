import pygame
import os
import assets.fonts.FontsManager as Fonts
import assets.ColoursManager as Colours
import assets.icons.IconsManager as Icons
from widgets.RoundedButton import *

class EditorView:

    viewComponents = []
    def show(self):
        pygame.init()
        screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
    
        screen = pygame.display.set_mode([screenWidth, screenHeight], pygame.RESIZABLE)
        pygame.display.set_caption("Bloks")

        titleBar = pygame.Rect(0, 0, screenWidth, 50)
        titleText = Fonts.productSansRegular(30).render('Bloks', True, Colours.WHITE)

        projectBar = pygame.Rect(0, 50, screenWidth, 50)
        fileButton = Fonts.productSansRegular(18).render('File', True, Colours.WHITE)
        fileButtonBox = fileButton.get_rect()
        fileButtonBox.left = 200
        fileButtonBox.centery = 25

        fileButtonHoverBox = fileButton.get_rect()
        fileButtonHoverBox.width += 40
        fileButtonHoverBox.height += 5
        fileButtonHoverBox.topleft =  180, fileButtonBox.top - 2.5

        btn = RoundedButton(fileButtonHoverBox, Colours.WHITE_ALPHA_80, 0.2)


        clock = pygame.time.Clock()
        done = False

        while(not done):
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    done = True 
                screen.fill(Colours.WHITE)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                pygame.draw.rect(screen, Colours.PRIMARY_900, titleBar)
                screen.blit(titleText, (50, (50 - titleText.get_rect().height)/2))
                screen.blit(fileButton, fileButtonBox)
                btn.draw(screen)
                pygame.draw.rect(screen, Colours.PRIMARY_700, projectBar)
                pygame.display.flip()
                clock.tick(60)
