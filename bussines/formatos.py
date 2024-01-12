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

def crear_formatos():
    print("-----MENU CREAR FORMATOS------")
    diccionaario ={}
    nactores=0
    while True:
        nactores+=1
        id = input("Ingrese identificacion: ")
        nombre=input("Ingrese el nombre del formato: ")
        diccionaario = {
            nactores:{
            "Identificacion" : id,
            "Nombre" : nombre,
            }}
        limpiar_pantalla()
        print("Crear otro formato")
        ingreso=-1
        ingreso = int(validar_opcion("Si desea crear otro Actor escriba 1, si no, escriba 0: ",0,1))
        if ingreso==0:
            break
    return diccionaario