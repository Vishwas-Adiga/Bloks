import pygame
import os
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
from client.widgets.RoundedButton import *
from client.widgets.DropDownPanel import DropDownPanel
from client.widgets.DropDownItem import DropDownItem
from types import MethodType

class TitleBar:
    def __init__(self, viewComponents, screenWidth, screenHeight):
        self.titleBar = pygame.Rect(0, 0, screenWidth, 50)
        self.titleText = Fonts.productSansRegular(30).render('Bloks', True, Colours.WHITE)
        
        self.fileButton = RoundedButton('File', Colours.WHITE_ALPHA_90, 0.2, (40, 5))
        self.fileButton.textRect.left = 205
        self.fileButton.textRect.centery = 25
        self.fileButton.redraw()
        viewComponents.append(self.fileButton)

        def onHover(self):
            self.setColour(Colours.WHITE_ALPHA_80)

        def noHover(self):
            self.setColour(Colours.WHITE_ALPHA_90)

        self.fileButton.onHover = MethodType(onHover, self.fileButton)
        self.fileButton.noHover = MethodType(noHover, self.fileButton)

        self.editButton = RoundedButton('Edit', Colours.WHITE_ALPHA_90, 0.2, (40, 5))
        self.editButton.textRect.left = 320
        self.editButton.textRect.centery = 25
        self.editButton.redraw()
        viewComponents.append(self.editButton)

        def onHover(self):
            self.setColour(Colours.WHITE_ALPHA_80)

        def noHover(self):
            self.setColour(Colours.WHITE_ALPHA_90)

        self.editButton.onHover = MethodType(onHover, self.editButton)
        self.editButton.noHover = MethodType(noHover, self.editButton)

        self.toolsButton = RoundedButton('Tools', Colours.WHITE_ALPHA_90, 0.2, (40, 5))
        self.toolsButton.textRect.left = 440
        self.toolsButton.textRect.centery = 25
        self.toolsButton.redraw()
        viewComponents.append(self.toolsButton)

        def onHover(self):
            self.setColour(Colours.WHITE_ALPHA_80)

        def noHover(self):
            self.setColour(Colours.WHITE_ALPHA_90)

        self.toolsButton.onHover = MethodType(onHover, self.toolsButton)
        self.toolsButton.noHover = MethodType(noHover, self.toolsButton)

        self.helpButton = RoundedButton('Help', Colours.WHITE_ALPHA_90, 0.2, (40, 5))
        self.helpButton.textRect.left = 575
        self.helpButton.textRect.centery = 25
        self.helpButton.redraw()
        viewComponents.append(self.helpButton)

        def onHover(self):
            self.setColour(Colours.WHITE_ALPHA_80)

        def noHover(self):
            self.setColour(Colours.WHITE_ALPHA_90)

        self.helpButton.onHover = MethodType(onHover, self.helpButton)
        self.helpButton.noHover = MethodType(noHover, self.helpButton)

        #Dropdown buttons
        this = self
        newProjectItem = DropDownItem('New', Colours.RED, 0, Colours.PRIMARY_900)
        self.fileDropDown = DropDownPanel(Colours.WHITE, 0.2, (5, 5), [newProjectItem, newProjectItem, newProjectItem], self.fileButton.rawRect)
        def onClick(self):
            print(this.fileDropDown.rawRect.width)
            this.fileDropDown.show()

        self.fileButton.onClick = MethodType(onClick, self.fileButton)
        viewComponents.append(self.fileDropDown)
        self.fileDropDown.redraw()
    
    def draw(self, surface):
        pygame.draw.rect(surface, Colours.PRIMARY_900, self.titleBar)
        surface.blit(self.titleText, (50, (50 - self.titleText.get_rect().height)/2))
        self.fileButton.draw(surface)
        self.editButton.draw(surface)
        self.toolsButton.draw(surface)
        self.helpButton.draw(surface)
        self.fileDropDown.draw(surface)
        


        
