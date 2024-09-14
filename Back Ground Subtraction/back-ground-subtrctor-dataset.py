import cv2
import numpy as np
from PIL import Image
import csv

cap = cv2.VideoCapture('yourvideo.mp4')

background = cv2.imread("background.jpeg", cv2.IMREAD_COLOR)

#_, first_frame = cap.read()
first_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)
_, first_gray = cv2.threshold(first_gray, 255, 255, cv2.THRESH_BINARY) 
first_gray     = cv2.resize(first_gray,(2320,1080))
cv2.imwrite('path-to-data'+str(22222)+'.jpeg',first_gray)

offset = 3
frame_count=0
counter = 0
#print("first_gray",first_gray.shape)
while True:
    

    _, frame   = cap.read()
    # Split
    red = frame[:, :, 0]
    counter = counter + 1
    
    
    orig_frame = frame.copy()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    #path for original img we need to train with them
    cv2.imwrite('path for original images'+str(frame_count)+'.jpeg',orig_frame)
    print(first_gray.shape)
    print("frame",gray_frame.shape)
    difference = cv2.absdiff(first_gray, gray_frame)
    _, difference = cv2.threshold(difference, 5, 255, cv2.THRESH_BINARY)          #150
    cv2.imshow("First frame", first_gray)
    cv2.imshow("Frame", frame)
    cv2.imshow("difference", difference)
    
    contours, hierarchy = cv2.findContours(difference, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #print(len(contours))
    #creating labels
    with open('path for labels'+str(frame_count)+'.txt', 'a', newline='') as file:
        writer = csv.writer(file,delimiter=' ')
        for contour in contours:
                    # continue through the loop if contour area is less than 500...
                    # ... helps in removing noise detection
            if cv2.contourArea(contour) <= 10:
                 continue
                    # get the xmin, ymin, width, and height coordinates from the contours
            (x, y, w, h) = cv2.boundingRect(contour)
            #print(x, y, w, h)
            # print("min max width hight",x,y,w,h)
            # draw the bounding boxes
            cv2.rectangle(orig_frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            #print("frame",orig_frame.shape)
            print("area",cv2.contourArea(contour))
            cv2.imshow('Detected Objects', orig_frame)

            #to check our labels is right or no we but them into our images to see how accurate it is
            cv2.imwrite('path to images with labels'+str(frame_count)+'.jpeg',orig_frame)

            # get labels ready for yolo formate
                
            if w >10 and h >10 :                                    
                offsetwidth=(h-w) if h > w else 0
                offsetheight=(w-h) if w > h else 0
                offsetwidth = int(offsetwidth / 2)
                offsetheight = int(offsetheight / 2)
                
                
                cropped_img=orig_frame[y-offsetheight-offset:y+h+offsetheight+offset,x-offsetwidth-offset:x+w+offsetwidth+offset]
                Xmin = x-offsetwidth-offset
                Xmax = x+w+offsetwidth+offset
                Ymin = y-offsetheight-offset
                Ymax = y+h+offsetheight+offset
                
               
                #print("cropped shap",cropped_img.shape)
                if cropped_img.shape[0]>10 and cropped_img.shape[1]>10:    
                    #save the croped item from original pics and its labels with respect to yolo
                    cv2.imwrite('croped labels img path'+str(frame_count)+'.jpeg',cropped_img)
                    #save labels into csv file
                    writer.writerow(["label name",Xmin, Ymin,Xmax, Ymax])
    file.close()
       
    frame_count = frame_count+1
    key = cv2.waitKey(10)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows

