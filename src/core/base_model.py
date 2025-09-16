"""
Módulo base para modelos de la aplicación.

Este módulo define la clase BaseModel, que actúa como clase raíz para todas las
entidades del sistema (por ejemplo, Contacto, Usuario, etc.). Su función principal
es proporcionar métodos genéricos de persistencia (CRUD) utilizando el DAO genérico.

Responsabilidades:
- Definir un identificador único (_id) para todas las entidades.
- Implementar métodos genéricos: save, update, delete, find_by_id, all.
- Servir como clase base para extender entidades específicas.

Extensibilidad:
- Para agregar un nuevo campo a una entidad:
    1. Definir el atributo en la subclase, prefijado con `_` (por ejemplo, _telefono).
    2. Agregar el nombre de la columna a la lista `COLUMNS` de la subclase.
    3. Asegurarse de que la base de datos tenga la columna correspondiente.
- Para agregar un método específico de negocio:
    - Definirlo directamente en la subclase, sin modificar BaseModel.
- Este diseño permite que múltiples programadores trabajen en distintas entidades sin pisarse.
"""

from datetime import datetime
from src.core.base_dao import DAO

class BaseModel:
    """
    BaseModel – Clase raíz de todas las entidades de la aplicación.

    Atributos:
        _id (int): Identificador único de la entidad.
        TABLE_NAME (str): Nombre de la tabla asociada a la entidad (debe ser definido en la subclase).
        COLUMNS (list): Lista de nombres de columnas que se corresponden con los atributos de la clase.

    Métodos principales:
        save(): Inserta un registro nuevo en la base de datos.
        update(): Actualiza un registro existente.
        delete(): Elimina el registro de la base de datos.
        find_by_id(id): Recupera un objeto según su id.
        all(): Recupera todos los objetos de la tabla.
        get_id(): Devuelve el id del objeto.

    Ejemplo de uso:
        >>> class Usuario(BaseModel):
        ...     TABLE_NAME = "usuarios"
        ...     COLUMNS = ["username", "password", "rol"]
        ...     def __init__(self, username, password, rol, id=None):
        ...         super().__init__(id)
        ...         self._username = username
        ...         self._password = password
        ...         self._rol = rol
        >>> u = Usuario("ana", "1234", "admin")
        >>> u.save()
        >>> u._id
        1
        >>> u2 = Usuario.find_by_id(1)
        >>> u2._username
        'ana'
    """

    _id: int
    TABLE_NAME = None
    COLUMNS = []

    def __init__(self, id: int = None):
        """
        Inicializa la entidad con un identificador opcional.

        Args:
            id (int): Identificador único del registro (por defecto None, para nuevos registros).

        Consideraciones:
            - Para nuevos registros, _id debe ser None y se asignará al insertar.
            - Subclases deben definir TABLE_NAME y COLUMNS.
        """
        self._id = id

    def save(self):
        """
        Inserta un nuevo registro en la base de datos.

        Flujo:
            1. Obtiene los valores de los atributos según COLUMNS.
            2. Llama a DAO.insert() para persistir en la tabla correspondiente.

        Consideraciones:
            - La tabla debe existir en la base de datos.
            - Todos los atributos en COLUMNS deben existir como atributos de la instancia.

        Ejemplo de uso:
            >>> c = Contacto(nombre="Juan", email="juan@mail.com")
            >>> c.save()
        """
        values = [getattr(self, f"_{col}") for col in self.COLUMNS]
        DAO.insert(self.TABLE_NAME, self.COLUMNS, values)

    def update(self):
        """
        Actualiza un registro existente en la base de datos.

        Flujo:
            1. Obtiene los valores de los atributos según COLUMNS.
            2. Llama a DAO.update() usando _id para identificar el registro.

        Consideraciones:
            - _id debe existir y corresponder a un registro en la tabla.
            - La tabla y columnas deben existir en la base de datos.

        Ejemplo de uso:
            >>> c = Contacto.find_by_id(1)
            >>> c._email = "nuevo@mail.com"
            >>> c.update()
        """
        values = [getattr(self, f"_{col}") for col in self.COLUMNS]
        DAO.update(self.TABLE_NAME, self.COLUMNS, values, self._id)

    def delete(self):
        """
        Elimina el registro de la base de datos.

        Consideraciones:
            - _id debe corresponder a un registro existente.
            - No se puede recuperar automáticamente el registro eliminado.

        Ejemplo de uso:
            >>> c = Contacto.find_by_id(1)
            >>> c.delete()
        """
        DAO.delete(self.TABLE_NAME, self._id)

    @classmethod
    def find_by_id(cls, id: int):
        """
        Recupera un objeto de la base de datos según su id.

        Args:
            id (int): Identificador del registro a buscar.

        Returns:
            instancia de cls: Objeto correspondiente al registro.
            None: Si no se encuentra el registro.

        Ejemplo de uso:
            >>> c = Contacto.find_by_id(1)
            >>> print(c._nombre)
        """
        rows = DAO.select_by_id(cls.TABLE_NAME, cls.COLUMNS, id)
        if rows:
            row = rows[0]
            obj = cls(**{col: row[idx] for idx, col in enumerate(cls.COLUMNS)})
            obj._id = id
            return obj
        return None

    @classmethod
    def all(cls):
        """
        Recupera todos los objetos de la tabla asociada a la clase.

        Returns:
            list: Lista de instancias de cls correspondientes a cada registro.

        Ejemplo de uso:
            >>> contactos = Contacto.all()
            >>> for c in contactos:
            >>>     print(c._nombre)
        """
        rows = DAO.select_all(cls.TABLE_NAME, cls.COLUMNS)
        objects = []
        for row in rows:
            obj = cls(**{col: row[idx] for idx, col in enumerate(cls.COLUMNS)})
            obj._id = row[0]  # asumimos que id es la primera columna
            objects.append(obj)
        return objects

    def get_id(self):
        """
        Devuelve el identificador del objeto.

        Returns:
            int: Valor del atributo _id.

        Ejemplo de uso:
            >>> c = Contacto.find_by_id(1)
            >>> print(c.get_id())
            1
        """
        return self._id

# 🔹 Extensibilidad de la clase:
# - Para agregar un nuevo campo a cualquier entidad:
#       1. Agregar atributo en la subclase con prefijo '_'.
#       2. Añadir el nombre del campo a COLUMNS de la subclase.
#       3. Actualizar la tabla de la base de datos con la nueva columna.
# - Para agregar un método de negocio específico:
#       - Definirlo en la subclase, nunca en BaseModel.
# - Esta estructura permite que entre compañeros agreguen entidades y campos
#   sin modificar el núcleo de persistencia, evitando conflictos.
