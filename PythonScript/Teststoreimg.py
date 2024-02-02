import numpy as np
import matplotlib.pyplot as plt
import cv2
import imagehash

from PIL import Image, ImageChops

im1 = Image.open("PythonScript/Test2.jpg") #C:\Audddxd\KMUTNB\Project\WebDev\PythonScript
im2 = Image.open("PythonScript/Test3.jpg")

# diff = ImageChops.difference(im2, im1)
# imgcompare = PIL.image_diff_percent(im1, im2)
# print(type(imgcompare))
# load images
img1 = cv2.resize(cv2.imread("PythonScript/Test2.jpg"), (300, 250)).astype(np.int32)
img2 = cv2.resize(cv2.imread("PythonScript/Test3.jpg"), (300, 250)).astype(np.int32)
image1 = cv2.imread("PythonScript/Test2.jpg",1)
image2 = cv2.imread("PythonScript/Test5.jpg",1)

resize1 = cv2.resize(image1, (300, 250))
resize2 = cv2.resize(image2, (300, 250))

arr2im = Image.fromarray(resize1)
arr3im = Image.fromarray(resize2)

img_before = Image.open("PythonScript/Test2.jpg")

phash_bef = imagehash.phash(arr2im)
gs_hash_bef = imagehash.hex_to_hash(str(phash_bef))
phash_bef1 = imagehash.phash(arr3im)
gs_hash_bef1 = imagehash.hex_to_hash(str(phash_bef1))

arr = np.array(img_before) #แปลง img to array
t = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB) #COLOR_GRAY2RGB
# t_re = cv2.cvtColor(image1, cv2.COLOR_GRAY2RGB)

arr1 = np.array(arr3im)

# cv2.cvtColor(arr, COLOR_BGRA2BGR)

# arr.save("a2.jpg")
# cv2.imwrite("aa.jpg",arr)
print(arr2im.mode)
# print(type(phash_bef))
# print(type(gs_hash_bef))
# print(type(arr2im))
# print(arr2im.mode)

print(gs_hash_bef-gs_hash_bef1)
# print(type(arr1))

# cv2.imwrite("a3.jpg",t)
# print(type(im1))
# img_before.show()
cv2.imshow('frame',resize1)
cv2.imshow('frame1',resize2)

cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows() 

# compute difference
# difference = cv2.subtract(image1, image2) 

# image3 = cv2.absdiff(img1, img2)
# diff = cv2.subtract(img1, img2)

# result = not np.any(diff) 

# if result is True:
#     print("The images are the same")
# else:
#     cv2.imwrite("result.jpg", diff)
#     print("the images are different")

# # color the mask red
# Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
# difference[mask != 255] = [0, 0, 255]

# # add the red mask to the images to make the differences obvious
# image1[mask != 255] = [0, 0, 255]
# image2[mask != 255] = [0, 0, 255]

# # store images
# cv2.imwrite('diffOverImage1.png', image1)
# cv2.imwrite('diffOverImage2.png', image1)
# cv2.imwrite('diff.png', difference)

# a = np.array([[4,2,0],[9,3,7],[1,2,1]])
# b = np.array([[3,1,1],[8,2,8],[2,3,4]])
# x1 = np.linalg.det(a)
# x2 = np.linalg.det(b)
# x3 = a.sum()
# x4 = b.sum()
# print(x1)
# print(x2)
# print(x3)
# print(x4)
# print(type(x1))
# print(type(a))

# ar1 = np.array([[1,1,2],
#                 [2,2,3],
#                 [3,3,4]])
# ar2 = np.array([[4,4,4],
#                 [2,2,2],
#                 [1,1,1]])

# print(ar1[0][0][0])