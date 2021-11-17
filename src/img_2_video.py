import cv2
import numpy as np
import glob
 
total = 1

img_array = []
for filename in glob.glob('/home/chungyu/test_ws/src/bag_to_video/images/*.png'):
    # img = cv2.imread(filename)
    # height, width, layers = img.shape
    # size = (width,height)
    # img_array.append(img)
    print(total)
    total = total + 1
 
for i in range(1, total):
    # print(i)
    path = "/home/chungyu/test_ws/src/bag_to_video/images/"
    str_index = str(i)
    filename = path + str_index + ".png"
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 13, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
