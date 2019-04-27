import os
import cv2

if not os.path.exists('cropped/'):
	os.system('mkdir cropped/')
else:
	os.system('rm cropped/*')

img_list = os.listdir('../dataset/test/images/')
inlist = ''
outlist = ''
for img in img_list:
	inlist += '../dataset/test/images/' + img + ' '
	outlist += 'cropped/' + img + ' '
cmd = 'python ../unet/predict.py -i '+inlist+' -o '+outlist
os.system(cmd)
