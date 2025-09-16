"""
Módulo de la interfaz de usuario para la gestión de contactos.

Este módulo contiene la clase ContactoMenu, que representa un menú en consola
para interactuar con los contactos del sistema. Se encarga de:
- Mostrar las opciones al usuario.
- Recibir inputs y delegar la lógica al ContactoController.
- Ejecutar acciones CRUD sobre contactos a través del controller.

Extensibilidad:
- Para agregar nuevas columnas a Contacto (por ejemplo 'telefono'), se deben:
    1. Añadir los atributos correspondientes en la clase Contacto.
    2. Modificar el ContactoController para aceptar/usar el nuevo campo.
    3. Ajustar la interacción en ContactoMenu (input/output) según sea necesario.
- Para agregar nuevas opciones de menú:
    1. Añadir un nuevo string a self.options.
    2. Agregar un bloque elif en ejecutar() que llame al método del controller correspondiente.
"""

from src.gui.menu import MenuBase
from src.controllers.contacto_controller import ContactoController

class ContactoMenu(MenuBase):
    """
    Clase que representa el menú de gestión de contactos en consola.
    
    Atributos:
        controller (ContactoController): Controlador que maneja la lógica de negocio de contactos.
        options (list): Lista de opciones que se muestran al usuario en el menú.
    
    Flujo de ejecución:
        1. Se instancia ContactoMenu.
        2. Se llama a ejecutar(), que muestra el menú y espera la opción del usuario.
        3. Según la opción seleccionada, se llama al método correspondiente del controller.
        4. Se muestra el resultado al usuario.
    
    Ejemplo de uso:
        >>> menu = ContactoMenu()
        >>> menu.ejecutar()
    """

    def __init__(self):
        """
        Inicializa el menú de contactos y su controlador.

        Extensibilidad:
            - Para añadir nuevas opciones, se puede extender self.options y agregar el correspondiente
              elif en ejecutar(), llamando al método apropiado del controller.
            - Para añadir nuevos campos de contacto, se deben actualizar los inputs y llamadas al controller.
        """
        super().__init__("Gestor de Contactos")
        self.controller = ContactoController()
        self.options = [
            "Crear contacto",
            "Modificar contacto",
            "Eliminar contacto",
            "Listar contactos",
            "Salir"
        ]

    def ejecutar(self):
        """
        Ejecuta el bucle principal del menú de contactos.

        Flujo:
            - Muestra el título y las opciones disponibles.
            - Espera que el usuario ingrese una opción.
            - Según la opción, llama al método correspondiente del ContactoController.
            - Permite salir con Enter o seleccionando la opción 'Salir'.

        Ejemplo de uso:
            >>> menu = ContactoMenu()
            >>> menu.ejecutar()

        Extensibilidad:
            - Para agregar una nueva opción, agregar un string en self.options.
            - Agregar un nuevo bloque elif que maneje la opción y llame a un método del controller.
            - Para añadir más campos de contacto, agregar inputs y pasarlos al controller.
        """
        while True:
            print(f"\n{self.title} - Seleccione una opción: (Enter para salir)")
            self.mostrar_opciones(self.options)
            opc = self.user_input("Ingrese una opción: ")

            if opc == "":
                break
            elif opc == "1":
                nombre = self.user_input("Nombre: ")
                email = self.user_input("Email: ")
                contacto = self.controller.crear_contacto(nombre, email)
                print("Contacto creado:", contacto)
            elif opc == "2":
                id = int(self.user_input("ID a modificar: "))
                nombre = self.user_input("Nuevo nombre: ")
                email = self.user_input("Nuevo email: ")
                c = self.controller.modificar_contacto(id, nombre, email)
                print("Contacto actualizado:", c if c else "No encontrado")
            elif opc == "3":
                id = int(self.user_input("ID a eliminar: "))
                self.controller.eliminar_contacto(id)
                print("Contacto eliminado")
            elif opc == "4":
                contactos = self.controller.listar_contactos()
                for idx, c in enumerate(contactos, start=1):
                    print(f"{idx}. {c}")
            elif opc == "5":
                print("Regresando al menú principal.")
                break
            else:
                print("Opción inválida.")
