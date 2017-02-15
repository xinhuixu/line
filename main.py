from display import *
from draw import *

s = new_screen()
org = 250
right = top = 500
left = bottom = 0

def default():
    draw_line(s,left,bottom,right,top,[0,255,0])
    draw_line(s,left,top,right,bottom,[0,255,0])
    draw_line(s,org,top,org,bottom,[0,0,255])
    draw_line(s,left,org,right,org,[0,0,255])
    draw_line(s,org,org,right,org+125,[255,0,0]) #I
    draw_line(s,org,org,org+125,top,[255,0,0]) #II
    draw_line(s,org,org,org-125,top,[255,0,0]) #III
    draw_line(s,org,org,left,org+125,[255,0,0]) #IV
    draw_line(s,org,org,left,org-125,[255,0,0]) #V
    draw_line(s,org,org,org-125,bottom,[255,0,0]) #VI
    draw_line(s,org,org,org+125,bottom,[255,0,0]) #VII
    draw_line(s,org,org,right,org-125,[255,0,0]) #VIII
'''
default()
display(s)
save_extension(s, 'img.png')
print "!image saved as img.png"
'''
s = new_screen()
def gallery():
    #triangle
    draw_line(s,org,org+100,org-85,org-50,[255,255,255])
    draw_line(s,org,org+100,org+85,org-50,[255,255,255])
    draw_line(s,org-85,org-50,org+85,org-50,[255,255,255])
    #incoming
    draw_line(s,left,org-30,org,org+30,[255,255,255]) 
    #rainbow
    i = 0
    y = 18
    while i<15:
        draw_line(s,org,org+30,right,org+y,[255,0,0])
        y-=1
        i+=1

gallery()
display(s)
save_extension(s, 'gal.png')
