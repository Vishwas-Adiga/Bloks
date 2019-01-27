import pygame
import os
import sys
import client.assets.fonts.FontsManager as Fonts
import client.assets.ColoursManager as Colours
from client.widgets.RoundedButton import *
import pkgutil
from pydoc import locate
import src.ComponentCategories as Categories
from src import ComponentTypeConstants
from types import MethodType

from client.bloks.MethodBlok import MethodBlok
from client.bloks.VariableBlok import VariableBlok

class CategoriesPanel:
    componentInstances = []
    categoryButtons = {}
    categoryIcons = []
    currentCategoryBloks = []
    def __init__(self, viewComponents, allBloks, screenWidth, screenHeight):
        self.screenHeight = screenHeight
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
            categoryButton.textRect.top = 120 + (category['id'] - 1)*60
            categoryButton.redraw()
            viewComponents.append(categoryButton)
            this = self

            def onHover(self):
                self.setColour(Colours.WHITE_ALPHA_80)

            def noHover(self):
                self.setColour(Colours.WHITE_ALPHA_90)

            
            def onClick(self):
                this.showCategory(self, viewComponents, allBloks)

            categoryButton.onHover = MethodType(onHover, categoryButton)
            categoryButton.noHover = MethodType(noHover, categoryButton)
            categoryButton.onClick = MethodType(onClick, categoryButton)
            self.categoryButtons.update({categoryButton : category['id']})
            self.categoryIcons.append(category['icon'])

            self.panel = pygame.Rect(50, 100, 300, screenHeight)
            self.categoryTitle = Fonts.productSansRegular(18).render('Interface', True, Colours.GREY_900)
            
    def showCategory(self, button, viewComponents, allBloks):
        for component in viewComponents:
                        if component.__class__.__name__  == 'MethodBlok' or component.__class__.__name__  == 'PropertyBlok':
                            viewComponents.remove(component)
        self.currentCategoryBloks[:] = []
        categoryId = self.categoryButtons[button]
        self.categoryTitle = Fonts.productSansRegular(18).render(Categories.getCategories()[categoryId - 1]['name'], True, Colours.GREY_900)
        for component in self.componentInstances:
            if component.category['id'] == categoryId:
                if component.type == ComponentTypeConstants.METHOD:
                    sampleBlok = MethodBlok(component, None)

                    def onClick(self, newComponent = component):
                        newBlok = MethodBlok(newComponent, None)
                        newBlok.left = 380
                        newBlok.top = sampleBlok.top + 120
                        onClick.allBloks.append(newBlok)

                    onClick.allBloks = allBloks
                    onClick.component = component
                    sampleBlok.onClick = MethodType(onClick, sampleBlok)
                    self.currentCategoryBloks.append(sampleBlok)
                    viewComponents.append(sampleBlok)
                elif component.type == ComponentTypeConstants.VARIABLE:
                    sampleBlok = VariableBlok(component, None)

                    def onClick(self, newComponent = component):
                        newBlok = VariableBlok(newComponent, None)
                        newBlok.left = 380
                        newBlok.top = sampleBlok.top + 120
                        onClick.allBloks.append(newBlok)

                    onClick.allBloks = allBloks
                    onClick.component = component
                    sampleBlok.onClick = MethodType(onClick, sampleBlok)
                    self.currentCategoryBloks.append(sampleBlok)
                    viewComponents.append(sampleBlok)
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
        rectTitle = self.categoryTitle.get_rect()
        rectTitle.centerx = 200
        rectTitle.top = 120
        surface.blit(self.categoryTitle, rectTitle)
        top = 180
        for blok in self.currentCategoryBloks:
            blok.left = 60
            blok.top = top
            top += blok.container.height + 20
            blok.draw(surface)




        
