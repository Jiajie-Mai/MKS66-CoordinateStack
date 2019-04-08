from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 200, 150, 100]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

parse_file( 'script1', edges, polygons, csystems, screen, color )
