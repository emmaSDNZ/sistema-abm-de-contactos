"""
Módulo de servicios de Contactos.

Este módulo actúa como capa intermedia entre la interfaz de usuario (GUI o Controllers)
y la capa de acceso a datos (DAO). Contiene la lógica de negocio para la gestión de contactos,
como crear, modificar, listar y eliminar.

Responsabilidades:
- Validar y transformar datos antes de enviarlos al DAO.
- Centralizar la lógica de negocio para que los menús o controladores no manejen directamente la base de datos.
- Facilitar extensibilidad agregando campos, métodos o reglas de negocio sin tocar la GUI ni el DAO.

Flujo principal:
1. Un menú o controlador llama a un método de ContactoService.
2. El servicio construye o actualiza un objeto Contacto.
3. El servicio invoca al ContactoDAO correspondiente.
4. El resultado se devuelve al menú o controlador.
"""

from src.models.contacto import Contacto
from src.dao.contacto_dao import ContactoDAO

class ContactoService:
    """
    Clase que maneja la lógica de negocio de los contactos.

    Atributos:
        dao (ContactoDAO): instancia de la capa de acceso a datos para realizar operaciones CRUD.

    Extensibilidad:
        - Para agregar un nuevo campo (por ejemplo 'direccion'):
            1. Agregar el atributo en la clase Contacto (models/contacto.py).
            2. Incluirlo en las columnas de ContactoDAO.
            3. Modificar los métodos de este servicio para aceptar y propagar el nuevo campo.
            4. Actualizar métodos de la GUI o controladores para capturar el nuevo valor.
        - Para agregar nuevas funciones de negocio (ej: buscar por email):
            1. Crear un nuevo método en ContactoService.
            2. Usar DAO para obtener la información.
            3. Devolver resultados listos para la GUI o controlador.
    """

    def __init__(self):
        """
        Inicializa el servicio creando una instancia del DAO.
        
        Ejemplo de uso:
            >>> service = ContactoService()
        """
        self.dao = ContactoDAO()

    def crear_contacto(self, nombre, email, telefono=""):
        """
        Crea un nuevo contacto y lo guarda en la base de datos.

        Args:
            nombre (str): Nombre del contacto.
            email (str): Email del contacto.
            telefono (str, opcional): Teléfono del contacto. Por defecto está vacío.

        Returns:
            Contacto: Objeto Contacto creado y persistido en la base de datos.

        Extensibilidad:
            - Para agregar un nuevo campo, simplemente agregarlo como argumento
              y pasarlo al constructor de Contacto.
            - Ejemplo:
                >>> service.crear_contacto("Juan", "juan@mail.com", "123456", direccion="Calle 1")
        """
        c = Contacto(nombre=nombre, email=email, telefono=telefono)
        self.dao.save(c)
        return c

    def modificar_contacto(self, id, nombre=None, email=None, telefono=None):
        """
        Modifica un contacto existente. Solo actualiza los campos proporcionados.

        Args:
            id (int): ID del contacto a modificar.
            nombre (str, opcional): Nuevo nombre.
            email (str, opcional): Nuevo email.
            telefono (str, opcional): Nuevo teléfono.

        Returns:
            Contacto o None: El contacto actualizado o None si no se encontró el ID.

        Extensibilidad:
            - Para agregar nuevos campos, agregar argumentos opcionales y actualizar
              el objeto Contacto antes de llamar al DAO.update_contact().
            - Ejemplo:
                >>> service.modificar_contacto(1, nombre="Nuevo Nombre", direccion="Calle X")
        """
        c = self.dao.get_by_id(id)
        if not c: 
            return None
        c._nombre = nombre or c._nombre
        c._email = email or c._email
        c._telefono = telefono or c._telefono
        self.dao.update_contact(c)
        return c

    def listar_contactos(self):
        """
        Devuelve una lista de todos los contactos registrados.

        Returns:
            list: Lista de objetos Contacto.

        Ejemplo de uso:
            >>> contactos = service.listar_contactos()
            >>> for c in contactos:
            >>>     print(c)

        Extensibilidad:
            - Para filtrar o paginar, crear métodos adicionales que llamen a DAO con criterios específicos.
            - Ejemplo:
                >>> service.listar_contactos_por_email("gmail.com")
        """
        return self.dao.list_all()

    def eliminar_contacto(self, id):
        """
        Elimina un contacto de la base de datos por su ID.

        Args:
            id (int): ID del contacto a eliminar.

        Returns:
            None

        Ejemplo de uso:
            >>> service.eliminar_contacto(3)

        Extensibilidad:
            - Para marcar como inactivo en lugar de eliminar, cambiar la lógica
              e incluir un campo 'activo' en Contacto y DAO.
        """
        self.dao.delete_contact(id)
