import cv2 as cv
import numpy as np
from tkinter import * 
from tkinter import filedialog

root=Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
var.set("Videoyu Seciniz\n\nIslem Bitince Pencere Kapanacaktir.\nLutfen Dokunmayin\n")
label.pack()

root.title('201613709010 Yarkın Çelikel')
root.fileName=filedialog.askopenfilename(title="Videoyu Seçin",filetypes=())

video=cv.VideoCapture(root.fileName)
fourcc = cv.VideoWriter_fourcc(*'XVID')

donderici=cv.VideoWriter('donmus_video.avi', fourcc, 30.0, (int(video.get(4)), int(video.get(3))))

while True:
    ret,kare=video.read() 
    if ret==True:
       donderici.write(cv.rotate(kare,cv.ROTATE_90_CLOCKWISE))   
    else:
        break
       
video.release()
donderici.release()
root.destroy()
cv.destroyAllWindows() 