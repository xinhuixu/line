from __future__ import division
from display import *

'''
def draw_line( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0
    m = (y1 - y0) / (1.0 * (x1 - x0))
    b = y - m * x 
    while x < x1:
        plot( screen, color, x, len(screen) - y )
        x += 1 
        y = int(m * x + b)
'''        
        
def draw_line(screen, x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0
    m = abs(dy / dx)
    A = dy
    B = -1*dx
    print dy, dx, m, A, B
    
    if (dy > 0) and (dx > 0): #QUADRANT I
        if m <= 1: #OCTANT I    
            draw_line_I(screen, x0, y0, x1, y1, color, A, B);
        else: #OCTANT II
            draw_line_II(screen, x0, y0, x1, y1, color, A, B);
    elif (dy > 0) and (dx < 0): #QUADRANT II
        if m <= 1: #OCTANT IV
            draw_line_IV(screen, x0, y0, x1, y1, color, A, B);
        else: #OCTANT III
            draw_line_III(screen, x0, y0, x1, y1, color, A, B);
    elif (dy < 0) and (dx < 0): #QUADRANT III
        if m <= 1: #OCTANT V
            draw_line_V(screen, x0, y0, x1, y1, color, A, B);
        else: #OCTANT VI
            draw_line_VI(screen, x0, y0, x1, y1, color, A, B);
    elif (dy < 0) and (dx > 0):
        if m <= 1: #OCTANT VIII
            draw_line_VIII(screen, x0, y0, x1, y1, color, A, B);
        else: #OCTANT VII
            draw_line_VII(screen, x0, y0, x1, y1, color, A, B);
    
    else:
        draw_line_quadrantal(screen, x0, y0, x1, y1, color, A, B);
'''
II:
d=A+2B
while y < y1
   d<0
   x++
   d+=2A
y++
d+=2B

VII:

V:
like I but swapped
if x1 < x0 SWAP y1 < y0 SWAP
'''
def draw_line_quadrantal(screen, x0, y0, x1, y1, color, A, B):
    pass

def draw_line_I( screen, x0, y0, x1, y1, color, A, B):
    x = x0
    y = y0
    d = 2 * A + B
    while x < x1:
        plot( screen, color, x, len(screen) - y)
        if d > 0:
            y += 1
            d += 2 * B            
        x += 1
        d += 2 * A

def draw_line_II( screen, x0, y0, x1, y1, color, A, B):
    x = x0
    y = y0
    d = 2 * B + A
    while y < y1:
        plot( screen, color, x, len(screen) - y)
        if d < 0:
            x += 1
            d += 2 * A            
        y += 1
        d += 2 * B    

def draw_line_III( screen, x0, y0, x1, y1, color, A, B):
    pass

def draw_line_IV( screen, x0, y0, x1, y1, color, A, B):
    pass

def draw_line_V( screen, x0, y0, x1, y1, color, A, B):
    pass

def draw_line_VI( screen, x0, y0, x1, y1, color, A, B):
    pass

def draw_line_VII( screen, x0, y0, x1, y1, color, A, B):
    x = x0
    y = y0
    d = A - 2*B

    while y > y1:
        plot( screen, color, x, len(screen) - y)
        if d < 0:
            x += 1
            d += 2*A            
        y -= 1
        d -= 2*B

def draw_line_VIII( screen, x0, y0, x1, y1, color, A, B ):
    x = x0
    y = y0
    d = 2 * A - B

    while x < x1:
        plot( screen, color, x, len(screen) - y)
        if d < 0:
            y -= 1
            d -= 2 * B
            
        x += 1
        d += 2 * A
