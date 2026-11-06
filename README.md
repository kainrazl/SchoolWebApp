# SchoolSysWeb - API Escolar MVP

Sistema de gestión escolar desarrollado con **FastAPI**, **SQLAlchemy 2.0 (asíncrono con `aiomysql`)**, **MySQL** y **Pydantic v2**.

---

## 🚀 Estructura del Proyecto

```text
SchoolSysWeb/
├── app/
│   ├── api/                    # Capa de transporte HTTP (Endpoints)
│   │   ├── deps.py             # Dependencias (DB Session, Usuario autenticado)
│   │   └── v1/
│   │       ├── router.py       # Enrutador principal v1
│   │       └── endpoints/      # Endpoints individuales por módulo
│   │           ├── auth.py
│   │           ├── users.py
│   │           ├── students.py
│   │           ├── groups.py
│   │           ├── subjects.py
│   │           ├── attendances.py
│   │           ├── grades.py
│   │           └── payments.py
│   ├── core/                   # Configuración y utilidades centrales
│   │   ├── config.py           # Variables de entorno y ajustes
│   │   ├── database.py         # Conexión Async Engine y SessionLocal
│   │   └── security.py         # Hash de contraseñas y tokens JWT
│   ├── models/                 # Modelos ORM (SQLAlchemy 2.0 Declarative)
│   │   ├── user.py             # Roles y Usuarios
│   │   ├── student.py          # Alumnos
│   │   ├── group.py            # Grupos
│   │   ├── subject.py          # Materias
│   │   ├── attendance.py       # Asistencias
│   │   ├── grade.py            # Calificaciones
│   │   └── payment.py          # Pagos
│   ├── schemas/                # Esquemas de validación y DTOs (Pydantic v2)
│   ├── services/               # Lógica de negocio (CRUD asíncrono y consultas)
│   └── main.py                 # Punto de entrada de la aplicación FastAPI
├── tests/                      # Pruebas automatizadas (pytest)
├── .env                        # Variables de entorno locales
├── .env.example                # Plantilla de variables de entorno
├── requirements.txt            # Dependencias del proyecto
└── README.md
```

---

## 🛠️ Requisitos Previos

- Python 3.10+
- Servidor MySQL activo (local o en contenedor Docker)
- Crear la base de datos en MySQL:
  ```sql
  CREATE DATABASE school_sys_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  ```

---

## ⚙️ Instalación y Configuración

1. **Crear y activar un entorno virtual**:
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**:
   Edita el archivo `.env` con tus credenciales de MySQL:
   ```env
   DATABASE_URL=mysql+aiomysql://admin:tu_password@localhost:3306/school_sys_db
   SECRET_KEY=clave_secreta_para_desarrollo
   ```

4. **Poblar la base de datos con datos iniciales (Seeds)**:
   Ejecuta el script para crear las tablas, roles, usuario administrador y registros de muestra:
   ```bash
   python -m scripts.seed_db
   ```
   **Credenciales por defecto creadas:**
   - **Usuario / Email:** `admin@schoolsys.com` (o username `admin`)
   - **Contraseña:** `admin123`

---

## ▶️ Ejecución del Servidor

Inicia el servidor con recarga en vivo (*hot-reload*):

```bash
uvicorn app.main:app --reload
```

- La API estará disponible en: [http://localhost:8000](http://localhost:8000)
- Documentación interactiva Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Documentación alternativa ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Ejecutar Pruebas

```bash
pytest
```

