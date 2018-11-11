import pygame
import os

currentPath = os.path.dirname( os.path.realpath( __file__ ) )

def shadowBottom(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'shadow_bottom.png'))
    return pygame.transform.scale(asset, (width, height))

def dustbin(height, width):
    asset = pygame.image.load(os.path.join(currentPath, 'dustbin.png'))
    return pygame.transform.scale(asset, (width, height))
