"""
Made by Brady Hodge
CSE 111
03 Prove Milestone: Writing Functions
"""

"""
TO DO:
    - fix def draw_mountain (optional)
    - fix def draw_clouds
"""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="#031742")

    draw_stars(canvas)
    draw_moon(canvas)
    draw_clouds(canvas)

def draw_clouds(canvas):
    """Draw clouds in the sky."""
    diameter = 25
    for i in range(2):
        diameter = random.randint(10, 50)
        x = random.randint(-20, 730)
        y = random.randint(300, 400)
        
        draw_oval(canvas, x, y, x + diameter * random.randint(2, 20), y + diameter, fill="#858585")

        x = random.randint(-20, 730)
        y = random.randint(300, 400)
        diameter = random.randint(10, 50)
    
        draw_oval(canvas, x, y, x + diameter * random.randint(5, 10), y + diameter, fill="#858585")


def draw_stars(canvas):
    """Draw stars in the sky."""
    
    for i in range(1000):
        diameter = random.randint(1, 3)
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="#FFFFFF")


def draw_moon(canvas):
    moon_center_x = 700
    moon_center_y = 400
    moon_radius = 50
    draw_oval(canvas, moon_center_x - moon_radius,
            moon_center_y - moon_radius,
            moon_center_x + moon_radius,
            moon_center_y + moon_radius,
            outline="gray20", width=1, fill="#FFFFFF")

def draw_mountain(canvas): # not currently working
    """Draw a mountain."""
    for x in range(10):
        x0 = 25
        y0 = 170
        x1 = 75
        y1 = 270
        x2 = 125
        y2 = 170

        draw_polygon(canvas, x0, y0, x1, y1, x2, y2,
        width=1, outline="black", fill="#222222")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="#042407")

    # Draw grass.
    draw_grass(scene_height, scene_width, canvas)

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

def draw_grass(scene_height, scene_width, canvas):

    third_height = round(scene_height / 3)
    min_diam = 15
    max_diam = 30
    # Draw grass
    for i in range(100000):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, third_height)
        diameter = random.randint(min_diam, max_diam)
        draw_arc(canvas, x, y, x + diameter, y + diameter,
                outline="#10641d")
    
    for i in range(10000):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, third_height)
        diameter = random.randint(min_diam, max_diam)
        draw_arc(canvas, x, y, x + diameter, y + diameter,
                outline="#0a5712")
    
    for i in range(1000):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, third_height)
        diameter = random.randint(min_diam, max_diam)
        draw_arc(canvas, x, y, x + diameter, y + diameter,
                outline="#0a5712")


def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="#000000", width=1, fill="#044a18")

def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    # draw_mountain(canvas)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Call the main function so that
# this program will start executing.
main()