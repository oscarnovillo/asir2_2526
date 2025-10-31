from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
from data.database import database
from data.alumno_repository import AlumnoRepository

import uvicorn

# Crear la aplicación FastAPI
app = FastAPI(title="Mi Primera Web FastAPI", description="Ejemplo básico con Jinja2")

# Configurar las plantillas
templates = Jinja2Templates(directory="templatesitos")

# Configurar archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")


# RUTAS GET
@app.get("/alumnos", response_class=HTMLResponse)
async def alumnos(request: Request):
    """Página de navegación con enlaces"""
    alumnos_repo = AlumnoRepository()
    alumnos = alumnos_repo.get_all(database)

    return templates.TemplateResponse("alumnos.html", {"request": request,
                                                       "alumnos": alumnos})


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


@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    """Página de inicio"""
    return templates.TemplateResponse("inicio.html", {
        "request": request, 
        "titulo": "Bienvenido a FastAPI",
        "mensaje": "Esta es tu primera aplicación web con FastAPI y Jinja2"
    })

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
