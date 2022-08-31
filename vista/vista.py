import os
from time import sleep
import sys


class Consola:
    '''
    Objeto que hace visible las funcionalidades del programa.
    '''
    def __init__(self):
        '''
        Valida el sistema operativo por el usuario
        para ejecutar correctamente el programa.
        '''
        if self.obtener_plataforma() == 'Windows':
            self.borrado_consola = lambda: os.system('cls')
        else:
            self.borrado_consola = lambda: os.system('clear')

    def obtener_plataforma(self):
        '''
        Valida el sistema operativo en el que se ejecuta la aplicación.
        '''
        plataformas = {
            'linux1': 'Linux',
            'linux2': 'Linux',
            'darwin': 'OS X',
            'win32': 'Windows'
        }
        if sys.platform not in plataformas:
            return sys.platform
        return plataformas[sys.platform]

    def iniciar_consola(self):
        '''
        Bienvenieda al usuario.
        '''
        print('Bienvenido')
        sleep(0.5)
        input('Presione cualquier tecla para iniciar.')

    def mostrar_menu_de_opciones(self):
        '''
        Menú principal de la aplicación.
        '''
        menu = '''    
            1. Procesar imágenes.
            2. Procesar imágenes transparentes a fondo blanco.
            
            Opciones generales
            3. Salir.
        '''
        print(menu)

    def obtener_opcion(self):
        '''
        Almenacena en ejecución las opciones elegidas
        por el usuario.
        '''
        try:
            return int(input('Opcion: '))
        except:
            return None

    def enviar_opcion_menu(self):
        '''
        Inicializa la vista del menu de opciones de la aplicacion.
        '''
        self.borrado_consola()
        print("Seleccione lo que desea hacer: ")
        self.mostrar_menu_de_opciones()
        return self.obtener_opcion()

    def mostrar(self, elemento):
        '''
        Imprime en la consola una relación ajustada en el controlador.
        '''
        self.borrado_consola()
        print(elemento)
        input('Presione enter para continuar.')

    def mostrar_error(self, error):
        '''
        Muestra un error generado por una excepcion
        enviada desde el controlador.
        '''
        self.borrado_consola()
        print('Error: {}'.format(error))
        sleep(1.5)
