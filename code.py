'''
Simple Face detector
@author: Suyash Phatak
Date: 30/06/2020
'''

# Importing the required libraries
import cv2

# Loading the face or eye cascade or xml file for face
face_cascade = cv2.CascadeClassifier('face_detector.xml')

# Input image
# To change the image change the below filename and extension of the image 
img = cv2.imread('test4.png')

# Detecting Faces
faces = face_cascade.detectMultiScale(img, 1.1, 4)

# Creating rectangle around the detected faces
for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

# Output Image
cv2.imwrite("face_detected.png", img)

print("Succesfully Saved")
