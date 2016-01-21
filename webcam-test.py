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
def draw_closing_lines(img, contours):
    for cont in contours:
        v1 = (np.roll(cont, -2, axis=0) - cont)
        v2 = (np.roll(cont, 2, axis=0) - cont)
        dotprod = np.sum(v1 * v2, axis=2)
        norm1 = np.sqrt(np.sum(v1 ** 2, axis=2))
        norm2 = np.sqrt(np.sum(v2 ** 2, axis=2))
        cosinus = (dotprod / norm1) / norm2
        indexes = np.where(0.95 < cosinus)[0]
        if len(indexes) == 1:
            # only one u-turn found, mark in yellow
            cv2.circle(img, tuple(cont[indexes[0], 0]), 3, (0, 255, 255))
        elif len(indexes) == 2:
            # two u-turns found, draw the closing line
            cv2.line(img, tuple(tuple(cont[indexes[0], 0])), tuple(cont[indexes[1], 0]), (0, 0, 255))
        else:
            # too many u-turns, mark in red
            for i in indexes:
                cv2.circle(img, tuple(cont[i, 0]), 3, (0, 0, 255))
cap = cv2.VideoCapture(0) #Mess with this to get externel usb cam

while True:
  ret, frame = cap.read()
  frame = cv2.resize(frame,(720,405))
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  blurred = cv2.GaussianBlur(gray,(3,3),0) # remove noise

  th3 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,33,2) # second from last var is block size
  
  auto = auto_canny(th3,1)#get edge

  im2, contours, hierachy = cv2.findContours(auto,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # find continous lines

  sort_key = lambda  cnt: cv2.arcLength(cnt,True) # assume closed, sort by arc lengeth
  cnts = sorted(contours,key=sort_key)[-2:] # Only want largest 2 contour
  cv2.drawContours(frame,cnts,-1,(0,255,0),3)#draw on orig
  draw_closing_lines(frame,cnts)
  cv2.imshow('bg',frame)

  if (cv2.waitKey(1) == ord('q')):
    break
