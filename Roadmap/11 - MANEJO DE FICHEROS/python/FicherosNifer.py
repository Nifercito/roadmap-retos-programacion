''' * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 
EJERCICIO:
Desarrolla un programa capaz de crear un archivo que se llame como tu usuario de GitHub y tenga la extensión .txt.
Añade varias líneas en ese fichero:
- Tu nombre.
- Edad.
- Lenguaje de programación favorito.
Imprime el contenido.
Borra el fichero.'''

import os

#Creación de ficheros
'''Para crear un fichero se utiliza utilizando la función open("nombreFichero", "x") que la función reservada para ficheros'''

'''fichero = open("nifer.txt", "w")'''

#Agregar información a un ficheros
'''Para agregar información el nombre del fichero y el metodo .write("el texto a agregar") '''

'''fichero.write("Jhonatan David Cifuentes Figueroa \n")
fichero.write("Edad: 24 años \n")
fichero.write("Por el momento es python que es el que estoy aprendiendo y me gustó JavaScript junto con HTML y CCS\n")'''

#metodo With con ficheros
'''El metodo with se usa para la creación de ficheros de manera segura que abre un fichero y lo cierra automaticamente y se usa de la siguiente manera: with open("nombreFichero.txt", "w") as nombreVariable:
Ejemplo'''

'''elfichero = "ficheroEjemploWith.txt"

with open(elfichero, "w") as ficheroEjemplo: 
    ficheroEjemplo.write("Este es un ejemplo con with \n")

#leer un fichero
with open(elfichero, "r") as ficheroEjemplo:
    print(ficheroEjemplo.read())'''

#Eliminar un fichero
'''Para borrar un fichero en se importa "os" y se borra con os.remove, donde también se puede utilizar un condicional para validar si el fichero existe'''

"os.remove(elfichero)"

'''DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un  archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera: [nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.'''

def ficheros():

    ficheroVentas = "elFicheroDeVentas" 
    open(ficheroVentas, "a")

    while True:
        print("1. Agregar producto.")
        print("2. Colsultar producto.")
        print("3. Actulizar producto.")
        print("4. Mostrar todos los productos.")
        print("5. Eliminar producto.")
        print("6. Calcular venta de productos.")
        print("7. Calcular venta total.")
        print("8. Salir.")
        print("------------")
        opcion = input("Seleccione la opción deseada: ")
        print("------------")

        if opcion == "1":
            try:
                nombreProducto = str(input("Agregue el nombre del producto: "))
            except ValueError as e:
                print("------------")
                print("Digite un texto.", type(e))
                print("------------")
                ficheros()
            try:
                precioProducto = int(input("Agregue el precio del producto: "))
                cantidadProducto = int(input("Agregue la cantidad vendida del producto: "))
            except ValueError as e:
                print("------------")
                print("Digite un valor entero", type(e))
                print("------------")
                ficheros()
            with open(ficheroVentas, "a") as archivo:
                archivo.write(f"{nombreProducto}, {precioProducto}, {cantidadProducto}\n")
        elif opcion == "2":
            productoConsultar = input("Digite el producto a consultar: ")
            with open(ficheroVentas, "r") as archivo:
                for objeto in archivo.readlines():
                    if objeto.split(", ")[0] == productoConsultar:
                        print(objeto)
                        break
        elif opcion == "3":
            productoCambio = input("Digite el producto a actualizar: ")
            nuevoProducto = input("Digite el nuevo nombre del producto: ")
            precioCambio = input("Digite el nuevo precio: ")
            cantidadCambio = input("Digite la nueva cantidad: ")
            with open(ficheroVentas, "r") as archivo:
                productos = archivo.readlines()
            with open(ficheroVentas, "w") as archivo:
                for objeto in productos:
                    if objeto.split(", ")[0] == productoCambio:
                        archivo.write(f"{nuevoProducto}, {precioCambio}, {cantidadCambio}\n")
                        break
                    else:
                        archivo.write(objeto)
        elif opcion == "4":
            with open(ficheroVentas, "r") as archivo:
                print(archivo.read())
        elif opcion == "5":
            productoAEliminar = input("Digite el producto que desea eliminar: ")
            with open(ficheroVentas, "r") as archivo:
                productosEliminar = archivo.readlines()
            with open(ficheroVentas, "w") as archivo:
                for objeto in productosEliminar:
                    if objeto.split(", ")[0].lower() != productoAEliminar.lower():
                        archivo.write(objeto)
        elif opcion == "6":
            productoCalcular = input("Digite el producto que quiere ver el total: ")
            resultado = 0
            with open(ficheroVentas, "r") as archivo:
                for objeto in archivo.readlines():
                    componentes = objeto.split(", ")
                    if componentes[0] == productoCalcular:
                        precio = float(componentes[1])
                        cantidad = int(componentes[2])
                        resultado += precio * cantidad
                        break
            print(f"El total vendido de {productoCalcular} es: {resultado}")
            print("------------")
        elif opcion == "7":
            total = 0
            with open(ficheroVentas, "r") as archivo:
                for objeto in archivo.readlines():
                    producto = objeto.split(", ")
                    precio = int(producto[1])
                    cantidad = int(producto[2])
                    total += precio * cantidad
            print(f"El total vendido es de: {total} ")
        elif opcion == "8":
            print("Saliendo del programa...")
            os.remove(ficheroVentas)
            break
ficheros()
