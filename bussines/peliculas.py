from bussines.generos import*
from commons.utils import*
from commons.menus import*
from bussines.actores import*
from bussines.formatos import*
def guardar_json(lista,modo):# si pasa "w" sobrescribe todo, si pasa "a" añade en lo que ya esta
    try:
      with open(os.path.join("data", "peliculas.json"), modo) as archivo_json:
        json.dump(lista, archivo_json, indent=2)
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya generos guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def crear_pelicula():
    npelicula=0
    diccionario={}
    while(True):
        print("------NUEVA PELICULA------")
        npelicula+=1
        npmbrepelicula=input("Ingrese el nombre de la pelicula:")
        sinompsis=input("Agrege una breve sinopsis de la pelicula: ")
        print("---De los actores disponibles elija el protagonista: ")
        duracion=input("Agrege la duracion en minutos  el la pelicula. ")
        actores=load_actores_json()
        lista=[ ]
        while "secundarios"=="":
            print("---De los actores disponibles elija los actores secundarios: ")
            print(actores)
            print("Ingrese de a un personaje: ")
            ingreseid=input("ingrese id del actor: ")
            secundarios=input("Ingrese el nombre de los personajes secundarios")
            rol=input("Asignele un rol: ")
            diccionario2={
                ingreseid:{
                    "Id":ingreseid,
                    "Nombre":secundarios,
                    "Rol":rol
                }
            }
            limpiar_pantalla()
            print("Agregar otro actor")
            ingreso=-1
            ingreso = int(validar_opcion("Si desea Agregar otro actor escriba 1, si no, escriba 0: ",0,1))
            if ingreso==0:
                break
            lista.append(diccionario2)
        generos=load_generos_json()
        listagenero=[ ]
        print("Asigne un genero de los siguientes: ")
        print(generos)
        ngenero=input("Ingrese el nombre del genero: ")
        for genero in generos:
            if genero["Nombre"]==ngenero:
                listagenero.append(genero)
        formatos=load_formatos_json()
        listaformatos=[]
        print("Formatos disponibles: ")
        print(formatos)
        ingreseformato=input("Ingrese el nombre del formato")
        for formato in formatos:
            if formato["Nombre"]==ingreseformato:
                listaformatos.append(formato)
        
        diccionario = { npelicula:{
            "Nombre":npmbrepelicula,
            "Sinopsis":sinompsis,
            "Duracion en min":duracion,
            "Actores":lista,
            "Genero":listagenero,
            "Formato":listaformatos
        }}
        limpiar_pantalla()
        print("Crear otra pelicula")
        ingreso=-1
        ingreso = int(validar_opcion("Si desea crear otra pelicula escriba 1, si no, escriba 0: ",0,1))
        if ingreso==0:
            break
    return diccionario
def editar_pelicula():

    peliculas=load_peliculas_json()
    print("---menu modificacion de peliculas---")
    while(True):
        ingreseid=input("Ingrese el Nombre del pelicula: ")
        encontro=False
        for peli in peliculas:
            if peli["Nombre"]==ingreseid:
                encontro=True
                if encontro==True:
                    print("Pelicula encontrado")
                    print("-------Informacion del Pelicula------")
                    print(peli)
                    print("¿Que opcion desea modificar del Pelicula? ")
                    print("1.Nombre")
                    print("2.Sinopsis")
                    print("3.Duracion en min")
                    print("4.Actores")
                    print("5.Genero")
                    print("6.Formato")
                    print("7.Salir")
                    op=validar_opcion("Opcion: ",1,7)
                    # limpiar_pantalla()
                    if op==1:
                        new_id=input("Ingrese la modificaion: ")
                        peli["Nombre"]=new_id
                        guardar_json(peliculas,"w")
                        return
                    if op==2:
                        new_apellido=input("Ingrese la nueva sinopsis:")
                        peli["Sinopsis"]=new_apellido
                        guardar_json(peliculas,"w")
                        return
                    if op==3:
                        new_nombre=input("Ingrese la mmodificacion de Duracion en min :")
                        peli["Duracion en min"]=new_nombre
                        guardar_json(peliculas,"w")
                        return
                    if op==4:
                        actores=load_actores_json()
                        listaa=[ ]
                        while (True):
                            print("---De los actores disponibles elija los actores: ")
                            print(actores)
                            while(True):
                                ingreseid=input("Ingrese el Nombre del actor que desea modificar: ")
                                encontro=False
                                for actor in actores:
                                    if actor["ingreseid"]==ingreseid:
                                        encontro=True
                                        if encontro==True:    
                                            ingreseid=input("ingrese modificacion de Id: ")
                                            secundarios=input("Ingrese nombre ")
                                            rol=input("Asigrese un rol: ")
                                            diccionario21={
                                                ingreseid:{
                                                    "Id":ingreseid,
                                                    "Nombre":secundarios,
                                                    "Rol":rol
                                                }
                                            }
                                            listaa.append(diccionario21)
                                            guardar_json(peliculas,"w")
                                if encontro==False:
                                    print("Desea corregir: ")
                                    print("la idetificaion no ha sido registrada.")
                                    print("1.Si")
                                    print("2.No")
                                    op=validar_opcion("Opcion: ",1,2)
                                if op==2:
                                    encontro=True
                                if encontro==True:
                                    break
                    if op==5:
                        generos=load_generos_json()
                        listaa1=[ ]
                        while (True):
                            print("---De los generos disponibles elija los generos: ")
                            print(generos)
                            while(True):
                                ingreseid=input("Ingrese el Nombre del actor que desea modificar: ")
                                encontro=False
                                for genero in generos:
                                    if genero["Nombre"]==ingreseid:
                                        encontro=True
                                        if encontro==True:    
                                            ingreseid=input("ingrese modificacion de Id: ")
                                            secundarios=input("Ingrese modificacion del nombre del genero")
                                            
                                            diccionario21={ingreseid:{
                                            "Identificacion" : ingreseid,
                                            "Nombre" : secundarios,
                                            }}
        
                                            listaa1.append(diccionario21)
                                            guardar_json(peliculas,"w")
                                if encontro==False:
                                    print("Desea corregir: ")
                                    print("la idetificaion no ha sido registrada.")
                                    print("1.Si")
                                    print("2.No")
                                    op=validar_opcion("Opcion: ",1,2)
                                if op==2:
                                    encontro=True
                                if encontro==True:
                                    break
                    if op==6: 
                        fomatos=load_formatos_json()
                        listaa1=[ ]
                        nactores=0
                        while (True):
                            print("---De los fomatos disponibles elija los fomatos: ")
                            print(fomatos)
                            while(True):
                                ingreseid=input("Ingrese la identificacion del formato que desea modificar: ")
                                encontro=False
                                for formato in fomatos:
                                    if formato["ingreseid"]==ingreseid:
                                        encontro=True
                                        if encontro==True:    
                                            nactores+=1
                                            id = input("Ingrese identificacion: ")
                                            nombre=input("Ingrese el nombre del formato: ")
                                            diccionario21 = {
                                                nactores:{
                                                "Identificacion" : id,
                                                "Nombre" : nombre,
                                                }}
        
                                            listaa1.append(diccionario21)
                                            guardar_json(peliculas,"w")
                                if encontro==False:
                                    print("Desea corregir: ")
                                    print("la idetificaion no ha sido registrada.")
                                    print("1.Si")
                                    print("2.No")
                                    op=validar_opcion("Opcion: ",1,2)
                                if op==2:
                                    encontro=True
                                if encontro==True:
                                    break
                    if op == 7:
                        print("ADIOS")
                        return
        if encontro==False:
            print("Desea corregir: ")
            print("la idetificaion no ha sido registrada.")
            print("1.Si")
            print("2.No")
            op=validar_opcion("Opcion: ",1,2)
            if op==2:
                encontro=True
        if encontro==True:
            break

def eliminar_pelicula():
    peliculas=load_peliculas_json
    encontro=False
    print("Eliminar Pelicula")
    id=input("Ingrese el nombre del id que desea eliminar: ")
    for actor in peliculas:
        if actor["Nombre"]==id:
           encontro=True
        if encontro==True:
            peliculas.remove(actor)
            guardar_json(peliculas,"w")
            break
        if encontro==False:
            print("Desea corregir: ")
            print("la idetificaion no ha sido registrada.")
            print("1.Si")
            print("2.No")
            op=validar_opcion("Opcion: ",1,2)
            if op==2:
                encontro=True
            if encontro==True:
                break

def eliminar_pelicula():
    encontro=False
    peliculas=load_peliculas_json
    while(True):
        print("Eliminar Actor")
        id=input("Ingrese el nombre del id que desea eliminar: ")
        for pelicula in peliculas:
            if pelicula["Nombre"]==id:
                encontro=True
                if encontro==True:
                    peliculas.remove(pelicula)
                    guardar_json(peliculas,"w")
                    break
        if encontro==False:
            print("Desea corregir: ")
            print("la idetificaion no ha sido registrada.")
            print("1.Si")
            print("2.No")
            op=validar_opcion("Opcion: ",1,2)
            if op==2:
                encontro=True
        if encontro==True:
            break