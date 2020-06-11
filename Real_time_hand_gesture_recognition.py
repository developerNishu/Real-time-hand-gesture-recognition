#!/usr/bin/python

#Real time hand gesture recognition program using python3-opencv(cv2)
#Video sequence is just a collection of frames or collection of images that runs with respect to time.
#Make code stare at background without hand
#Bring hand in foreground with background
#Apply background-subtraction
#Thresholding is the assigment of pixel intensities to 0’s and 1’s based a particular threshold level so that our object of interest alone is captured from an image.
#Contour is the outline or boundary of an object located in an image.

#--------------------------------------------------------------------------------------------------
import cv2
import numpy as np
import math
import sys

cap = cv2.VideoCapture(0)

flag_data1 = 1
flag_data2 = 2
flag_display = 1
data1=0
data2=0

while(cap.isOpened()):
    ret, img = cap.read()
    cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
    crop_img = img[100:300, 100:300]
    #crop_img = cv2.flip(crop_img,0)
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('Thresholded', thresh1)
    #_ , contours, _ = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
    contours, _ = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
            cv2.CHAIN_APPROX_NONE)
    max_area = -1
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i
    cnt=contours[ci]
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop_img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    #cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img,far,1,[0,0,255],-1)
        #dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(crop_img,start,end,[0,255,0],2)
        #cv2.circle(crop_img,far,5,[0,0,255],-1)
        
    if count_defects == 0:
        # cv2.putText(img,"I'M NISHANT SHARMA", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        cv2.putText(img,"HEY! I'M NISHANT SHARMA", (50,50),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
        
    elif count_defects == 1:
        cv2.putText(img, "THIS IS two", (5,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
    elif count_defects == 2:
        cv2.putText(img,"This is Three (:", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
    elif count_defects == 3:
        cv2.putText(img,"This is four", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
    elif count_defects == 4:
        cv2.putText(img,"This is five", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
    
    else:
        cv2.putText(img,"GOOD AFTERNOON TEACHERS", (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
    if count_defects > 0:
        if flag_data1  == 1 and flag_data2 == 2:
            data1 = count_defects+1
            flag_data1 = 2
            flag_data2 = 1
        elif flag_data1  == 2 and flag_data2 == 1:
            data2 = count_defects+1
            flag_data1 = 1
            flag_data2 = 2
    
        Sum = data1 + data2

        message = str(data1) + '+' + str(data2) + "=" + str(Sum)
        cv2.putText(img, message, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)

        '''
        if flag_display == 1:
            flag_display += 1

        if flag_display >= 1:
            flag_display = 1 
            data1 = 0
        '''    
            
    #print(str(data1) + '+' + str(data2) + "=" + str(Sum))
    cv2.imshow('drawing', drawing)
    cv2.imshow('end', crop_img)

    cv2.imshow('Gesture', img)
    all_img = np.hstack((drawing, crop_img))
    #cv2.imshow('Contours', all_img)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
sys.exit()
