# import cv2 
# import numpy as np 
# import matplotlib.pyplot as plt 

# img = cv2.imread(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\dog.jpeg')

# print(type(img))  #<class 'numpy.ndarray'>

# cv2.imshow("window",img)
# cv2.waitKey(0)

# -------------------------------------------------------------------------------------------------------------------

#  Converting RGB image to Grayscale

# import cv2 
# import numpy as np 

# img = cv2.imread(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\dog.jpeg')
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.imshow('window',img)
# cv2.imshow('window2',img_gray)
# cv2.waitKey(0)


# -------------------------------------------------------------------------------------------------------------------
# Image Resizing

# import cv2 
# import numpy as np 

# img = cv2.imread(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\dog.jpeg')
# img_resize = cv2.resize(img,(256,256))
# img_resize2 = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))  # this is used for half the image if the image size is not known 

# cv2.imshow('window',img)
# cv2.imshow('window2',img_resize)
# cv2.imshow('window3',img_resize2)

# cv2.waitKey()


# -------------------------------------------------------------------------------------------------------------------
#  Flipping an Image

# import cv2 
# import numpy as np 

# img = cv2.imread(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\dog.jpeg')
# img_flip1 = cv2.flip(img,0)
# img_flip2 = cv2.flip(img,1)
# img_flip3 = cv2.flip(img,-1)


# cv2.imshow('window',img)
# cv2.imshow('window1',img_flip1)
# cv2.imshow('window2',img_flip2)
# cv2.imshow('window3',img_flip3)

# cv2.waitKey()


# -------------------------------------------------------------------------------------------------------------------
# CROPPING THE IMAGE 

# import cv2 
# import numpy as np 

# img = cv2.imread(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\dog.jpeg')
# img_crop = img[100:200,50:100]
# # print(img.shape)

# cv2.imshow('window',img_crop)

# cv2.waitKey()


# -------------------------------------------------------------------------------------------------------------------
# SAVING IMAGE 

# import cv2 
# import numpy as np 

# img = cv2.imread(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\dog.jpeg')

# cv2.imshow('window',img)
# cv2.imwrite('Dog.png',img)

# cv2.waitKey()


# -------------------------------------------------------------------------------------------------------------------
# Drawing Shapes and Text on Images

# import cv2 
# import numpy as np 

# #Read an image 
# img = np.zeros((512,512,3))

# #Rectangle 
# cv2.rectangle(img,pt1=(100,100),pt2=(400,400),color=(255,0,0),thickness=-1)

# #circle 
# cv2.circle(img,center=(200,300),radius=100,color=(0,255,0),thickness=-1)

# #Line 
# cv2.line(img,pt1=(0,0),pt2=(512,512),color=(0,0,255),thickness=2)

# #Text 
# cv2.putText(
#     img, 
#     org=(100, 100), 
#     fontScale=4, 
#     color=(0, 255, 255), 
#     thickness=2, 
#     lineType=cv2.LINE_AA, 
#     text="Hello", 
#     fontFace=cv2.FONT_ITALIC
# )

# cv2.imshow('window',img)
# cv2.waitKey(0)


# -------------------------------------------------------------------------------------------------------------------
# Working with OpenCV Events

# import cv2 
# import numpy as np 

# drawing = False 
# ix = -1 
# iy = -1

# def draw(event,x,y,flag,params):

#     global drawing,ix,iy

#     if event == 1:
#         drawing=True
#         ix = x 
#         iy = y 
#     elif event == 0 :
#         if drawing == True :
#             cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(255,0,255),thickness=-1)
#     elif event == 4:
#         drawing=False
#         cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(255,0,255),thickness=-1)


# cv2.namedWindow(winname='window')
# cv2.setMouseCallback('window',draw)

# img = np.zeros((700,1000,3))

# while True :

#     cv2.imshow('window',img)

#     if cv2.waitKey(1) & 0xFF == ord('t'):
#         break

# cv2.destroyAllWindows()

# -------------------------------------------------------------------------------------------------------------------

# Building a Cropping Tool

# import cv2 
# import numpy as np

# drawing = False 
# ix = -1 
# iy = -1 

# def crop(event,x,y,flags,params):

#     global drawing,ix,iy
#     if event == 1 :
#         drawing = True
#         ix = x 
#         iy = y 

#     # elif event == 0 :
#     #     if drawing == True :
#     #         cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,0),thickness=1)

#     elif event == 4 :
#         drawing = False
#         cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,0),thickness=1)

#         ## Croping Tool 
#         crop_img = img[iy:y,ix:x]
#         cv2.imshow('new_window',crop_img)
#         cv2.waitKey(0)



# img = cv2.imread(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\dog.jpeg')
# img = cv2.resize(img,(700,700))

# cv2.namedWindow(winname='Dog')
# cv2.setMouseCallback('Dog',crop)

# while True :

#     cv2.imshow("Dog",img)
#     if cv2.waitKey(1) & 0xFF ==ord('x'):
#         break

# cv2.destroyAllWindows()


# -------------------------------------------------------------------------------------------------------------------
# Working with Videos using OpenCV

# import cv2 
# # import numpy as np 

# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

# while True:
#     ret,frame = cap.read()

#     # img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     out.write(frame)

#     cv2.imshow('webcam',frame)

#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break 

# out.release()
# cv2.destroyAllWindows()


# -------------------------------------------------------------------------------------------------------------------

# import cv2
# import numpy as np 
# import time 

# cap = cv2.VideoCapture('output.avi')

# while True:

#     ret,frame = cap.read()
#     time.sleep(1/20)
#     cv2.imshow('window',frame)
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break

# cv2.destroyAllWindows()


# -------------------------------------------------------------------------------------------------------------------

# Face and Eye Detection from Images using HAAR Cascade Classifier

# import cv2 
# import numpy as np 

# # We point Open CV CascadeClassifier function to where our 
# # Classifier (XML file format) is stored 
# face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

# # Load our image then convert it into Gray Scale 

# img = cv2.imread(r'Images/Harshal image.png')
# img = cv2.resize(img,(700,600))
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# # Our classifier return the ROI of the detected face as a tuple 
# # It stores the Top left coordinate and the Bottom right coordinates 
# faces = face_classifier.detectMultiScale(img_gray,scaleFactor=1.05,minNeighbors=5)n

# # When no faces detected , face_Classifier return an empty tuple 
# if faces is None :
#     print("No Faces Found !")


# # We iterate  through our faces array and draw a rectangle 
# # over each face in faces 
# for(x,y,w,h) in faces :
#     cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(127,9,255),thickness=2)
#     cv2.imshow('Face_Detection',img)
#     cv2.waitKey(0)

# cv2.destroyAllWindows()



# -------------------------------------------------------------------------------------------------------------------

# import cv2 
# import numpy as np

# face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
# eye_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')

# img = cv2.imread(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\Images\Elon_Musk.org&utm_campaign=api&utm_content=thumbnail')
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# faces = face_classifier.detectMultiScale(img_gray,scaleFactor=1.05,minNeighbors=5)

# if faces is None:
#     print("No Face Detected")

# for (x,y,w,h) in faces :
#     cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(127,0,255),thickness=2)
#     cv2.imshow('Face_Window',img)
#     cv2.waitKey(0)
#     roi_gray = img_gray[y:y+h,x:x+w]
#     roi_color = img[y:y+h,x:x+w]
#     eyes = eye_classifier.detectMultiScale(roi_gray, scaleFactor=1.05, minNeighbors=3)

#     for (ex,ey,ew,eh) in eyes:
#         cv2.rectangle(roi_color,pt1=(ex,ey),pt2=(ex+ew,ey+eh),color=(255,255,0),thickness=2)
#         cv2.imshow('eye_window',roi_color)
#         cv2.waitKey(0)

# cv2.destroyAllWindows()     


# -------------------------------------------------------------------------------------------------------------------

# import cv2 
# import numpy as np

# face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
# eye_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')

# # Defining a function that will do detection 
# def detect (video_gray,frame):
#     faces = face_classifier.detectMultiScale(video_gray,scaleFactor=1.05,minNeighbors=5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(127,0,255),thickness=2)
#         roi_gray = video_gray[y:y+h,x:x+h]
#         roi_color = frame[y:y+h,x:x+h]

#         eyes = eye_classifier.detectMultiScale(roi_gray,scaleFactor=1.05,minNeighbors=5)
#         for (ex,ey,ew,eh) in eyes:
#             cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(127,0,255),thickness=2)
#     return frame 

# ## Doing some face detection using webcame 

# video_capture = cv2.VideoCapture(0)
# while True :
#     ret,frame = video_capture.read()
#     video_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     canvas = detect(video_gray,frame)
#     cv2.imshow('video_window',canvas)
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break

# video_capture.release()
# cv2.destroyAllWindows()

# -------------------------------------------------------------------------------------------------------------------

# Pedestrian Detection using OpenCV from Videos 

import cv2
import numpy as np 
import time 

body_classifier = cv2.CascadeClassifier(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\Haarcascades\haarcascade_fullbody.xml')

def Process(gray,frame):
    bodies = body_classifier.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=3)
    for (x,y,w,h) in bodies :
        cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,255,255),thickness=2)
    return frame

cap = cv2.VideoCapture(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\Images\walking (1).avi')

while True:
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    H = Process(gray,frame)
    time.sleep(1/100000000)
    cv2.imshow('video',H)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()



# -------------------------------------------------------------------------------------------------------------------
# Car Detection using HAAR Cascade and Opencv from Videos.

# import cv2 
# import numpy as np 
# import time 

# car_Classifier = cv2.CascadeClassifier(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\Haarcascades\haarcascade_car.xml')

# cap = cv2.VideoCapture(r'C:\Users\HARSHAL\OneDrive\Desktop\Machine Learning\Images\cars.avi')

# while True :
#     ret,frame = cap.read()

#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#     cars = car_Classifier.detectMultiScale(gray,scaleFactor=1.4,minNeighbors=2)

#     for (x,y,w,h) in cars :
#         cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,255),thickness=2)
#         time.sleep(1/25)
#         cv2.imshow('car',frame)
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break

# cv2.destroyAllWindows()