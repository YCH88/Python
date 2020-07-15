import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image

cap = cv2.VideoCapture(0)


while True:
    ret, kare = cap.read()

    if not ret:
        print("«Kare alınamadı çıkılıyor…")
        break
    gray = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)    
    for (x, y, w, h) in faces:
        kare=cv2.rectangle(kare, (x, y), (x+w, y+h), (255, 255, 0), 2)
        kare=cv2.putText(kare, "YUZ", (x+w-int((w/4)),y+h), cv2.FONT_HERSHEY_COMPLEX_SMALL,1 , (0,0,0))    
    cv2.imshow('Yuz_Tanıma', kare)    
   
    k=cv2.waitKey(60)           
    if k == ord('d'):
        break
    
cap.release()
cv2.destroyAllWindows()