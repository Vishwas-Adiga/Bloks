import pygame
from client.widgets.RoundedButtonHelper import *
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours

class RoundedButton:
    rect = None
    rawRect = None
    radius = None

    textContent = None
    text = None
    textRect = None

    padding = None
    colour  = None
    
    def __init__(self, text, colour, radius, padding):
        self.colour = colour
        self.textContent = text
        self.padding = padding
        self.text = Fonts.productSansRegular(18).render(text, True, Colours.WHITE)
        self.textRect = self.text.get_rect()

        paddingL, paddingT = padding
        self.rawRect = self.textRect
        self.rawRect.width += paddingL
        self.rawRect.height += paddingT
        self.rawRect.topleft =  self.textRect.left - paddingL/2, self.textRect.top - paddingT/2
        self.radius = radius
        self.rect = RoundedButtonHelper(self.rawRect, colour, radius)

    def isMouseOver(self, point):
        return self.rawRect.collidepoint(point)

    def onClick(self):
        pass
    
    def onHover(self):
        pass

    def noHover(self):
        pass
    
    def draw(self, surface):
        self.rect.draw(surface)
        textRect = self.text.get_rect()
        textRect.center = self.rawRect.center
        surface.blit(self.text, textRect)

    def setColour(self, colour):
        self.colour = colour
        self.rect = RoundedButtonHelper(self.rawRect, colour, self.radius)

    def setRadius(self, radius):
        self.radius = radius
        self.rect = RoundedButtonHelper(self.rawRect, self.colour, radius)

    def redraw(self):
        paddingL, paddingT = self.padding
        self.rawRect = self.textRect
        self.rawRect.width += paddingL
        self.rawRect.height += paddingT
        self.rawRect.topleft = (self.textRect.left - paddingL/2, self.textRect.top - paddingT/2)
        self.rect = RoundedButtonHelper(self.rawRect, self.colour, self.radius)
