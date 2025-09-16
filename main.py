"""
Módulo principal del sistema de gestión de contactos.

Propósito:
Este módulo se encarga de inicializar la base de datos y ejecutar la interfaz de usuario
del Gestor de Contactos (ContactoMenu). Representa el punto de entrada del programa.

Flujo principal:
1. Se llama a init_db() para asegurar que las tablas existen.
2. Se instancia ContactoMenu, que es el menú de gestión de contactos.
3. Se ejecuta el método ejecutar() del menú, que gestiona la interacción con el usuario.

Extensibilidad:
- Para agregar nuevas opciones al menú:
    1. Modificar la lista self.options dentro de ContactoMenu.
    2. Implementar un nuevo método en ContactoMenu para manejar la funcionalidad.
    3. Agregar un bloque if/elif en el método ejecutar() que llame a ese nuevo método.
- Para agregar campos adicionales a Contacto:
    1. Modificar la clase Contacto en src/models/contacto.py agregando nuevos atributos y métodos get/set.
    2. Modificar ContactoDAO para incluir los nuevos campos en los métodos save, update_contact y list_all.
    3. Ajustar ContactoMenu para solicitar los nuevos datos al usuario y mostrarlos en listados.
- Para agregar nuevas funcionalidades globales:
    1. Crear un nuevo archivo en src/services o src/controllers según corresponda.
    2. Llamar a la nueva funcionalidad desde ContactoMenu o desde main.py según el flujo.

Ejemplo de uso:
    >>> from main import init_db, ContactoMenu
    >>> init_db()
    >>> menu = ContactoMenu()
    >>> menu.ejecutar()
"""

from src.config.db import init_db
from src.gui.contacto_menu import ContactoMenu

# Inicialización de la base de datos
init_db()

if __name__ == "__main__":
    # Instancia del menú principal de contactos
    main_menu = ContactoMenu()
    # Inicio del loop de interacción con el usuario
    main_menu.ejecutar()
