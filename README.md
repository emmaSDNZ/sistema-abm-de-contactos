# 🚀 ABM de Contactos – Proyecto Profesional Escalable

## 📌 Descripción General

El proyecto **ABM de Contactos** es un sistema de gestión de contactos desarrollado en **Python**, aplicando **Programación Orientada a Objetos (POO)**, con interfaz gráfica en **Tkinter** y persistencia de datos en **SQLite**.

Este desarrollo tiene un enfoque profesional y escalable, aplicando **principios SOLID, modularidad, pruebas unitarias y documentación formal**, simulando el flujo completo de trabajo en un proyecto real de software.

El sistema permite:

-   **Alta** de nuevos contactos (nombre, apellido, teléfono, email).
-   **Baja** de contactos existentes.
-   **Modificación** de la información de contactos.
-   **Consulta y listado** de contactos.
-   Organización de contactos en **grupos** (Familia, Amigos, Trabajo).
-   **Historial de operaciones** sobre contactos.
-   **Exportación a CSV** para análisis externo.

Cada integrante del equipo recorre **el ciclo completo de desarrollo**, incluyendo diseño de base de datos, definición de clases y objetos, conexión con GUI, testing y documentación.

---

## 🎯 Objetivos del Proyecto

1.  Diseñar un sistema ABM escalable y modular con POO en Python.
2.  Crear una interfaz gráfica funcional con Tkinter.
3.  Implementar persistencia de datos en SQLite con operaciones CRUD.
4.  Aplicar buenas prácticas profesionales: SOLID, modularidad, testing y documentación.
5.  Documentar clases, métodos y flujos de datos.
6.  Realizar pruebas unitarias y funcionales para garantizar calidad del software.
7.  Generar experiencia profesional para CV y LinkedIn.

---

## 🗂 Estructura del Repositorio


proyecto_abm_contactos/

├── src/                      # Código fuente
│   ├── main.py               # Entrada principal (GUI)
│   ├── contacto.py           # Clase Contacto
│   ├── grupo.py              # Clase Grupo
│   ├── historial.py          # Clase Historial
│   ├── database_manager.py   # Persistencia SQLite
│   └── services.py           # Lógica de negocio
├── tests/                    # Pruebas unitarias y funcionales
│   ├── test_contacto.py
│   ├── test_grupo.py
│   ├── test_historial.py
│   └── test_services.py
├── docs/                     # Documentación
│   ├── diagramas/            # Diagramas UML y de flujo
│   ├── informe.pdf           # Documento de diseño profesional
│   └── manual_usuario.pdf    # Guía de uso del sistema
├── data/                     # Base de datos y exportaciones CSV
│   ├── contactos.db
│   └── export_csv/
├── scripts/                  # Scripts de inicialización y migración
│   └── init_db.py
├── .gitignore                # Archivos y carpetas a ignorar
├── README.md                 # Este archivo
├── requirements.txt          # Librerías necesarias
└── setup.py (opcional)       # Para empaquetar proyecto como módulo

---

##  🏗 Arquitectura del Sistema

El sistema se basa en una arquitectura modular y escalable, con capas bien definidas para una clara separación de responsabilidades:

*   Capa de GUI (Tkinter): main.py maneja la interacción directa con el usuario, mostrando la interfaz y capturando los eventos.

*   Capa de Lógica / Servicios: services.py actúa como el "cerebro" del sistema, coordinando la comunicación entre la GUI y la base de datos, aplicando validaciones y reglas de negocio.

*   Capa de Persistencia: database_manager.py gestiona la conexión con la base de datos SQLite, encargándose de las operaciones CRUD (Create, Read, Update, Delete) y el manejo de transacciones.

*   Modelo de Datos: Las clases Contacto, Grupo e Historial representan las entidades del negocio, encapsulando sus atributos y la lógica específica de cada una.

Cada integrante del equipo desarrolló y documentó el ciclo completo: desde el diseño de la clase hasta la persistencia y las pruebas de su funcionalidad.

---

## 👥 Flujo de Trabajo por Integrante

Cada uno de los 6 integrantes del equipo siguió un flujo de trabajo completo para cada módulo asignado:

1.  Diseño: Creación de diagramas de clases y modelo de datos para una comprensión clara de la estructura.

2.  Desarrollo de clase / módulo: Implementación de la Programación Orientada a Objetos (POO) con documentación clara de atributos, métodos y sus funcionalidades.

3.  Conexión a base de datos: Implementación de las operaciones CRUD necesarias para la persistencia de datos.

4.  Integración con GUI: Vinculación de la lógica del módulo con la interfaz gráfica para una experiencia de usuario fluida.

5. Testing: Creación de pruebas unitarias y funcionales para asegurar la calidad y consistencia del software.

6. Documentación: Descripción detallada del funcionamiento de los métodos, el flujo de datos y las decisiones de diseño.

---

## ⚙ Instalación y Ejecución
Sigue estos pasos para poner en marcha la aplicación en tu entorno local:

* Clonar el repositorio:

git clone [https://github.com/emmaSDNZ/sistema-abm-de-contactos](https://github.com/emmaSDNZ/sistema-abm-de-contactos)

cd proyecto_abm_contactos

* Crear y activar un entorno virtual (recomendado):

python -m venv venv

# En Linux / Mac

source venv/bin/activate

# En Windows
venv\Scripts\activate

* Instalar las dependencias:

pip install -r requirements.txt

* Inicializar la base de datos:

python scripts/init_db.py

* Ejecutar la aplicación:


python src/main.py

---

## 🧪 Testing

El proyecto cuenta con un conjunto robusto de pruebas para garantizar su fiabilidad:

Pruebas unitarias para cada clase y módulo de la lógica de negocio (tests/).

Pruebas funcionales para las operaciones CRUD y la interacción con la GUI.

Se recomienda utilizar pytest para la ejecución de las pruebas:

Bash

pytest tests/

---

## 📊 Diagramas y Documentación
La documentación detallada es una parte crucial del proyecto:

Diagramas UML: Diagramas de clases, secuencias y flujo de datos se encuentran en docs/diagramas/.

Informe de Diseño Profesional: Un documento exhaustivo que detalla la arquitectura y las decisiones de diseño, disponible en docs/informe.pdf.

Manual de Usuario: Una guía para la utilización del sistema, ubicada en docs/manual_usuario.pdf.

---


## 🔄 Control de Versiones
Se utiliza un flujo de trabajo de Git Flow simplificado para el control de versiones:

main: La rama principal que contiene la versión estable y lista para producción.

dev: La rama de desarrollo donde se integran todos los cambios de las diferentes funcionalidades.

feature/ branches: Ramas dedicadas a cada nueva funcionalidad (ej. feature/gui, feature/db), creadas a partir de dev.

---

## 📂 Roles de Integrantes

Cada integrante se encargó de desarrollar una porción de las clases y módulos, siguiendo el flujo de trabajo completo para una experiencia integral en el desarrollo de software.

Integrantes: [Nombre del Integrante 1], [Nombre del Integrante 2], [Nombre del Integrante 3], [Nombre del Integrante 4], [Nombre del Integrante 5], [Nombre del Integrante 6].

Ejemplo de Responsabilidad: Diseño de la clase Contacto, conexión con la base de datos, pruebas unitarias, integración con la GUI y documentación completa del módulo.

📌 Contacto
Este proyecto fue desarrollado para la Tecnicatura en Ciencias de Datos e Inteligencia Artificial.

Instructor: Alejandro Mainero

Autores: 
Isaias Emanuel Sudañez [https://github.com/emmaSDNZ](https://github.com/emmaSDNZ)

Joaquín Pedrone Pfeiffer, [LINK GITHUB]

Christian Quispe, [LINK GITHUB] 
