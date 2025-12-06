"""
Script de prueba para las dependencias refactorizadas con TemplateResponse

Crear rutas de prueba en main.py para verificar el correcto funcionamiento
de las dependencias de roles con la nueva plantilla 403.html
"""

# Agregar estas rutas de prueba a main.py:

"""
# ========== RUTAS DE PRUEBA - DEPENDENCIES ==========

@app.get("/test/admin")
async def test_admin(request: Request, usuario: dict = Depends(require_admin)):
    '''Prueba require_admin - Solo admin y superadmin'''
    return templates.TemplateResponse("base.html", {
        "request": request,
        "usuario": usuario,
        "contenido": f"✅ Acceso concedido a: {usuario['username']}<br>Rol: {usuario.get('role', 'sin rol')}"
    })

@app.get("/test/superadmin")
async def test_superadmin(request: Request, usuario: dict = Depends(require_superadmin)):
    '''Prueba require_superadmin - Solo superadmin'''
    return templates.TemplateResponse("base.html", {
        "request": request,
        "usuario": usuario,
        "contenido": f"✅ Acceso concedido al SUPER ADMIN: {usuario['username']}"
    })

@app.get("/test/teacher")
async def test_teacher(request: Request, usuario: dict = Depends(require_role("teacher"))):
    '''Prueba require_role con rol específico'''
    return templates.TemplateResponse("base.html", {
        "request": request,
        "usuario": usuario,
        "contenido": f"✅ Acceso concedido al profesor: {usuario['username']}"
    })

@app.get("/test/staff")
async def test_staff(request: Request, usuario = Depends(require_any_role("teacher", "admin", "coordinator"))):
    '''Prueba require_any_role con múltiples roles'''
    return templates.TemplateResponse("base.html", {
        "request": request,
        "usuario": usuario,
        "contenido": f"✅ Acceso concedido al staff: {usuario['username']}<br>Rol: {usuario.get('role')}"
    })

# ========== FIN RUTAS DE PRUEBA ==========
"""

# ========================================
# CASOS DE PRUEBA MANUALES
# ========================================

TEST_CASES = """
## 📋 CASOS DE PRUEBA MANUAL

### Setup:
1. Crear usuarios con diferentes roles en la BD:
   ```sql
   -- Usuario admin
   UPDATE usuarios SET role = 'admin' WHERE username = 'admin';
   
   -- Usuario superadmin
   UPDATE usuarios SET role = 'superadmin' WHERE username = 'superadmin';
   
   -- Usuario teacher
   INSERT INTO usuarios (username, password_hash, email, role) 
   VALUES ('teacher1', '$2b$12$...', 'teacher@test.com', 'teacher');
   
   -- Usuario student (sin permisos)
   INSERT INTO usuarios (username, password_hash, email, role) 
   VALUES ('student1', '$2b$12$...', 'student@test.com', 'student');
   ```

2. Iniciar servidor:
   ```bash
   uvicorn main:app --reload
   ```

---

### TEST 1: require_admin
**URL**: http://localhost:8000/test/admin

| Usuario | Rol | Resultado Esperado |
|---------|-----|-------------------|
| admin | admin | ✅ Acceso concedido |
| superadmin | superadmin | ✅ Acceso concedido |
| teacher1 | teacher | ❌ 403 con 🔒 y mensaje "Requiere Administrador" |
| student1 | student | ❌ 403 con 🔒 y mensaje "Requiere Administrador" |
| (sin login) | - | ↩️ Redirige a /auth/login |

**Verificar**:
- Icono mostrado: 🔒
- Mensaje: "Esta página requiere permisos de Administrador"
- Roles permitidos: "admin, superadmin"
- Tu rol actual: Se muestra correctamente

---

### TEST 2: require_superadmin
**URL**: http://localhost:8000/test/superadmin

| Usuario | Rol | Resultado Esperado |
|---------|-----|-------------------|
| superadmin | superadmin | ✅ Acceso concedido |
| admin | admin | ❌ 403 con 👑 y mensaje "Requiere Super Administrador" |
| teacher1 | teacher | ❌ 403 con 👑 |
| student1 | student | ❌ 403 con 👑 |
| (sin login) | - | ↩️ Redirige a /auth/login |

**Verificar**:
- Icono mostrado: 👑
- Mensaje: "Esta página requiere permisos de Super Administrador"
- Rol requerido: "Solo el super administrador tiene acceso"

---

### TEST 3: require_role("teacher")
**URL**: http://localhost:8000/test/teacher

| Usuario | Rol | Resultado Esperado |
|---------|-----|-------------------|
| teacher1 | teacher | ✅ Acceso concedido |
| admin | admin | ❌ 403 con 🚫 y "Se requiere rol: teacher" |
| superadmin | superadmin | ❌ 403 con 🚫 |
| student1 | student | ❌ 403 con 🚫 |
| (sin login) | - | ↩️ Redirige a /auth/login |

**Verificar**:
- Icono mostrado: 🚫
- Mensaje: "No tienes permisos suficientes..."
- Rol requerido: "Se requiere rol: teacher"

---

### TEST 4: require_any_role("teacher", "admin", "coordinator")
**URL**: http://localhost:8000/test/staff

| Usuario | Rol | Resultado Esperado |
|---------|-----|-------------------|
| teacher1 | teacher | ✅ Acceso concedido |
| admin | admin | ✅ Acceso concedido |
| superadmin | superadmin | ❌ 403 con ⚠️ y "Roles permitidos: teacher, admin, coordinator" |
| student1 | student | ❌ 403 con ⚠️ |
| (sin login) | - | ↩️ Redirige a /auth/login |

**Verificar**:
- Icono mostrado: ⚠️
- Mensaje: "No tienes permisos suficientes..."
- Roles permitidos: "teacher, admin, coordinator"

---

### TEST 5: Diseño de página 403
Acceder a cualquier ruta protegida sin permisos y verificar:

✅ **Layout**:
- Fondo degradado morado
- Caja blanca centrada con sombra
- Animación de entrada suave

✅ **Contenido dinámico**:
- Icono correcto según dependencia
- Mensaje personalizado
- Rol requerido visible
- Tu rol actual visible (en caja azul)

✅ **Botones**:
- "🏠 Volver al Inicio" → href="/"
- "← Página Anterior" → javascript:history.back()
- Hover effects funcionando

✅ **Responsividad**:
- Probar en móvil (Chrome DevTools)
- Probar en tablet
- Probar en desktop

---

### TEST 6: Edge Cases

#### Sin rol asignado
```python
# Usuario sin campo role o role = NULL
usuario = {"user_id": 1, "username": "norol"}
```
**Resultado esperado**: "Tu rol actual: sin rol"

#### Rol inválido/desconocido
```python
usuario = {"user_id": 1, "username": "test", "role": "unknown"}
```
**Resultado esperado**: Página 403 con "Tu rol actual: unknown"

#### Request faltante (prueba de error)
```python
# Si accidentalmente olvidas Request en la ruta
@app.get("/test/error")
async def test_error(usuario = Depends(require_admin)):
    return {"message": "test"}
```
**Resultado esperado**: 
```
TypeError: role_checker() missing 1 required positional argument: 'request'
```

---

## 🎯 CHECKLIST DE VALIDACIÓN

- [ ] TEST 1: require_admin funciona correctamente
- [ ] TEST 2: require_superadmin funciona correctamente
- [ ] TEST 3: require_role funciona correctamente
- [ ] TEST 4: require_any_role funciona correctamente
- [ ] TEST 5: Diseño de página 403 correcto
- [ ] TEST 6: Edge cases manejados
- [ ] Todos los iconos se muestran correctamente
- [ ] Mensajes personalizados aparecen
- [ ] Roles requeridos y actuales se muestran
- [ ] Botones de navegación funcionan
- [ ] Sin errores en consola del servidor
- [ ] Sin errores en consola del navegador
- [ ] Animaciones CSS funcionan
- [ ] Responsive design funciona

---

## 🐛 DEBUGGING

Si algo no funciona:

### 1. Verificar imports en dependencies.py
```python
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
```

### 2. Verificar inicialización de templates
```python
templates = Jinja2Templates(directory="templatesitos")
```

### 3. Verificar que 403.html existe
```bash
ls templatesitos/403.html
```

### 4. Verificar sintaxis de Jinja2 en 403.html
```html
{{ icon | default('🚫') }}
{{ message | default('...') }}
{% if required_role %}...{% endif %}
{% if current_role %}...{% endif %}
```

### 5. Ver errores en terminal del servidor
```bash
# Errores de sintaxis Python
# Errores de template Jinja2
# Errores de dependencias
```

### 6. Inspeccionar Response en navegador
- F12 → Network → Click en request
- Ver Status Code (debe ser 403)
- Ver HTML response
- Ver si tiene los datos dinámicos

---

## 📊 RESULTADOS ESPERADOS

| Aspecto | Antes | Después |
|---------|-------|---------|
| **HTML inline** | ✅ 100+ líneas x4 | ❌ Eliminado |
| **TemplateResponse** | ❌ No usado | ✅ Usado |
| **Plantilla única** | ❌ No | ✅ 403.html |
| **Iconos personalizados** | ❌ No | ✅ Por rol |
| **Rol actual visible** | ❌ No | ✅ Sí |
| **Mantenibilidad** | ⚠️ Baja | ✅ Alta |
| **Código limpio** | ⚠️ Duplicado | ✅ DRY |

---

## 🎉 ÉXITO SI:

✅ Todas las rutas de prueba funcionan
✅ Página 403 se ve bonita y profesional
✅ Iconos correctos según dependencia
✅ Mensajes dinámicos aparecen
✅ Rol actual se muestra
✅ No hay errores en logs
✅ Código más limpio y mantenible

---

"""

print(TEST_CASES)

# ========================================
# SCRIPT PARA CREAR USUARIOS DE PRUEBA
# ========================================

CREATE_TEST_USERS = """
-- Script SQL para crear usuarios de prueba

-- 1. Agregar columna role si no existe
ALTER TABLE usuarios ADD COLUMN role VARCHAR(50) DEFAULT 'user';

-- 2. Crear índice en role
CREATE INDEX idx_usuarios_role ON usuarios(role);

-- 3. Asignar roles a usuarios existentes
UPDATE usuarios SET role = 'admin' WHERE username = 'admin';
UPDATE usuarios SET role = 'superadmin' WHERE username = 'superadmin';

-- 4. Crear usuarios de prueba (ajustar hash de password)
INSERT INTO usuarios (username, password_hash, email, role) 
VALUES 
    ('teacher1', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5NU7TLFdRDgVe', 'teacher@test.com', 'teacher'),
    ('student1', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5NU7TLFdRDgVe', 'student@test.com', 'student'),
    ('coordinator1', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5NU7TLFdRDgVe', 'coord@test.com', 'coordinator');

-- Nota: Todos los usuarios de prueba tienen password: "test123"
-- Generar nuevo hash: python -c "import bcrypt; print(bcrypt.hashpw('test123'.encode(), bcrypt.gensalt()).decode())"
"""

print("\n\n=== SQL PARA CREAR USUARIOS DE PRUEBA ===")
print(CREATE_TEST_USERS)

if __name__ == "__main__":
    print("\n✅ Guía de pruebas generada")
    print("\n📝 Pasos siguientes:")
    print("1. Agregar rutas de prueba a main.py")
    print("2. Ejecutar script SQL para crear usuarios")
    print("3. Iniciar servidor: uvicorn main:app --reload")
    print("4. Probar cada ruta con diferentes usuarios")
    print("5. Verificar que página 403 se vea correcta")
    print("\n🎯 Ver TEST_CASES arriba para casos de prueba detallados")
