from pygame import *

def roundedRectangle(rect, colour, radius = 0.2):    
    rect = Rect(rect)
    colour = Color(*colour)
    alpha = colour.a
    colour.a = 0
    pos = rect.topleft
    rect.topleft = 0,0
    rectangle = Surface(rect.size,SRCALPHA)
    circle = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius = rectangle.blit(circle,(0,0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(colour,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)
    return rectangle


