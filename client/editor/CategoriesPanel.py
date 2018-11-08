import pygame
import os
import sys
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
from client.widgets.RoundedButton import *
import pkgutil
from pydoc import locate
import src.ComponentCategories as Categories
from types import MethodType

class CategoriesPanel:
    componentInstances = []
    categoryButtons = []
    categoryIcons = []
    def __init__(self, viewComponents, screenWidth, screenHeight):
        self.screenHeight = screenHeight
        self.panel = pygame.Rect(50, 100, 300, screenHeight)
        self.tabs = pygame.Rect(0, 100, 50, screenHeight)
        self.components = [name for _, name, _ in pkgutil.iter_modules(['src'])]
        self.components.remove('ComponentTypeConstants')
        self.components.remove('Component')
        self.components.remove('ComponentCategories')
        self.components.remove('ComponentHeaders')
        for component in self.components:
            componentClass = locate('src.' + component + '.' + component)
            instance = componentClass()
            self.componentInstances.append(instance)

        for category in Categories.getCategories():
            categoryButton = RoundedButton('      ', Colours.WHITE_ALPHA_90, 1, (7, 7))
            categoryButton.textRect.centerx = 25
            categoryButton.textRect.top = 150 + (category['id'] - 1)*60
            categoryButton.redraw()
            viewComponents.append(categoryButton)
            this = self

            def onHover(self):
                self.setColour(Colours.WHITE_ALPHA_80)

            def noHover(self):
                self.setColour(Colours.WHITE_ALPHA_90)

            def onClick(self):
                this.showCategory(category['id'])

            print(category['id'])
            categoryButton.onHover = MethodType(onHover, categoryButton)
            categoryButton.noHover = MethodType(noHover, categoryButton)
            categoryButton.onClick = MethodType(onClick, categoryButton)
            self.categoryButtons.append(categoryButton)
            self.categoryIcons.append(category['icon'])
    
    def showCategory(self, id):
        print(id)

    def draw(self, surface):
        pygame.draw.rect(surface, Colours.GREY_300, self.panel)
        pygame.draw.line(surface, Colours.GREY_500, (350, 100), (350, self.screenHeight))
        pygame.draw.rect(surface, Colours.GREY_400, self.tabs)
        pygame.draw.line(surface, Colours.GREY_500, (50, 100), (50, self.screenHeight))
        i = 0
        for categoryButton in self.categoryButtons:
            categoryButton.draw(surface)
            rect = self.categoryIcons[i].convert_alpha().get_rect()
            rect.center = categoryButton.rawRect.center
            surface.blit(self.categoryIcons[i].convert_alpha(), rect)
            i+= 1



        
