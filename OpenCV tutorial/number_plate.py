import cv2
import numpy as np

numberPlateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
img = cv2.imread("sampleimages\car1.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

numPlate = numberPlateCascade.detectMultiScale(imgGray,1.1,4)
# print(numPlate)
for (x,y,w,h) in numPlate:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(img,"Tracked Number",(x+(w//2)+250,y+(h//2)+200),cv2.FONT_ITALIC,1,(149,150,0),4)
    imgRoi = img[y:y+h,x:x+w]
    cv2.imshow("ROI ",imgRoi)

cv2.imshow("License Number ",img)
# cv2.imshow("License Gray ",imgGray)
#saving the sccanned image
count = 0
cv2.imwrite("scanned/plate_number_"+str(count)+".jpg",imgRoi)
cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
cv2.putText(img,"Number Saved",(150,265),cv2.FONT_ITALIC,2,(0,0,255),2)
cv2.imshow("Result ",img)
cv2.waitKey(0)