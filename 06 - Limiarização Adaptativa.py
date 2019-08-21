#Importando as bilbiotecas
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregando a imagem
imagem = cv2.imread("rickmorty.jpg", 0) # Flag determina se a imagem vai ser em P&B ou colorida (pode omitir)

#imagem, tom do outro conjunto, média ou gaussiana, tipo, vizinhança limiar, valor que subtrai da média
adp1 = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                             cv2.THRESH_BINARY, 11, 2) # baseado na média dos tons, escolhe o limiar

adp2 = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                             cv2.THRESH_BINARY, 11, 2) # baseado na média dos tons, escolhe o limiar

# Mostrando as imagens
cv2.imshow("Rick and Morty", imagem) #Título da imagem e a imagem carregada
cv2.imshow("Rick and Morty 2", adp1) #Título da imagem e a imagem carregada
cv2.imshow("Rick and Morty 3", adp2) #Título da imagem e a imagem carregada
cv2.waitKey(0) #Espera indefinidamente até o usuário digitar alguma tecla
cv2.destroyAllWindows() #Fecha as janelas de imagem

#Salvando a Imagem
cv2.imwrite("rickmorty_adptive_thresh_mean.jpg", adp1) #Nome da imagem salva, imagem carregada
cv2.imwrite("rickmorty_adptive_thresh_gaussian.jpg", adp2) #Nome da imagem salva, imagem carregada