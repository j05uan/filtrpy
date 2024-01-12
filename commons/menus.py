## menus
import os
from commons.utils import*
#def limpiar_pantalla():
#    os.system('clear' if os.name == 'posix' else 'cls')  

def menu_principal():
    limpiar_pantalla()
    print("-----------SISTEMA GESTOR DE MATRICULAS BLOCKBUSTER-----------")
    print("1. Administrador de generos")
    print("2. Administrador de Actores")
    print("3. Administrador de Formatos")
    print("4. Gestor de Informes")
    print("5. Gestor Peliculas")
    print("6. Salir")      
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_generos():
    limpiar_pantalla()
    print("---------GESTOR DE GENEROS-----------")
    print("1. Crear Genero")
    print("2. Crear Genero")
    print("3. Listar Genero")
    print("4. Salir")      
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_actores():
    limpiar_pantalla()
    print("---------GESTOR DE ACTORES-----------")
    print("1. Crear Actor")
    print("2. Listar Actor")
    print("3. Eliminar o modificar Actor")
    print("4. Salir")      
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_FORMATOS():
    limpiar_pantalla()
    print("---------GESTOR DE FORMATOS-----------")
    print("1. Crear Formatos")
    print("2. Listar Formatos")
    print("3. Salir")      
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_gestor_peliculas():
    limpiar_pantalla()
    print("-----------} GESTOR DE PELICULAS-----------")
    print("1. Agregar Pelicula")
    print("2. Listar Peliculas")
    print("3. Buscar Pelicula")
    print("4. Editar Pelicula")
    print("5. Eliminar Pelicula")
    print("6. Salir")      
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_gestor_informes():
    limpiar_pantalla()
    print("---------GESTOR DE INFORMES-----------")
    print("1. Listar las peliculas de un genero especifico")
    print("2. Lisar las peliculas en donde aparezca un actor especifico")
    print("3. Mostrar pelicula ")
    print("4. Salir")      
    op=validar_opcion("Opcion: ",1,4)
    return op



