# Sistema de Autenticación - Guía de Instalación

## 📋 Descripción

Sistema de autenticación con login seguro implementado en FastAPI con las siguientes características:

- ✅ Contraseñas hasheadas con **bcrypt**
- ✅ Gestión de sesiones con **Starlette SessionMiddleware**
- ✅ Rutas de autenticación en router separado
- ✅ Protección de rutas privadas
- ✅ Interfaz de login y registro moderna

## 🚀 Instalación

### 1. Instalar las dependencias

```powershell
pip install -r requirements.txt
```

### 2. Crear la tabla de usuarios en la base de datos

Ejecuta el script SQL en tu base de datos MySQL:

```sql
USE oscar;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARBINARY(255) NOT NULL,
    email VARCHAR(100),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

Puedes encontrar el script completo en: `sql/create_usuarios_table.sql`

### 3. Crear un usuario inicial

Ejecuta el script para crear el usuario administrador:

```powershell
python crear_usuario_inicial.py
```

Esto creará un usuario con las siguientes credenciales:
- **Usuario:** admin
- **Contraseña:** admin123

⚠️ **IMPORTANTE:** Cambia esta contraseña después del primer inicio de sesión.

### 4. Iniciar la aplicación

```powershell
python main.py
```

La aplicación estará disponible en: http://127.0.0.1:8000

## 🔐 Rutas de Autenticación

### Públicas (no requieren login)
- `GET /auth/login` - Formulario de inicio de sesión
- `POST /auth/login` - Procesar login
- `GET /auth/registro` - Formulario de registro
- `POST /auth/registro` - Procesar registro

### Privadas (requieren login)
- `GET /` - Página de inicio
- `GET /alumnos` - Lista de alumnos
- `GET /insert_alumnos` - Formulario insertar alumno
- `POST /do_insertar_alumno` - Procesar inserción
- `GET /borrar` - Formulario borrar alumno
- `POST /do_borrar_alumno` - Procesar borrado
- `GET /auth/logout` - Cerrar sesión

## 📁 Estructura del Proyecto

```
├── routers/
│   └── auth_router.py          # Router de autenticación
├── utils/
│   └── session.py              # Gestión de sesiones
├── data/
│   ├── usuario_repository.py   # Repositorio de usuarios
│   └── database.py             # Conexión a BD
├── domain/
│   └── model/
│       └── Usuario.py          # Modelo de usuario
├── templatesitos/
│   ├── login.html              # Plantilla de login
│   └── registro.html           # Plantilla de registro
└── sql/
    └── create_usuarios_table.sql # Script SQL
```

## 🔒 Seguridad

### Contraseñas
- Las contraseñas se hashean con **bcrypt** usando salt automático
- El hash se almacena como `VARBINARY(255)` en la base de datos
- Nunca se almacenan contraseñas en texto plano

### Sesiones
- Las sesiones se gestionan con **Starlette SessionMiddleware**
- La cookie de sesión es **httponly** para prevenir XSS
- Tiempo de expiración: 7 días
- Clave secreta configurable en `main.py`

⚠️ **IMPORTANTE:** Cambia la clave secreta en producción en el archivo `main.py`:
```python
app.add_middleware(
    SessionMiddleware,
    secret_key="tu_clave_secreta_super_segura_para_produccion"
)
```

## 📝 Uso

### Crear un nuevo usuario

1. Accede a http://127.0.0.1:8000/auth/registro
2. Completa el formulario con:
   - Usuario (mínimo 3 caracteres)
   - Email (opcional)
   - Contraseña (mínimo 6 caracteres)
   - Confirmar contraseña
3. Haz clic en "Crear Cuenta"

### Iniciar sesión

1. Accede a http://127.0.0.1:8000/auth/login
2. Ingresa tu usuario y contraseña
3. Haz clic en "Iniciar Sesión"

### Cerrar sesión

- Haz clic en el botón "Cerrar Sesión" en la esquina superior derecha

## 🛠️ Personalización

### Cambiar la clave secreta de sesiones

Edita `main.py`:
```python
app.add_middleware(
    SessionMiddleware,
    secret_key="tu_nueva_clave_super_secreta"
)
```

### Cambiar el tiempo de expiración de sesiones

En `main.py`, modifica el valor `max_age` (en segundos):
```python
app.add_middleware(
    SessionMiddleware,
    secret_key="tu_clave_secreta",
    max_age=3600 * 24 * 30  # 30 días
)
```

### Proteger nuevas rutas

Para proteger una nueva ruta, agrega esta verificación:

```python
from utils.session import obtener_usuario_actual

@app.get("/mi_ruta_protegida")
async def mi_ruta(request: Request):
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/auth/login", status_code=303)
    
    return templates.TemplateResponse("mi_template.html", {
        "request": request,
        "usuario": usuario
    })
```

## 📚 Tecnologías Utilizadas

- **FastAPI** - Framework web
- **bcrypt** - Hash de contraseñas
- **Starlette SessionMiddleware** - Gestión de sesiones
- **Jinja2** - Motor de plantillas
- **MySQL** - Base de datos

## ⚙️ Requisitos

- Python 3.7+
- MySQL 5.7+
- Dependencias en `requirements.txt`

## 🐛 Solución de Problemas

### Error: "No module named 'bcrypt'"
```powershell
pip install bcrypt
```

### Error: "No module named 'starlette'"
```powershell
pip install starlette
```

### Error al conectar con la base de datos
Verifica la configuración en `data/database.py`

### Error: "Table 'usuarios' doesn't exist"
Ejecuta el script SQL para crear la tabla: `sql/create_usuarios_table.sql`
