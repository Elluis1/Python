# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:

from grafo1 import Grafo

grafoPersonajes=Grafo(dirigido=False)

# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;

grafoPersonajes.insert_vertice("Luke Skywalker")
grafoPersonajes.insert_vertice("Leia Organa")
grafoPersonajes.insert_vertice("Han Solo")
grafoPersonajes.insert_vertice("Darth Vader")
grafoPersonajes.insert_vertice("Yoda")
grafoPersonajes.insert_vertice("Boba Fett")
grafoPersonajes.insert_vertice("C-3PO")
grafoPersonajes.insert_vertice("Rey")
grafoPersonajes.insert_vertice("Kylo Ren")
grafoPersonajes.insert_vertice("Chewbacca")
grafoPersonajes.insert_vertice("R2-D2")
grafoPersonajes.insert_vertice("BB-8")


grafoPersonajes.insert_arist("Luke Skywalker","Leia Organa",3)
grafoPersonajes.insert_arist("Luke Skywalker","Han Solo",4)
grafoPersonajes.insert_arist("Leia Organa","Han Solo",2)
grafoPersonajes.insert_arist("Darth Vader","Han Solo",5)
grafoPersonajes.insert_arist("Darth Vader","Yoda",1)
grafoPersonajes.insert_arist("Boba Fett","Rey",1)
grafoPersonajes.insert_arist("C-3PO","R2-D2",8)
grafoPersonajes.insert_arist("Kylo Ren","BB-8",2)
grafoPersonajes.insert_arist("Han Solo","Chewbacca",6)
grafoPersonajes.insert_arist("Darth Vader","Rey",6)



grafoPersonajes.barrido()

# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
bosque, control = grafoPersonajes.kruskal()

for arbol in bosque:
    print('arbol')
    for nodo in arbol.split(';'):
        print(nodo)

if control is not None:
    print('Esta yoda')
else:
    print('No esta Yoda')

# c) determinar cuál es el número máximo de episodio que comparten dos personajes y quienes son
print(grafoPersonajes.barrido_mayor())


# d) agregar al ejercicio de grafo camino mas corto desde Yoda a Rey
print('Camino mas corto')
ori = 'Yoda'
des = 'Rey'

# valida que exista un camino posible
path=grafoPersonajes.has_path(ori,des)

# busca los vertices
origen = grafoPersonajes.search_vertice(ori)
destino = grafoPersonajes.search_vertice(des)

# variables para dar posterior respuesta
camino_mas_corto = None
peliculas=0

if(origen is not None and destino is not None):
    if path == True: # confirma que si existe un posible camino
        camino_mas_corto = grafoPersonajes.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop() # value toma valor de camino_mas_corto y lo borra de este
            if fin == value[0]:
                peliculas += value[1] # suma el peso a la variable personajes
                print(value[0],'peliculas', value[1])
                fin = value[2]
          # printea en caso que exista un camino posible con la cantidad de metros de personajes necesarios
        print(f'La conexion entre los personajes es despues de {peliculas} peliculas')
    else: # en caso que no exista camino
        print("No existe camino entre", ori, "y", des)