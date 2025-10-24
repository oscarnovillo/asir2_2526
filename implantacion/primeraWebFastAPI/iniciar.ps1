# Script PowerShell para iniciar la aplicación FastAPI

Write-Host "🚀 Iniciando Mi Primera Web FastAPI..." -ForegroundColor Green
Write-Host ""

# Verificar si Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Error: Python no está instalado o no está en el PATH" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "📋 Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencias instaladas correctamente" -ForegroundColor Green
} else {
    Write-Host "❌ Error instalando dependencias" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🌐 Iniciando servidor FastAPI..." -ForegroundColor Yellow
Write-Host ""
Write-Host "💡 La aplicación estará disponible en: http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "🛑 Para detener el servidor presiona Ctrl+C" -ForegroundColor Cyan
Write-Host ""

# Iniciar la aplicación
python main.py
