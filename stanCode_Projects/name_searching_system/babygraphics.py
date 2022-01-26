"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # count the average width of each year
    avg_width = int((width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS))
    x_position = GRAPH_MARGIN_SIZE + year_index * avg_width
    return x_position


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    returns the y coordinate where the rank should be drawn.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The y coordinate of the rank.
    """
    # if rank is greater than MAX the y position would at the bottom of the graph
    if int(rank) > MAX_RANK:
        y_coordinate = height - GRAPH_MARGIN_SIZE
    # if not count the y position
    else:
        y_coordinate = GRAPH_MARGIN_SIZE + int((height / MAX_RANK) * int(rank))

    return y_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # draw the top of the margin
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # draw the bottom of the margin
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    # draw the left of the margin
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    # draw the line of each year
    for i in range(0, len(YEARS)):
        x_position = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_position, 0, x_position, CANVAS_HEIGHT)
        canvas.create_text(x_position + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anch=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    name_list = []
    for name in lookup_names:
        # count the name to draw the color orderly
        name_list.append(name)
        num = (len(name_list) - 1) % 4
        color = COLORS[num]
        if name in name_data:
            # save every year position in the following list
            x_positions = []
            y_positions = []
            for y in range(len(YEARS)):
                # if there is data of the year
                if str(YEARS[y]) in name_data[name].keys():
                    x_pos = get_x_coordinate(CANVAS_WIDTH, y)
                    y_pos = get_y_coordinate(CANVAS_HEIGHT, name_data[name][str(YEARS[y])])
                    x_positions.append(x_pos)
                    y_positions.append(y_pos)
                    canvas.create_text(x_pos + TEXT_DX, y_pos,
                                       text=name + ' ' + name_data[name][str(YEARS[y])],
                                       anch=tkinter.NW, fill=color)
                    # year of '1900' no need to draw the line
                    if y is not 0:
                        canvas.create_line(x_positions[y - 1], y_positions[y - 1], x_pos, y_pos,
                                           width=LINE_WIDTH, fill=color)
                # if there is no data of the year
                else:
                    x_pos = get_x_coordinate(CANVAS_WIDTH, y)
                    y_pos = get_y_coordinate(CANVAS_HEIGHT, MAX_RANK + 1)
                    x_positions.append(x_pos)
                    y_positions.append(y_pos)
                    canvas.create_text(x_pos + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2,
                                       text=name + ' *', anch=tkinter.NW, fill=color)
                    # year of '1900' no need to draw the line
                    if y is not 0:
                        canvas.create_line(x_positions[y - 1], y_positions[y - 1], x_pos, y_pos,
                                           width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
