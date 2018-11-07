from pygame import *

class RoundedButton:
    
    pos = None
    rectangle = None
    def __init__(self, rect, colour, radius = 0.2):
        rect = Rect(rect)
        colour = Color(*colour)
        alpha = colour.a
        colour.a = 0
        self.pos = rect.topleft
        rect.topleft = 0,0
        self.rectangle = Surface(rect.size,SRCALPHA)
        circle = Surface([min(rect.size)*3]*2,SRCALPHA)
        draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
        circle = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

        radius = self.rectangle.blit(circle,(0,0))
        radius.bottomright = rect.bottomright
        self.rectangle.blit(circle,radius)
        radius.topright = rect.topright
        self.rectangle.blit(circle,radius)
        radius.bottomleft = rect.bottomleft
        self.rectangle.blit(circle,radius)

        self.rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
        self.rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

        self.rectangle.fill(colour,special_flags=BLEND_RGBA_MAX)
        self.rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

    def draw(self, surface):
        return surface.blit(self.rectangle, self.pos)

