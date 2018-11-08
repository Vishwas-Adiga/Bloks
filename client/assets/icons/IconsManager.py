import pygame
import os

currentPath = os.path.dirname( os.path.realpath( __file__ ) )

def backActionLight(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'back_action_light.png'))
    return pygame.transform.scale(asset, (width, height))

def editActionLight(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'edit_action_light.png'))
    return pygame.transform.scale(asset, (width, height))

def backActionDark(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'back_action_dark.png'))
    return pygame.transform.scale(asset, (width, height))

def systemCategory(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'category_system.png'))
    return pygame.transform.scale(asset, (width, height))

def logicCategory(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'category_logic.png'))
    return pygame.transform.scale(asset, (width, height))

def mathCategory(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'category_math.png'))
    return pygame.transform.scale(asset, (width, height))

def controlCategory(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'category_control.png'))
    return pygame.transform.scale(asset, (width, height))

def interfaceCategory(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'category_interface.png'))
    return pygame.transform.scale(asset, (width, height))
