import pygame
import os
import assets.fonts.FontsManager as Fonts
import assets.ColoursManager as Colours
import assets.icons.IconsManager as Icons
from widgets.RoundedButton import *
from editor.TitleBar import *
from editor.ProjectBar import *
from editor.CategoriesPanel import *
from editor.DropPanel import *
from types import MethodType
from client.bloks.Blok import Blok

class EditorView:

    viewComponents = []
    allBloks = []
    def __init__(self):
        pygame.init()
        screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
    
        screen = pygame.display.set_mode([screenWidth, screenHeight], pygame.RESIZABLE)
        pygame.display.set_caption("Bloks")

        self.titleBar = TitleBar(self.viewComponents, screenWidth, screenHeight)
        self.dropPanel = DropPanel(screenWidth, screenHeight, self.allBloks)
        self.projectBar = ProjectBar(self.viewComponents, screenWidth, screenHeight, self)
        self.categoriesPanel = CategoriesPanel(self.viewComponents, self.allBloks, screenWidth, screenHeight)

       

        clock = pygame.time.Clock()
        done = False
        mouseDownLeftPosition = None
        while(not done):
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for blok in self.allBloks:
                        if blok.isMouseOver(pos):
                            blok.startMotion(pos)
                            break
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for component in self.viewComponents:
                        if component.isMouseOver(pos):
                            component.onClick()
                    for blok in self.allBloks:
                        blok.stopMotion(pos, self.allBloks)
                        if blok.isCollidingWith([self.dropPanel.dustbinBox]):
                            if not blok.__class__.__name__ == 'InitBlok':
                                self.allBloks.remove(blok)
                elif event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    for blok in self.allBloks:
                        if blok.dragging:
                            blok.moveTo(pos)
                    for component in self.viewComponents:
                        pos = pygame.mouse.get_pos()
                        if component.isMouseOver(pos):
                            component.onHover()
                        else:
                            component.noHover()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        for blok in self.allBloks:
                            if blok.__class__.__name__ == 'VariableBlok' and blok.isInTextMode:
                                blok.isInTextMode = False
                    elif event.key == pygame.K_BACKSPACE:
                        for blok in self.allBloks:
                            if blok.__class__.__name__ == 'VariableBlok' and blok.isInTextMode:
                                blok.textContent = blok.textContent[:-1]
                    else:
                        for blok in self.allBloks:
                            if blok.__class__.__name__ == 'VariableBlok' and blok.isInTextMode:
                                blok.textContent += event.unicode
                screen.fill(Colours.WHITE)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                self.dropPanel.draw(screen)
                self.titleBar.draw(screen)
                self.categoriesPanel.draw(screen)
                self.dropPanel.drawBloks(screen, self.allBloks)
                self.projectBar.draw(screen)
                pygame.display.flip()
                clock.tick(60)

    def parse(self):
        headers = []
        for blok in self.allBloks:
            if blok.component == None:
                continue
            for header in blok.component.headers:
                headers.append(header)
        headers = list(set(headers))

        headersString = ''
        for header in headers:
            headersString += '#include <' + header + '>\n'

        parserResult = 'using namespace std; \nint main() {'
        parserResult += self.dropPanel.initBlok.parse()
        parserResult += '}'

        currentPath = os.path.dirname( os.path.realpath( __file__ ) )
        f = open(currentPath + 'untitled.cpp', 'w')
        f.write(headersString)
        f.write(parserResult)

        print('"A:/Vishwas/School/Class 12/CS Project/compiler/bin/g++" "' + currentPath +  'untitled.cpp" -o "' + currentPath + 'testfile.exe"')
        os.system('"' + currentPath + 'testfile.exe"')
        
