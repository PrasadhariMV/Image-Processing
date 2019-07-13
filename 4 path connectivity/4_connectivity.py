import cv2 as cv
import numpy as np
import math


def create_points(n_sides, radius):
    points = []
    x_center = 300
    y_center = 200
    angle = 0
    angle_increment = (2 * 3.142) / n_sides
    for i in range(n_sides):
        points.append((x_center + radius * math.cos(angle), y_center + radius * math.sin(angle)))
        angle += angle_increment
    return (np.array(points, dtype='int32'))


def create_image(sides, color,object_color):
    blank_image = np.zeros((400, 600, 3), dtype=np.uint8)
    blank_image[:] = (255, 255, 255)

    points = create_points(sides, 100)
    cv.fillConvexPoly(blank_image, points, object_color)
    for i in range(sides - 1):
        cv.line(blank_image, tuple(points[i]), tuple(points[i + 1]), color, thickness=1)
    cv.line(blank_image, tuple(points[sides - 1]), tuple(points[0]), color, thickness=1)
    return blank_image, points[0]


def make_4_connectivity(image, point, clr, color,object_color):
    # clr = 8 connectivity color
    last_done = [-1, -1]
    current = point[::-1]
    while True:
        image_segment = image[current[0]-1:current[0]+2 , current[1]-1:current[1]+2]
        done = False
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                if (image_segment[i,j] == clr).all() == True:
                    location = np.array([current[0]+i - 1,current[1]+j-1])
                    if (location == last_done).all() == True:
                        continue
                    if location[0] - current[0] == 0 or location[1] - current[1] == 0:
                        done =True
                        last_done = current
                        current = location
                        break
                    if (image[current[0]+(location[0] - current[0]),current[1]] == object_color).all() == True or (image[current[0]+(location[0] - current[0]),current[1]] == color).all() == True:
                        image[current[0] + (location[0] - current[0]), current[1]] = color
                        last_done = current
                        current = location
                        done = True
                        break
                    elif (image[current[0] , current[1] + (location[1] - current[1])]==object_color).all() == True or (image[current[0] , current[1] + (location[1] - current[1])]==color).all() == True:
                        image[current[0], current[1] + (location[1] - current[1])] = color
                        last_done = current
                        current = location
                        done = True
                        break
            if done == True:
                break
        image[current[0], current[1]] = color
        if (current == point[::-1]).all() == True:
            break
    return image


sides = 10
color_8 = (0, 51, 0)
color_4 = (0, 0, 255)
object_color = (255,255,102)
image, start_point = create_image(sides, color_8,object_color)
cv.namedWindow('Original Image')
cv.imshow('Original Image', image)
changed_image = make_4_connectivity(image.copy(), start_point, color_8, color_4,object_color)
cv.namedWindow('Altered Image')
cv.imshow('Altered Image', changed_image)
cv.waitKey(0)
cv.destroyAllWindows()
