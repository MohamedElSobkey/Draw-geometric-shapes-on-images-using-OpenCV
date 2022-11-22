import cv2
import numpy as np

#img = cv2.imread('./lena.jpg', 1)
#creating window
img = np.zeros([512,512,3], np.uint8) #512 columns
                                      # 512 rows 
                                      # 3 matrix 3x3

# to create line on image                                      
##img = cv2.line(img, (0,0) , (256,256) , (0,255,0) , 10)   
# to creat arrowed line
##img = cv2.arrowedLine(img , (0,256) , (256,256) , (0,255,255) , 10) 
                                   
# to create rectangle
##img = cv2.rectangle(img, (384,0) , (510,128), (0,0,255), 10) # 10 for thichness if u replace 10 by -1 it will fill the rectangle with the color
# to creat circle
##img = cv2.circle(img, (447,63), 63 , (0,255,0) , 5)

# to write on the window
##font = cv2.FONT_HERSHEY_SIMPLEX #type of font
##img = cv2.putText(img, 'OpenCv', (10,210), font, 4, (0, 255, 255), 10, cv2.LINE_AA)# write a text

# to create polyline
#pts = np.array([[10,5], [20,30], [70,20],[50,10]], np.int32)#make array to draw it by polylines
#img = cv2.polylines(img,[pts], True, (0,255,255) ) 


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
                                      