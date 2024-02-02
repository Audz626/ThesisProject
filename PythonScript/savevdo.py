# Python program to save a 
# video using OpenCV
  
from datetime import datetime   
import cv2
import time
  
   
# Create an object to read 
# from camera
video = cv2.VideoCapture(0)
   
# We need to check if camera
# is opened previously or not
if (video.isOpened() == False): 
    print("Error reading video file")
  
# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(video.get(3))
frame_height = int(video.get(4))
   
size = (frame_width, frame_height)
   
# Below VideoWriter object will create
# a frame of above defined The output 
# is stored in 'filename.avi' file.
count = 10
if(count == 10):
    first_datetimeVDO = datetime.now().strftime('%Y-%m-%d %H-%M-%S') #
    time.sleep(5.0)
    second_datetimeVDO = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    count -= 10

if (first_datetimeVDO < second_datetimeVDO):
    result = cv2.VideoWriter('static/VDO/'+str(second_datetimeVDO)+'Test.mkv', cv2.VideoWriter_fourcc(*'x264'), 10, size)#DIVX

last_datetimeVDO = None

# if (start_datetimeVDO < last_datetimeVDO):
#     print('start < end')

# print(start_datetimeVDO)

    
while(True):
    ret, frame = video.read()
  
    if ret == True: 
  
        # Write the frame into the
        # file 'filename.avi'
        result.write(frame)
  
        # Display the frame
        # saved in the file
        cv2.imshow('Frame', frame)
  
        # Press S on keyboard 
        # to stop the process
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
  
    # Break the loop
    else:
        break
  
# When everything done, release 
# the video capture and video 
# write objects
video.release()
result.release()
    
# Closes all the frames
cv2.destroyAllWindows()
   
print("The video was successfully saved")