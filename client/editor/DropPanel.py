import pygame
import os
import sys
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
import client.assets.images.ImagesManager as Images
from types import MethodType

from client.bloks.MethodBlok import MethodBlok

class DropPanel:
    allBloks = []
    def __init__(self, screenWidth, screenHeight):
        self.dropArea = pygame.Rect(350, 100, screenWidth - 350, screenHeight - 100)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.dustbin = Images.dustbin(100, 100)
        self.dustbinBox = self.dustbin.get_rect()

    def draw(self, surface):
        pygame.draw.rect(surface, Colours.WHITE, self.dropArea)
        isEnd = False
        x = 350
        y = 100
        while not isEnd:
            pygame.draw.circle(surface, Colours.GREY_200, (x, y), 5)
            x += 25
            if x > self.screenWidth:
                x = 350
                y += 25
            if y > self.screenHeight:
                isEnd = True
        
        self.dustbinBox.left = self.screenWidth - 130
        self.dustbinBox.top = self.screenHeight - 130
        surface.blit(self.dustbin, self.dustbinBox)

    def drawBloks(self, surface, allBloks):
        for blok in allBloks:
            blok.draw(surface)



        
