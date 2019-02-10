import os
import cv2

for i,img_file in enumerate(os.listdir('train')):
    if i%100==0:
        print('Resizing file: ',i)
    image = cv2.imread('train\\'+img_file)
    image = cv2.resize(image,(256,256))
    cv2.imwrite('train_resize\\'+img_file,image)