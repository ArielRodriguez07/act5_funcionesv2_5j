print("funciones version 2")
print("ariel rodriguez")
#zona de listas tuplas sets y diccionarios
celulares=["samsung","iphone 11","chafa"]
bandas=["enjambre","zoe","porter"]
#zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)
def verbanda(rock):
    for unabanda in rock:
        print(unabanda)

#llamada de funciones
print("imprime celulares de una lista ")
verlista(celulares)
print("imprime una lista de bandas de rock")
verbanda(bandas)
