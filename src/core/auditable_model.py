"""
Módulo base para modelos auditables.

Este módulo define la clase AuditableModel, que proporciona funcionalidad común
para todas las entidades del sistema que requieren campos de auditoría, como
created_at y updated_at.

Responsabilidades principales:
- Mantener un identificador único (_id) para cada registro.
- Registrar la fecha y hora de creación (created_at).
- Registrar la fecha y hora de la última modificación (updated_at).
- Proporcionar un método para actualizar automáticamente los timestamps.

Flujo principal:
1. Al instanciar un modelo, se asigna un ID (opcional) y se registran
   los timestamps de creación y actualización.
2. Cada vez que se modifica un atributo del modelo, se llama a set_timestamps()
   para actualizar el campo updated_at.
"""

from datetime import datetime

class AuditableModel:
    """
    Clase base para modelos que requieren auditoría de creación y actualización.

    Atributos:
        _id (int): Identificador único de la entidad.
        created_at (str): Timestamp de creación en formato ISO 8601.
        updated_at (str): Timestamp de última modificación en formato ISO 8601.

    Ejemplo de uso:
        >>> from core.auditable_model import AuditableModel
        >>> entidad = AuditableModel()
        >>> print(entidad.created_at, entidad.updated_at)
        2025-09-16T12:00:00 2025-09-16T12:00:00
    """

    def __init__(self, id=None):
        """
        Inicializa un objeto auditable.

        Args:
            id (int, opcional): Identificador del registro. Si no se provee,
                                 se asignará None y luego lo generará la base de datos.

        Consideraciones:
            - created_at y updated_at se generan automáticamente en el momento de la creación.
            - Esta clase está diseñada para ser la superclase de todas las entidades
              que necesiten campos de auditoría.

        Extensibilidad:
            - Para agregar un nuevo campo que también deba actualizar su timestamp,
              se puede sobrescribir el método set_timestamps() o agregar un método
              adicional para manejar lógica específica.
            - Se pueden agregar atributos adicionales (por ejemplo, usuario_creacion, usuario_actualizacion)
              en clases que hereden de AuditableModel sin modificar la clase base.
        """
        self._id = id
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def set_timestamps(self):
        """
        Actualiza el timestamp de la última modificación.

        Flujo:
            1. Se llama cada vez que se modifica cualquier atributo del modelo.
            2. updated_at se actualiza con la fecha y hora actual.

        Ejemplo de uso:
            >>> entidad = AuditableModel()
            >>> entidad.set_timestamps()
            >>> print(entidad.updated_at)

        Extensibilidad:
            - Las clases hijas pueden llamar a este método dentro de setters de nuevos atributos
              para mantener la consistencia de auditoría.
            - Se puede sobrescribir para registrar información adicional, como usuario que hizo la modificación.
        """
        self.updated_at = datetime.now().isoformat()





