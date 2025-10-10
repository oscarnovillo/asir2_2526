# CRUD de Series de TV en Python

Este proyecto implementa un sistema CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar series de TV mediante línea de comandos, utilizando **arquitectura de capas** y **persistencia en memoria**.

## Características

- ✅ **Crear** nuevas series con información completa
- 📋 **Listar** todas las series registradas
- 🔍 **Buscar** series por ID, título o género
- ✏️ **Actualizar** información de series existentes
- 🗑️ **Eliminar** series del sistema
- 📊 **Estadísticas** completas del catálogo
- 🏗️ **Arquitectura de capas** (UI, Domain, Data)
- 💾 **Persistencia en memoria** con patrón Repository
- 🎨 **Interfaz** amigable en línea de comandos
- 🔌 **Inyección de dependencias**

## Arquitectura del Proyecto

```
ejemplos/
├── app.py                          # Punto de entrada principal
├── ui/                            # 🎨 Capa de Presentación
│   ├── __init__.py
│   └── main.py                    # Interfaz de usuario y menús
├── domain/                        # 🧠 Capa de Dominio (Lógica de Negocio)
│   ├── __init__.py
│   ├── serie_manager.py           # Servicios de dominio
│   └── model/                     # Modelos del dominio
│       ├── __init__.py
│       └── serie.py               # Entidad Serie
├── data/                          # 💾 Capa de Datos
│   ├── __init__.py
│   └── serie_repository.py        # Repositorio en memoria
└── README.md                      # Documentación
```

## Principios de Arquitectura

### 🏗️ Separación de Capas
- **UI (User Interface)**: Maneja la interacción con el usuario
- **Domain**: Contiene la lógica de negocio y reglas del dominio
- **Data**: Maneja la persistencia y acceso a datos

### 🔌 Patrón Repository
- Encapsula la lógica de acceso a datos
- Separa la persistencia de la lógica de negocio
- Facilita el mantenimiento del código

## Uso

### Ejecutar el programa:
```bash
python app.py
```

### Menú Principal:
1. **Crear nueva serie** - Agregar una serie al catálogo
2. **Listar todas las series** - Mostrar todas las series registradas
3. **Buscar series** - Buscar por ID, título o género
4. **Actualizar serie** - Modificar información de una serie existente
5. **Eliminar serie** - Remover una serie del catálogo
6. **Estadísticas** - Ver estadísticas del catálogo
7. **Salir** - Cerrar el programa

## Funcionalidades Detalladas

### Crear Serie
- Título (obligatorio)
- Género (obligatorio)  
- Número de temporadas (obligatorio, > 0)
- Año de estreno (1900-2030)
- Calificación (0-10, opcional)

### Buscar Series
- **Por ID**: Busca una serie específica
- **Por título**: Busca series que contengan el texto
- **Por género**: Filtra series por género

### Estadísticas
- Total de series registradas
- Calificación promedio
- Total de temporadas
- Serie mejor calificada
- Distribución por géneros

## Ejemplos de Series

Algunas series de ejemplo que puedes agregar:

| Título | Género | Temporadas | Año | Calificación |
|--------|---------|------------|-----|--------------|
| Breaking Bad | Drama | 5 | 2008 | 9.5 |
| The Office | Comedia | 9 | 2005 | 8.8 |
| Game of Thrones | Fantasía | 8 | 2011 | 8.5 |
| Stranger Things | Ciencia Ficción | 4 | 2016 | 8.7 |
| Friends | Comedia | 10 | 1994 | 8.9 |

## Validaciones

El sistema incluye validaciones para:
- Campos obligatorios no vacíos
- Números de temporadas válidos (> 0)
- Años de estreno realistas (1900-2030)
- Calificaciones en rango válido (0-10)
- IDs existentes para operaciones de actualización/eliminación

## Persistencia de Datos

Los datos se mantienen **en memoria** durante la ejecución del programa:
- Las series se inicializan con datos de ejemplo al arrancar
- Los cambios persisten mientras la aplicación esté ejecutándose
- Al cerrar el programa, los datos se pierden (persistencia en memoria)
- Fácilmente extensible para agregar persistencia en archivo, base de datos, etc.

## Extensibilidad

Gracias a la arquitectura por capas, es fácil:
- **Cambiar persistencia**: Modificar `SerieRepositoryInMemory` o crear una nueva clase
- **Cambiar UI**: Reemplazar la capa UI manteniendo el domain y data
- **Agregar validaciones**: Extender los servicios de dominio
- **Testing**: Crear repositorios mock para pruebas

### Ejemplo: Agregar persistencia en JSON
```python
class SerieRepositoryJSON:
    def __init__(self, filename='series.json'):
        self.filename = filename
        # Implementar métodos para JSON
```

## Requisitos

- Python 3.7 o superior (para type hints)
- Módulos estándar de Python (os, sys, typing, abc)
- No requiere instalación de paquetes externos