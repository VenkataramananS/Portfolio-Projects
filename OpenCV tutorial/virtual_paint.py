import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,100) #adjusting brightness

myColors = [
    # [0,179,0,42,90,255], # white
    # [0,23,41,255,0,255], # brown
    [170,179,87,255,127,255], # red
    [101,109,131,255,0,255], # blue
    [33,74,109,245,87,241], # green
    [23,30,75,221,130,255], # yellow
    [46,179,55,145,139,255] # pink
]
myBorderValues = [ # bgr color codes
    [255,6,6],
    [6,31,255],
    [3,172,54],
    [255,249,34],
    [255,0,213]
]
pointsPalaced = []  #x,y,colorID

def findColor(img,myColors,myBorderValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContour(mask)
        cv2.circle(imgResult,(x,y),10,myBorderValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
    return newPoints

def getContour(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
        peri = cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCamera(pointsPalaced,myBorderValues):
    for point in pointsPalaced:
        cv2.circle(imgResult,(point[0],point[1]),10,myBorderValues[point[2]],cv2.FILLED)



while True:
    success,img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myBorderValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            pointsPalaced.append(newP)
    if len(pointsPalaced)!=0:
        drawOnCamera(pointsPalaced,myBorderValues)

    cv2.imshow("Result ",imgResult)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break