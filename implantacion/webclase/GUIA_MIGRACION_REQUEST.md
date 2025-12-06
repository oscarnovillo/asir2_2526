# 📝 Guía de Migración: Actualizar Rutas con Dependencias de Roles

## ⚠️ Cambio Requerido

Después de la refactorización a `TemplateResponse`, todas las rutas que usen dependencias de roles **deben incluir `request: Request`** como parámetro.

---

## 🔄 Ejemplos de Migración

### ❌ ANTES (sin Request)

```python
@app.get("/admin")
async def admin_page(usuario: dict = Depends(require_admin)):
    return {"message": f"Hola {usuario['username']}"}

@app.get("/superadmin")
async def superadmin_page(usuario: dict = Depends(require_superadmin)):
    return {"message": "Panel de super admin"}

@app.get("/teacher/dashboard")
async def teacher_dashboard(usuario: dict = Depends(require_role("teacher"))):
    return {"message": "Dashboard del profesor"}

@app.get("/staff")
async def staff_area(usuario = Depends(require_any_role("teacher", "admin"))):
    return {"message": "Área de staff"}
```

---

### ✅ AHORA (con Request)

```python
from fastapi import Request

@app.get("/admin")
async def admin_page(
    request: Request,
    usuario: dict = Depends(require_admin)
):
    return {"message": f"Hola {usuario['username']}"}

@app.get("/superadmin")
async def superadmin_page(
    request: Request,
    usuario: dict = Depends(require_superadmin)
):
    return {"message": "Panel de super admin"}

@app.get("/teacher/dashboard")
async def teacher_dashboard(
    request: Request,
    usuario: dict = Depends(require_role("teacher"))
):
    return {"message": "Dashboard del profesor"}

@app.get("/staff")
async def staff_area(
    request: Request,
    usuario = Depends(require_any_role("teacher", "admin"))
):
    return {"message": "Área de staff"}
```

---

## 🔍 Dependencias Afectadas

Las siguientes dependencias **requieren Request**:

| Dependencia | Requiere Request | Motivo |
|------------|------------------|--------|
| `require_auth` | ❌ No | Redirige a login (no usa templates) |
| `optional_auth` | ❌ No | Solo retorna usuario o None |
| `require_admin` | ✅ **Sí** | Usa TemplateResponse para error 403 |
| `require_superadmin` | ✅ **Sí** | Usa TemplateResponse para error 403 |
| `require_role()` | ✅ **Sí** | Usa TemplateResponse para error 403 |
| `require_any_role()` | ✅ **Sí** | Usa TemplateResponse para error 403 |

---

## 📋 Checklist de Migración

Para cada ruta que use dependencias de roles:

- [ ] Verificar si usa `require_admin`, `require_superadmin`, `require_role()` o `require_any_role()`
- [ ] Importar `Request` de `fastapi`
- [ ] Agregar `request: Request` como **primer parámetro** después de `self` (si es método de clase)
- [ ] Mantener las dependencias en `Depends()`
- [ ] Probar la ruta accediendo sin permisos (debe mostrar página 403 bonita)
- [ ] Probar la ruta con permisos correctos (debe funcionar normal)

---

## 🎯 Ejemplos Completos por Caso de Uso

### 1. Ruta con TemplateResponse

```python
@app.get("/admin/dashboard")
async def admin_dashboard(
    request: Request,  # ✅ Agregado
    usuario: dict = Depends(require_admin)
):
    # Renderizar plantilla
    return templates.TemplateResponse("admin_dashboard.html", {
        "request": request,
        "usuario": usuario,
        "stats": get_admin_stats()
    })
```

---

### 2. Ruta con JSON Response

```python
@app.get("/api/admin/users")
async def get_admin_users(
    request: Request,  # ✅ Agregado (necesario para dependencia)
    usuario: dict = Depends(require_admin)
):
    # Retornar JSON
    users = get_all_users()
    return {"users": users}
```

**Nota**: Aunque retornes JSON, **necesitas Request** porque la dependencia lo usa para renderizar el error 403.

---

### 3. Ruta con Factory `require_role()`

```python
@app.get("/teacher/classes")
async def teacher_classes(
    request: Request,  # ✅ Agregado
    usuario: dict = Depends(require_role("teacher"))
):
    classes = get_teacher_classes(usuario["user_id"])
    return {"classes": classes}
```

---

### 4. Ruta con Múltiples Roles

```python
@app.get("/staff/reports")
async def staff_reports(
    request: Request,  # ✅ Agregado
    usuario = Depends(require_any_role("teacher", "admin", "coordinator"))
):
    reports = generate_reports()
    return {"reports": reports}
```

---

### 5. Ruta con Otros Parámetros

```python
from fastapi import Query

@app.get("/admin/search")
async def admin_search(
    request: Request,  # ✅ Siempre primero
    query: str = Query(...),  # Luego otros parámetros
    usuario: dict = Depends(require_admin)  # Dependencias al final
):
    results = search_users(query)
    return {"results": results}
```

**Orden recomendado**:
1. `request: Request`
2. Path parameters
3. Query parameters
4. Body parameters
5. Dependencies (`Depends()`)

---

### 6. Ruta con Form Data

```python
from fastapi import Form

@app.post("/admin/users/create")
async def create_user(
    request: Request,  # ✅ Siempre primero
    username: str = Form(...),
    email: str = Form(...),
    usuario: dict = Depends(require_admin)  # Dependencias al final
):
    new_user = create_new_user(username, email)
    return {"user": new_user}
```

---

## 🚨 Errores Comunes

### Error 1: Olvidar Request
```python
# ❌ Error
@app.get("/admin")
async def admin_page(usuario = Depends(require_admin)):
    return {"message": "Hola"}
```

**Error al ejecutar**:
```
TypeError: role_checker() missing 1 required positional argument: 'request'
```

**Solución**: Agregar `request: Request`
```python
# ✅ Correcto
@app.get("/admin")
async def admin_page(request: Request, usuario = Depends(require_admin)):
    return {"message": "Hola"}
```

---

### Error 2: Request en orden incorrecto
```python
# ❌ Error
@app.get("/admin/{user_id}")
async def admin_user(
    user_id: int,
    usuario = Depends(require_admin),
    request: Request  # ❌ Request debe ir primero
):
    return {"user_id": user_id}
```

**Solución**: Poner Request primero
```python
# ✅ Correcto
@app.get("/admin/{user_id}")
async def admin_user(
    request: Request,  # ✅ Primero
    user_id: int,
    usuario = Depends(require_admin)
):
    return {"user_id": user_id}
```

---

### Error 3: Confundir con require_auth
```python
# ❌ Innecesario (require_auth NO necesita Request)
@app.get("/profile")
async def profile(request: Request, usuario = Depends(require_auth)):
    return {"usuario": usuario}

# ✅ Correcto (require_auth no usa templates)
@app.get("/profile")
async def profile(usuario = Depends(require_auth)):
    return {"usuario": usuario}
```

**Excepción**: Si tu ruta **por otro motivo** necesita `request`, entonces inclúyelo:
```python
# ✅ También válido
@app.get("/profile")
async def profile(request: Request, usuario = Depends(require_auth)):
    # Usar request para algo más
    return templates.TemplateResponse("profile.html", {
        "request": request,
        "usuario": usuario
    })
```

---

## 🔧 Herramienta de Búsqueda

Para encontrar rutas que necesiten actualización:

### Buscar en tu código:
```bash
# Buscar rutas con require_admin sin Request
grep -n "Depends(require_admin)" *.py | grep -v "request: Request"

# Buscar rutas con require_superadmin sin Request
grep -n "Depends(require_superadmin)" *.py | grep -v "request: Request"

# Buscar rutas con require_role sin Request
grep -n "Depends(require_role" *.py | grep -v "request: Request"

# Buscar rutas con require_any_role sin Request
grep -n "Depends(require_any_role" *.py | grep -v "request: Request"
```

O con Python:
```python
import re
import os

def find_routes_to_update(directory="."):
    patterns = [
        r'Depends\(require_admin\)',
        r'Depends\(require_superadmin\)',
        r'Depends\(require_role\(',
        r'Depends\(require_any_role\(',
    ]
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                for pattern in patterns:
                    if re.search(pattern, content):
                        # Verificar si tiene Request
                        if 'request: Request' not in content:
                            print(f"⚠️  {filepath} - Usa {pattern} sin Request")
```

---

## 📝 Script de Migración Automática (Regex)

**Advertencia**: Revisar manualmente después de aplicar.

```python
import re

def add_request_parameter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Patrón: función con dependencia de rol pero sin Request
    pattern = r'(async def \w+\()(\w+: [\w\[\]]+[, ]*)'
    
    def replacer(match):
        func_def = match.group(1)
        params = match.group(2)
        
        # Si ya tiene request, no hacer nada
        if 'request: Request' in params:
            return match.group(0)
        
        # Si usa dependencia de rol, agregar request
        if any(dep in content for dep in ['require_admin', 'require_superadmin', 'require_role', 'require_any_role']):
            return f"{func_def}request: Request, {params}"
        
        return match.group(0)
    
    new_content = re.sub(pattern, replacer, content)
    
    # Asegurar que Request esté importado
    if 'from fastapi import' in new_content and 'Request' not in new_content:
        new_content = new_content.replace(
            'from fastapi import',
            'from fastapi import Request,'
        )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

# Usar con precaución
# add_request_parameter('main.py')
```

---

## ✅ Validación Post-Migración

Después de actualizar las rutas:

### 1. Verificar sintaxis
```bash
python -m py_compile main.py
python -m py_compile routers/*.py
```

### 2. Ejecutar servidor
```bash
uvicorn main:app --reload
```

### 3. Probar cada ruta protegida
- Acceder sin sesión → Redirige a login ✅
- Acceder con sesión pero sin rol → Muestra página 403 bonita ✅
- Acceder con rol correcto → Funciona normal ✅

### 4. Verificar logs
```bash
# No debe haber errores de tipo:
# TypeError: ... missing 1 required positional argument: 'request'
```

---

## 📚 Referencia Rápida

```python
# ✅ SIEMPRE INCLUIR REQUEST EN:
require_admin
require_superadmin
require_role()
require_any_role()

# ❌ NO ES NECESARIO EN:
require_auth
optional_auth

# 📝 SINTAXIS:
async def ruta(
    request: Request,          # 1. Request primero (si es necesario)
    path_param: int,           # 2. Path params
    query_param: str = None,   # 3. Query params
    form_data: str = Form(),   # 4. Form/Body
    usuario = Depends(...)     # 5. Dependencies último
):
    pass
```

---

**Fecha**: 2024
**Versión**: 1.0
**Estado**: ✅ Guía Completa
