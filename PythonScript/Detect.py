from PIL import Image
import imagehash
import cv2
import os
from numpy import insert
from datetime import datetime

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def draw_boundary(img,classifier,scaleFactor,minNighbors,color,text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #แปลงภาพเป็น gay scale 
    features=classifier.detectMultiScale(gray,scaleFactor,minNighbors)      
    coords=[]
        
    for(x,y,w,h) in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
            coords=[x,y,w,h]
            return coords,img
        
def detect(img,faceCascade):
    #color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, (255,0,0), "UNKNOWN")
 
    return img

cap = cv2.VideoCapture(0)
(grabbed, frame) = cap.read()
fheight,fwidth,_ = frame.shape
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# result = cv2.VideoWriter("../VDO/Testvdo.mp4",fourcc,30, (fwidth,fheight))
#os.system('python Face_detect.py')

while True:
	# e_time += 1
	# ret,frame_faceDet = cap.read()

	_,frame1 = cap.read()
	_,frame2 = cap.read()
	# _,frame3 = cap.read()

	# frame = detect(frame3,faceCascade)

	diff_frame = cv2.absdiff(frame1, frame2) #ผลต่างระหว่างเฟรม
	gray = cv2.cvtColor(diff_frame, cv2.COLOR_BGR2GRAY) #แปลงภาพให้เป็น gray scale
	blur = cv2.GaussianBlur(gray, (21, 21), 0) #ทำให้ภาพเบลอ
	_, thresh_frame = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	di = cv2.dilate(thresh_frame, None, iterations = 0) #ขยายพื้นที่เส้นให้ชัดเจน

	cnts,_ = cv2.findContours(di,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #หาเส้น contour
	cv2.putText(frame1,str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")),(0, 30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1,cv2.LINE_AA)

	for contour in cnts:
		(x, y, w, h) = cv2.boundingRect(contour) #ทำให้เส้น contour เป็น สีเหลี่ยม
		if cv2.contourArea(contour) < 700:
			continue
		cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
		# result.write(frame1) #บันทึก VDO
		# cv2.imwrite("pig.+n+ jpg",frame1)
		# n = n+1
        
	#cv2.imshow("Gray Frame", gray)
	#cv2.imshow("Difference Frame", diff_frame)
	#cv2.imshow("Threshold Frame", thresh_frame)
	cv2.imshow("motion detect", frame1)
	# cv2.imshow("face detect", frame)

	#frame = frame2
	#check, frame2 = cap.read()

	key = cv2.waitKey(1)
	if key == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
