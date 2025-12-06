# 🎯 Versión Mejorada: Dependencies con Response Helpers

## ✅ Nueva estructura más limpia

En lugar de tener HTML inline en las dependencias, ahora usamos un helper:

### Archivo: `utils/response_helpers.py`

```python
from fastapi.responses import HTMLResponse

def forbidden_response(mensaje: str, rol_requerido: str = None) -> HTMLResponse:
    """Genera una respuesta HTML 403 bonita"""
    # HTML bonito y reutilizable
    return HTMLResponse(content=html_content, status_code=403)
```

### Archivo: `utils/dependencies.py` (versión mejorada)

```python
from utils.response_helpers import forbidden_response

def require_admin(usuario: dict = Depends(require_auth)) -> dict:
    if usuario.get("role") not in ["admin", "superadmin"]:
        # ✅ Mucho más limpio
        return forbidden_response(
            mensaje="Esta página requiere permisos de Administrador",
            rol_requerido="admin o superadmin"
        )
    return usuario
```

---

## 📊 Comparación: Antes vs Ahora

### ❌ Antes (HTTPException - JSON feo)

```python
def require_admin(usuario: dict = Depends(require_auth)) -> dict:
    if usuario.get("role") not in ["admin", "superadmin"]:
        raise HTTPException(status_code=403, detail="Requiere admin")
        # ❌ Devuelve JSON: {"detail": "Requiere admin"}
        # ❌ Feo para páginas web
    return usuario
```

**Resultado en navegador:**
```json
{"detail": "Requiere permisos de administrador"}
```

---

### ⚠️ Intermedio (HTML inline - funcional pero sucio)

```python
def require_admin(usuario: dict = Depends(require_auth)) -> dict:
    if usuario.get("role") not in ["admin", "superadmin"]:
        html_content = """
        <!DOCTYPE html>
        <html>
        ... 50 líneas de HTML ...
        </html>
        """  # ❌ HTML mezclado con lógica
        return HTMLResponse(content=html_content, status_code=403)
    return usuario
```

**Problemas:**
- ❌ Código muy largo
- ❌ HTML mezclado con Python
- ❌ Difícil de mantener
- ❌ Repetición si hay múltiples dependencias

---

### ✅ Ahora (Response Helper - Limpio y profesional)

```python
from utils.response_helpers import forbidden_response

def require_admin(usuario: dict = Depends(require_auth)) -> dict:
    if usuario.get("role") not in ["admin", "superadmin"]:
        return forbidden_response(
            mensaje="Esta página requiere permisos de Administrador",
            rol_requerido="admin o superadmin"
        )
    return usuario
```

**Ventajas:**
- ✅ **Código limpio** (3 líneas vs 50)
- ✅ **Reutilizable** (un helper para todas las dependencias)
- ✅ **Fácil de mantener** (cambias el HTML en un solo lugar)
- ✅ **Separación de responsabilidades** (lógica vs presentación)

**Resultado en navegador:**
```
┌─────────────────────────────────────┐
│         🚫 Acceso Denegado         │
│     HTTP 403 - Forbidden           │
│                                     │
│  Esta página requiere permisos     │
│  de Administrador                  │
│                                     │
│  🔐 Rol requerido:                 │
│  admin o superadmin                │
│                                     │
│  [ 🏠 Volver al Inicio ]           │
│  [ ← Página Anterior ]             │
└─────────────────────────────────────┘
```

---

## 🚀 Otros Response Helpers útiles

### 1. unauthorized_response (401)
```python
def require_auth(request: Request):
    usuario = obtener_usuario_actual(request)
    if not usuario:
        # Opción 1: Redirigir (para web)
        return RedirectResponse(url="/auth/login", status_code=303)
        
        # Opción 2: Mostrar página de error (para APIs)
        return unauthorized_response("Debes iniciar sesión")
    return usuario
```

---

### 2. not_found_response (404)
```python
def not_found_response(recurso: str = "recurso") -> HTMLResponse:
    """Genera una respuesta HTML 404 bonita"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <body>
        <h1>404 - No Encontrado</h1>
        <p>El {recurso} que buscas no existe.</p>
        <a href="/">Volver al inicio</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=404)

# Uso:
@app.get("/alumno/{id}")
async def get_alumno(id: int):
    alumno = repo.get_by_id(database, id)
    if not alumno:
        return not_found_response("alumno")
    return alumno
```

---

### 3. server_error_response (500)
```python
def server_error_response(error: str = None) -> HTMLResponse:
    """Genera una respuesta HTML 500 bonita"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <body>
        <h1>500 - Error del Servidor</h1>
        <p>Lo sentimos, algo salió mal.</p>
        {f'<pre>{error}</pre>' if error else ''}
        <a href="/">Volver al inicio</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=500)
```

---

## 🎨 Estructura final recomendada

```
utils/
├── dependencies.py          # Lógica de autenticación
├── session.py              # Gestión de sesiones
└── response_helpers.py     # ✨ Helpers para respuestas bonitas
    ├── forbidden_response()      → 403
    ├── unauthorized_response()   → 401
    ├── not_found_response()      → 404
    └── server_error_response()   → 500
```

---

## 💡 Ventajas de esta arquitectura

| Aspecto | Antes (HTTPException) | Ahora (Response Helpers) |
|---------|---------------------|-------------------------|
| **Código limpio** | ❌ JSON feo | ✅ HTML bonito |
| **Mantenibilidad** | ❌ Cambiar en cada ruta | ✅ Un solo lugar |
| **Reutilización** | ❌ No reutilizable | ✅ Muy reutilizable |
| **UX** | ❌ Malo (JSON crudo) | ✅ Excelente (HTML) |
| **Separación** | ❌ Lógica + presentación | ✅ Separados |

---

## 🎯 Resumen

**Antes:**
```python
raise HTTPException(403, "Error")  # JSON feo
```

**Ahora:**
```python
return forbidden_response("Error", "admin")  # HTML bonito
```

**Beneficio:**
- ✅ Código más limpio (3 líneas vs 50)
- ✅ Reutilizable
- ✅ Experiencia de usuario profesional
- ✅ Fácil de mantener

---

¡Tu aplicación ahora tiene páginas de error profesionales! 🎉
