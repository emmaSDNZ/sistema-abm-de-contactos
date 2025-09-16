"""
Módulo de control para la gestión de contactos.

Este módulo define la clase ContactoController, que actúa como intermediario
entre la capa de presentación (GUI o API) y la capa de servicios (logica de negocio).

Responsabilidades principales:
- Recibir solicitudes desde la interfaz de usuario.
- Delegar la ejecución de la lógica de negocio a ContactoService.
- Retornar resultados o estados de las operaciones hacia la capa superior.

Extensibilidad:
- Nuevos métodos pueden agregarse en ContactoService y ser expuestos aquí.
- Nuevos campos en Contacto se manejan agregando parámetros opcionales en los métodos
  y actualizando el servicio para procesarlos.
- Siempre se recomienda mantener el Controller como capa fina, delegando la lógica
  al Service para no mezclar responsabilidades.
"""

from src.services.contacto_services import ContactoService

class ContactoController:
    """
    Controlador de contactos.

    Atributos:
        service (ContactoService): Instancia del servicio que maneja la lógica de contactos.

    Flujo de uso:
        1. La GUI solicita la creación, modificación, listado o eliminación de un contacto.
        2. ContactoController recibe la solicitud y la delega al ContactoService.
        3. ContactoService realiza la operación sobre la base de datos usando ContactoDAO.
        4. Los resultados se retornan a la GUI a través del Controller.
    """

    def __init__(self):
        """
        Inicializa el controlador creando una instancia de ContactoService.

        Ejemplo de uso:
            >>> controller = ContactoController()
        """
        self.service = ContactoService()

    def crear_contacto(self, nombre, email, telefono=""):
        """
        Crea un nuevo contacto.

        Args:
            nombre (str): Nombre del contacto.
            email (str): Email del contacto.
            telefono (str, opcional): Teléfono del contacto. Por defecto está vacío.

        Returns:
            Contacto: Instancia del contacto creado.

        Ejemplo de uso:
            >>> contacto = controller.crear_contacto("Juan", "juan@mail.com", "123456789")
            >>> print(contacto)
            Nombre: Juan, Email: juan@mail.com

        Extensibilidad:
            - Para agregar un nuevo campo, por ejemplo 'direccion':
                1. Agregar el parámetro opcional direccion en este método.
                2. Actualizar ContactoService.crear_contacto para aceptar y guardar direccion.
                3. Actualizar la clase Contacto y ContactoDAO para manejar el nuevo campo.
        """
        return self.service.crear_contacto(nombre, email, telefono)

    def modificar_contacto(self, id, nombre=None, email=None, telefono=None):
        """
        Modifica un contacto existente.

        Args:
            id (int): ID del contacto a modificar.
            nombre (str, opcional): Nuevo nombre. Si es None, se mantiene el anterior.
            email (str, opcional): Nuevo email. Si es None, se mantiene el anterior.
            telefono (str, opcional): Nuevo teléfono. Si es None, se mantiene el anterior.

        Returns:
            Contacto: Instancia del contacto actualizado, o None si no se encontró.

        Ejemplo de uso:
            >>> contacto = controller.modificar_contacto(1, email="nuevo@mail.com")
            >>> print(contacto)
            Nombre: Juan, Email: nuevo@mail.com

        Extensibilidad:
            - Para agregar un nuevo campo:
                1. Agregar un parámetro opcional al método.
                2. Delegar el manejo del campo al ContactoService.
                3. Asegurarse de actualizar ContactoDAO y Contacto para persistir el nuevo campo.
        """
        return self.service.modificar_contacto(id, nombre, email, telefono)

    def listar_contactos(self):
        """
        Retorna todos los contactos existentes.

        Returns:
            list: Lista de instancias Contacto.

        Ejemplo de uso:
            >>> contactos = controller.listar_contactos()
            >>> for c in contactos:
            >>>     print(c)

        Extensibilidad:
            - Para filtrar contactos por un nuevo campo:
                1. Agregar un parámetro opcional de filtro aquí.
                2. Pasarlo al ContactoService y actualizar el método listar_contactos.
        """
        return self.service.listar_contactos()

    def eliminar_contacto(self, id):
        """
        Elimina un contacto de la base de datos.

        Args:
            id (int): ID del contacto a eliminar.

        Returns:
            bool: True si se eliminó correctamente, False si no se encontró.

        Ejemplo de uso:
            >>> resultado = controller.eliminar_contacto(1)
            >>> print(resultado)
            True

        Extensibilidad:
            - Para operaciones lógicas adicionales antes de eliminar, agregar hooks
              en ContactoService y llamar aquí desde el Controller.
        """
        return self.service.eliminar_contacto(id)
