from os.path import dirname
import os


class ReadFolder (object):
    def __init__(self, name_folder):
        self.name_folder = name_folder

    @staticmethod
    # Para salir del directorio actual a uno más alto de jerarquia
    def root(root):
        new_root = dirname(root)
        return new_root

    @staticmethod
    # Para listar el contenido de un directorio actual dado
    def index_content_folder(path):
        data = []
        content = os.listdir(path)
        for i in content:
            evaluated = i.__contains__('.') or i.__contains__('__pycache__')
            if not evaluated:
                data.append(i)
        return data

    # Recurrencia para salir hasta un directorio más alto en jararquia dado
    def exit_folder(self, path, name_folder):
        try:
            data = self.index_content_folder(path)
            if data:
                if data.__contains__(name_folder):
                    return path
                else:
                    return self.exit_folder(self.root(path), name_folder)
            else:
                return self.exit_folder(self.root(path), name_folder)
        except NotADirectoryError:
            return self.exit_folder(self.root(path), name_folder)

    # Retorno de ruta raiz de un proyecto dato
    def root_project(self):
        root_file = os.path.abspath(os.curdir)
        path_root = self.exit_folder(root_file, self.name_folder)
        return path_root

    # Buscar un archivo dado un directorio raiz
    def search_file(self, path: str, search: str):
        for f in os.listdir(path):
            item = os.path.join(path, f)
            if os.path.isfile(item) and f == search:
                break
            elif os.path.isdir(item):
                item = self.search_file(item, search)
                if item:
                    break
        else:
            item = None
        return item


class HandlerFiles(ReadFolder):
    def __init__(self, name_file, name_folder):
        self.name_file = name_file
        ReadFolder.__init__(self, name_folder)

    # Parseo de manejo de rutas para mostrar templates en el sitio web
    @staticmethod
    def separator(path):
        separator = "pages"
        path_separate = path.split(separator)
        return path_separate[1]

    # Reemplar carácter de la ruta '\' por '/' reconocible en el sistema de rutas de Python Flask
    @staticmethod
    def replace_path(path):
        replace_character = u"\u005C"  # Character in Unicode - ASCII '\'
        new_path = path.replace(replace_character, "/")
        return new_path

    # Retorno de ruta absoluta de un archivo para visualización del sitio web
    def route_absolute(self):
        path_root = self.root_project()
        path_absolute = self.search_file(path_root, self.name_file)
        return path_absolute

    # Retorno de ruta relativa de un archivo para visualización del sitio web
    def route_relative(self):
        path_relatives = self.separator(self.route_absolute())
        return path_relatives

