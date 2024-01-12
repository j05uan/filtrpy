
import os
import json
def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')    

def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")
def guardar_json_generos(lista):
    try:
      with open(os.path.join("data", "generos.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def load_generos_json():
    try:
      with open(os.path.join("data", "generos.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")

def guardar_json(lista,modo):# si pasa "w" sobrescribe todo, si pasa "a" añade en lo que ya esta
    try:
      with open(os.path.join("data", "generos.json"), modo) as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def guardar_json_actores(lista):
    try:
      with open(os.path.join("data", "actores.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def load_actores_json():
    try:
      with open(os.path.join("data", "actores.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def guardar_json_formatos(lista):
    try:
      with open(os.path.join("data", "formatos.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def load_formatos_json():
    try:
      with open(os.path.join("data", "formatos.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")

def guardar_json_peliculas(lista):
    try:
      with open(os.path.join("data", "peliculas.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def load_peliculas_json():
    try:
      with open(os.path.join("data", "peliculas.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
##Listar
def mostrar_lista_con_diccionarios(lista):
    for datos in lista:
        print(datos)