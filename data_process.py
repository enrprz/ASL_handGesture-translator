# pylint: disable=E1101
import numpy as np
import cv2
import os

#########################################################
path = 'dataset_2/Asl-alphabet-training'
mlist = os.listdir(path)
#print (mlist)
#########################################################

images = []
calssNo = []
numOfLetters = len(mlist)

for x in mlist:
    myPicList = os.listdir(path + "/" + str(x))
    for y in myPicList:
        curImg = cv2.imread(path + "/" + str(x) + "/" + y)
        curImg = cv2.resize(curImg,(50,50))
        images.append(curImg)
        calssNo.append(x)

images = np.array(images)
calssNo = np.array(calssNo)