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
    if x0 > x1:
        #print "SWAP"
        tx = x1
        x1 = x0
        x0 = tx
        ty = y1
        y1 = y0
        y0 = ty
        
    dx = x1 - x0
    dy = y1 - y0
    if dx == 0:
        m = 'und'
    else:
        m = abs(dy / dx)
    A = dy
    B = -1*dx

    #print dy, dx, m, A, B
#    print "slope: ", m

    if m == 'und':
        draw_line_und(screen, x0, y0, x1, y1, color);
    elif (dy >= 0) and (dx >= 0): #QUADRANT I
        if m <= 1: #OCTANT I    
            draw_line_I(screen, x0, y0, x1, y1, color, A, B);
        else: #OCTANT II
            draw_line_II(screen, x0, y0, x1, y1, color, A, B);
    elif (dy > 0) and (dx < 0): #QUADRANT II
        if m <= 1: #OCTANT IV
            draw_line_VIII(screen, x0, y0, x1, y1, color, A, B);
        else: #OCTANT III
            draw_line_VII(screen, x0, y0, x1, y1, color, A, B);
    elif (dy <= 0) and (dx <= 0): #QUADRANT III
        if m <= 1: #OCTANT V
            draw_line_I(screen, x0, y0, x1, y1, color, A, B);
        else: #OCTANT VI
            draw_line_II(screen, x0, y0, x1, y1, color, A, B);
    elif (dy < 0) and (dx > 0):
        if m <= 1: #OCTANT VIII
            draw_line_VIII(screen, x0, y0, x1, y1, color, A, B);
        else: #OCTANT VII
            draw_line_VII(screen, x0, y0, x1, y1, color, A, B);
    
def draw_line_und( screen, x0, y0, x1, y1, color ):
    y = y0
    if y0 < y1:
        while y < y1:
            plot(screen, color, x0, len(screen)-y)
            y += 1
    elif y0 > y1:
        while y > y1:
            plot(screen, color, x0, len(screen)-y)
            y -= 1


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

def draw_line_VII( screen, x0, y0, x1, y1, color, A, B):
    x = x0
    y = y0
    d = A - 2*B

    while y > y1:
        plot( screen, color, x, len(screen) - y)
        if d > 0:
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
