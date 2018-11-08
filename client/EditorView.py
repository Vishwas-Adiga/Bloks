import pygame
import os
import assets.fonts.FontsManager as Fonts
import assets.ColoursManager as Colours
import assets.icons.IconsManager as Icons
from widgets.RoundedButton import *
from editor.TitleBar import *
from editor.ProjectBar import *
from editor.CategoriesPanel import *
from types import MethodType

class EditorView:

    viewComponents = []
    def show(self):
        pygame.init()
        screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
    
        screen = pygame.display.set_mode([screenWidth, screenHeight], pygame.RESIZABLE)
        pygame.display.set_caption("Bloks")

        titleBar = TitleBar(self.viewComponents, screenWidth, screenHeight)
        projectBar = ProjectBar(self.viewComponents, screenWidth, screenHeight)
        categoriesPanel = CategoriesPanel(self.viewComponents, screenWidth, screenHeight)
       

        clock = pygame.time.Clock()
        done = False

        while(not done):
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    done = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1: #left button clicked
                         for component in self.viewComponents:
                            if component.isMouseOver((mouse_x, mouse_y)):
                                component.onClick()
                #--lastly check for hover events
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for component in self.viewComponents:
                    if component.isMouseOver((mouse_x, mouse_y)):
                        component.onHover()
                    else:
                        component.noHover()
                screen.fill(Colours.WHITE)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                titleBar.draw(screen)
                categoriesPanel.draw(screen)
                projectBar.draw(screen)
                pygame.display.flip()
                clock.tick(60)
