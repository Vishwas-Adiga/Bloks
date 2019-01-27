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
    def __init__(self, component, parent):
        Blok.__init__(self, component, parent)
        self.container = pygame.Rect(self.left + 15, self.top, 245, 30)
        self.roundedContainer = BlokHelper.roundedRectangle(self.container, Colours.GREEN_900, 1)
        self.collideArea = []
        offsetX = 10
        offsetY = 10
        
    def parse(self):
        parserResult = ''
        for blockInstance in self.children: 
            parserResult += blockInstance.parse()
        parserResult = self.component.parse(parserResult.split('/**/'))
        return parserResult

    def alignChildren(self):
        index = 1
        for child in self.children:
            child.left = self.left + self.container.width
            child.top = self.top+ 35*index
        
    def draw(self, surface):
        height = 30
        for arg in self.component.args:
            height += 35

        self.container = pygame.Rect(self.left + 15, self.top, 245, height)
        self.upperTriangle = pygame.draw.polygon(surface, Colours.PURPLE_900, [(self.left + 35, self.top), (self.left + 35, self.top - 5), (self.left + 40, self.top)])
        self.lowerTriangle = pygame.draw.polygon(surface, Colours.PURPLE_900, [(self.left + 37, self.top + height), (self.left + 42, self.top + height + 5), (self.left + 42, self.top + height)])
        title = Fonts.robotoMedium(16).render(self.component.name, True, Colours.WHITE)
        tempBox = pygame.Rect(self.left + 15, self.top, 245, height - 30)
        tempBox.top += 15
        midBlitBox = tempBox
        pygame.draw.rect(surface, Colours.PURPLE_900, tempBox)
        tempBox = pygame.Rect(self.left + 15, self.top, 245, 30)
        tempRoundedBox = BlokHelper.roundedRectangle(tempBox, Colours.PURPLE_900, 1)
        upperBlitBox = surface.blit(tempRoundedBox, tempBox)
        
        titleBox = title.get_rect()
        titleBox.centery = tempBox.centery
        titleBox.left = self.left + 40

        tempBox = pygame.Rect(self.left + 15, self.container.bottom - 30, 245, 30)
        tempRoundedBox = BlokHelper.roundedRectangle(tempBox, Colours.PURPLE_900, 1)
        
        lowerBlitBox = surface.blit(tempRoundedBox, tempBox)
        surface.blit(title, titleBox)

        tempBox = pygame.Rect(self.left + 15, self.top, 245, 30)
        index = 1
        for arg in self.component.args:
            argName = Fonts.robotoMedium(14).render(arg, True, Colours.WHITE)
            argNameBox = argName.get_rect()
            argNameBox.left = self.left + 245 - argNameBox.width - 10
            argNameBox.centery = tempBox.centery + 35*index
            surface.blit(argName, argNameBox)
            pygame.draw.circle(surface, Colours.PURPLE_900, (self.left + 245 + 10, tempBox.centery + 35*index), 10)
            index += 1
        self.collideArea = [upperBlitBox, midBlitBox, lowerBlitBox]

    def onClick(self):
        pass
