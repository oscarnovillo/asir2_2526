# 🎯 Guía de Dependencias (Dependencies) en FastAPI

## ¿Qué son las Dependencies?

Las **Dependencies** (Dependencias) son el equivalente de **interceptores/filtros** en FastAPI. Funcionan como middleware a nivel de ruta.

## 🔄 Comparación con otros frameworks:

| Framework | Concepto similar |
|-----------|-----------------|
| **Spring Boot** | `@PreAuthorize`, Interceptors |
| **Django** | Decorators, Middleware |
| **Express.js** | Middleware functions |
| **ASP.NET** | Filters, Middleware |
| **FastAPI** | **Dependencies** ✅ |

---

## ✅ ANTES vs DESPUÉS

### ❌ ANTES (Sin dependencias - Código repetido):

```python
@app.get("/ruta1")
async def ruta1(request: Request):
    # ❌ Código repetido
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/auth/login", status_code=303)
    # ... lógica de la ruta

@app.get("/ruta2")
async def ruta2(request: Request):
    # ❌ Código repetido otra vez
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/auth/login", status_code=303)
    # ... lógica de la ruta

@app.get("/ruta3")
async def ruta3(request: Request):
    # ❌ Y otra vez...
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/auth/login", status_code=303)
    # ... lógica de la ruta
```

### ✅ DESPUÉS (Con dependencias - DRY):

```python
from fastapi import Depends
from utils.dependencies import require_auth

@app.get("/ruta1")
async def ruta1(request: Request, usuario: dict = Depends(require_auth)):
    # ✅ El usuario ya está autenticado y disponible
    # ... lógica de la ruta

@app.get("/ruta2")
async def ruta2(request: Request, usuario: dict = Depends(require_auth)):
    # ✅ Una sola línea para proteger la ruta
    # ... lógica de la ruta

@app.get("/ruta3")
async def ruta3(request: Request, usuario: dict = Depends(require_auth)):
    # ✅ Reutilizable en cualquier ruta
    # ... lógica de la ruta
```

---

## 📚 Tipos de dependencias creadas

### 1. `require_auth` - Autenticación obligatoria

```python
@app.get("/admin")
async def admin_panel(usuario: dict = Depends(require_auth)):
    # Si no está autenticado → Redirect a /auth/login
    # Si está autenticado → Continúa
    return {"mensaje": f"Bienvenido admin {usuario['username']}"}
```

### 2. `optional_auth` - Autenticación opcional

```python
@app.get("/home")
async def home(usuario: Optional[dict] = Depends(optional_auth)):
    # Si está autenticado → usuario tiene datos
    # Si NO está autenticado → usuario = None (sin redirect)
    if usuario:
        return {"mensaje": f"Hola {usuario['username']}"}
    else:
        return {"mensaje": "Hola invitado"}
```

---

## 🚀 Casos de uso avanzados

### 1. Proteger un grupo de rutas (Router):

```python
# routers/admin_router.py
from fastapi import APIRouter, Depends
from utils.dependencies import require_auth

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(require_auth)]  # ✅ Todas las rutas protegidas
)

@router.get("/users")
async def list_users():
    # Ya está protegida automáticamente
    return {"users": [...]}

@router.get("/settings")
async def settings():
    # También protegida
    return {"settings": {...}}
```

### 2. Dependencias encadenadas:

```python
def require_admin(usuario: dict = Depends(require_auth)) -> dict:
    """Requiere que el usuario sea admin"""
    if usuario.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return usuario

@app.get("/admin/panel")
async def admin_panel(usuario: dict = Depends(require_admin)):
    # Solo admins pueden acceder
    return {"mensaje": "Panel de administración"}
```

### 3. Múltiples dependencias:

```python
def get_db():
    db = database
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
async def list_users(
    usuario: dict = Depends(require_auth),  # Requiere auth
    db = Depends(get_db)                    # Inyecta DB
):
    # Ambas dependencias resueltas
    return {"users": db.query(...)}
```

---

## 🎨 Ventajas de usar Dependencies

### ✅ 1. DRY (Don't Repeat Yourself)
```python
# Una sola vez
def require_auth(request: Request) -> dict:
    ...

# Usar en N rutas
usuario: dict = Depends(require_auth)
```

### ✅ 2. Testeable
```python
# En tests
def override_auth():
    return {"user_id": 1, "username": "test_user"}

app.dependency_overrides[require_auth] = override_auth
```

### ✅ 3. Composable
```python
def require_auth(...) -> dict: ...
def require_admin(usuario = Depends(require_auth)) -> dict: ...
def require_superadmin(usuario = Depends(require_admin)) -> dict: ...
```

### ✅ 4. Autodocumentación
FastAPI documenta automáticamente las dependencias en Swagger UI.

### ✅ 5. Type hints
```python
usuario: dict = Depends(require_auth)
# FastAPI sabe que usuario es un dict
# Tu IDE te da autocompletado
```

---

## 🔥 Comparación con Middleware

### Middleware:
- Se ejecuta en **TODAS** las peticiones
- Útil para logging, CORS, sesiones
- No puede inyectar datos en funciones específicas

### Dependencies:
- Se ejecuta solo en **rutas específicas**
- Puede inyectar datos en la función
- Más granular y flexible

```python
# Middleware (global)
@app.middleware("http")
async def log_requests(request, call_next):
    # Se ejecuta en TODAS las peticiones
    print(f"Request: {request.url}")
    return await call_next(request)

# Dependency (específica)
@app.get("/protected")
async def protected(usuario = Depends(require_auth)):
    # Solo se ejecuta en esta ruta
    return {"user": usuario}
```

---

## 📖 Ejemplo completo en tu proyecto

### Archivo: `utils/dependencies.py`
```python
from fastapi import Request, Depends
from fastapi.responses import RedirectResponse

def require_auth(request: Request) -> dict:
    usuario = obtener_usuario_actual(request)
    if not usuario:
        raise RedirectResponse(url="/auth/login", status_code=303)
    return usuario
```

### Archivo: `main.py`
```python
from fastapi import FastAPI, Depends
from utils.dependencies import require_auth

@app.get("/")
async def inicio(usuario: dict = Depends(require_auth)):
    return {"mensaje": f"Bienvenido {usuario['username']}"}

@app.get("/alumnos")
async def alumnos(usuario: dict = Depends(require_auth)):
    # Código limpio, sin verificaciones
    return {"alumnos": [...]}
```

---

## 🎓 Resumen

| Característica | Valor |
|---------------|-------|
| **Reutilizable** | ✅ Una vez, úsalo N veces |
| **Testeable** | ✅ Fácil de mockear |
| **Limpio** | ✅ Sin código repetido |
| **Type-safe** | ✅ Con type hints |
| **Documentado** | ✅ Aparece en Swagger |
| **Flexible** | ✅ Composable y encadenable |

---

## 🔗 Recursos

- [FastAPI Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Advanced Dependencies](https://fastapi.tiangolo.com/advanced/advanced-dependencies/)
- [Security Dependencies](https://fastapi.tiangolo.com/tutorial/security/)

---

**¡Esto es lo que hace FastAPI tan poderoso!** 🚀
