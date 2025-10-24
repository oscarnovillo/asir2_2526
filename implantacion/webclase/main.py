from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
import uvicorn

# Crear la aplicación FastAPI
app = FastAPI(title="Mi Primera Web FastAPI", description="Ejemplo básico con Jinja2")

# Configurar las plantillas
templates = Jinja2Templates(directory="templatesitos")

# Configurar archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")


# RUTAS GET

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
