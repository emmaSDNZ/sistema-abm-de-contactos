"""
Módulo DAO para la entidad Contacto.

Este módulo define la clase ContactoDAO, que se encarga de manejar
todas las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre
la tabla 'contactos' en la base de datos.

Responsabilidades:
- Insertar nuevos contactos.
- Modificar contactos existentes.
- Eliminar contactos por ID.
- Listar todos los contactos.
- Obtener un contacto por su ID.

Extensibilidad:
- Para agregar un nuevo campo a la tabla 'contactos' (por ejemplo 'direccion'):
    1. Agregar el campo en la base de datos mediante migración o ALTER TABLE.
    2. Agregar el atributo correspondiente en la clase Contacto en models/contacto.py.
    3. Incluir el nuevo campo en las consultas INSERT, UPDATE y SELECT de este DAO.
- Para agregar un nuevo método (por ejemplo, buscar por email):
    1. Crear un nuevo método dentro de ContactoDAO, usando self.execute_query().
    2. Retornar instancias de Contacto según corresponda.
- La estructura permite que varios desarrolladores trabajen simultáneamente sin pisarse:
    - Cada DAO maneja una sola entidad.
    - Se recomienda crear métodos nuevos solo dentro del DAO correspondiente.
"""

from src.core.base_dao import DAO
from src.models.contacto import Contacto

class ContactoDAO(DAO):
    """
    DAO para la entidad Contacto.

    Atributos:
        table_name (str): Nombre de la tabla en la base de datos.
        columns (list): Lista de columnas de la tabla.

    Relación con otras clases:
        - Usa la clase Contacto para instanciar objetos desde la base de datos.
        - Hereda de DAO para acceder a métodos genéricos de ejecución de queries.
    """

    def __init__(self):
        """
        Inicializa el DAO de contactos.

        Consideraciones:
            - Se establece table_name como 'contactos'.
            - Se define la lista de columnas actuales de la tabla.

        Ejemplo de uso:
            >>> dao = ContactoDAO()
        """
        super().__init__()
        self.table_name = "contactos"
        self.columns = ["id","nombre","telefono","email","created_at","updated_at"]

    def save(self, contacto: Contacto):
        """
        Inserta un nuevo contacto en la base de datos.

        Args:
            contacto (Contacto): Instancia de Contacto a guardar.

        Flujo:
            1. Construye el query INSERT.
            2. Ejecuta el query usando execute_non_query() heredado de DAO.

        Ejemplo de uso:
            >>> contacto = Contacto(nombre="Juan", email="juan@mail.com")
            >>> dao.save(contacto)
            >>> print("Contacto creado")

        Extensibilidad:
            - Para agregar un campo adicional, incluirlo en la consulta INSERT
              y pasar el valor correspondiente del objeto Contacto.
        """
        query = "INSERT INTO contactos (nombre, telefono, email) VALUES (?, ?, ?)"
        self.execute_non_query(query, (contacto._nombre, contacto._telefono, contacto._email))

    def update_contact(self, contacto: Contacto):
        """
        Actualiza los datos de un contacto existente en la base de datos.

        Args:
            contacto (Contacto): Instancia de Contacto con ID válido y campos a actualizar.

        Flujo:
            1. Construye el query UPDATE.
            2. Ejecuta el query usando execute_non_query() heredado de DAO.

        Ejemplo de uso:
            >>> contacto = dao.get_by_id(1)
            >>> contacto.set_email("nuevo@mail.com")
            >>> dao.update_contact(contacto)
            >>> print("Contacto actualizado")

        Extensibilidad:
            - Para agregar un campo nuevo, añadirlo en la cláusula SET
              y pasar el valor correspondiente.
        """
        query = "UPDATE contactos SET nombre=?, telefono=?, email=? WHERE id=?"
        self.execute_non_query(query, (contacto._nombre, contacto._telefono, contacto._email, contacto._id))

    def delete_contact(self, contacto_id: int):
        """
        Elimina un contacto de la base de datos por su ID.

        Args:
            contacto_id (int): ID del contacto a eliminar.

        Flujo:
            1. Construye el query DELETE.
            2. Ejecuta el query usando execute_non_query() heredado de DAO.

        Ejemplo de uso:
            >>> dao.delete_contact(1)
            >>> print("Contacto eliminado")

        Extensibilidad:
            - Para validaciones adicionales antes de borrar, agregar lógica previa
              a la llamada execute_non_query().
        """
        query = "DELETE FROM contactos WHERE id=?"
        self.execute_non_query(query, (contacto_id,))

    def list_all(self):
        """
        Lista todos los contactos de la base de datos.

        Returns:
            list: Lista de instancias Contacto.

        Flujo:
            1. Construye el query SELECT.
            2. Ejecuta el query usando execute_query() heredado de DAO.
            3. Mapea cada fila a un objeto Contacto.

        Ejemplo de uso:
            >>> contactos = dao.list_all()
            >>> for c in contactos:
            >>>     print(c)

        Extensibilidad:
            - Para agregar nuevas columnas, asegurarse de mapearlas en la creación
              de cada objeto Contacto.
            - Para filtros personalizados, crear un nuevo método que use SELECT con WHERE.
        """
        query = "SELECT * FROM contactos"
        rows = self.execute_query(query)
        return [Contacto(id=row['id'], nombre=row['nombre'], telefono=row['telefono'], email=row['email']) for row in rows]

    def get_by_id(self, contacto_id: int):
        """
        Obtiene un contacto de la base de datos por su ID.

        Args:
            contacto_id (int): ID del contacto a buscar.

        Returns:
            Contacto: Instancia de Contacto si se encuentra, None si no existe.

        Flujo:
            1. Construye el query SELECT WHERE id=?.
            2. Ejecuta el query usando execute_query().
            3. Retorna un objeto Contacto mapeado o None.

        Ejemplo de uso:
            >>> contacto = dao.get_by_id(1)
            >>> if contacto:
            >>>     print(contacto)
            >>> else:
            >>>     print("No encontrado")

        Extensibilidad:
            - Para buscar por otros campos (email, nombre), crear un método
              similar con cláusula WHERE específica.
            - Para agregar columnas adicionales, mapearlas en el constructor de Contacto.
        """
        query = "SELECT * FROM contactos WHERE id=?"
        rows = self.execute_query(query, (contacto_id,))
        if rows:
            row = rows[0]
            return Contacto(id=row['id'], nombre=row['nombre'], telefono=row['telefono'], email=row['email'])
        return None
