from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

add_box(polygons,200,200,50,100,100,0)

clear_screen(screen)
draw_lines(edges, screen, color)
draw_polygons(polygons, screen, color)
display(screen)
save_extension(screen, pic.png)

parse_file( 'script', edges, polygons, csystems, screen, color )
