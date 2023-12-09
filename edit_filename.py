from pathlib import Path
import os
import time


def replace_characters(dir_path_to_rename, deleted_char, added_char):
    if dir_path_to_rename is None:
        dir_path_to_rename = Path(__file__).parent.absolute()
    else:
        dir_path_to_rename = Path(dir_path_to_rename).absolute()
    if deleted_char is None:
        deleted_char = " "
    if added_char is None:
        added_char = "_"
    files = []
    # get all files in folder
    for entry in os.scandir(dir_path_to_rename):
        if entry.is_file():
            files.append(entry)
    for file in files:
        old_name = file.name
        new_name = old_name.replace(deleted_char, added_char)
        os.rename(file.path, str(dir_path_to_rename) + "\\" + new_name)


show_menu = True
while show_menu:
    option = input("Qué deseas hacer: \n a) Sustituir un caracter " +
                   "\n b) Eliminar  un caracter \n s) Salir \n")
    if option.lower() == "a":
        dir_path = input("Indica la ruta de los ficheros a editar: ")
        dropped_char = input("Indica el caracter a sustituir (por defecto, espacios en blanco): ")
        new_char = input("Indica el caracter de sustitución (por defecto \"_\"): ")
        start_time = time.time()
        replace_characters(dir_path, dropped_char, new_char)
        end_time = time.time()
        print(f"Renombrados todos los ficheros en {dir_path}")
        print(f"El proceso ha durado: {(end_time - start_time) * 10 ** 3:.03f}ms")
    elif option.lower() == "b":
        dir_path = input("Indica la ruta de los ficheros a editar: ")
        dropped_char = input("Indica el caracter a eliminar (por defecto, espacios en blanco): ")
        start_time = time.time()
        replace_characters(dir_path, dropped_char, "")
        end_time = time.time()
        print(f"Eliminado el carácter {dropped_char} todos los ficheros en {dir_path}")
        print(f"El proceso ha durado: {(end_time - start_time) * 10 ** 3:.03f}ms")
    elif option.lower() == "s":
        print("Saliendo de la aplicación")
        show_menu = False
    else:
        print("Opciónn errónea")
