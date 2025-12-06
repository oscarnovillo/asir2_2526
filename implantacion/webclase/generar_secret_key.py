"""
Script para generar una clave secreta segura para producción
Ejecutar: python generar_secret_key.py
"""

import secrets

def generar_secret_key():
    """Genera una clave secreta criptográficamente segura"""
    # Genera 32 bytes aleatorios y los convierte a hexadecimal
    secret_key = secrets.token_hex(32)
    
    print("=" * 70)
    print("🔐 CLAVE SECRETA GENERADA PARA PRODUCCIÓN")
    print("=" * 70)
    print()
    print("Tu nueva clave secreta es:")
    print()
    print(f"    {secret_key}")
    print()
    print("=" * 70)
    print()
    print("📝 Cómo usarla:")
    print()
    print("1. Copia la clave de arriba")
    print("2. Abre el archivo 'main.py'")
    print("3. Reemplaza esta línea:")
    print('   secret_key="tu_clave_secreta_muy_segura_cambiala_en_produccion"')
    print()
    print("   Por:")
    print(f'   secret_key="{secret_key}"')
    print()
    print("=" * 70)
    print()
    print("⚠️  IMPORTANTE:")
    print("   - NO compartas esta clave con nadie")
    print("   - NO la subas a GitHub o repositorios públicos")
    print("   - Guárdala en variables de entorno o archivos .env")
    print("   - Cada entorno (dev/prod) debe tener su propia clave")
    print()
    print("💡 Alternativa profesional (usando variable de entorno):")
    print()
    print("   En PowerShell:")
    print(f'   $env:SECRET_KEY="{secret_key}"')
    print()
    print("   En main.py:")
    print('   import os')
    print('   secret_key = os.getenv("SECRET_KEY", "clave_por_defecto_solo_dev")')
    print()
    print("=" * 70)

if __name__ == "__main__":
    generar_secret_key()
