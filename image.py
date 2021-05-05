import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread("team-india.jpeg") #reading the colored image
gr_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting the colored image to grayscale
faces=face_cascade.detectMultiScale(gr_img,1.5,3) #searching for the face coordinates
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3) #drawing rectangle
cv2.imshow('Display', img)
cv2.waitKey(0)
cv2.destroyAllWindows()