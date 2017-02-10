from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0
    m = (y1 - y0) / (1.0 * (x1 - x0))
    b = y - m * x 
    while x < x1:
        plot( screen, color, x, len(screen) - y )
        x += 1 
        y = int(m * x + b) #dont work bc non integer indices
        
        
def bresenham_draw_line( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0
    A = y1 - y0 #A = delta y
    B = -(x1 - x0) #B = -delta x
    d = 2 * A + B

    while x < x1:
        plot( screen, color, x, len(screen) - y)
        if d > 0:
            y += 1
            d += 2 * B
        x += 1
        d += 2 * A
