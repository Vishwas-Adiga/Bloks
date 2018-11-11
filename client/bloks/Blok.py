import pygame
import os
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
import client.assets.icons.IconsManager as Icons
from client.widgets.RoundedButton import *
from types import MethodType

class Blok:

    dragging = False
    offsetX = 0
    offsetY = 0
    collideArea = None
    left = 0
    top = 0
    
    def __init__(self, component, parent):
        self.component = component
        self.title = component.name        
        self.parent = parent
        self.children = []
        
        if(self.parent != None): 
            parent.addChild(self)
        
    def parse(self):
        pass
        
    def addChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.remove(child)
        
    def setParent(self, parent):
        if(self.parent != None):
            self.parent.getChildren().remove(self);
        self.parent = parent
        if(parent != None):
            parent.addChild(self)
        
    def getChildren(self):
            return self.children

    def moveTo(self, pos, allBloks):
        mouseX, mouseY = pos
        self.left = mouseX - self.offsetX
        self.top = mouseY - self.offsetY
        self.alignChildren()

        for block in allBloks:
            if self.isCollidingWith(block.collideArea):
                self.setParent(block)
                break
        else:
            self.setParent(None)

    def alignChildren(self):
        pass

    def isCollidingWith(self, otherCollideArea):
        for area in self.collideArea:
            for otherArea in otherCollideArea:
                if otherArea.colliderect(area):
                    return True
        return False

    def onHover(self):
        pass

    def noHover(self):
        pass

    def isMouseOver(self, pos):
        pass

    def onClick(self):
        pass

    def startMotion(self, pos):
        self.dragging = True
        self.offsetX, self.offsetY = pos
        self.offsetX -= self.left
        self.offsetY -= self.top

    def stopMotion(self):
        self.dragging = False
