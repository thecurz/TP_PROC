import cv2
import pickle

FILE_NAME = 'sitios.png'
PKL_FILE_NAME = 'sitios.pkl'
NUM_SPACES = 18

img = cv2.imread(FILE_NAME)

espacios = []

for x in range(NUM_SPACES):
    espacio = cv2.selectROI('espacio', img, False)
    cv2.destroyWindow('espacio')
    espacios.append(espacio)

    for x, y, w, h in espacios:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

with open(PKL_FILE_NAME, 'wb') as file:
    pickle.dump(espacios, file)
