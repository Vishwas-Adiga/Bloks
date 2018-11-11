import pygame
import os
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
import client.assets.icons.IconsManager as Icons
from client.widgets.RoundedButton import *
from types import MethodType
from client.bloks.Blok import Blok
from client.bloks import BlokHelper
 
class MethodBlok(Blok):
    args = None
    def __init__(self, component, parent, passedArgs):
        Blok.__init__(self, component, parent)
        self.passedArgs = passedArgs
        self.container = pygame.Rect(self.left + 15, self.top, 245, 30)
        self.roundedContainer = BlokHelper.roundedRectangle(self.container, Colours.GREEN_900, 1)
        self.collideArea = []
        offsetX = 10
        offsetY = 10
        
    def parse(self):
        parserResult = ''
        for blockInstance in self.children: 
            parserResult += blockInstance.parse()
        parserResult += component.parse(self.passedArgs)
        return parserResult

    def alignChildren(self):
        pass

    def isMouseOver(self, pos):
        for area in self.collideArea:
            if area.collidepoint(pos):
                return True
        return False

    def draw(self, surface):
        self.container = pygame.Rect(self.left + 15, self.top, 245, 30)
        self.roundedContainer = BlokHelper.roundedRectangle(self.container, Colours.GREEN_900, 1)
        self.upperTriangle = pygame.draw.polygon(surface, Colours.GREEN_900, [(self.left + 35, self.top), (self.left + 35, self.top - 5), (self.left + 40, self.top)])
        self.lowerTriangle = pygame.draw.polygon(surface, Colours.GREEN_900, [(self.left + 37, self.top + 30), (self.left + 42, self.top + 35), (self.left + 42, self.top + 30)])
        blitContainer = surface.blit(self.roundedContainer, self.container)
        title = Fonts.robotoMedium(16).render(self.component.name, True, Colours.WHITE)
        titleBox = title.get_rect()
        titleBox.centery = self.container.centery
        titleBox.left = self.left + 40
        surface.blit(title, titleBox)
        self.collideArea = [blitContainer]

    def onClick(self):
        pass
