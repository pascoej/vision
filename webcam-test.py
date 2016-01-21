#Test to see if we can get lines from rope / cord 
#in opencv

import cv2
import numpy as np

def auto_canny(image,sigma=.33):
  v = np.median(image)
  lower = int(max(0,(1.0-sigma)*v))
  upper = int(min(255,(1.0+sigma)*v))
  edged = cv2.Canny(image,lower,upper)
  return edged

cap = cv2.VideoCapture(0) #Mess with this to get externel usb cam

while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  blurred = cv2.GaussianBlur(gray,(3,3),0) # remove noise

  th3 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,2) # second from last var is block size
  
  auto = auto_canny(th3,1)#get edge

  cv2.imshow('ok',auto)
  im2, contours, hierachy = cv2.findContours(auto,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # find continous lines

  sort_key = lambda  cnt: cv2.arcLength(cnt,True) # assume closed, sort by arc lengeth
  cnts = sorted(contours,key=sort_key)[-2:] # Only want largest 2 contour
  cv2.drawContours(frame,cnts,-1,(0,255,0),3)#draw on orig
  cv2.imshow('bg',frame)

  if (cv2.waitKey(1) == ord('q')):
    break
