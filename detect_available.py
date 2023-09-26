import cv2
import pickle
import numpy as np
from utils import detect_color_boundaries
# LOWER_COLOR = np.array([43, 21, 127])
# UPPER_COLOR = np.array([92, 73, 203])
LOWER_COLOR = np.array([31, 20, 86])
UPPER_COLOR = np.array([92, 73, 203])
MIN_PCT = 0.50
PKL_FILE_NAME = 'sitios.pkl'
# VIDEO_FILE_NAME = 'video.mp4'
VIDEO_FILE_NAME = 'trimmed_video.mp4'

sitios = []
with open(PKL_FILE_NAME, 'rb') as file:
    sitios = pickle.load(file)

video = cv2.VideoCapture(VIDEO_FILE_NAME)

while True:
    check, img = video.read()
    imgMedian = cv2.medianBlur(img, 5)
    kernel = np.ones((5, 5), np.int8)
    imgDil = cv2.dilate(imgMedian, kernel)

    for x, y, w, h in sitios:
        espacio = imgDil[y:y+h, x:x+w]
        if not espacio.size:
            continue
        
        TOTAL = len(espacio) * len(espacio[0])  
        MIN_COUNT = (TOTAL * MIN_PCT)

        # print(detect_color_boundaries(espacio))

        mask = cv2.inRange(espacio, LOWER_COLOR, UPPER_COLOR)
        non_matching_pixels = cv2.bitwise_not(mask)
        count = cv2.countNonZero(non_matching_pixels)
        
        cv2.putText(img, str(int(count/TOTAL * 100)) + "%", (x, y+h-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)

        if count < MIN_COUNT:
            # LIBRE
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        else:
            # OCUPADO
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('video', img)
    cv2.waitKey(10)
