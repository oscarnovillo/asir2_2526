# 🔧 Solución: RedirectResponse en Dependencies

## ❌ El Problema

Cuando intentas usar `raise RedirectResponse(...)` en una dependencia de FastAPI:

```python
def require_auth(request: Request) -> dict:
    usuario = obtener_usuario_actual(request)
    if not usuario:
        raise RedirectResponse(url="/auth/login", status_code=303)  # ❌ ERROR
    return usuario
```

**Error**: `exceptions must derive from BaseException`

### ¿Por qué falla?

`RedirectResponse` es una **respuesta HTTP**, no una **excepción**. Solo puedes hacer `raise` con objetos que hereden de `BaseException`.

---

## ✅ La Solución: Excepción Personalizada

### Paso 1: Crear una excepción personalizada

```python
# utils/dependencies.py

class RedirectException(Exception):
    def __init__(self, url: str, status_code: int = 303):
        self.url = url
        self.status_code = status_code
```

### Paso 2: Usar la excepción en las dependencias

```python
def require_auth(request: Request) -> dict:
    usuario = obtener_usuario_actual(request)
    if not usuario:
        raise RedirectException(url="/auth/login", status_code=303)  # ✅ CORRECTO
    return usuario
```

### Paso 3: Crear un handler para la excepción

```python
# main.py

from utils.dependencies import RedirectException

@app.exception_handler(RedirectException)
async def redirect_exception_handler(request: Request, exc: RedirectException):
    """Maneja las excepciones de redirección"""
    return RedirectResponse(url=exc.url, status_code=exc.status_code)
```

---

## 🔄 Cómo Funciona

```
┌─────────────────────────────────────────────────────────────┐
│                    FLUJO DE EJECUCIÓN                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Usuario intenta acceder a /alumnos                      │
│     ↓                                                        │
│  2. FastAPI ejecuta la dependencia require_auth()           │
│     ↓                                                        │
│  3. require_auth verifica si hay sesión                     │
│     ↓                                                        │
│  4. ❌ No hay sesión                                        │
│     ↓                                                        │
│  5. Lanza RedirectException("/auth/login")                  │
│     ↓                                                        │
│  6. FastAPI captura la excepción                            │
│     ↓                                                        │
│  7. Ejecuta redirect_exception_handler()                    │
│     ↓                                                        │
│  8. ✅ Redirige al usuario a /auth/login                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Otras Soluciones Posibles

### Opción 1: Usar HTTPException (Para APIs REST)

```python
from fastapi import HTTPException, status

def require_auth(request: Request) -> dict:
    usuario = obtener_usuario_actual(request)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No autenticado"
        )
    return usuario
```

**Ventajas**: Estándar de FastAPI
**Desventajas**: Devuelve JSON, no redirige (malo para web tradicional)

---

### Opción 2: Middleware Global

```python
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    # Lista de rutas protegidas
    protected_routes = ["/alumnos", "/borrar", "/insert_alumnos"]
    
    if request.url.path in protected_routes:
        usuario = obtener_usuario_actual(request)
        if not usuario:
            return RedirectResponse(url="/auth/login", status_code=303)
    
    return await call_next(request)
```

**Ventajas**: No necesita excepción personalizada
**Desventajas**: Menos flexible, difícil de mantener

---

### Opción 3: Verificación manual en cada ruta (Lo que teníamos antes)

```python
@app.get("/alumnos")
async def alumnos(request: Request):
    usuario = obtener_usuario_actual(request)
    if not usuario:
        return RedirectResponse(url="/auth/login", status_code=303)
    # ... resto del código
```

**Ventajas**: Simple, directo
**Desventajas**: Código repetido (DRY violation)

---

## ✅ Por qué la Solución con Excepción Personalizada es la Mejor

| Característica | HTTPException | Middleware | Manual | RedirectException ✅ |
|----------------|--------------|------------|--------|---------------------|
| **Reutilizable** | ✅ | ✅ | ❌ | ✅ |
| **Redirige** | ❌ | ✅ | ✅ | ✅ |
| **Flexible** | ✅ | ❌ | ❌ | ✅ |
| **Type-safe** | ✅ | ❌ | ✅ | ✅ |
| **Testeable** | ✅ | ❌ | ✅ | ✅ |
| **DRY** | ✅ | ✅ | ❌ | ✅ |

---

## 🎓 Resumen

### Archivos modificados:

1. **`utils/dependencies.py`**
   - Creada clase `RedirectException`
   - Modificada función `require_auth()` para usar la excepción

2. **`main.py`**
   - Importada `RedirectException`
   - Agregado `@app.exception_handler(RedirectException)`

### Resultado:

✅ Las dependencias ahora pueden redirigir correctamente
✅ El código sigue siendo limpio y reutilizable
✅ Funciona igual que antes, pero sin errores

---

## 💡 Uso

```python
# Ruta protegida
@app.get("/admin")
async def admin(usuario: dict = Depends(require_auth)):
    # Si no está autenticado → Automáticamente redirige a /auth/login
    # Si está autenticado → Continúa normalmente
    return {"mensaje": f"Hola {usuario['username']}"}
```

---

¡Problema resuelto! 🎉
