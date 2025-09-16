"""
Módulo de definición de la entidad Contacto.

Este módulo define la clase Contacto, que representa un contacto dentro del sistema.
Hereda de AuditableModel para incluir campos de auditoría como created_at y updated_at.

Responsabilidades:
- Mantener la información básica de un contacto (nombre, teléfono, email).
- Integrarse con el DAO para persistencia en la base de datos.
- Facilitar la extensión futura agregando nuevos campos o métodos sin afectar la lógica existente.
"""

from src.core.auditable_model import AuditableModel

class Contacto(AuditableModel):
    """
    Clase que representa un contacto en la agenda.

    Hereda de AuditableModel para incluir auditoría automática de creación y actualización.

    Atributos:
        TABLE_NAME (str): Nombre de la tabla en la base de datos asociada a esta entidad.
        COLUMNS (list): Lista de columnas que corresponden a los atributos de la tabla.
        _nombre (str): Nombre del contacto.
        _telefono (str): Número de teléfono del contacto.
        _email (str): Correo electrónico del contacto.
    
    Extensibilidad:
        - Para agregar un nuevo campo, por ejemplo 'direccion', se deben seguir los siguientes pasos:
            1. Agregar el campo en la lista COLUMNS:
                COLUMNS = ["id", "nombre", "telefono", "email", "direccion", "created_at", "updated_at"]
            2. Agregar un atributo privado en el constructor:
                self._direccion = direccion
            3. Crear métodos getter y setter para el nuevo campo:
                def get_direccion(self):
                    return self._direccion
                def set_direccion(self, direccion):
                    self._direccion = direccion
                    self.set_timestamps()
            4. Actualizar el DAO correspondiente para manejar la persistencia del nuevo campo.
        - Para agregar métodos de utilidad (por ejemplo validaciones o formatos especiales):
            1. Crear el método dentro de la clase Contacto.
            2. Usar los atributos existentes y/o nuevos sin modificar los existentes.
            3. Garantizar que el método no afecte la persistencia de datos directamente; para eso usar DAO.

    Ejemplo de uso:
        >>> contacto = Contacto(nombre="Juan Perez", email="juan@email.com")
        >>> print(contacto)
        Nombre: Juan Perez, Email: juan@email.com
    """

    TABLE_NAME = "contactos"
    COLUMNS = [
        "id", 
        "nombre", 
        "telefono", 
        "email", 
        "created_at", 
        "updated_at"
    ]

    def __init__(self, id=None, nombre="", telefono="", email=""):
        """
        Constructor de la clase Contacto.

        Args:
            id (int): Identificador único del contacto (asignado por la base de datos).
            nombre (str): Nombre completo del contacto.
            telefono (str): Número de teléfono del contacto.
            email (str): Correo electrónico del contacto.

        Ejemplo de uso:
            >>> c = Contacto(nombre="Ana", email="ana@email.com")
        """
        super().__init__(id)
        self._nombre = nombre
        self._telefono = telefono
        self._email = email

    def __str__(self):
        """
        Representación en string del contacto, útil para impresión en menús y logs.

        Returns:
            str: Cadena con nombre y email del contacto.

        Ejemplo de uso:
            >>> c = Contacto(nombre="Ana", email="ana@email.com")
            >>> print(c)
            Nombre: Ana, Email: ana@email.com
        """
        return f"Nombre: {self._nombre}, Email: {self._email}"
