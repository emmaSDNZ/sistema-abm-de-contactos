from datetime import datetime
from src.core.base_model import BaseModel
from src.core.base_dao import DAO
class Usuario(BaseModel):
    """
    Clase base para representar un usuario del sistema.

    Pilares de POO aplicados:
    - Encapsulación: atributos privados (_username, _passwordHash, _rol)
    - Abstracción: métodos para login, logout, permisos, sin exponer detalles internos
    - Herencia: hereda los métodos de persistencia de BaseModel.
    - Polimorfismo: se puede tratar cualquier subclase de Usuario como un Usuario
    """
    TABLE_NAME = "usuarios"
    COLUMNS = ["id","username", "password", "rol", "ultimo_acceso"]

    def __init__(self, id: int = None, username: str = "", password: str = "", rol: str = "basico", ultimo_acceso=None):
        super().__init__(id)
        self._username = username
        self._password = password   # 👈 usamos _password en todos lados
        self._rol = rol
        self._ultimo_acceso = ultimo_acceso
        self._loggeado = False

    def get_username(self):
        return self._username

    def set_password(self, new_password: str):
        self._password = new_password   # 👈 corregido

    def get_rol(self):
        return self._rol

    def get_ultimo_acceso(self):
        return self._ultimo_acceso

    def login(self, username: str, password: str):
        if username == self._username and password == self._password:  # 👈 corregido
            self._loggeado = True
            self._ultimo_acceso = datetime.now()
            self.update()
            print(f"[INFO] Usuario '{self._username}' loggeado correctamente.")
            return True
        print(f"[WARN] Login fallido para usuario '{username}'.")
        return False
    
    def logout(self):
        if self._loggeado:
            self._loggeado = False
            print(f"[INFO] Usuario '{self._username}' deslogueado.")
        else:
            print(f"[WARN] Usuario '{self._username}' no estaba loggeado.")


class UsuarioBasico(Usuario):
    """
    Usuario con permisos limitados: solo puede agendar contactos.
    """
    def __init__(self, id=None, username="", password=""):
        super().__init__(id=id, username=username, password=password, rol="basico")

    # Polimorfismo: redefine permisos
    def tiene_permiso(self, accion: str) -> bool:
        allowed = ["agregar_contacto"]
        return accion in allowed


class UsuarioAdmin(Usuario):
    """
    Usuario avanzado/admin: permisos totales
    """
    def __init__(self, id=None, username="", password=""):
        super().__init__(id=id, username=username, password=password, rol="admin")

    # Polimorfismo: redefine permisos
    def tiene_permiso(self, accion: str) -> bool:
        # Admin tiene todos los permisos
        return True
