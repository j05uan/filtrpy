from bussines.generos import*
from commons.utils import*
from commons.menus import*
from bussines.actores import*
from bussines.formatos import*
from bussines.peliculas import*
while(True):
    op=menu_principal()
    if(op==1):
        while(True):
            op=menu_generos()    
            if(op==1):
                generos=load_generos_json()
                generos.append(crear_genero())
                guardar_json_generos(generos)
            elif(op==2):
                generos=load_generos_json()
                generos.append(modificacion_genero())
                guardar_json_generos(generos)
            elif(op == 3):
                generos = load_generos_json()
                mostrar_lista_con_diccionarios(generos)
                input("Oprima cualquier tecla para salir")    
            elif(op == 4):
                print("ADIOS")
                break
    elif(op==2):
        while(True):
            op=menu_actores()
            if(op==1):
                actores=load_actores_json()
                actores.append(crear_actores())
                guardar_json_actores(actores)
            elif(op==2):
                actores = load_actores_json()
                mostrar_lista_con_diccionarios(actores)
                input("Oprima cualquier tecla para actores")
            elif(op==3):
                actores=load_actores_json()
                actores.append(eliminar_actor())
                guardar_json_actores(actores)   
            elif(op == 4):
                print("ADIOS")
                break
    elif(op==3):
        while(True):
            op=menu_FORMATOS()
            if(op==1):
                formatos=load_actores_json()
                formatos.append(crear_formatos())
                guardar_json_formatos(formatos)
            elif(op==2):
                formatos = load_formatos_json()
                mostrar_lista_con_diccionarios(formatos)
                input("Oprima cualquier tecla para salir")
            elif(op == 3):
                print("ADIOS")
                break
    elif(op==4):   
        while(True):
            op=menu_gestor_peliculas()
            if(op==1):
                peliculas=load_peliculas_json()
                peliculas.append(crear_pelicula())
                guardar_json_peliculas(peliculas)
            elif(op==2):
                peliculas = load_peliculas_json()
                mostrar_lista_con_diccionarios(peliculas)
                input("Oprima cualquier tecla para salir")
            elif(op==3):
                peliculas=load_actores_json()
                nombre=input("Ingrese el nombre de la peliculas: ")
                for pelicula in peliculas:
                    if pelicula["Nombre"]==nombre:
                        print(pelicula)
            elif(op==4):
                peliculas=load_peliculas_json()
                peliculas.append(editar_pelicula())
                guardar_json_peliculas(peliculas)
            elif(op==5):
                peliculas=load_actores_json()
                peliculas.append(eliminar_pelicula())
                guardar_json_peliculas(peliculas)

            elif(op==6):
                print("ADIOS")
                break       
    elif(op==5):
        while(True):
            op=menu_gestor_informes()
            if(op==1):
                peliculas=load_actores_json()
                print(peliculas)
                nombregenero=input("Ingrese el nombre del genero del cualquiere ver las peliculas disponibles: ")
                for pelicula in peliculas:
                    if pelicula["npelicula"]["Genero"]==nombregenero:
                        print(pelicula)
            if(op==2):
                peliculas=load_actores_json()
                print(peliculas)
                nombregenero=input("Ingrese el nombre del genero del cualquiere ver las peliculas disponibles: ")
                for pelicula in peliculas:
                    if pelicula["Nombre"]==nombregenero:
                        print(pelicula)
                
                    
