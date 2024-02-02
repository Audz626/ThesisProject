import numpy as np
import cv2
from pyfcm import FCMNotification
import MySQLdb
# cap = cv2.VideoCapture(0)


db = MySQLdb.connect("localhost","root","","crud")
chk = db.cursor()
# sql_chkUpdate = "UPDATE user SET chk_update = 1"

sql_getToken = "SELECT token FROM user"
p = chk.execute(sql_getToken)
tokens = chk.fetchall()

# push_service = FCMNotification(api_key="AAAAr4xwlvg:APA91bFidNYFnfOOlzvO-xJebUrX2JU7CzlpZIWF1SqEl_x06-L9t-lITkRVu7mhnA1_hIb9yK72Jn0kaYaDhII5zr7juA_31F2sIHs8ibjWRXZQ52PH_Oxr5IjrYSF2uAtZVB4yarrj")
# registration_id = "f4qLEw43Q8WAoaVlxWLWgA:APA91bFpy0KTUOyRJ4mkjhuj-O7aZeBypnU6_ic0Layz0YuSBh9eAT-32RiU_xJscZScAIUw_1Wd95Mu_qr5fQSg0m1GuUZk0kWAbW1aVKjk2N2iN_uyFlBgmzcTGiFIHS4EOp5tEjZS"

# chk.execute(sql_chkUpdate)
db.commit()

print(tokens)
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'H264')
# out = cv2.VideoWriter('output1.mp4',fourcc, 20.0, (640,480))

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#         out.write(frame)

#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()