import cv2
import numpy as np
import random
from scipy import misc
def combine(inp,out):
	i=1
	for i in range(1,inp-1):
		im1="out/"+str(i)+".png"
		im2="out/"+str(i+1)+".png"
		img1=cv2.imread(im1)
		img2=cv2.imread(im2)
		vis=np.concatenate((img1,img2),axis=1)
		cv2.imwrite(im2,vis)
	oimg="captchaout/"+str(out)+".png"
	#cv2.imwrite(oimg,vis)

# 0. Read the image
	#image  = misc.imread(oimg,mode="L")

# 1. Add noises to the image
	noisy1 = vis + 3 * vis.std() * np.random.random(vis.shape)
	cv2.imwrite(oimg,noisy1)
	print oimg



		
	
