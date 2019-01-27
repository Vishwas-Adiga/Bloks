import pygame
from client.widgets.RoundedButtonHelper import *
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
from client.widgets.Button import Button

class DropDownItem(Button):
    
    def __init__(self, text, colour, radius, textColour):
        self.radius = radius
        Button.__init__(self, text, colour, (0, 0), textColour)

    def setRadius(self, radius):
        self.radius = radius
        self.rect = RoundedButtonHelper(self.rawRect, self.colour, radius)
