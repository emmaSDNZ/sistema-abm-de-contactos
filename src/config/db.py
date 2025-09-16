"""
Módulo de configuración de la base de datos SQLite.

Propósito:
Este módulo proporciona funciones para conectarse e inicializar la base de datos.
Contiene:
- get_connection(): para abrir una conexión SQLite.
- init_db(): para crear las tablas necesarias si no existen.

Responsabilidades:
- Centralizar la configuración de la base de datos.
- Garantizar que las tablas básicas ('usuarios' y 'contactos') existan antes de cualquier operación.
- Permitir que futuros desarrolladores puedan extender la base de datos agregando tablas o columnas sin afectar la funcionalidad existente.

Extensibilidad:
- Para agregar un nuevo campo a una tabla existente, agregar la columna en la definición SQL dentro de init_db() y luego actualizar las clases y DAOs correspondientes para manejar el nuevo campo.
- Para agregar una nueva tabla, añadir un nuevo bloque cursor.execute() con la sentencia CREATE TABLE IF NOT EXISTS y luego crear el modelo, DAO y servicios correspondientes.
- Todas las operaciones deben mantenerse usando get_connection() para asegurar consistencia y reaprovechamiento de la conexión.
"""

import sqlite3

DB_NAME = "abm_contactos.db"


def get_connection():
    
    """
    Devuelve una conexión activa a la base de datos SQLite.

    Returns:
        sqlite3.Connection: Objeto de conexión listo para ejecutar consultas.

    Consideraciones:
        - La conexión utiliza row_factory para acceder a las columnas por nombre.
        - Las tablas deben existir antes de ejecutar consultas, aseguradas por init_db().

    Ejemplo de uso:
        >>> conn = get_connection()
        >>> cursor = conn.cursor()
        >>> cursor.execute("SELECT * FROM contactos")
        >>> resultados = cursor.fetchall()
        >>> conn.close()

    Extensibilidad:
        - Siempre usar esta función para abrir la base de datos.
        - No se recomienda abrir conexiones directas fuera de esta función.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn



def init_db():

    """
    Inicializa la base de datos creando las tablas 'usuarios' y 'contactos' si no existen.

    Consideraciones:
        - Debe llamarse antes de ejecutar cualquier operación sobre la base de datos.
        - No elimina ni modifica datos existentes.
        - Asegura que las tablas tengan las columnas mínimas requeridas para el sistema.

    Ejemplo de uso:
        >>> init_db()
        >>> print("Tablas creadas si no existían")

    Extensibilidad:
        - Para agregar un campo nuevo a 'usuarios' o 'contactos', añadir la columna en el CREATE TABLE y actualizar los modelos y DAOs correspondientes.
            Ejemplo:
                cursor.execute(\"\"\"
                    CREATE TABLE IF NOT EXISTS contactos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        telefono TEXT,
                        email TEXT,
                        fecha_nacimiento TEXT,  # Nuevo campo agregado
                        created_at TEXT,
                        updated_at TEXT
                    )
                \"\"\")
        - Para agregar una tabla nueva:
            1. Añadir un bloque cursor.execute() con CREATE TABLE IF NOT EXISTS.
            2. Crear un modelo en src/models que represente la nueva entidad.
            3. Crear un DAO en src/dao que gestione las operaciones CRUD de la nueva tabla.
            4. Integrar la nueva entidad en los servicios y menús correspondientes.
    """

    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabla de usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            rol TEXT NOT NULL,
            ultimo_acceso TEXT,
            created_at TEXT,
            updated_at TEXT
        )
    """)

    # Tabla de contactos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT,
            email TEXT,
            created_at TEXT,
            updated_at TEXT
        )
    """)

    conn.commit()
    conn.close()
