"""
Módulo de definición de menús del sistema.

Este módulo contiene clases base y específicas para los menús de la aplicación.
Permite manejar la interacción con el usuario desde la consola, mostrando opciones,
recibiendo inputs y ejecutando acciones asociadas a cada opción.

Flujo principal:
1. Se instancia un menú (ejemplo: UsuarioMenu).
2. Se llama al método ejecutar() para iniciar la interacción.
3. El usuario selecciona opciones y se ejecutan métodos correspondientes.
4. Se repite hasta que el usuario elige salir.
"""

class MenuBase:
    """
    Clase base para todos los menús de la aplicación.

    Propósito:
        Proveer funcionalidad común para mostrar opciones en consola
        y recibir inputs del usuario.

    Atributos:
        title (str): Título del menú que se muestra al usuario.

    Métodos:
        user_input(prompt): Recibe la entrada del usuario con un mensaje.
        mostrar_opciones(options): Muestra en consola una lista de opciones numeradas.

    Extensibilidad:
        - Para crear un nuevo menú, heredar de MenuBase.
        - Se puede agregar un método adicional para cada nueva opción.
        - No se debe modificar directamente esta clase para extender menús.
    """

    def __init__(self, title):
        """
        Inicializa el menú con un título.

        Args:
            title (str): Título del menú.
        """
        self.title = title

    def user_input(self, prompt):
        """
        Solicita una entrada al usuario.

        Args:
            prompt (str): Mensaje que se muestra al usuario.

        Returns:
            str: Texto ingresado por el usuario.

        Ejemplo de uso:
            >>> menu = MenuBase("Demo")
            >>> nombre = menu.user_input("Ingrese su nombre: ")
        """
        return input(prompt).strip()

    def mostrar_opciones(self, options):
        """
        Muestra una lista numerada de opciones en la consola.

        Args:
            options (list of str): Lista de opciones a mostrar.

        Ejemplo de uso:
            >>> menu = MenuBase("Demo")
            >>> menu.mostrar_opciones(["Opción 1", "Opción 2"])
            1. Opción 1
            2. Opción 2
        """
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")
        print("")


class UsuarioMenu(MenuBase):
    """
    Menú específico para gestión de usuarios.

    Propósito:
        Permite al usuario registrar cuentas, iniciar sesión o ingresar como invitado.
        Hereda funcionalidades comunes de MenuBase.

    Atributos:
        options (list of str): Lista de opciones específicas del menú de usuario.

    Métodos:
        ejecutar(): Inicia el bucle del menú y ejecuta las acciones correspondientes.
        registrar_usuario(): Función simulada para registrar usuarios.
        iniciar_sesion(): Función simulada para iniciar sesión.

    Extensibilidad:
        - Para agregar nuevas opciones:
            1. Agregar el texto de la opción a la lista `self.options`.
            2. Crear un método en la clase que implemente la acción de la opción.
            3. Agregar un bloque `elif` en ejecutar() para la nueva opción.
        - Para agregar campos adicionales a los usuarios (ej: email, teléfono):
            1. Modificar la clase de modelo Usuario correspondiente.
            2. Adaptar los métodos registrar_usuario() e iniciar_sesion() para manejar los nuevos campos.
            3. No es necesario modificar MenuBase.
    """

    def __init__(self):
        """
        Inicializa el menú de usuario con su título y opciones predeterminadas.
        """
        super().__init__("Menú Usuario")
        self.options = ["Registrar usuario", "Iniciar sesión", "Ingresar como invitado", "Salir"]

    def ejecutar(self):
        """
        Ejecuta el bucle principal del menú, mostrando opciones y recibiendo inputs.

        Flujo:
            1. Muestra el título y las opciones.
            2. Solicita al usuario que ingrese una opción.
            3. Llama al método correspondiente según la opción seleccionada.
            4. Permite salir al ingresar "" o seleccionar "Salir".

        Ejemplo de uso:
            >>> menu = UsuarioMenu()
            >>> menu.ejecutar()
            Menú Usuario - Seleccione una opción:
            1. Registrar usuario
            2. Iniciar sesión
            3. Ingresar como invitado
            4. Salir
        """
        while True:
            print(f"\n{self.title} - Seleccione una opción:")
            self.mostrar_opciones(self.options)
            opc = self.user_input("Ingrese una opción: ")
            
            if opc == "":
                print("Adiós.")
                break
            elif opc == "1":
                self.registrar_usuario()
            elif opc == "2":
                self.iniciar_sesion()
            elif opc == "3":
                print("Ingresando como invitado...")
                break
            elif opc == "4":
                print("Adiós.")
                exit()
            else:
                print("Opción inválida.")

    def registrar_usuario(self):
        """
        Simula el registro de un usuario.

        Consideraciones:
            - Actualmente no guarda en base de datos, sirve como plantilla.
            - Para funcionalidad real, integrar con un DAO y modelo Usuario.

        Ejemplo de uso:
            >>> menu = UsuarioMenu()
            >>> menu.registrar_usuario()
            Función registrar_usuario() - Aquí iría la lógica real
        """
        print("Función registrar_usuario() - Aquí iría la lógica real")

    def iniciar_sesion(self):
        """
        Simula la acción de iniciar sesión de un usuario.

        Consideraciones:
            - Actualmente solo imprime un mensaje.
            - Para funcionalidad real, debe verificar credenciales contra la base de datos.

        Ejemplo de uso:
            >>> menu = UsuarioMenu()
            >>> menu.iniciar_sesion()
            Función iniciar_sesion() - Aquí iría la lógica real
        """
        print("Función iniciar_sesion() - Aquí iría la lógica real")
