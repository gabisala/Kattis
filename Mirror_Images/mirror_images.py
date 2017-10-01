
# -*- coding:utf-8 -*-

import sys

# Read data
data_input = []

for line in sys.stdin:
    data_input.append(line.split())

# Cut after number of test cases
data = data_input[1:]


# Extract images from data
def extract_image(data):

    images_extracted = []
    i = 0

    while i < len(data):

        cut = int(data[i][0])
        begin_cut = i + 1
        end_cut = begin_cut + cut

        image_line = data[begin_cut: end_cut]
        images_extracted.append(image_line)

        i = end_cut

    return images_extracted

images = extract_image(data)
flip_images = images[:]


# Flip images top to bottom
def top_to_bottom(images):

    top_to_bottom = []

    for image in images:

        flip = image[::-1]
        top_to_bottom.append(flip)

    return top_to_bottom

flip_top_to_bottom = top_to_bottom(flip_images)
flip_images_again = flip_top_to_bottom[:]


# Flip images left to right
def left_to_right(images):

    left_to_right_flip =[]

    for image in images:
        reversed_row = []

        for row in image:

            for pixel_line in row:
                reversed_pixel_line = pixel_line[::-1]
                reversed_row.append(reversed_pixel_line)

        left_to_right_flip.append(reversed_row)

    return left_to_right_flip

mirror_images = left_to_right(flip_images_again)

# Output mirrored images
for i, image in enumerate(mirror_images):
    print 'Test {}'.format(i + 1)
    for row in image:
        print row
