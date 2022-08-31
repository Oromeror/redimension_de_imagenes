import os


class Archivo:
    def _init_(self):
        self.ruta = None
        self.contenido = None
        self.archivos = None

    def __str__(self):
        return self.ruta

    def validar_ruta_archivo(self):
        if os.path.exists('Archivo de Imagenes'):
            self.ruta = 'Archivo de Imagenes'
            self.contenido = os.listdir(self.ruta)
            return True

    def cargar_archivos(self):
        if self.validar_ruta_archivo():
            return self.contenido