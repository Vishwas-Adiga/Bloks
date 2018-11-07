import pygame
import os

currentPath = os.path.dirname( os.path.realpath( __file__ ) )

def backActionLight(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'back_action_light.png'))
    return pygame.transform.scale(asset, (width, height))

def backActionDark(height, width):
    return pygame.image.load(os.path.join(currentPath, 'back_action_dark.png'))
