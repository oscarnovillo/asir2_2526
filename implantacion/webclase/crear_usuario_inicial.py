"""
Script para crear un usuario inicial en la base de datos
Ejecutar: python crear_usuario_inicial.py
"""

from data.database import database
from data.usuario_repository import UsuarioRepository

def crear_usuario_admin():
    """Crea un usuario administrador inicial"""
    usuario_repo = UsuarioRepository()
    
    # Verificar si ya existe un usuario admin
    usuario_existente = usuario_repo.get_by_username(database, "admin")
    
    if usuario_existente:
        print("❌ El usuario 'admin' ya existe en la base de datos.")
        return
    
    # Crear el usuario
    try:
        usuario_repo.insertar_usuario(
            database, 
            username="admin", 
            password="admin123",
            email="admin@example.com"
        )
        print("✅ Usuario 'admin' creado exitosamente!")
        print("   Username: admin")
        print("   Password: admin123")
        print("\n⚠️  IMPORTANTE: Cambia esta contraseña después del primer inicio de sesión.")
    except Exception as e:
        print(f"❌ Error al crear el usuario: {e}")

if __name__ == "__main__":
    print("=== Creación de Usuario Inicial ===\n")
    crear_usuario_admin()
