# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:26:15 2022

@author: Omar
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:33:19 2022

@author: Omar
"""

import cv2  
from PIL import Image
import glob
import numpy as np
image_list=[]

main_id = 0

target_dir = "your target directory/"
for filename in glob.glob(target_dir + "*.jpg"):
    if "#" in filename:
        continue
    main_id += 1
    image=Image.open(filename)
    

    image_list.append(image)
    image_data = np.asarray(image) 
    #edged = cv2.Canny(image, 10, 250) 
    #scale_percent = 0.30769230769230769230769230769231
    scale_percent = 1280.0/image_data.shape[1]
    
    #calculate the 50 percent of original dimensions
    width = int(image_data.shape[1] * scale_percent )
    height = int(image_data.shape[0] * scale_percent)
    
    # dsize
    dsize = (width, height)
    
    # resize image
    resized = cv2.resize(image_data, dsize)

    
    #convert BGR TO RGB if neccessary depends on camera
    image_data = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    # bluring using gaussian filter
    blurred = cv2.GaussianBlur(resized, (5,5), 0)

    #canny edge detection
    edged = cv2.Canny(blurred, 10, 250) 
   
    _,cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    sub_id = 0 
    offset = 20
    for c in cnts:
            x,y,w,h = cv2.boundingRect(c) 
            if w>50 and h>50: 
                sub_id+=1 
                new_img=image_data[y-offset:y+h+offset,x-offset:x+w+offset]
                filename = filename.rsplit( ".jpg", 1 )[ 0 ]
                print(filename)
                cv2.imwrite(filename+ "#" +str(sub_id) + '.png', new_img)
        
         
	     
	     	    
	   
		          
    
#cv2.imshow("im",image_data) 
#cv2.waitKey(0) 