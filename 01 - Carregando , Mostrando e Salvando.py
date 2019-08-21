#Importando a bilbioteca
import cv2

# Carregando uma imagem
imagem = cv2.imread("rickmorty.jpg", 0) # Flag determina se a imagem vai ser em P&B ou colorida (pode omitir)

#Mostrando uma imagem
cv2.imshow("Rick and Morty", imagem) #Título da imagem e a imagem carregada
cv2.waitKey(0) #Espera indefinidamente até o usuário digitar alguma tecla
cv2.destroyAllWindows() #Fecha as janelas de imagem

#Salvando a Imagem
cv2.imwrite("rickmortypb.jpg", imagem) #Nome da imagem salva, imagem carregada

