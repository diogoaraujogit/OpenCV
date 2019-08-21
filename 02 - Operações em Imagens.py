#Importando as bilbiotecas
import cv2
import numpy

# A origem da imagem é no topo superior esquerdo. E a ordem é (y,x)
# Carregando uma imagem
imagem = cv2.imread("rickmorty.jpg") # Flag determina se a imagem vai ser em P&B ou colorida (pode omitir)

print(imagem.shape) # Largura, altura, números de canais de cor (BGR)
print(imagem.item(380, 380, 2), imagem.item(380, 380, 1), imagem.item(380, 380, 0)) # Mostrar os canais Vermelho, Verde e Azul do pixel

# Modificar cor do pixel
imagem.itemset((380, 380, 2), 255) # Vermelho 255 no pixel 380,380. Restante em 0
imagem.itemset((380, 380, 1), 0)
imagem.itemset((380, 380, 0), 0)

'''
# Mostrando uma imagem
cv2.imshow("Rick and Morty", imagem) #Título da imagem e a imagem carregada
cv2.waitKey(0) #Espera indefinidamente até o usuário digitar alguma tecla
cv2.destroyAllWindows() #Fecha as janelas de imagem
'''

# Região de Interesse
morty_head = imagem[164:359, 529:784]
#Salvando a Imagem
cv2.imwrite("morty_head.jpg", morty_head) #Nome da imagem salva, imagem carregada

# Colocando essa imagem em outra parte da imagem
imagem[0:195, 224:479] = morty_head

# Mostrando uma imagem
cv2.imshow("Rick and Morty", imagem) #Título da imagem e a imagem carregadao
cv2.waitKey(0) #Espera indefinidamente até o usuário digitar alguma tecla
cv2.destroyAllWindows() #Fecha as janelas de imagem

#Salvando a Imagem
cv2.imwrite("rick_with_morty_head.jpg", imagem) #Nome da imagem salva, imagem carregada