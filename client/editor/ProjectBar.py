import pygame
import os
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
import client.assets.icons.IconsManager as Icons
import client.assets.images.ImagesManager as Images
from client.widgets.RoundedButton import *
from types import MethodType

class ProjectBar:
    def __init__(self, viewComponents, screenWidth, screenHeight, editor):
        self.projectBar = pygame.Rect(0, 50, screenWidth, 50)
        self.projectTitle = Fonts.productSansRegular(20).render('Untitled Project', True, Colours.WHITE)

        self.editNameButton = RoundedButton('      ', Colours.WHITE_ALPHA_90, 1, (5, 5))
        self.editNameButton.textRect.left = self.projectTitle.get_rect().width + 60
        self.editNameButton.textRect.centery = 75
        self.editNameButton.redraw()
        viewComponents.append(self.editNameButton)
        self.screenWidth = screenWidth

        def onHover(self):
            self.setColour(Colours.WHITE_ALPHA_80)

        def noHover(self):
            self.setColour(Colours.WHITE_ALPHA_90)

        def onClick(self):
            editor.parse()

        self.editNameButton.onHover = MethodType(onHover, self.editNameButton)
        self.editNameButton.noHover = MethodType(noHover, self.editNameButton)
        self.editNameButton.onClick = MethodType(onClick, self.editNameButton)
    
    def draw(self, surface):
        surface.blit(Images.shadowBottom(30, self.screenWidth + 20), (-10, 85))
        pygame.draw.rect(surface, Colours.PRIMARY_700, self.projectBar)
        surface.blit(self.projectTitle, (50, (100 + 50 - self.projectTitle.get_rect().height)/2))
        surface.blit(Icons.editActionLight(30, 30), self.editNameButton.rawRect)
        self.editNameButton.draw(surface)
        


        
