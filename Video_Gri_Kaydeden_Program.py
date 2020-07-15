# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:01:16 2020

@author: DC
"""
import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
video = cv.VideoWriter('a.avi',fourcc,30,(640,480),False)
kayit=False   

if not cap.isOpened():
    print("Kamera açılamadı")
    exit()
   
ret,frame = cap.read() 

while True:
    ret, frame = cap.read()
   
    if not ret:
        print("«Kare alınamadı çıkılıyor…")
        break
  
    cv.imshow('frame',frame)
    edges = cv.Canny(frame,100,200)
    edges=  cv.resize(edges,dsize=(640, 480), interpolation=cv.INTER_CUBIC) 
    cv.imshow('digeri',edges)
    
    k=cv.waitKey(33)
    if k == ord('k'):
       kayit=True
       
    if kayit:
       video.write(edges)   
            
    if k == ord('d'):
        kayit=False
        break
    
cap.release()
video.release()
cv.destroyAllWindows()