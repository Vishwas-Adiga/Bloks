import pygame
import os
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
import client.assets.icons.IconsManager as Icons
from client.widgets.RoundedButton import *
from types import MethodType
from client.bloks.Blok import Blok
from client.bloks import BlokHelper
 
class VariableBlok(Blok):
    def __init__(self, component, parent):
        Blok.__init__(self, component, parent)
        self.container = pygame.Rect(self.left + 15, self.top, 245, 30)
        self.roundedContainer = BlokHelper.roundedRectangle(self.container, Colours.GREEN_900, 1)
        self.collideArea = []
        self.width = 100
        self.textContent = ''
        self.text = None
        self.pos = 0, 0
        self.isInTextMode = False
        
    def parse(self):
        return self.textContent + '/**/'

    def alignChildren(self):
        pass
        
    def draw(self, surface):
        self.text = Fonts.robotoMedium(16).render(self.textContent, True, Colours.WHITE)
        self.container = pygame.Rect(self.left + 15, self.top, self.width, 30)
        self.roundedContainer = BlokHelper.roundedRectangle(self.container, Colours.RED_900, 1)
        blitContainer = surface.blit(self.roundedContainer, self.container)
        pygame.draw.circle(surface, Colours.RED_900, (self.left + 15 + 5, self.container.centery), 10)

        textArea = pygame.Rect(self.left + 19, self.top + 4, self.width - 8, 22)
        roundedTextArea = BlokHelper.roundedRectangle(textArea, Colours.RED_300, 1)
        textAreaBlitContainer = surface.blit(roundedTextArea, textArea)

        textBox = self.text.get_rect()
        textBox.centery = textArea.centery
        textBox.left = textArea.left + 10

        surface.blit(self.text, textBox)
        if textBox.width < 100:
            self.width = 100
        else:
            self.width = textBox.width + 30

        self.collideArea = [blitContainer, textAreaBlitContainer]

    def onClick(self):
        pass

    def startMotion(self, pos):
        Blok.startMotion(self, pos)
        self.pos = pos

    def stopMotion(self, pos, allBloks):
        self.dragging = False
        for blok in allBloks:
            if self.isCollidingWith(blok.collideArea) and not blok == self:
                self.setParent(blok)
                break
        self.alignChildren()
        if pos == self.pos:
            self.isInTextMode = True
        else:
            self.isInTextMode = False
