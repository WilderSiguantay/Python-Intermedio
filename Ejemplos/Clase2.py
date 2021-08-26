#class ClassName:
    #declaraciones
'''
class Persona:
    nombre = ''
    apellido = ''
    universidad = ''
    dpi = ''
    nit = ''

#INSTANCIA DE UN OBJETO

eduardo = Persona()

eduardo.nombre = 'Eduardo'
eduardo.apellido = 'Cuevas'
eduardo.universidad = 'USAC'
eduardo.dpi = '21452145132154'
eduardo.nit = '1234567'

print("Nombre de nuestro objeto ", eduardo.nombre)
print("El apellido es: " + eduardo.apellido)
print("La universidad es: %s y su DPI es: %s" % (eduardo.universidad,eduardo.dpi))
'''
'''
class Persona:
    nombre = ''
    universidad = ''

    def print_nombre(self):
        print(self.nombre)

    def print_uni(self):
        print(self.universidad)

    def print_datos(self):
        print(self.nombre," ", self.universidad)


eduardo = Persona()

eduardo.nombre = 'Eduardo'
eduardo.universidad = 'USAC'

eduardo.print_nombre()
eduardo.print_uni()
eduardo.print_datos()

'''
'''
class Person:

    def __init__(self, n, u):
        self.name = n
        self.universidad = u

    #metodo 1
    def print_name(self):
        print(self.name)
    
    #metodo 2
    def print_universidad(self):

        print(self.universidad)
        return 'La Universidad es: ' + self.universidad

jorge = Person('Jorge', 'Universidad de San Carlos')

jorge.print_name()
jorge.print_universidad()

jorgeUniversidad = jorege.print_universidad()

print(jorgeUniversidad)
    

'''

#SINTAXIS DE UN METODO
# def nombredelmetodo:
    #bloque de codigo

#SINTAXIS DE UNA FUNCION 
# def nombredelafuncion:
    #bloque de codigo
    #retorno

#EJEMPLOS DE FUNCIONES
#Funcion sin retorno

def sumar(n1, n2):
    resultado = 0
    resultado = n1 + n2
    print("El resultado de la suma es: ", resultado)

#sumar(3,5)

#Funcion con retorno
def resta(n1, n2):
    resultado = 0
    resultado = n1 - n2
    return resultado

#resResta = resta(9,4)

#print(resResta)


#Funcion con argumentos arbitrarios

def my_funcion(*kids):
    print('Funcion con parametros arbitrarios')
    print('El niño mas pequeño es: ' + kids[0])

my_funcion("Eduardo", "Wilder", "Matias", "Giovanni", "Jose")
             # 0         #1        #2       #3          #4

#Funcion con argumentos Clave

def funcion_clave(child2, child1, child3):
    print("Funcion con argumentos Clave")
    print("El mas pequeño es: " + child2) 

funcion_clave(child2='Jorge', child1='Eduardo', child3='Giovanni')
funcion_clave('jorge', 'giovanni', 'eduardo')


#Funcion con argumentos clave valor arbitrarios

def func_arbitr_CV(**frutas):
    
    for clave in frutas:
        print('El valor de : ', clave," es " , frutas[clave]  )

func_arbitr_CV(fruta1='manzana', fruta2='naranja', fruta3='pera')
