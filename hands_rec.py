# pylint: disable=E1101
import cv2
import sys

video_cap = cv2.VideoCapture(0)
img_count = 0


while True:
    ret, frame = video_cap.read()
    k = cv2.waitKey(1)

    cv2.imshow('FaceDetection', frame)

    if k%256 == 27: #Stop when ESC is pressed
        break
    elif k%256 == 32: #Take a picture when space is pressed
        img_name = "facedetect_webcam_{}.png".format(img_count)
        cv2.imwrite(img_name,frame)
        print("{} written!".format(img_name))
        img_count += 1

video_cap.release()
cv2.destroyAllWindows()