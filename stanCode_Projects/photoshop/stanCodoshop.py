"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    dist = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    rgb = []
    pixels_red = 0
    pixels_green = 0
    pixels_blue = 0
    # sum all the elements of rge in the pixels
    for pixel in pixels:
        pixels_red += pixel.red
        pixels_green += pixel.green
        pixels_blue += pixel.blue
    # average the pixels and add to the list of rgb
    rgb.append(int(pixels_red / len(pixels)))
    rgb.append(int(pixels_green / len(pixels)))
    rgb.append(int(pixels_blue / len(pixels)))
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    rgb = get_average(pixels)
    dist = []
    # save all the distance in a list
    for pixel in pixels:
        dist_pixel = get_pixel_dist(pixel, rgb[0], rgb[1], rgb[2])
        dist.append(dist_pixel)
    # find the smallest of the distance
    best_index = dist.index(min(dist))
    # find the pixel index of the smallest distance
    best_pixel = pixels[best_index]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # save all the position in a list
    position = []
    for x in range(width):
        for y in range(height):
            position.append([x, y])

    for i in position:
        # save all the pixel in the pixels list
        pixels = []
        # find all the pixel in the image
        for image in images:
            pixel = image.get_pixel(i[0], i[1])
            pixels.append(pixel)
        best = get_best_pixel(pixels)

        # fill the best pixel in the result image
        r_p1 = result.get_pixel(i[0], i[1])
        g_p1 = result.get_pixel(i[0], i[1])
        b_p1 = result.get_pixel(i[0], i[1])

        r_p1.red = best.red
        g_p1.green = best.green
        b_p1.blue = best.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
