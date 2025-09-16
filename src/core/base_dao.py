"""
Módulo DAO (Data Access Object) genérico.

Este módulo define la clase base DAO, responsable de manejar operaciones básicas
de acceso a la base de datos SQLite. Sirve como clase padre para cualquier DAO
específico de entidad (por ejemplo, ContactoDAO, UsuarioDAO).

Responsabilidades:
- Abrir y cerrar la conexión a la base de datos.
- Ejecutar consultas SQL de lectura (SELECT) y escritura (INSERT, UPDATE, DELETE).
- Proporcionar una base extensible para que otras clases DAO puedan especializarse.
"""

import sqlite3
from src.config.db import get_connection

class DAO:
    """
    Clase base DAO para operaciones genéricas de base de datos.

    Atributos:
        conn (sqlite3.Connection): Conexión abierta a la base de datos.
    
    Consideraciones de uso:
        - Siempre cerrar la conexión llamando a close() al terminar las operaciones.
        - Utilizar execute_query() para SELECT y execute_non_query() para INSERT/UPDATE/DELETE.
        - Las clases hijas pueden definir atributos como table_name y columns
          para especializarse en una tabla específica.
    
    Ejemplo de uso:
        >>> dao = DAO()
        >>> resultados = dao.execute_query("SELECT * FROM contactos")
        >>> dao.close()
    """

    def __init__(self):
        """
        Inicializa la conexión a la base de datos y asegura que se pueda acceder
        a las columnas por nombre.
        """
        self.conn = get_connection()
        self.conn.row_factory = sqlite3.Row  

    def close(self):
        """
        Cierra la conexión a la base de datos.

        Ejemplo de uso:
            >>> dao = DAO()
            >>> # operaciones con la base de datos
            >>> dao.close()
        
        Extensibilidad:
            - Siempre llamar a este método en DAOs especializados después de operaciones
              largas o al final de métodos de servicio que manejen transacciones.
        """
        self.conn.close()

    def execute_query(self, query, params=()):
        """
        Ejecuta una consulta SQL de lectura (SELECT) y devuelve los resultados.

        Args:
            query (str): Consulta SQL a ejecutar, con placeholders '?' si corresponde.
            params (tuple): Valores para reemplazar los placeholders de la consulta.

        Returns:
            list[sqlite3.Row]: Lista de filas resultantes de la consulta.

        Ejemplo de uso:
            >>> dao = DAO()
            >>> resultados = dao.execute_query("SELECT * FROM contactos WHERE id=?", (1,))
            >>> for fila in resultados:
            >>>     print(fila['nombre'])
            >>> dao.close()

        Extensibilidad:
            - Las clases hijas pueden usar este método para construir métodos específicos
              como select_all(), select_by_id(), filtrando por cualquier columna nueva.
            - Para agregar nuevos campos a una tabla, solo hace falta incluirlos en el SELECT.
        """
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def execute_non_query(self, query, params=()):
        """
        Ejecuta una consulta SQL de escritura (INSERT, UPDATE, DELETE).

        Args:
            query (str): Consulta SQL a ejecutar, con placeholders '?' si corresponde.
            params (tuple): Valores para reemplazar los placeholders de la consulta.

        Returns:
            None

        Ejemplo de uso:
            >>> dao = DAO()
            >>> dao.execute_non_query("INSERT INTO contactos (nombre, email) VALUES (?, ?)", ("Juan", "juan@email.com"))
            >>> dao.close()

        Extensibilidad:
            - Las clases hijas pueden crear métodos como save(), update(), delete()
              llamando a este método con los parámetros adecuados.
            - Para agregar nuevas columnas a la tabla:
                1. Añadir la columna en la base de datos (DB).
                2. Actualizar los métodos en la clase DAO especializada para incluir la columna.
                3. Este método sigue funcionando sin cambios.
            - Permite mantener todo el acceso a DB centralizado y consistente.
        """
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
