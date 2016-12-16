import cv2
import numpy as np
import pyautogui as au
cap = cv2.VideoCapture(0)
 
while(1):
 
# Take each frame
  _, image = cap.read()
  image=cv2.flip(frame,1)
     
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
  
  lower_blue = np.array([60,100,90])#RGB value of the Object to be used for detection
  upper_blue = np.array([110,255,255])
  

  mask = cv2.inRange(hsv, lower_blue, upper_blue)
  mask = cv2.erode(mask, None, iterations=2) #to remove small blobs
  mask = cv2.dilate(mask, None, iterations=2)
 
  res = cv2.bitwise_and(image,image, mask= mask)
  imgray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
  ret,thresh = cv2.threshold(imgray,5,255,0)

  contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  areas = [cv2.contourArea(c) for c in contours]
  max_index = np.argmax(areas)
  cnt=contours[max_index]
  

  
  # hull = cv2.convexHull(cnt)
  # # k = cv2.isContourConvex(cnt)
  cv2.drawContours(frame,contours,-1, (0,255,0), -1)

  (x,y),radius = cv2.minEnclosingCircle(cnt)
  center = (int(x),int(y))
  radius = int(radius)
  cv2.circle(frame,center,radius,(0,0,255),-1)
  # print center
  au.moveTo(center[0]*5.13,center[1]*2.25)


  cv2.imshow('mask',image)# comment this out for smooth operation
 
  k = cv2.waitKey(5) & 0xFF
  if k == 27:#press esc to exit
    break
cv2.destroyAllWindows()
