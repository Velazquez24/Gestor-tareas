class Tabla_de_puntuaciones:
    def mostrar_menu(self):
        print('Menu principal'.center(60,'-'))
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
    def ingresar_puntuacion(self):
        while True:
            print('Por favor, introduzca una puntuación en una escala de 1 a 5')
            point = input()

            if point.isdecimal():
                point = int(point)
                
                if point <= 0 or point > 5: 
                        print('Indíquelo en una escala de 1 a 5')
                else:
                        print('Por favor, introduzca un comentario')
                        comment = input()
                        post = f'punto: {point} comentario: {comment}'
                        file_pc = open("data.txt", 'a')
                        file_pc.write(f'{ post } \n')
                        file_pc.close()
                        break
            else:
                    print('Por favor, introduzca la puntuación en números')
    def comprobar_resultado(self):
              print ('resultados hasta la fecha')
              try:
                    with open("data.txt", "r") as read_file:
                        print(read_file.read())
              except FileNotFoundError:
                   print ('no hay datos disponibles')
    def finalizar(self):
             print ('finalizando')
             return True
    
    def inciar(self):
            while True:
                self.mostrar_menu()
                num = input('Seleccione una opcion: ')
                
                if num.isdecimal():
                    num = int(num)
                    if num == 1:
                        self.ingresar_puntuacion()
                    elif num == 2:
                        self.comprobar_resultado()
                    elif num == 3:
                        if self.finalizar():
                            break
                else:
                    print('Introduzca un número del 1 al 3')
            else:
                print('Introduzca un número del 1 al 3')
procesador = Tabla_de_puntuaciones()
procesador.inciar()