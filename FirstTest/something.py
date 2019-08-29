import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


thepic = "test3.jpg"
img = cv2.imread(thepic,1)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
print(type(face))
f =(type(face))
print(face)
f1=face


for x,y,w,h in face:
    img = cv2.rectangle(img,(x,y),(x+w,y+h), (0,225,0),3)
resized = cv2.resize(img,(int(img.shape[1]),(int(img.shape[0]))))
resize = cv2.resize(img,(int(img.shape[1]/3),(int(img.shape[0]/3))))
cv2.imshow("DontV",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

