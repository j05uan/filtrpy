import json
import os
from commons.utils import *
from commons.menus import *

def guardar_json(lista,modo):# si pasa "w" sobrescribe todo, si pasa "a" añade en lo que ya esta
    try:
      with open(os.path.join("data", "generos.json"), modo) as archivo_json:
        json.dump(lista, archivo_json, indent=2)
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya generos guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def crear_genero ():
    print("-----MENU CREAR GENERO------")
    diccionaario ={}
    while True:
        id = input("Ingrese identificacion: ")
        nombre=input("Ingrese el nombre del genero: ")
        diccionaario = {
            id:{
            "Identificacion" : id,
            "Nombre" : nombre,
            }}
        limpiar_pantalla()
        print("Crear otro genero")
        ingreso=-1
        ingreso = int(validar_opcion("Si desea crear otro genero escriba 1, si no, escriba 0: ",0,1))
        if ingreso==0:
            break
    return diccionaario


def modificacion_genero():
    generos=load_generos_json()
    print("---menu modificacion de genero---")
    while(True):
        ingreseid=input("Ingrese la identificacion del genero: ")
        encontro=False
        for genero in generos:
            if genero["Identificacion"]==ingreseid:
                encontro=True
                print("genero encontrado")
                print("-------Informacion del genero------")
                print(genero)
                print("¿Que opcion desea modificar del genero? ")
                print( "1.id")
                print("3.Nombre")
                print("4.Salir")
                op=validar_opcion("Opcion: ",1,4)
                # limpiar_pantalla()
                if op==1:
                    new_id=input("Ingrese la modificaion: ")
                    genero["Identificacion"]=new_id
                    guardar_json(generos,"w")
                    return
                if op==2:
                    new_nombre=input("Ingrese el nuevo nombre:")
                    genero["Nombre"]=new_nombre
                    guardar_json(generos,"w")
                    return
                if op == 9:
                    print("ADIOS")
                    return
        if encontro==False:
            print("Desea corregir: ")
            print("Genero no encontrado")
            print("1.Si")
            print("2.No")
            op=validar_opcion("Opcion: ",1,2)
            if op==2:
                encontro=True
        if encontro==True:
            break