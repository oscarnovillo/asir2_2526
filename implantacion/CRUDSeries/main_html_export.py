#!/usr/bin/env python3
"""
Exportador HTML para Series de TV
Genera un archivo HTML con una tabla de todas las series
"""

import sys
import os
from datetime import datetime

# Agregar el directorio raíz al path para importaciones
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from domain.serie_manager import SerieManager

def generar_html_series(series, nombre_archivo="series_table.html"):
    """Genera un archivo HTML con una tabla de series"""
    
    # Template HTML con estilos CSS
    html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo de Series de TV</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        h1 {{
            color: #2c3e50;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }}
        
        .subtitle {{
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 30px;
            font-style: italic;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        
        th {{
            background-color: #3498db;
            color: white;
            padding: 15px 10px;
            text-align: left;
            font-weight: bold;
            border-bottom: 2px solid #2980b9;
        }}
        
        td {{
            padding: 12px 10px;
            border-bottom: 1px solid #ecf0f1;
        }}
        
        tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        
        tr:hover {{
            background-color: #e8f4fd;
            transition: background-color 0.3s ease;
        }}
        
        .calificacion {{
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 15px;
            color: white;
        }}
        
        .calificacion.excelente {{
            background-color: #27ae60;
        }}
        
        .calificacion.muy-buena {{
            background-color: #2ecc71;
        }}
        
        .calificacion.buena {{
            background-color: #f39c12;
        }}
        
        .calificacion.regular {{
            background-color: #e67e22;
        }}
        
        .calificacion.mala {{
            background-color: #e74c3c;
        }}
        
        .genero {{
            background-color: #ecf0f1;
            padding: 5px 10px;
            border-radius: 12px;
            font-size: 0.9em;
            color: #2c3e50;
        }}
        
        .stats {{
            margin-top: 30px;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #3498db;
        }}
        
        .stats h3 {{
            color: #2c3e50;
            margin-top: 0;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 30px;
            color: #95a5a6;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎬 Catálogo de Series de TV</h1>
        <p class="subtitle">Generado el {fecha_generacion}</p>
        
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Título</th>
                    <th>Género</th>
                    <th>Temporadas</th>
                    <th>Año de Estreno</th>
                    <th>Calificación</th>
                </tr>
            </thead>
            <tbody>
                {filas_series}
            </tbody>
        </table>
        
        <div class="stats">
            <h3>📊 Estadísticas del Catálogo</h3>
            {estadisticas}
        </div>
        
        <div class="footer">
            <p>Exportado desde CRUD Series TV - Total de series: {total_series}</p>
        </div>
    </div>
</body>
</html>
"""
    
    # Generar filas de la tabla
    filas_html = []
    for serie in series:
        # Determinar clase CSS para la calificación
        if serie.calificacion >= 9.0:
            clase_calificacion = "excelente"
        elif serie.calificacion >= 8.0:
            clase_calificacion = "muy-buena"
        elif serie.calificacion >= 7.0:
            clase_calificacion = "buena"
        elif serie.calificacion >= 5.0:
            clase_calificacion = "regular"
        else:
            clase_calificacion = "mala"
        
        fila = f"""
                <tr>
                    <td>{serie.id}</td>
                    <td><strong>{serie.titulo}</strong></td>
                    <td><span class="genero">{serie.genero}</span></td>
                    <td>{serie.temporadas}</td>
                    <td>{serie.año_estreno}</td>
                    <td><span class="calificacion {clase_calificacion}">{serie.calificacion}/10</span></td>
                </tr>"""
        filas_html.append(fila)
    
    # Generar estadísticas
    if series:
        total_series = len(series)
        promedio_calificacion = sum(s.calificacion for s in series) / total_series
        total_temporadas = sum(s.temporadas for s in series)
        
        # Contar géneros
        generos = {}
        for serie in series:
            generos[serie.genero] = generos.get(serie.genero, 0) + 1
        
        generos_str = ", ".join([f"{genero}: {cantidad}" for genero, cantidad in generos.items()])
        
        # Serie mejor calificada
        mejor_serie = max(series, key=lambda s: s.calificacion)
        
        estadisticas_html = f"""
            <p><strong>Total de series:</strong> {total_series}</p>
            <p><strong>Calificación promedio:</strong> {promedio_calificacion:.2f}/10</p>
            <p><strong>Total de temporadas:</strong> {total_temporadas}</p>
            <p><strong>Serie mejor calificada:</strong> {mejor_serie.titulo} ({mejor_serie.calificacion}/10)</p>
            <p><strong>Géneros:</strong> {generos_str}</p>
        """
    else:
        estadisticas_html = "<p>No hay series en el catálogo.</p>"
    
    # Completar el template
    html_completo = html_template.format(
        fecha_generacion=datetime.now().strftime("%d de %B de %Y a las %H:%M"),
        filas_series="".join(filas_html),
        estadisticas=estadisticas_html,
        total_series=len(series)
    )
    
    return html_completo

def main():
    """Función principal para exportar series a HTML"""
    print("🎬 Exportador de Series a HTML")
    print("=" * 50)
    
    try:
        # Crear instancia del manager
        serie_manager = SerieManager()
        
        # Obtener todas las series
        series = serie_manager.listar_series()
        
        if not series:
            print("❌ No hay series en el catálogo para exportar.")
            return
        
        print(f"📚 Se encontraron {len(series)} series en el catálogo")
        
        # Solicitar nombre del archivo
        print("\n📁 Configuración del archivo:")
        nombre_archivo = input("Nombre del archivo HTML (por defecto: series_table.html): ").strip()
        if not nombre_archivo:
            nombre_archivo = "series_table.html"
        
        # Asegurar extensión .html
        if not nombre_archivo.endswith('.html'):
            nombre_archivo += '.html'
        
        # Generar HTML
        print("\n🔄 Generando archivo HTML...")
        html_content = generar_html_series(series, nombre_archivo)
        
        # Guardar archivo
        ruta_completa = os.path.join(os.getcwd(), nombre_archivo)
        with open(ruta_completa, 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        print(f"✅ Archivo HTML generado exitosamente!")
        print(f"📍 Ubicación: {ruta_completa}")
        print(f"📊 Series exportadas: {len(series)}")
        
        # Mostrar estadísticas
        estadisticas = serie_manager.obtener_estadisticas()
        print(f"\n📈 Estadísticas del catálogo:")
        print(f"   • Total de series: {estadisticas['total_series']}")
        print(f"   • Calificación promedio: {estadisticas['promedio_calificacion']}/10")
        print(f"   • Total de temporadas: {estadisticas['total_temporadas']}")
        if estadisticas['serie_mejor_calificada']:
            mejor = estadisticas['serie_mejor_calificada']
            print(f"   • Mejor calificada: {mejor.titulo} ({mejor.calificacion}/10)")
        
        # Preguntar si abrir el archivo
        print(f"\n💡 Para ver el archivo, abre: {ruta_completa}")
        abrir = input("¿Deseas abrir el archivo ahora? (s/N): ").strip().lower()
        if abrir in ['s', 'si', 'sí', 'y', 'yes']:
            os.startfile(ruta_completa)  # Windows
        
    except Exception as e:
        print(f"❌ Error al generar el archivo HTML: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()