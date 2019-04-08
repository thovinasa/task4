import cv2
import numpy as np
import random
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
	for i in range(100):
		a= random.randint(1, 400)
		b= random.randint(1, 100)
		cv2.circle(vis,(a,b), 2, (0,0,254), -1)
		cv2.imwrite(oimg,vis)
	print oimg



		
	
