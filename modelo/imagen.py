import numpy as np
import cv2
import os


class Imagen:
    def _init_(self):
        self.imagen = None

    def cortar_imagenes(self, ruta, imagenes):
        for archivo in range(len(imagenes)):
            ruta_imagen = ruta + "/" + imagenes[archivo]
            print(ruta_imagen)
            img = cv2.imread(ruta_imagen, cv2.IMREAD_UNCHANGED)

            altura = img.shape[0]
            anchura = img.shape[1]

            if altura > anchura:

                imgn = np.ones((altura, altura, 4)) * 400
                aux = int((altura - anchura) / 2)
                imgn[:, aux:(aux + anchura), :] = img

            elif anchura > altura:

                imgn = np.ones((anchura, anchura, 4)) * 400
                aux = int((anchura - altura) / 2)
                imgn[aux:(aux + altura), :, :] = img

            else:
                imgn = img

            imgn = cv2.resize(imgn, (400, 400))
            cv2.imwrite(ruta_imagen, imgn)

        print('Número de fotos procesadas: ', len(imagenes))

    def cortar_imagenes_blanco(self, ruta, imagenes):
        for archivo in range(len(imagenes)):
            ruta_imagen = ruta + "/" + imagenes[archivo]
            print(ruta_imagen)
            img = cv2.imread(ruta_imagen, cv2.IMREAD_UNCHANGED)

            masc_transp = img[:, :, 2] == 0
            img[masc_transp] = [255, 255, 255]

            altura = img.shape[0]
            anchura = img.shape[1]

            if altura > anchura:

                imgn = np.ones((altura, altura, 4)) * 255
                aux = int((altura - anchura) / 2)
                imgn[:, aux:(aux + anchura), :] = img

            elif anchura > altura:

                imgn = np.ones((anchura, anchura, 4)) * 255
                aux = int((anchura - altura) / 2)
                imgn[aux:(aux + altura), :, :] = img

            else:
                imgn = img

            imgn = cv2.resize(imgn, (400, 400))
            cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            cv2.imwrite(ruta_imagen, imgn)

        print('Número de fotos procesadas: ', len(imagenes))

    '''
    # Revisar
    def validar_imagenes(self):
        imgs = self.cargar_imagenes()
        for aux in imgs:
            img = cv2.imread(imgs.index(aux)) 
            altura = img.shape[0]
            anchura = img.shape[1]
            if altura > 2000 
            img_disminuida = cv2.resize(img,(100,100),inerpolation='linear')
            return img_disminuida
    '''