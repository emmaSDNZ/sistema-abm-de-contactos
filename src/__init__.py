from abc import ABC, abstractmethod
 
class BaseModel(ABC):
    
    """
    Calse abstracta que define la estrctura base de todas las entidades del sistema.
    Encapsula Id y define metodos abstractos de persistencia.

    Atributos:
        id (int): Identificador único de la entidad.  
    
    """
    _id: int

    def __init__(self, id: int = None):
        self._id = id

    @abstractmethod
    def save(self):
        """Guarda la entidad en la base de datos."""
        pass

    @abstractmethod
    def update(self):
        """Actualiza la entidad en la base de datos."""
        pass
    @abstractmethod
    def delete(self):
        """Elimina la entidad de la base de datos."""
        pass
    @abstractmethod
    def load(self, id: int):
        """Carga la entidad desde la base de datos usando su ID."""
        pass

    @classmethod
    @abstractmethod
    def find_all(cls):
        """Retorna todas las entidades de este tipo desde la base de datos."""
        pass
    
    def find_by_id(self, id: int):
        """Retorna la entidad con el ID especificado desde la base de datos."""
        pass

    def get_id(self) -> int:
        """Retorna el ID de la entidad."""
        return self._id