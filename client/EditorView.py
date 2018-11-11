import pygame
import os
import assets.fonts.FontsManager as Fonts
import assets.ColoursManager as Colours
import assets.icons.IconsManager as Icons
from widgets.RoundedButton import *
from editor.TitleBar import *
from editor.ProjectBar import *
from editor.CategoriesPanel import *
from editor.DropPanel import *
from types import MethodType
from client.bloks.Blok import Blok

class EditorView:

    viewComponents = []
    allBloks = []
    def show(self):
        pygame.init()
        screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
    
        screen = pygame.display.set_mode([screenWidth, screenHeight], pygame.RESIZABLE)
        pygame.display.set_caption("Bloks")

        titleBar = TitleBar(self.viewComponents, screenWidth, screenHeight)
        projectBar = ProjectBar(self.viewComponents, screenWidth, screenHeight)
        categoriesPanel = CategoriesPanel(self.viewComponents, self.allBloks, screenWidth, screenHeight)
        dropPanel = DropPanel(screenWidth, screenHeight)

       

        clock = pygame.time.Clock()
        done = False
        mouseDownLeftPosition = None
        while(not done):
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for blok in self.allBloks:
                        if blok.isMouseOver(pos):
                            blok.startMotion(pos)
                            break
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for component in self.viewComponents:
                        if component.isMouseOver(pos):
                            component.onClick()
                    for blok in self.allBloks:
                        blok.stopMotion()
                        if blok.isCollidingWith([dropPanel.dustbinBox]):
                                self.allBloks.remove(blok)
                elif event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    for blok in self.allBloks:
                        if blok.dragging:
                            blok.moveTo(pos, self.allBloks)
                    for component in self.viewComponents:
                        pos = pygame.mouse.get_pos()
                        if component.isMouseOver(pos):
                            component.onHover()
                        else:
                            component.noHover()
                screen.fill(Colours.WHITE)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                dropPanel.draw(screen)
                titleBar.draw(screen)
                categoriesPanel.draw(screen)
                dropPanel.drawBloks(screen, self.allBloks)
                projectBar.draw(screen)
                pygame.display.flip()
                clock.tick(60)
