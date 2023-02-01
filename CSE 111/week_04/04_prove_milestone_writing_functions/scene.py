"""
Made by Brady Hodge
CSE 111
03 Prove Milestone: Writing Functions
"""

# import functions to draw the scene 
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

# import randint to generate random numbers for the clouds, stars, ect.
from random import randint

def main():

    # define scene width and height
    scene_width = 800
    scene_height = 500

    
    # start the drawing
    canvas = start_drawing("Scene", scene_width, scene_height)
    
    # draw the sky and ground (and the functions included in them)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    
    # finish the drawing
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="#031742")

    # define where the stars will be
    min_x = 0
    max_x = 800
    min_y = 0
    max_y = 500
    draw_stars(canvas, min_x, max_x, min_y, max_y)

    # define where the moon will be
    moon_center_x = 700
    moon_center_y = 400
    moon_radius = 50
    draw_moon(canvas, moon_center_x, moon_center_y, moon_radius)

    # define where the clouds will be
    min_x = -20
    max_x = 730
    min_y = 300
    max_y = 400
    draw_clouds(canvas, min_x, max_x, min_y, max_y)

def draw_clouds(canvas, min_x, max_x, min_y, max_y):
    """Draw random clouds in the sky."""
    diameter = 25
    for i in range(2):
        # draw larger clouds
        x = randint(min_x, max_x)
        y = randint(min_y, max_y)
        diameter = randint(10, 50)
        draw_oval(canvas, x, y, x + diameter * randint(2, 20), y + diameter, fill="#858585")

        # draw smaller clouds 
        x = randint(min_x, max_x)
        y = randint(min_y, max_y)
        diameter = randint(10, 50)
        draw_oval(canvas, x, y, x + diameter * randint(5, 10), y + diameter, fill="#858585")


def draw_stars(canvas, min_x, max_x, min_y, max_y):
    """Draw random stars in the sky."""
    
    for i in range(1000):
        diameter = randint(1, 3)
        x = randint(min_x, max_x)
        y = randint(min_y, max_y)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="#FFFFFF")


def draw_moon(canvas, moon_center_x, moon_center_y, moon_radius):
    draw_oval(canvas, moon_center_x - moon_radius, moon_center_y - moon_radius, moon_center_x + moon_radius, moon_center_y + moon_radius, outline="gray20", width=1, fill="#FFFFFF")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    
    # draw the dirt
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="#042407")
    
    draw_grass(scene_height, scene_width, canvas)

    # define where the first tree will be
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # define where the second tree will be
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)


def draw_grass(scene_height, scene_width, canvas):
    """Draw the grass. randomly"""
    third_height = round(scene_height / 3)
    min_diam = 15
    max_diam = 30
    
    # draw light(ish) grass
    for i in range(100000):
        x = randint(0, scene_width - max_diam)
        y = randint(0, third_height)
        diameter = randint(min_diam, max_diam)
        draw_arc(canvas, x, y, x + diameter, y + diameter,
                outline="#10641d")
    
    # draw darker grass
    for i in range(10000):
        x = randint(0, scene_width - max_diam)
        y = randint(0, third_height)
        diameter = randint(min_diam, max_diam)
        draw_arc(canvas, x, y, x + diameter, y + diameter,
                outline="#0a5712")
    
    # draw darkest grass
    for i in range(1000):
        x = randint(0, scene_width - max_diam)
        y = randint(0, third_height)
        diameter = randint(min_diam, max_diam)
        draw_arc(canvas, x, y, x + diameter, y + diameter,
                outline="#0a5712")


def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree."""
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    
    draw_polygon(canvas, center_x, skirt_top, skirt_right, trunk_top, skirt_left, trunk_top, outline="#000000", width=1, fill="#044a18")

main()