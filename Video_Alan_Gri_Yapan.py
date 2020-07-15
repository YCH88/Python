import cv2 as cv
import numpy as np
from tkinter import * 
from tkinter import filedialog

root=Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
var.set("Videoyu Seciniz\n\nIslem Bitince Pencere Kapanacaktir.\nLutfen Dokunmayin")
label.pack()

root.title('201613709010 Yarkın Çelikel')
root.fileName=filedialog.askopenfilename(title="Videoyu Seçin",filetypes=())

video=cv.VideoCapture(root.fileName)
fourcc = cv.VideoWriter_fourcc(*'XVID')

out=cv.VideoWriter('gri.avi', fourcc, 80.0, (int(video.get(3)), int(video.get(4))),False)

while True:
    ret,kare=video.read() 
    if ret==True:
        gray = cv.cvtColor(kare, cv.COLOR_BGR2GRAY)
        out.write(gray)
    else:
        break
    
video.release()
out.release()
root.destroy()
cv.destroyAllWindows() 