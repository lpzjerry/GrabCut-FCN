import cv2
import numpy as np
import os
import sys

img_list = os.listdir('images')
img_list.sort()
w = open('all.txt','w')
for i in img_list:
	w.write(i+'\n')
