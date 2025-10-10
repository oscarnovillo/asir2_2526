#!/usr/bin/env python3
"""
CRUD de Series de TV
Aplicación con arquitectura de capas y persistencia en memoria
"""

import sys
import os

# Agregar el directorio raíz al path para importaciones
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.main import MenuCRUD

def main():
    """Función principal de la aplicación"""
    print("🎬 Iniciando CRUD de Series de TV...")
    print("📁 Usando persistencia en memoria con arquitectura de capas\n")
    
    menu = MenuCRUD()
    try:
        menu.ejecutar()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()

