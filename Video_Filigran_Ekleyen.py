import cv2 as cv
import random


def yazi(frame):
     renk=random.randint(1,5)
     font = cv.FONT_ITALIC
     if renk==1:
          l=cv.putText(frame,'Yarkin Yakup Celikel',(10, 100),font,1,(255, 0, 0),1,cv.LINE_4)
         
     elif renk==2:
          l=cv.putText(frame,'Yarkin Yakup Celikel',(10, 100),font,1,(255, 0, 255),1,cv.LINE_4)

     elif renk==3:
          l=cv.putText(frame,'Yarkin Yakup Celikel',(10, 100),font,1,(255, 255, 255),1,cv.LINE_4)
    
     elif renk==4:
          l=cv.putText(frame,'Yarkin Yakup Celikel',(10, 100),font,1,(0, 0, 0),1,cv.LINE_4)

     else:
          l=cv.putText(frame,'Yarkin Yakup Celikel',(10, 100),font,1,(0, 0, 255),1,cv.LINE_4)
 
     return l
 
cap = cv.VideoCapture(0)
 

if not cap.isOpened():
    print("Kamera açılamadı")
    exit()
   
ret,frame = cap.read() 

while True:
    ret, frame = cap.read()

    if not ret:
        print("«Kare alınamadı çıkılıyor…")
        break
 
    cv.imshow('frame',yazi(frame))
 
    
    k=cv.waitKey(60)           
    if k == ord('d'):
        break
    
cap.release()
cv.destroyAllWindows()


   