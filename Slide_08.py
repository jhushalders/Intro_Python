#NumPy com Imagens
import os
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
imagem = io.imread('IMG_1803.jpg')
print("shape:", imagem.shape,
"| dtype:", imagem.dtype,
"| min/max:", imagem.min(), imagem.max())
#mostrar imagem
plt.imshow(imagem)
plt.show()
#Transformações Simples: Flip e Transpose
plt.imshow(imagem[::-1, :]) # inverte linhas
plt.imshow(imagem[:, ::-1]) # inverte colunas
plt.imshow(imagem.transpose(1,0,2)) # transposta
#[::-1] → percorre o array de trás para frente (espelhamento).
#transpose(1,0,2) → troca linhas por colunas, girando a imagem.
#acessando canais de cor
R, G, B = imagem[:,:,0], imagem[:,:,1], imagem[:,:,2]
plt.imshow(R, cmap='Reds')
plt.imshow(G, cmap='Greens')
plt.imshow(B, cmap='Blues')

#Recortes, subamostragens e modificação de pixel
#Recorte: seleciona apenas parte da foto, como se fosse um "zoom".
#Subamostragem: pula pixels, gerando efeito pixelado.
#np.where: altera condicionalmente, criando efeitos como limiarização (clarear/escurecer pixels).
plt.imshow(imagem[0:300,0:350]) # recorte da imagem
plt.imshow(imagem[::10,0::10]) # linhas/colunas de 10 em 10
nova_imagem = np.where(imagem > 150, 250, 0)
plt.imshow(nova_imagem)
plt.show()
#Salvando Imagens
io.imsave('imagem_modificada.png', nova_imagem.astype(np.uint8))
print("Imagem salva como 'imagem_modificada.png'")
#astype(np.uint8) → converte os valores para o formato correto de imagem (0-255).
#io.imsave → função do skimage para salvar imagens.
