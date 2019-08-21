#Importando as bilbiotecas
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregando uma imagem
imagem = cv2.imread("rickmorty.jpg", 0) # Flag determina se a imagem vai ser em P&B ou colorida (pode omitir)

# Função de limiarização
# Parametros: nome da imagem, limiar, que cor os pixels acima do limiar vão receber, como a limiarização vai funcionar
limiar, imagemLimiar = cv2.threshold(imagem, 150, 255, cv2.THRESH_BINARY) #Abaixo ou igual ao limiar recebe 0. Acima recebe 255
limiar, imagemLimiar = cv2.threshold(imagem, 150, 255, cv2.THRESH_BINARY_INV) #Abaixo ou igual ao limiar recebe 255. Acima recebe 0
limiar, imagemLimiar = cv2.threshold(imagem, 150, 255, cv2.THRESH_TRUNC) #Abaixo ou igual ao limiar, mantém. Acima, recebe o limiar
limiar, imagemLimiar = cv2.threshold(imagem, 150, 255, cv2.THRESH_TOZERO) #Todos acima do limiar, mantém. Abaixo, recebe 0
limiar, imagemLimiar = cv2.threshold(imagem, 150, 255, cv2.THRESH_TOZERO_INV) #Abaixo ou igual ao limiar, mantém. Acima recebe 0
# Mostrando uma imagem
cv2.imshow("Rick and Morty", imagemLimiar) #Título da imagem e a imagem carregada
cv2.waitKey(0) #Espera indefinidamente até o usuário digitar alguma tecla
cv2.destroyAllWindows() #Fecha as janelas de imagem
    
#Salvando a Imagem
cv2.imwrite("rickmorty_thresh_tozero_inv.jpg", imagemLimiar) #Nome da imagem salva, imagem carregada