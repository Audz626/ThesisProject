from ast import And
from pyfcm import FCMNotification
from datetime import datetime
from PIL import Image
import imagehash
import mysql.connector
import cv2
import os

host = "localhost"
user = "root"
passw = ""
dbname = "loginregis"

db = mysql.connector.connect(host=host, user=user, password=passw, db=dbname) 
insert_img = db.cursor()
insert_vdo = db.cursor()
update_img = db.cursor()
sql_insert = "insert into images(img_name,img_address) value (%s,%s)"
sql_insert2 = "insert into vdo(file_name,file_address) value (%s,%s)"
# sql_chkUpdate = "UPDATE user SET chk_update = 1"

sql_getToken = "SELECT token FROM user"
# p = update_img.fetchmany(sql_getToken)
# print(p)

image_path = "C:/Audddxd/KMUTNB/Project/WebDev - 2/static/imgs/" #C:\Audddxd\KMUTNB\Project\WebDev\static\imgs ||static/imgs/pic.
video_path = "C:/Audddxd/KMUTNB/Project/WebDev - 2/static/VDO/"

push_service = FCMNotification(api_key="AAAAr4xwlvg:APA91bFidNYFnfOOlzvO-xJebUrX2JU7CzlpZIWF1SqEl_x06-L9t-lITkRVu7mhnA1_hIb9yK72Jn0kaYaDhII5zr7juA_31F2sIHs8ibjWRXZQ52PH_Oxr5IjrYSF2uAtZVB4yarrj")

faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml") #C:\\Users\\LEGION\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml

def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors,minSize=(55, 55))
        coords=[]
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
                coords=[x,y,w,h]
        return img,coords 

threshold_value = 23
count_pic = 0
count_id = 1
f_img = 1  
s_time = 5
e_time = 0
img_id = 0

f_frame = None
l_frame = None
get_l_frame = None

url_camera = 'rtsp://admin:aud0821721605@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1'

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

(grabbed, frame) = cap.read()
fheight,fwidth,fshape = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'x264') #mp4v *'H264' MJPG XVID

# curr_datetimeVDO = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
compareFirst_time = datetime.now().strftime('%Y-%m-%d')
saveDatetime = compareFirst_time

result = cv2.VideoWriter(video_path+str(compareFirst_time)+".mkv",fourcc,30, (fwidth,fheight))

get_url_vdo = video_path+str(compareFirst_time)+"_"+".mkv"
addr_vdo = (str(compareFirst_time)+".mkv",get_url_vdo)
insert_vdo.execute(sql_insert2,addr_vdo)
db.commit()
print("Save VDO to DB...")

while (True):
        #************************************ Record Vedio when moving only**************************************************************
        compareSecond_time = datetime.now().strftime('%Y-%m-%d')
        # future_datetimeVDO = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        if(compareSecond_time > saveDatetime):
                result = cv2.VideoWriter(video_path+str(compareSecond_time)+".mkv",fourcc,30, (fwidth,fheight))
                print('Save new video...')
                get_url_vdo = str(video_path)+str(compareSecond_time)+".mkv"
                addr_vdo = (str(compareSecond_time)+".mkv",get_url_vdo)
                insert_vdo.execute(sql_insert2,addr_vdo)
                db.commit()
                print("Save VDO to DB...")
                saveDatetime = compareSecond_time

        _,frame1 = cap.read()
        _,frame2 = cap.read()
        diff_frame = cv2.absdiff(frame1, frame2) #ผลต่างระหว่างเฟรม
        gray = cv2.cvtColor(diff_frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (21, 21), 0)
        _, thresh_frame = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        di = cv2.dilate(thresh_frame, None, iterations = 0)

        cnts,_ = cv2.findContours(di,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.putText(frame2,str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")),(10, 60),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 0),2)

        for contour in cnts:
                (x, y, w, h) = cv2.boundingRect(contour) #ทำให้เส้น contour เป็น สีเหลี่ยม
                if cv2.contourArea(contour) < 1000:
                        continue
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # print(frame1)
                result.write(frame2)
       
        cv2.imshow("motion detect", frame1)

        # ************************************** Face Detection for saving IMG *******************************************************
        e_time += 1 #end_time เอาไว้ delay 
        ret,frame_faceDet = cap.read() #อ่านภาพจากกล้อง

        if(e_time>s_time): #loop ให้ครบ 20 frame ถึงเข้า loop 1 ครั้ง
                img,coords=draw_boundary(frame_faceDet,faceCascade,1.1,10,(255,255,255),"")                     #ตีกรอบใบหน้าคน จาก frame ภาพที่รับมา
                if len(coords) == 4:                                                                        #เอาไว้เช็ค ถ้าเจอหน้าคน ใน frame ถึงจะเข้า loop ได้ ถ้ามีหน้าคนใน frame จะไม่เข้า loop ไปสร้าง .jpg 
                        result_face = frame_faceDet[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]] # ตัดให้ภาพ 1 เฟรม ให้เหลือเฉพาะแค่ใบหน้าที่ detect ได้
                        resize = cv2.resize(result_face, (400, 350))
                        arr_frame = resize

                        if(f_frame is None):                                                          #อันนี้เอาไว้ delay รูปภาพให้มันสร้างfileไปก่อน 5 ภาพ แล้วค่อยเริ่มเอามาเปรียบเทียบกัน (เคยลองแบบไม่ delay แล้วมัน error)
                                arr_to_img1 = Image.fromarray(resize)
                                f_frame = arr_to_img1
                                print(f_frame.mode)
                                # print(type(f_frame))
                                curr_datetime1 = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                                get_url1 = str(image_path)+"pic."+str(curr_datetime1)+"_"+str(count_id)+".jpg"
                                cv2.putText(arr_frame,str(curr_datetime1),(5, 40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0, 255, 0),2)
                                cv2.imwrite(get_url1,arr_frame)
                                print('save new face first frame',get_url1)

                                addr_img1 = ("pic."+str(curr_datetime1)+"_"+str(count_id)+".jpg",get_url1)
                                insert_img.execute(sql_insert,addr_img1)
                                print("Save to DB...")
                                
                                chk = db.cursor()
                                sql_getToken = "SELECT token FROM `user` GROUP BY token"
                                p = chk.execute(sql_getToken)
                                tokens = chk.fetchall()

                                db.commit()
                                for token in tokens:
                                        if token[0] != None:
                                                print(token[0])
                                                message_title = "Security System"
                                                message_body = "มีคนมา"
                                                result_noti = push_service.notify_single_device(registration_id=token[0], message_title=message_title, message_body=message_body)
                                                print (result_noti)

                                
                                count_id += 1

                        else:
                                arr_to_img2 = Image.fromarray(resize)
                                l_frame = arr_to_img2 #type image
                                
                                if(l_frame is not None and f_frame is not None):
                                        phash_bef= imagehash.phash(f_frame)
                                        
                                        phash_af = imagehash.phash(l_frame)
                                        hth_bef = imagehash.hex_to_hash(str(phash_bef))
                                        hth_af = imagehash.hex_to_hash(str(phash_af))
                                        
                                        print('Hamming Distance :',hth_bef - hth_af)
                                        if(hth_bef - hth_af >= 27):

                                                curr_datetime2 = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                                                
                                                get_url2 = str(image_path)+"pic."+str(curr_datetime2)+"_"+str(count_id)+".jpg"
                                                cv2.putText(arr_frame,str(curr_datetime2),(0, 50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0, 255, 0),2)

                                                cv2.imwrite(get_url2,arr_frame)
                                                print('save new face'+str(count_id))

                                                addr_img2 = ("pic."+str(curr_datetime2)+"_"+str(count_id)+".jpg",get_url2)
                                                insert_img.execute(sql_insert,addr_img2)
                                                print("Save to DB...")
                                                # update_img.execute(sql_chkUpdate)

                                                chk = db.cursor()
                                                sql_getToken = "SELECT token FROM `user` GROUP BY token"
                                                p = chk.execute(sql_getToken)
                                                tokens = chk.fetchall()

                                                db.commit()
                                                for token in tokens:
                                                        if token[0] != None:
                                                                message_title = "Security System"
                                                                message_body = "มีคนมา"
                                                                result_noti2 = push_service.notify_single_device(registration_id=token[0], message_title=message_title, message_body=message_body)
                                                                print (result_noti2)
                                                                
                                                count_id += 1
                                                f_frame = l_frame
                        img_id += 1 #เอาไว้ นับ จำนวนเฟรมภาพที่มีการ detect กับ นับมาตั้งชื่อไฟล์ที่ใช้เปรียบเทียบ 
                        e_time = 0 #ถ้าครบ 20 แล้วให้ set เป็น 0

        cv2.imshow('frame',frame_faceDet)
#****************************************************** Saving IMG End Stage ************************************************************
        if(cv2.waitKey(1) & 0xFF== ord('q')):
                db.close()
                break
cap.release()
cv2.destroyAllWindows()
