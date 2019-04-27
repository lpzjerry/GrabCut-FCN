import cv2
import os
import numpy as np
r = open('rect.txt').readlines()

os.system('mkdir crop_images')
os.system('mkdir crop_labels')
for i in r:
	e = i.split()
	bbox = [int(e[1]),int(e[2]),int(e[3]),int(e[4])]
	img = cv2.imread('images/'+e[0])
	crop_img = img[bbox[1]:bbox[3], bbox[0]:bbox[2]]
	cv2.imwrite('crop_images/'+e[0],crop_img)
	img = cv2.imread('labels/'+e[0])
	crop_img = img[bbox[1]:bbox[3], bbox[0]:bbox[2]]
	cv2.imwrite('crop_labels/'+e[0],crop_img)
