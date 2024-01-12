import json
import os
from commons.utils import *
from commons.menus import *

def guardar_json(lista,modo):# si pasa "w" sobrescribe todo, si pasa "a" añade en lo que ya esta
    try:
      with open(os.path.join("data", "actores.json"), modo) as archivo_json:
        json.dump(lista, archivo_json, indent=2)
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya generos guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def crear_actores ():
    print("-----MENU CREAR ACTORES------")
    diccionaario ={}
    nactores=0
    while True:
        nactores+=1
        id = input("Ingrese identificacion: ")
        nombre=input("Ingrese el nombre del Actor: ")
        diccionaario = {
            nactores:{
            "Identificacion" : id,
            "Nombre" : nombre,
            }}
        limpiar_pantalla()
        print("Crear otro Actor")
        ingreso=-1
        ingreso = int(validar_opcion("Si desea crear otro Actor escriba 1, si no, escriba 0: ",0,1))
        if ingreso==0:
            break
    return diccionaario

def eliminar_actor():
    actoters=load_actores_json()
    print("-----Menu Eliminar o Modificar Actores-----")
    print("Actores disponibles: ")
    print(actoters)
    print("Elija:")
    print("1. Modificar Actor")
    print("2. Eliminar Actor")
    op=validar_opcion("Opcion: ",1,2)
    while(True): 
        if (op==1):
            encontro=False
            print("Modificar Actor")
            id=input("Ingrese el nombre del id que desea modificar: ")
            for actor in actoters:
                if actor["Nombre"]==id:
                    encontro=True
                    if encontro==True:
                        print("Actor encontrado")
                        print("Seleccione la opcion que desea modificar:")
                        print("1.Identificacion")
                        print("2.Nombre")
                        print("3.Salir")
                        op=validar_opcion("Opcion: ",1,3)
                        if op==1:
                            newid=input("Ingrese el nuevo ID: ")
                            actor["Identificacion"]=newid
                            guardar_json(actoters,"w")
                        elif op==2:
                            newname=input("Ingrese la modificacion del nombre: ")
                            actor["Nombre"]=newname
                            guardar_json(actoters,"w")
                        elif op==3:
                            print("ADIOS")
                            break
            if encontro==False:
                print("Desea corregir: ")
                print("la idetificaion no ha sido registrada.")
                print("1.Si")
                print("2.No")
                p=validar_opcion("Opcion: ",1,2)
                if op==2:
                    encontro=True
            if encontro==True:
                break
        elif(op==2):
            encontro=False
            print("Eliminar Actor")
            id=input("Ingrese el nombre del id que desea eliminar: ")
            for actor in actoters:
                if actor["Nombre"]==id:
                    encontro=True
                    if encontro==True:
                        actoters.remove(actor)
                        guardar_json(actoters,"w")
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
        