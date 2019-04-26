
# coding: utf-8

# In[4]:


import numpy as np
import cv2 as cv
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
import glob
import itertools


# In[62]:


images = [cv.imread(file) for file in glob.glob("Data/png/images/*.png")]
masks = [cv.imread(file) for file in glob.glob("Data/images-labels/*.png")]
fnames = [glob.glob("Data/png/images/*.png")]
fnames = list(itertools.chain.from_iterable(fnames))

fnames_anno = [glob.glob("Data/images-labels/*.png")]
fnames_anno = list(itertools.chain.from_iterable(fnames_anno))

fnames_old = [glob.glob("Data/images/*.jpg")]
fnames_old = list(itertools.chain.from_iterable(fnames_old))

rects = [(150,30,300,300),(80,80,500,300),(10,50,350,300),(50,5,300,500),(50,5,300,500),(20,150,250,450),(120,80,400,300),
         (150,100,350,250),(30,50,250,450),(200,0,350,320),(130,30,250,320),(100,190,250,400),(170,30,350,300),(70,10,400,200),
         (10,90,260,400),(90,60,300,450),(180,30,350,320),(5,0,430,320),(100,50,400,150),(100,80,380,180),(100,100,400,230),
         (80,150,500,250),(50,80,450,250),(50,120,450,250),(10,100,480,230),(50,10,350,300),(10,10,500,350),(300,130,420,300),
         (10,20,600,430),(20,80,600,450),(20,80,600,450),(50,50,450,320),(100,200,230,350),(50,50,480,300),(0,100,220,350),
         (100,100,320,230),(150,150,380,350),(20,70,480,350),(0,120,250,500),(80,250,380,430),(200,120,500,300),(200,150,400,400),
         (270,10,420,300),(250,60,370,160),(90,200,500,350),(130,150,450,220),(80,40,600,450),(180,150,500,450),(150,50,350,550),
         (100,320,280,450),(80,100,400,350),(290,0,500,280),(100,100,350,250),(180,150,290,250),(90,100,340,250),(90,120,490,350),
         (90,200,320,350),(50,360,350,500),(200,120,450,300),(100,140,320,250),(120,60,320,300),(100,40,400,350),(80,70,300,350),
         (150,70,330,180),(170,70,380,350),(200,130,400,300),(180,50,500,350),(100,30,550,430),(80,200,300,480),(80,200,200,250),
         (120,10,300,600),(60,0,280,500),(100,100,380,350),(200,70,400,300),(0,20,450,500),(100,50,500,500),(150,70,450,400),
         (10,50,600,500),(170,150,320,450),(10,50,600,500),(0,50,800,600),(100,0,800,600),(150,40,300,300),(100,100,400,300),
         (200,0,300,230),(100,120,360,350),(80,180,320,500),(100,90,400,300),(10,25,250,220),(0,100,250,350),(250,100,350,200),
         (20,140,140,220),(130,200,250,300),(150,30,550,450),(70,70,600,450),(100,120,500,450),(160,200,300,550),(300,60,500,450),
         (100,150,210,480),(150,120,300,500),(150,100,280,450),(50,80,650,500),(0,0,450,400),(300,0,500,400),(100,50,350,300),
         (100,150,220,400),(50,20,250,370),(100,50,430,300),(100,50,430,300),(250,140,400,350),(290,0,390,300),(200,0,390,300),
         (90,40,500,300),(220,150,310,300),(200,150,320,350),(40,120,150,260),(330,100,430,400),(270,50,500,400),(210,20,360,300),
         (250,20,380,350),(390,50,500,300),(200,50,500,400),(100,80,250,400),(280,70,500,400),(170,60,400,350),(100,50,300,250),
         (170,150,300,330),(350,50,500,350),(200,150,350,400),(180,0,250,300),(20,150,120,270),(210,130,290,220),(0,50,290,340),
         (20,100,250,330),(80,100,250,480),(20,50,600,430),(150,180,300,400),(0,70,190,200),(50,120,300,300),(100,170,330,280),
         (150,140,400,300),(30,150,200,280),(200,50,480,430),(200,10,480,430),(50,50,230,330),(150,100,300,460),(0,40,210,250),
         (0,50,400,260),(50,80,500,150),(100,60,450,300),(190,200,430,270)]


for i in range(151):
    
    img = images[i]
    print(fnames[i],i)
    plt.figure()
    img = img[:,:,[2,1,0]]
    plt.imshow(img),plt.colorbar(),plt.show()
    
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    
    height, width, channels = img.shape
    print(height,width)
    
    rect = (0,0,width-1,height-1)
    cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    plt.figure()
    img = img[:,:,[2,1,0]]
    plt.imshow(img),plt.colorbar(),plt.show()
    cv.imwrite('grabcut_anno/result_rect/' + fnames[i][16:], img)
    #li = cv.LineIterator(img, (0, 0), (img.rows, img.cols)) #So loop the entire matrix

    
    '''
    for x in range(height):
        for y in range(width):
            (r,g,b) = img[x,y] # 这里可以处理每个像素点
            if r>0 or g>0 or b>0:
                r = 255
                g = 255
                b = 255
                img[x,y] = (r,g,b)
    plt.imshow(img),plt.colorbar(),plt.show()
    cv.imwrite('grabcut_nothing/mask_binary/' + fnames[i][16:], img)
    '''
    
   
    print(fnames_anno[i],i)
    newmask = masks[i]
    plt.imshow(newmask),plt.colorbar(),plt.show()
    
    # wherever it is marked white (sure foreground), change mask=1
    # wherever it is marked black (sure background), change mask=0
    mask[(newmask[:,:,2] == 255)] = 1
    mask[(newmask[:,:,2] == 219)] = 0
    plt.imshow(mask),plt.colorbar(),plt.show()
    cv.imwrite('grabcut_anno/mask_anno/' + fnames[i][16:], (mask)/3.0*255)
    mask, bgdModel, fgdModel = cv.grabCut(img,mask,None,bgdModel,fgdModel,5,cv.GC_INIT_WITH_MASK)
    mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    plt.imshow(mask),plt.colorbar(),plt.show()
    cv.imwrite('grabcut_anno/mask_binary/' + fnames[i][16:], mask*255)
    
    img = img*mask[:,:,np.newaxis]
    plt.imshow(img),plt.colorbar(),plt.show()
    cv.imwrite('grabcut_anno/result_anno/' + fnames[i][16:], img)


# annotation 顔色
# 
# background: 紅色:(0B,0G,219R)
# foreground: 米白色:(207B,255G,255R)
