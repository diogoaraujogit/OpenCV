#Importando as bilbiotecas
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregando uma imagem
imagem = cv2.imread("rickmorty.jpg") # Flag determina se a imagem vai ser em P&B ou colorida (pode omitir)

# Criando os 3 histogramas
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([imagem], [i], None, [256], [0, 256]) #Plotando pelo próprio cv2
    plt.plot(histr, color = col)
    plt.xlim([0, 256])

#Mostrando a imagem e o histograma
cv2.imshow("Rick and Morty", imagem) #Título da imagem e a imagem carregada
plt.show()
cv2.waitKey(0) #Espera indefinidamente até o usuário digitar alguma tecla
cv2.destroyAllWindows() #Fecha as janelas de imagem