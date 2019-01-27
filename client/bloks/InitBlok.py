import pygame
import os
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
import client.assets.icons.IconsManager as Icons
from client.widgets.RoundedButton import *
from types import MethodType
from client.bloks.Blok import Blok
from client.bloks import BlokHelper
 
class InitBlok(Blok):
    def __init__(self):
        self.component = None
        self.parent = None
        self.title = 'Start'
        self.children = []
        
        self.container = pygame.Rect(self.left + 15, self.top, 245, 30)
        self.roundedContainer = BlokHelper.roundedRectangle(self.container, Colours.GREEN_900, 1)
        self.bloksContainerArea = pygame.Surface((245, len(self.children)*30))
        self.collideArea = []
        self.type = None
        self.acceptedChildrenTypes = ['R1']
        
    def parse(self):
        parserResult = ''
        for blockInstance in self.children: 
            parserResult += blockInstance.parse()
        return parserResult

    def alignChildren(self):
        i = self.top + 35
        for child in self.children:
            child.top = i
            i += child.container.height + 5
            child.left = self.left

    def isMouseOver(self, pos):
        for area in self.collideArea:
            if area.collidepoint(pos):
                return True
        return False

    def draw(self, surface):
        self.container = pygame.Rect(self.left + 15, self.top, 245, 30)
        self.roundedContainer = BlokHelper.roundedRectangle(self.container, Colours.ORANGE_500, 1)
        height = 0
        for child in self.children:
            height += child.container.height
        self.bloksContainerArea = pygame.Surface((50, height), pygame.SRCALPHA)
        self.bloksContainerArea.fill(Colours.WHITE_ALPHA_100)
        blitBloksContainerArea = surface.blit(self.bloksContainerArea, (self.container.left, self.container.top + 30))
        self.lowerTriangle = pygame.draw.polygon(surface, Colours.ORANGE_500, [(self.left + 37, self.top + 30), (self.left + 42, self.top + 35), (self.left + 42, self.top + 30)])
        blitContainer = surface.blit(self.roundedContainer, self.container)
        title = Fonts.robotoMedium(16).render('Start', True, Colours.WHITE)
        titleBox = title.get_rect()
        titleBox.centery = self.container.centery
        titleBox.left = self.left + 40
        surface.blit(title, titleBox)
        self.collideArea = [blitContainer, blitBloksContainerArea]

    def onClick(self):
        return
