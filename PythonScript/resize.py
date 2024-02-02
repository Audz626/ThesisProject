import numpy as np
from PIL import Image
import cv2
from datetime import datetime
import imagehash
from skimage.metrics import structural_similarity as ssim
from skimage import measure

image1 = cv2.imread('PythonScript/Test.jpg')
image2 = cv2.imread('PythonScript/Test2.jpg')
image3 = cv2.imread('PythonScript/Test3.jpg',0)
image4 = cv2.imread('PythonScript/Test4.jpg',0)
image5 = cv2.imread('PythonScript/Test5.jpg')

# img1 = cv2.resize(cv2.imread("PythonScript/Test2.jpg"), (300, 250)).astype(np.int32)
resize1 = cv2.resize(image1, (300, 250))
resize2 = cv2.resize(image5, (300, 250))

grayA = cv2.cvtColor(resize1, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(resize2, cv2.COLOR_BGR2GRAY)


# rin = cv2.imread('rin10c01.png',0)
# ret,rinth = cv2.threshold(image1,0,255,cv2.THRESH_OTSU)
# ret2,rinth2 = cv2.threshold(image2,0,255,cv2.THRESH_OTSU)
# ret3,rinth3 = cv2.threshold(image3,0,255,cv2.THRESH_OTSU)
# ret4,rinth4 = cv2.threshold(image4,0,255,cv2.THRESH_OTSU)
# ret5,rinth5 = cv2.threshold(image5,0,255,cv2.THRESH_OTSU)
# cv2.imwrite('rin10c03.png',rinth)



try:
    slope, intercept = ssim(grayA, grayB)
except TypeError:
    slope, intercept = 0,0

# print(resize1.shape)
# print(resize2.shape)
# print(score)
print(slope)
# print(ret) # ได้ 118
# print(ret2)
# print(ret3)
# print(ret4)
# print(ret5)
# new_image = image.resize((300, 250))
# # cv2.putText(new_image,str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")),(0, 30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),2)
# new_image.save('image_400.jpg')
# # cv2.imwrite("newre.jpg",new_image)

# # cv2.imshow('new',image)

# print(image.size) # Output: (1920, 1280)
# print(new_image) # Output: (400, 400)

# cap = cv2.VideoCapture(0)

# # cap.set(3, 176)
# # cap.set(4, 144)

# while(True):
#     ret, frame = cap.read()
#     resize = cv2.resize(frame, (300, 250)) 
#     cv2.imshow('frame',resize)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             break
