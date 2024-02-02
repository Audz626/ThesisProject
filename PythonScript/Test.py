import cv2
url = 'rtsp://admin:aud0821721605@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1'
RTSP_URL = 'rtsp://192.168.1.108:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
# url = 'rtsp://admin:aud0821721605@192.168.1.108:554/H264?ch=1&subtype=0' #RTSP URL ที่ได้มาจากข้อก่อนหน้า
capture = cv2.VideoCapture(RTSP_URL) 
while True:
  ret, frame = capture.read()
  cv2.imshow('Output', frame)
  k = cv2.waitKey(10) &0xFF
  if k == 27:
     break
capture.release()
cv2.destroyAllWindows()