import cv2
import numpy as np
import os
import sys

r1 = open('all.txt').readlines()
r2 = open('test.txt').readlines()
w = open('train.txt','w')
for i in r1:
	if not i in r2:
		w.write(i)