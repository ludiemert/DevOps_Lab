import os
import cv2
import face_recognition as fr

# Carregar imagens
imgElon = fr.load_image_file('images/Elon.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgElonTest = fr.load_image_file('images/ElonTest.jpg')
imgElonTest = cv2.cvtColor(imgElonTest, cv2.COLOR_BGR2RGB)

# Processar imagens
faceLoc = fr.face_locations(imgElon)[0]
encodeElon = fr.face_encodings(imgElon)[0]
encodeElonTest = fr.face_encodings(imgElonTest)[0]

# Comparar rostos
comparacao = fr.compare_faces([encodeElon], encodeElonTest)
distancia = fr.face_distance([encodeElon], encodeElonTest)

print(f"Comparação: {comparacao}, Distância: {distancia}")

# Mostrar imagens (remova para uso em headless container)
cv2.imshow('Elon', imgElon)
cv2.imshow('ElonTest', imgElonTest)
cv2.waitKey(0)
