import pygame
from client.widgets.RoundedButtonHelper import *
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours

class DropDownPanel:
    rect = None
    rawRect = None
    radius = None

    padding = None
    colour  = None

    dropDownItems = None
    
    def __init__(self, colour, radius, padding, dropDownItems, triggerRect):
        self.colour = colour
        self.padding = padding

        paddingL, paddingT = padding
        self.rawRect = dropDownItems[0].rawRect
        self.rawRect.width = paddingL + 70
        self.rawRect.height = paddingT + len(dropDownItems)*dropDownItems[0].rawRect.height 
        self.rawRect.topleft =  (triggerRect.top + triggerRect.height + 5, triggerRect.left + 5)
        self.radius = radius
        self.rect = RoundedButtonHelper(self.rawRect, colour, radius)
        self.dropDownItems = dropDownItems
        self.isShowing = False
        self.triggerRect = triggerRect
        

    def isMouseOver(self, point):
        return self.rawRect.collidepoint(point) or self.triggerRect.collidepoint(point)

    def onClick(self):
        pass
    
    def onHover(self):
        pass

    def noHover(self):
        self.hide()
    
    def draw(self, surface):
        if self.isShowing:
            self.rect.draw(surface)
            paddingL, paddingT = self.padding
            top = self.rawRect.top + paddingT/2
            left = self.rawRect.left + paddingL/2
            for item in self.dropDownItems:
                item.topleft = top, left
                item.draw(surface)
                top += item.rawRect.height

    def show(self):
        self.isShowing = True

    def hide(self):
        self.isShowing = False

    def addDropDownItem(self, item):
        self.dropDownItems.append(item)
        self.redraw()

    def removeDropDownItem(self, item):
        if len(self.dropDownItems) > 0:
            self.dropDownItems.remove(item)
            self.redraw()

    def setTrigger(self, triggerRect):
        self.triggerRect = triggerRect
        
    def redraw(self):
        paddingL, paddingT = self.padding
        self.rawRect.width += paddingL
        self.rawRect.height = paddingT + len(self.dropDownItems)*self.dropDownItems[0].rawRect.height 
        self.rawRect.topleft =  self.triggerRect.top + self.triggerRect.height + 5, self.triggerRect.left + 5
        self.rect = RoundedButtonHelper(self.rawRect, self.colour, self.radius)

