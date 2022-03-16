#IMPORTS
import cv2
import os,sys, os.path
import numpy as np

#Pegar Imagem da Webcam
def Webcam(imagem):

    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    imagem_lower_hsvAzul = np.array([65, 100, 120])  
    imagem_upper_hsvAzul = np.array([110, 150, 150])
    maskAzul = cv2.inRange(imagem_hsv, imagem_lower_hsvAzul, imagem_upper_hsvAzul)

    imagem_lower_hsvVermelho1 = np.array([0, 120, 100])  
    imagem_upper_hsvVermelho1 = np.array([10, 255, 255])
    maskVermelho1 = cv2.inRange(imagem_hsv, imagem_lower_hsvVermelho1, imagem_upper_hsvVermelho1)

    imagem_lower_hsvVermelho2 = np.array([170, 120, 100])  
    imagem_upper_hsvVermelho2 = np.array([180, 255, 255])
    maskVermelho2 = cv2.inRange(imagem_hsv, imagem_lower_hsvVermelho2, imagem_upper_hsvVermelho2)

    mask_hsvVermelho = cv2.bitwise_or(maskVermelho1, maskVermelho2)
    maskFinal = cv2.bitwise_or(mask_hsvVermelho, maskAzul)

    return maskFinal

#Abrir Tela com imagem capturada da WebCam
cv2.namedWindow("Pré-Visualização")
video = cv2.VideoCapture(0)


if video.isOpened():
    rval, frame = video.read()
else:
    rval = False
while rval:
    imagem = Webcam(frame)
    cv2.imshow("Pré-Visualização", imagem)
    rval, frame = video.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("Pré-Visualização")
video.release()
