from display import *
from draw import *

def main(x0, y0, x1, y1, color, algo):
    screen = new_screen()
    #color = [ 0, 255, 0 ]
    if algo == 'b':
        bresenham_draw_line(screen, x0, y0, x1, y1, color)
    elif algo == 'm':
        draw_line(screen, x0, y0, x1, y1, color)
    else:
        print 'error'    
    display(screen)
    save_extension(screen, 'img.png')

main(0,0,400,200,[0,255,0],'b')
main(0,0,400,200,[255,0,0],'m')
