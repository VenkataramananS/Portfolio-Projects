import cv2
import numpy as np

imgWidth = 480
imgHeight = 640

cap = cv2.VideoCapture(0)
cap.set(3,imgWidth) #width
cap.set(4,imgHeight) #height
cap.set(10,100) #adjusting brightness


def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(img,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDialation = cv2.dilate(imgCanny,kernel=kernel,iterations=2)
    imgThreshold = cv2.erode(imgDialation,kernel=kernel,iterations=1)
    return imgThreshold

def reOrder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1) # 1 represents axis 1
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew


def getWarp(img,biggest):
    biggest = reOrder(biggest)
    pts1 = np.float32(biggest) # these values are obtained by keeping cursor over the edges in paint
    pts2 = np.float32([[0,0],[imgWidth,0],[0,imgHeight],[imgWidth,imgHeight]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    # print(matrix,biggest)
    imgOutput = cv2.warpPerspective(img,matrix,(imgWidth,imgHeight))
    return imgOutput

def getContour(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    maxArea = 0
    biggest = np.array([])
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        peri = cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        objCorner = len(approx)
        if area > maxArea and objCorner == 4:
            biggest = approx
            maxArea = area
        # x,y,w,h = cv2.boundingRect(approx)
    cv2.drawContours(imgContour,biggest,-1,(255,0,0),20)
    return biggest

while True:
    success,img = cap.read()
    img = cv2.resize(img,(imgWidth,imgHeight))
    imgContour = img.copy()
    imgThreshold = preProcessing(img)
    biggest = getContour(imgThreshold)
    if biggest.size!=0:
        imgWarped = getWarp(img,biggest)
        hrstack = np.hstack((img,imgContour))
        cv2.imshow("Warped ",imgWarped)
        cv2.imshow("Threshold ",imgThreshold)
        cv2.imshow("Original & Contour ",hrstack)

    else:
        cv2.imshow("Original ",img)
        cv2.imshow("Threshold ",imgThreshold)
    
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break