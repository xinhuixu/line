from display import *
from draw import *

s = new_screen()

org = 250
right = top = 500
left = bottom = 0

draw_line(s,left,bottom,right,top,[0,255,0])
draw_line(s,left,top,right,bottom,[0,255,0])
draw_line(s,org,top,org,bottom,[0,0,255])
draw_line(s,left,org,right,org,[0,0,255])
print '------------------'

draw_line(s,org,org,right,org+100,[255,204,153]) #I
draw_line(s,org,org,org+100,top,[255,204,153]) #II
draw_line(s,org,org,org-100,top,[255,204,153]) #III
draw_line(s,org,org,left,org+100,[255,204,153]) #IV
draw_line(s,org,org,left,org-100,[255,204,153]) #V
draw_line(s,org,org,org-100,bottom,[255,204,153]) #VI
draw_line(s,org,org,org+100,bottom,[255,204,153]) #VII
draw_line(s,org,org,right,org-100,[255,204,153]) #VIII


display(s)
save_extension(s, 'img.png')
print "!image saved as img.png"
