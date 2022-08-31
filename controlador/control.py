from vista.vista import Consola
from modelo.imagen import Imagen
from modelo.archivo import Archivo


class Ejecutor:
    def __init__(self):

        self.consola = Consola()
        self.archivo = Archivo()
        self.imagen = Imagen()
        self.iniciar()

    def iniciar(self):
        '''
            Controla la relación entre la vista y el controlador.
        '''
        opcion = self.consola.enviar_opcion_menu()
        if opcion == 1:
            self.procesar_imagenes()
        elif opcion == 2:
            self.procesar_imagenes_a_blanco()
        elif opcion == 3:
            exit()
        else:
            self.consola.mostrar_error('Seleccione una opción valida.')

    def procesar_imagenes(self):
        if self.archivo.validar_ruta_archivo():
            self.imagen.cortar_imagenes(self.archivo.ruta,
                                        self.archivo.cargar_archivos())
        else:
            self.consola.mostrar_error("No existe el Archivo de Imagenes")
        input("Presione una tecla para continuar")

    def procesar_imagenes_a_blanco(self):
        if self.archivo.validar_ruta_archivo():
            self.imagen.cortar_imagenes_blanco(self.archivo.ruta, 
                                                self.archivo.cargar_archivos())
        else:
            self.consola.mostrar_error("No existe el Archivo de Imagenes")
        input("Presione una tecla para continuar")