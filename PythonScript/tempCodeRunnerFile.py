def draw_boundary(img,classifier,scaleFactor,minNighbors,color,text):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #แปลงภาพเป็น gay scale 
#     features=classifier.detectMultiScale(gray,scaleFactor,minNighbors)      
#     coords=[]
        
#     for(x,y,w,h) in features:
#             cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
#             cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
#             coords=[x,y,w,h]
#             return coords,img
        
# def detect(img,faceCascade):
#     coords = draw_boundary(img, faceCascade, 1.1, 10, (255,0,0), "UNKNOWN")
 
#     return img