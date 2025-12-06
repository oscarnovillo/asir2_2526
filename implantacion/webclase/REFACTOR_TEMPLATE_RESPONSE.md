# 🔄 Refactorización: TemplateResponse en Dependencies

## 📌 Objetivo
Reemplazar el HTML hardcodeado inline en las dependencias de roles por `TemplateResponse` usando la plantilla `403.html`.

## ✅ Cambios Realizados

### 1. **Plantilla 403.html Actualizada**

**Antes** (valores fijos):
```html
<div class="error-icon">🚫</div>
<h1>Acceso Denegado</h1>
<p class="error-message">
    No tienes los permisos necesarios para acceder a este recurso.
</p>
<div class="required-role">
    <strong>🔐 Permisos requeridos:</strong><br>
    Solo usuarios con rol específico pueden acceder
</div>
```

**Ahora** (valores dinámicos con Jinja2):
```html
<div class="error-icon">{{ icon | default('🚫') }}</div>
<h1>Acceso Denegado</h1>
<p class="error-message">
    {{ message | default('No tienes los permisos necesarios...') }}
</p>

{% if required_role %}
<div class="required-role">
    <strong>🔐 Permisos requeridos:</strong><br>
    {{ required_role }}
</div>
{% endif %}

{% if current_role %}
<div class="info-box">
    🔑 Tu rol actual: <strong>{{ current_role }}</strong>
</div>
{% endif %}
```

**Variables aceptadas**:
- `icon`: Emoji del error (default: 🚫)
- `message`: Mensaje principal de error
- `required_role`: Roles requeridos para acceder
- `current_role`: Rol actual del usuario (opcional)

---

### 2. **Dependencies Refactorizadas**

#### ✅ `require_admin`

**Antes** (HTML inline):
```python
def require_admin(usuario: dict = Depends(require_auth)) -> dict:
    if usuario.get("role") not in ["admin", "superadmin"]:
        from fastapi.responses import HTMLResponse
        html_content = """
        <!DOCTYPE html>
        <html>
        ...100+ líneas de HTML...
        </html>
        """
        return HTMLResponse(content=html_content, status_code=403)
    return usuario
```

**Ahora** (TemplateResponse):
```python
def require_admin(request: Request, usuario: dict = Depends(require_auth)) -> dict:
    """Requiere rol de administrador"""
    if usuario.get("role") not in ["admin", "superadmin"]:
        return templates.TemplateResponse(
            "403.html",
            {
                "request": request,
                "message": "Esta página requiere permisos de Administrador.",
                "required_role": "Roles permitidos: admin, superadmin",
                "current_role": usuario.get("role", "sin rol"),
                "icon": "🔒"
            },
            status_code=403
        )
    return usuario
```

**Beneficios**:
- ✅ Solo 10 líneas vs 60+ líneas
- ✅ Usa plantilla reutilizable
- ✅ Separación de lógica y presentación
- ✅ Fácil de modificar el diseño en un solo lugar

---

#### ✅ `require_superadmin`

```python
def require_superadmin(request: Request, usuario: dict = Depends(require_auth)) -> dict:
    """Requiere rol de super administrador"""
    if usuario.get("role") != "superadmin":
        return templates.TemplateResponse(
            "403.html",
            {
                "request": request,
                "message": "Esta página requiere permisos de Super Administrador.",
                "required_role": "Solo el super administrador tiene acceso",
                "current_role": usuario.get("role", "sin rol"),
                "icon": "👑"
            },
            status_code=403
        )
    return usuario
```

**Icono personalizado**: 👑 para super admin

---

#### ✅ `require_role` (factory)

```python
def require_role(required_role: str):
    """Factory para crear dependencias de roles específicos"""
    def role_checker(request: Request, usuario: dict = Depends(require_auth)) -> dict:
        if usuario.get("role") != required_role:
            return templates.TemplateResponse(
                "403.html",
                {
                    "request": request,
                    "message": f"No tienes permisos suficientes para acceder a esta página.",
                    "required_role": f"Se requiere rol: {required_role}",
                    "current_role": usuario.get("role", "sin rol"),
                    "icon": "🚫"
                },
                status_code=403
            )
        return usuario
    return role_checker
```

---

#### ✅ `require_any_role` (múltiples roles)

```python
def require_any_role(*roles: str):
    """Requiere cualquiera de los roles especificados"""
    def role_checker(request: Request, usuario: dict = Depends(require_auth)) -> dict:
        if usuario.get("role") not in roles:
            roles_text = ", ".join(roles)
            return templates.TemplateResponse(
                "403.html",
                {
                    "request": request,
                    "message": "No tienes permisos suficientes para acceder a esta página.",
                    "required_role": f"Roles permitidos: {roles_text}",
                    "current_role": usuario.get("role", "sin rol"),
                    "icon": "⚠️"
                },
                status_code=403
            )
        return usuario
    return role_checker
```

---

## ⚠️ IMPORTANTE: Request como Parámetro

**CAMBIO CRÍTICO**: Ahora las dependencias de roles **requieren `Request`** como primer parámetro.

### Antes:
```python
@app.get("/admin")
async def admin_page(usuario: dict = Depends(require_admin)):
    return {"message": f"Hola admin {usuario['username']}"}
```

### Ahora:
```python
@app.get("/admin")
async def admin_page(request: Request, usuario: dict = Depends(require_admin)):
    return {"message": f"Hola admin {usuario['username']}"}
```

**¿Por qué?**
- `TemplateResponse` necesita el objeto `request` en su contexto
- Es el estándar de Jinja2Templates en FastAPI

---

## 📊 Resumen de Beneficios

| Aspecto | Antes | Ahora |
|---------|-------|-------|
| **Líneas de código** | ~300 líneas | ~80 líneas |
| **Mantenibilidad** | Cambiar 4 lugares | Cambiar 1 plantilla |
| **Consistencia** | HTML duplicado | Plantilla única |
| **Personalización** | Difícil | Variables dinámicas |
| **Iconos** | Todos iguales | Personalizados por rol |
| **Info usuario** | No mostraba | Muestra rol actual |

---

## 🎨 Iconos por Tipo de Error

| Dependencia | Icono | Significado |
|------------|-------|-------------|
| `require_role` | 🚫 | Prohibido genérico |
| `require_admin` | 🔒 | Bloqueado - Admin |
| `require_superadmin` | 👑 | Corona - Super Admin |
| `require_any_role` | ⚠️ | Advertencia - Roles múltiples |

---

## 📝 Ejemplos de Uso

### Ejemplo 1: Ruta solo para admins
```python
@app.get("/admin/dashboard")
async def admin_dashboard(
    request: Request,
    usuario: dict = Depends(require_admin)
):
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "usuario": usuario
    })
```

**Si accede un usuario sin rol admin**, verá:
- 🔒 Icono de candado
- Mensaje: "Esta página requiere permisos de Administrador"
- Roles permitidos: "admin, superadmin"
- Tu rol actual: "user" (o lo que tenga)

---

### Ejemplo 2: Ruta solo para super admin
```python
@app.get("/superadmin/settings")
async def superadmin_settings(
    request: Request,
    usuario: dict = Depends(require_superadmin)
):
    return {"settings": "..."}
```

**Si accede un admin normal**, verá:
- 👑 Icono de corona
- Mensaje: "Esta página requiere permisos de Super Administrador"
- Rol requerido: "Solo el super administrador tiene acceso"
- Tu rol actual: "admin"

---

### Ejemplo 3: Rol específico personalizado
```python
@app.get("/teacher/classes")
async def teacher_classes(
    request: Request,
    usuario: dict = Depends(require_role("teacher"))
):
    return {"classes": [...]}
```

**Si accede un usuario sin rol teacher**, verá:
- 🚫 Icono de prohibido
- Mensaje: "No tienes permisos suficientes..."
- Rol requerido: "Se requiere rol: teacher"
- Tu rol actual: "student"

---

### Ejemplo 4: Múltiples roles permitidos
```python
@app.get("/staff/resources")
async def staff_resources(
    request: Request,
    usuario: dict = Depends(require_any_role("teacher", "admin", "coordinator"))
):
    return {"resources": [...]}
```

**Si accede un estudiante**, verá:
- ⚠️ Icono de advertencia
- Mensaje: "No tienes permisos suficientes..."
- Roles permitidos: "teacher, admin, coordinator"
- Tu rol actual: "student"

---

## 🔧 Archivos Modificados

1. **`templatesitos/403.html`**
   - Agregadas variables Jinja2: `icon`, `message`, `required_role`, `current_role`
   - Condicionales `{% if %}` para mostrar secciones dinámicamente

2. **`utils/dependencies.py`**
   - Importado `Jinja2Templates`
   - Inicializado `templates = Jinja2Templates(directory="templatesitos")`
   - Refactorizadas todas las dependencias de roles
   - Agregado parámetro `request: Request` en todas las dependencias de roles

---

## ✅ Testing

### Probar cada dependencia:

```python
# En main.py o router de prueba
@app.get("/test/admin")
async def test_admin(request: Request, usuario = Depends(require_admin)):
    return {"message": "Acceso concedido"}

@app.get("/test/superadmin")
async def test_superadmin(request: Request, usuario = Depends(require_superadmin)):
    return {"message": "Acceso concedido"}

@app.get("/test/teacher")
async def test_teacher(request: Request, usuario = Depends(require_role("teacher"))):
    return {"message": "Acceso concedido"}

@app.get("/test/staff")
async def test_staff(request: Request, usuario = Depends(require_any_role("teacher", "admin"))):
    return {"message": "Acceso concedido"}
```

**Probar con usuarios de diferentes roles** para ver cómo se personaliza la página 403.

---

## 🚀 Próximos Pasos

1. **Implementar sistema de roles completo**:
   - [ ] Agregar columna `role` a tabla `usuarios`
   - [ ] Actualizar modelo `Usuario` con campo `role`
   - [ ] Actualizar `usuario_repository.py` para manejar roles
   - [ ] Actualizar sesiones para incluir rol del usuario
   - [ ] Crear script para asignar roles a usuarios existentes

2. **Probar dependencias con usuarios reales**:
   - [ ] Crear usuarios con diferentes roles
   - [ ] Probar todas las rutas protegidas
   - [ ] Verificar que las páginas 403 muestren la info correcta

3. **Documentación adicional**:
   - [ ] Agregar ejemplos de uso en README_AUTH.md
   - [ ] Crear guía de roles y permisos

---

## 📚 Referencias

- [FastAPI TemplateResponse](https://fastapi.tiangolo.com/advanced/templates/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [Dependencies en FastAPI](https://fastapi.tiangolo.com/tutorial/dependencies/)

---

**Fecha**: 2024
**Autor**: Sistema de Autenticación FastAPI
**Estado**: ✅ Completado
