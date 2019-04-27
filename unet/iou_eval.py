import cv2
import numpy as np
import os
import sys

img_list = os.listdir('cropped/')
print(len(img_list))
#img_list = os.listdir(sys.argv[1])
sum_of_iou = 0.0
for i in img_list:
	pred = cv2.imread('cropped/'+i,0)
	#print('average',np.average(pred))
	true = cv2.imread('../dataset/test/masks/'+i,0)
	pred = np.where(pred>0.5, 1, 0).astype('uint8')
	true = np.where(true>0.5, 1, 0).astype('uint8')
	intersection = np.logical_and(true, pred)
	union = np.logical_or(true, pred)
	iou_score = np.sum(intersection) / np.sum(union)
	#print(np.sum(intersection), np.sum(union))
	sum_of_iou += iou_score
iou = sum_of_iou / len(img_list)

print("%d images, mean IoU = %f" % (len(img_list), iou))
