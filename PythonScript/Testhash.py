from PIL import Image
import imagehash
import cv2

img_before = cv2.imread("data/pig.12.jpg")
img_after = cv2.imread("data/pig.13.jpg")

image_file1 = Image.open("data/pig.12.jpg")
image_file2 = Image.open("data/pig.13.jpg")
phash1 = imagehash.phash(image_file1)
phash2 = imagehash.phash(image_file2)
print(phash1)
print(phash2)

gs_hash = imagehash.hex_to_hash(str(phash1))
ori_hash = imagehash.hex_to_hash(str(phash2))
print('Hamming distance:', gs_hash - ori_hash)

# gray_bef = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
# gray_af = cv2.cvtColor(img_after, cv2.COLOR_BGR2GRAY)

# phash_bef = imagehash.phash(gray_bef)
# phash_af = imagehash.phash(gray_af)

# gs_hash_bef = imagehash.hex_to_hash(phash_bef)
# gs_hash_af = imagehash.hex_to_hash(phash_af)

# print(gs_hash_bef - gs_hash_af)

from PIL import Image
import imagehash
import cv2
import os

faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img_value = 0 

def save_Img(img,img_id):
        threshold_value = 20
        
        cv2.imwrite("data/pig."+str(img_id)+".jpg",img)

        if(img_id > 5):
                img_before = Image.open("data/pig."+str(img_id-1)+".jpg")
                img_after = Image.open("data/pig."+str(img_id)+".jpg")

                # gray_bef = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
                # gray_af = cv2.cvtColor(img_after, cv2.COLOR_BGR2GRAY)

                phash_bef = imagehash.phash(img_before)
                phash_af = imagehash.phash(img_after)
                gs_hash_bef = imagehash.hex_to_hash(str(phash_bef))
                gs_hash_af = imagehash.hex_to_hash(str(phash_af))

                print(gs_hash_bef - gs_hash_af)

                if(gs_hash_bef - gs_hash_af < threshold_value ):
                        os.remove("data/pig."+str(img_id-1)+".jpg")
        
        # if(gs_hash_bef-gs_hash_af > threshold_value ):


def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors,minSize=(55, 55))
        coords=[]
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
                coords=[x,y,w,h]
        return img,coords 


       
s_time = 20
e_time = 0
img_id = 0    
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
while (True):
        e_time += 1
        ret,frame = cap.read()

        if(e_time>s_time):
                img,coords=draw_boundary(frame,faceCascade,1.1,10,(0,0,255),"")
                if len(coords) == 4:
                        result = frame[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
                        save_Img(result,img_id)
                        img_id += 1
                # frame=detect(frame,faceCascade,img_id)
                e_time = 0

        cv2.imshow('frame',frame)
        
        if(cv2.waitKey(1) & 0xFF== ord('q')):
            break
cap.release()
cv2.destroyAllWindows()

from PIL import Image
import imagehash
import cv2
import os

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


url = 'rtsp://admin:aud0821721605@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0'

# threshold_value = 20
# count_pic = 0
# count_id = 1
# f_img = 1  
# s_time = 20
# e_time = 0
# img_id = 0 

cap = cv2.VideoCapture(0)
(grabbed, frame) = cap.read()
fheight,fwidth,fshape = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter("../VDO/Tester5.avi",fourcc,30, (fwidth,fheight))

while True:
	check, frame1 = cap.read()
	check, frame2 = cap.read()
	check, frame3 = cap.read()
	frame = detect(frame3,faceCascade)


	diff_frame = cv2.absdiff(frame1, frame2) #ผลต่างระหว่างเฟรม
	gray = cv2.cvtColor(diff_frame, cv2.COLOR_BGR2GRAY) #แปลงภาพให้เป็น gray scale
	blur = cv2.GaussianBlur(gray, (21, 21), 0) #ทำให้ภาพเบลอ
	_, thresh_frame = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	di = cv2.dilate(thresh_frame, None, iterations = 0) #ขยายพื้นที่เส้นให้ชัดเจน

	cnts,_ = cv2.findContours(di,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #หาเส้น contour

	for contour in cnts:
		(x, y, w, h) = cv2.boundingRect(contour) #ทำให้เส้น contour เป็น สีเหลี่ยม
		if cv2.contourArea(contour) < 700:
			continue
		cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
		result.write(frame1) #บันทึก VDO
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



#******************************** Old Version **********************************************************
from PIL import Image
import imagehash
import cv2
import os

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
        
# def detect(img,faceCascade):
#     #color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}
#     coords = draw_boundary(img, faceCascade, 1.1, 10, (255,0,0), "UNKNOWN")
 
#     return img

url = 'rtsp://admin:aud0821721605@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0'

# threshold_value = 20
# count_pic = 0
# count_id = 1
# f_img = 1  
# s_time = 20
# e_time = 0
# img_id = 0 

cap = cv2.VideoCapture(0)
(grabbed, frame) = cap.read()
fheight,fwidth,fshape = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter("../VDO/Tester5.avi",fourcc,30, (fwidth,fheight))

while True:
	# e_time += 1
	# ret,frame_faceDet = cap.read()

	check, frame1 = cap.read()
	check, frame2 = cap.read()
	check, frame3 = cap.read()

	# frame = detect(frame3,faceCascade)

	diff_frame = cv2.absdiff(frame1, frame2) #ผลต่างระหว่างเฟรม
	gray = cv2.cvtColor(diff_frame, cv2.COLOR_BGR2GRAY) #แปลงภาพให้เป็น gray scale
	blur = cv2.GaussianBlur(gray, (21, 21), 0) #ทำให้ภาพเบลอ
	_, thresh_frame = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	di = cv2.dilate(thresh_frame, None, iterations = 0) #ขยายพื้นที่เส้นให้ชัดเจน

	cnts,_ = cv2.findContours(di,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #หาเส้น contour

	for contour in cnts:
		(x, y, w, h) = cv2.boundingRect(contour) #ทำให้เส้น contour เป็น สีเหลี่ยม
		if cv2.contourArea(contour) < 700:
			continue
		cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
		result.write(frame1) #บันทึก VDO
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
