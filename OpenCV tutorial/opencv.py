import cv2
import numpy as np

print("packages are imported")
'''
Images
'''
# img = cv2.imread("sampleimages/4493425-hd-wallpapers-1080p.jpg")
# cv2.imshow("Output ",img)
# cv2.waitKey(1000)

'''
Video
'''
# cap = cv2.VideoCapture("video\colors.mp4")
# while True:
#     success,img = cap.read()
#     cv2.imshow("Video ",img)
#     if cv2.waitKey(1)& 0xFF == ord('q'):
#         break
'''
Using Webcam
'''
cap = cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,100) #adjusting brightness
while True:
    success,img = cap.read()
    cv2.imshow("Video ",img)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

'''
Graying, Blurring, finding the edges of a image, Dialation,Erode a image
'''
# img = cv2.imread("sampleimages/4493425-hd-wallpapers-1080p.jpg")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #Second parameter is kernel and it should be odd
# imgCanny = cv2.Canny(img,100,100)
# kernel = np.ones((5,5),np.uint8)
# imgDialation = cv2.dilate(imgCanny,kernel=kernel,iterations=3)
# imgEroded = cv2.erode(imgDialation,kernel=kernel,iterations=1)
# cv2.imshow("Gray Image ",imgGray)
# cv2.imshow("Blur Image ",imgBlur)
# cv2.imshow("Canny Image ",imgCanny)
# cv2.imshow("Dialated Image ",imgDialation)
# cv2.imshow("Eroded Image ",imgEroded)
# cv2.waitKey(0)

'''
Resizing, Cropping an image
'''
# img = cv2.imread("sampleimages/4493425-hd-wallpapers-1080p.jpg")
# print(img.shape) # first is height,width,channel  number  BGR
# imgResize = cv2.resize(img,(480,480)) # width,height
# imgCropped = img[300:1200,300:700] # height,width
# cv2.imshow("Image ",img)
# cv2.imshow("Resized image ",imgResize)
# cv2.imshow("image cropped ",imgCropped)
# cv2.waitKey(0)
'''
Drawing shapes on a image
'''
# img = np.zeros((1280,720,3),np.uint8)
# # img[200:300,100:500] = 255,0,0 # color specific region
# # img[:] = 255,0,0 # color entire image
# cv2.line(img,(0,0),(300,300),(0,255,255),3) # starting point, ending point, color, thickness
# cv2.rectangle(img,(0,0),(250,350),(0,243,120),cv2.FILLED)
# cv2.circle(img,(400,50),30,(120,200,180),3)
# cv2.putText(img,"This is a sample Text",(300,100),cv2.FONT_ITALIC,1,(0,150,0),4)
# cv2.imshow("image ",img)
# cv2.waitKey(0)
'''
Warp function
'''
# img = cv2.imread("sampleimages\error.png")
# width,height = 1000,500 #width,height
# pts1 = np.float32([[356,351],[356,508],[766,351],[766,508]]) # these values are obtained by keeping cursor over the edges in paint
# pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))
# cv2.imshow("Image ",img)
# cv2.imshow("warped image ",imgOutput)
# cv2.waitKey(0)
'''
Joining Images
'''
# img = cv2.imread("sampleimages\error.png")
# horzStack = np.hstack((img,img))
# vertStack = np.vstack((img,img))
# cv2.imshow("Image ",img)
# cv2.imshow("horizontal image ",horzStack)
# cv2.imshow("vertical image ",vertStack)
# cv2.waitKey(0)
'''
Color Detection
'''
# def empty(val):
#     pass

# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240)
# cv2.createTrackbar("Hue Minimum","TrackBars",0,179,empty)
# cv2.createTrackbar("Hue Maximum","TrackBars",179,179,empty)
# cv2.createTrackbar("Saturation Minimum","TrackBars",0,255,empty)
# cv2.createTrackbar("Saturation Maximum","TrackBars",255,255,empty)
# cv2.createTrackbar("Value Minimum","TrackBars",0,255,empty)
# cv2.createTrackbar("Value Maximum","TrackBars",255,255,empty)
# while True:
#     # img = cv2.imread("sampleimages/4493425-hd-wallpapers-1080p.jpg")
#     imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("Hue Minimum","TrackBars")
#     h_max = cv2.getTrackbarPos("Hue Maximum","TrackBars")
#     s_min = cv2.getTrackbarPos("Saturation Minimum","TrackBars")
#     s_max = cv2.getTrackbarPos("Saturation Maximum","TrackBars")
#     v_min = cv2.getTrackbarPos("Value Minimum","TrackBars")
#     v_max = cv2.getTrackbarPos("Value Maximum","TrackBars")
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max,s_max,v_max])
#     mask = cv2.inRange(imgHSV,lower,upper)
#     imgResult = cv2.bitwise_and(img,img,mask=mask)
#     cv2.imshow("Image ",img)
#     cv2.imshow("HSV Image ",imgHSV)
#     cv2.imshow("Mask Image ",mask)
#     cv2.imshow("Mask Image-2 ",imgResult)
#     cv2.waitKey(1)
'''
Contour and Shape Detection
'''
# def getContour(img):
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         cv2.drawContours(imgContour,cnt,-1,(149,150,151),3)
#         peri = cv2.arcLength(cnt,True)
#         approx = cv2.approxPolyDP(cnt,0.02*peri,True)
#         objCorner = len(approx)
#         x,y,w,h = cv2.boundingRect(approx)
#         if objCorner == 3:
#             objectType = "Triangle"
#         elif objCorner == 4:
#             aspectRatio = w/float(h)
#             if aspectRatio >0.95 and aspectRatio < 1.05:
#                 objectType="Square"
#             else:
#                 objectType = "Rectangle"
#         elif objCorner > 4:
#             objectType="Circles"
#             # objectType=""
#         # if objCorner == 4:
#         #     objectType = "Rectangle or Square"
        
#         cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
#         cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_ITALIC,1,(0,150,0),4)

# img = cv2.imread("sampleimages\shapes.png")
# img = cv2.resize(img,(480,480))
# imgContour = img.copy()
# imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# imgCanny = cv2.Canny(img,50,50)
# getContour(imgCanny)

# hrtStack = np.hstack((img,imgContour))
# hrtStack1 = np.hstack((imgCanny,imgGray))

# cv2.imshow("Original & Contour ",hrtStack)
# cv2.imshow("Canny & Gray ",hrtStack1)
# cv2.waitKey(0)

'''
Face Detection
'''
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("sampleimages\R 7521.JPG")
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(img,"Face",(x+(w//2)+250,y+(h//2)+200),cv2.FONT_ITALIC,1,(149,150,0),4)

cv2.imshow("Recognised Face ",img)
cv2.waitKey(0)
