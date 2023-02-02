import cv2
import numpy as np
from tensorflow.keras.models import model_from_json

cap = cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,100) #adjusting brightness
emotions = {0:"Angry",1:"Disgusted",2:"Fearful",3:"Happy",4:"Neutral",5:"Sad",6:"Surprised"}
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#loading the model
json_file = open("expressionModel2.json","r")
load_model_json = json_file.read()
json_file.close()
exp_model = model_from_json(load_model_json)

exp_model.load_weights("expressionModel2.h5")

def identifyFace(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roiGrayFrame = imgGray[y:y+h,x:x+w]
        croppedImg = np.expand_dims(np.expand_dims(cv2.resize(roiGrayFrame,(48,48)),-1),0)
        emotionPrediction = exp_model(croppedImg)
        maxindex = int(np.argmax(emotionPrediction))
        # print(maxindex)
        cv2.putText(img,emotions[maxindex],(x+(w//2)+25,y+(h//2)+50),cv2.FONT_ITALIC,1,(149,150,0),4)
    
while True:
    success,img = cap.read()
    identifyFace(img)
    cv2.imshow("Video ",img)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

cv2.waitKey(1)