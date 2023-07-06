import cv2

trained_faces=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread("/Users/akshayapujithakolli/Downloads/pujitha.jpg")

#Must covert to the gray sacle computer doesnt need color photo
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Diaplay an image
cv2.imshow('my photo',gray_img)
#To wait and show the image other wise it will close fast
#cv2.waitKey()

#Detect Faces and it gives the face cordinates
face_coordinates=trained_faces.detectMultiScale(gray_img)
print(face_coordinates)

 
for x,y,w,h in face_coordinates:
    cv2.rectangle(gray_img,(x,y),(x+w,y+h),(0,255,0),5)
    #cv2.imshow('my photo',gray_img)
    #cv2.waitKey()

#For real time video
webcam=cv2.VideoCapture(0) 
while True:
    ret,frame=webcam.read()
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    face_coordinates=trained_faces.detectMultiScale(gray_img)
    print(face_coordinates)
    for x,y,w,h in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
    cv2.imshow('my photo',frame)
    #iy waits for 1ms
    key=cv2.waitKey(1)
    if key=='81' and key==113:
        break
webcam.release()

    
