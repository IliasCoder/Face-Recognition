import cv2
import numpy as np
import face_recognition
import os

elon_path = "ImagesBasic/Elon Musk.jpg"
test_path = "ImagesBasic/Elon Test.jpg"

if not os.path.exists(elon_path):
    raise FileNotFoundError(f"File not found: {elon_path}")
if not os.path.exists(test_path):
    raise FileNotFoundError(f"File not found: {test_path}")

imgElon = face_recognition.load_image_file(elon_path)
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file(test_path)
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)  # Fixed: use imgTest, not imgElon

#looking for the face location and encoding it
faceLocationsElon = face_recognition.face_locations(imgElon)
if len(faceLocationsElon) == 0:
    raise Exception("No face found in Elon Musk image.")
faceLocation = faceLocationsElon[0] #this gives four values(top,right,bottom,left)
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]),(255,0,255),2)

faceLocsTest = face_recognition.face_locations(imgTest)
if len(faceLocsTest) == 0:
    raise Exception("No face found in Elon Test image.")
faceLocTest = faceLocsTest[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results=face_recognition.compare_faces([encodeElon],encodeTest)
faceDistance = face_recognition.face_distance([encodeElon],encodeTest)
print(faceDistance)
cv2.putText(imgTest,f'{results} {round(faceDistance[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)
cv2.waitKey(0)
