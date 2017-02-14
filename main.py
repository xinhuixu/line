from display import *
from draw import *

screen = new_screen()

draw_line(screen,250,250,500,350,[255,153,153]) #I
draw_line(screen,250,250,350,500,[255,204,153]) #II
draw_line(screen,250,250,350,500,[255,204,153]) #III
draw_line(screen,250,250,350,0,[255,204,153]) #VII
draw_line(screen,250,250,500,150,[255,204,153]) #VIII


display(screen)
save_extension(screen, 'img.png')
