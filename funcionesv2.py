print("funciones version 2")
print("ariel rodriguez")
#zona de listas tuplas sets y diccionarios
celulares=["samsung","iphone 11","chafa"]
bandas=["enjambre","zoe","porter"]
canciones=["bajo la lluvia","azul","murcielago"]
computadoras=["hp","mac","microsoft"]
#zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)
def verbanda(rock):
    for unabanda in rock:
        print(unabanda)
def vercanciones(songs):
    for unacancion in songs:
        print(unacancion)
def vercomputadoras(marca):
    for unacompu in marca:
        print(unacompu)

#llamada de funciones
print("imprime celulares de una lista ")
verlista(celulares)
print("imprime una lista de bandas de rock")
verbanda(bandas)
print("imprime una lista de canciones de rock")
verbanda(canciones)
print("imprime una lista de computadoras")
verbanda(computadoras)
print("Esto es un ejemplo de diccionario")
## diccionario
audifonos = {
  "marca": "apple",
  "modelo": "version 1.9",
  "año": 2024
}
print(audifonos)