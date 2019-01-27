import pygame
from client.widgets.RoundedButtonHelper import *
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
from client.widgets.Button import Button

class RoundedButton(Button):
    
    def __init__(self, text, colour, radius, padding):
        self.radius = radius
        Button.__init__(self, text, colour, padding)

    def setRadius(self, radius):
        self.radius = radius
        self.rect = RoundedButtonHelper(self.rawRect, self.colour, radius)
