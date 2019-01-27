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
        self.acceptedChildrenTypes = component.acceptedReturnTypes
        self.type = component.returnType
        
        if(self.parent != None): 
            parent.addChild(self)
        
    def parse(self):
        pass
        
    def addChild(self, child):
        if child.type in self.acceptedChildrenTypes:
            self.children.append(child)
            self.alignChildren()

    def removeChild(self, child):
        if child in self.children:
            self.children.remove(child)
        
    def setParent(self, parent):
        if parent != None:
            if not self.type in parent.acceptedChildrenTypes:
                return
        if(self.parent != None):
            if self in self.parent.getChildren():
                self.parent.getChildren().remove(self);
        self.parent = parent
        if(parent != None):
            parent.addChild(self)
            if parent in self.children:
                self.children.remove(parent)
        
    def getChildren(self):
            return self.children

    def moveTo(self, pos):
        mouseX, mouseY = pos
        self.left = mouseX - self.offsetX
        self.top = mouseY - self.offsetY
        self.alignChildren()

    def alignChildren(self):
        return

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
        for area in self.collideArea:
            if area.collidepoint(pos):
                return True
        return False


    def onClick(self):
        pass

    def startMotion(self, pos):
        self.dragging = True
        self.offsetX, self.offsetY = pos
        self.offsetX -= self.left
        self.offsetY -= self.top

    def stopMotion(self, pos, allBloks):
        self.dragging = False
        for blok in allBloks:
            if self.isCollidingWith(blok.collideArea) and not blok == self:
                self.setParent(blok)
                break
        else:
            self.setParent(None)
        self.alignChildren()
