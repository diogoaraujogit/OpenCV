#Importando as bilbiotecas
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregando uma imagem
imagem = cv2.imread("rickmorty.jpg", 0) # Flag determina se a imagem vai ser em P&B ou colorida (pode omitir)
plt.hist(imagem.ravel(), 256, [0, 256]) # Hist trabalha com vetor 1-D, vavel modifica a matriz

#Mostrando a imagem e o histograma
cv2.imshow("Rick and Morty", imagem) #Título da imagem e a imagem carregada
plt.show()
cv2.waitKey(0) #Espera indefinidamente até o usuário digitar alguma tecla
cv2.destroyAllWindows() #Fecha as janelas de imagem