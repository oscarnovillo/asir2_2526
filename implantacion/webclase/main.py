from typing import Annotated
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from typing import Optional
from data.database import database
from data.alumno_repository import AlumnoRepository
from domain.model.Alumno import Alumno
from utils.dependencies import require_auth
from routers import auth_router, juego_router


import uvicorn

# Crear la aplicación FastAPI
app = FastAPI(title="Mi Primera Web FastAPI", description="Ejemplo básico con Jinja2")

# ⭐ IMPORTANTE: Agregar el middleware de sesiones
# Cámbiala clave secreta en producción
app.add_middleware(
    SessionMiddleware,
    secret_key="tu_clave_secreta_muy_segura_cambiala_en_produccion",
    session_cookie="session",
    max_age=3600 * 24 * 7,  # 7 días
    same_site="lax",
    https_only=False  # Cambiar a True en producción con HTTPS
)

# Configurar las plantillas
templates = Jinja2Templates(directory="templatesitos")

# Configurar archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir el router de autenticación
app.include_router(auth_router.router)
app.include_router(juego_router.juego_router)



#RUTA RAIZ
@app.get("/")
async def inicio(request: Request, usuario: dict = Depends(require_auth)):
    """Página de inicio - Requiere autenticación"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "usuario": usuario
    })

# RUTA INSERTAR
@app.post("/do_insertar_alumno")
async def do_insertar_alumnos(
    request: Request,
    nombre: Annotated[str, Form()] = None,
    usuario: dict = Depends(require_auth)
):
    """Inserta un alumno - Requiere autenticación"""
    alumnos_repo = AlumnoRepository()
    alumno = Alumno(0, nombre)
    alumnos_repo.insertar_alumno(database, alumno)

    return templates.TemplateResponse("do_insert_alumnos.html", {
        "request": request,
        "usuario": usuario
    })


# RUTA INSERTAR
@app.get("/insert_alumnos")
async def insert_alumnos(request: Request, usuario: dict = Depends(require_auth)):
    """Formulario para insertar alumno - Requiere autenticación"""
    return templates.TemplateResponse("insert_alumnos.html", {
        "request": request,
        "usuario": usuario
    })


# RUTA Borrar
@app.get("/borrar")
async def borrar_alumnos(request: Request, usuario: dict = Depends(require_auth)):
    """Formulario para borrar alumnos - Requiere autenticación"""
    alumnos_repo = AlumnoRepository()
    alumnos = alumnos_repo.get_all(database)

    return templates.TemplateResponse("borrar_alumnos.html", {
        "request": request,
        "alumnos": alumnos,
        "usuario": usuario
    })



# RUTA BORRAR
@app.post("/do_borrar_alumno")
async def do_borrar_alumno(
    request: Request,
    id: Annotated[str, Form()],
    usuario: dict = Depends(require_auth)
):
    """Borra un alumno - Requiere autenticación"""
    alumnos_repo = AlumnoRepository()
    alumnos_repo.borrar_alumno(database, int(id))

    return templates.TemplateResponse("do_borrar_alumnos.html", {
        "request": request,
        "usuario": usuario
    })



# RUTAS GET
@app.get("/alumnos", response_class=HTMLResponse)
async def alumnos(request: Request, usuario: dict = Depends(require_auth)):
    """Lista de alumnos - Requiere autenticación"""
    alumnos_repo = AlumnoRepository()
    alumnos = alumnos_repo.get_all(database)

    return templates.TemplateResponse("alumnos.html", {
        "request": request,
        "alumnos": alumnos,
        "usuario": usuario
    })


@app.get("/naruto", response_class=HTMLResponse)
async def naruto(request: Request,
                 numero: int,
                 operacion: str,
                 var: str = "hola"):
    """Página de navegación con enlaces"""
    num = int(var) + 10
    for i in range(5):
        num = num + 10     

    num = int(var) + numero
    mensaje: str = "Bienvenido al mundo de tuputamdare"


    return templates.TemplateResponse("naruto.html", 
                                      {"request": request, 
                                       "montoya": mensaje,
                                       "var": num})



@app.get("/pagina", response_class=HTMLResponse)
async def deotramanera(request: Request):
    x= 9
    y= 5
    z= x + y
    return templates.TemplateResponse("pagina.html", {
        "request": request, 
        "nombre": "Óscar",
        "edad": 30,
        "resultado": z,
    })

@app.get("/c", response_class=HTMLResponse)
async def deotramanera(request: Request,
                       num1: Optional[str] = None,
                       num2: Optional[str] = None,
                       op : Optional[str] = None):
    error = None
    resultado = None
    operacion = None
    if (num1  and num2 ):
        if (num1.isdigit() and num2.isdigit()):
            if op == "s":
                resultado= int(num1) + int(num2)
                operacion = "+"
            elif op == "r":
                resultado= int(num1) - int(num2)
                operacion = "-"
            elif op == "m":
                resultado= int(num1) * int(num2)
                operacion = "*"
            elif op == "d":
                if int(num2) == 0:
                    error = "Error: División por cero"
                else:
                    resultado= int(num1) / int(num2)
                    operacion = "/"
            else:
                error = "Operación no válida"
        else:
            error = "Los parámetros num1 y num2 deben ser números enteros"
    else:
        error = "Faltan parámetros num1 o num2"

    return templates.TemplateResponse("calculadora.html", {
        "request": request, 
        "num1":num1,
        "num2": num2,
        "resultado": resultado,
        "operacion": operacion,
        "error": error
    })




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
