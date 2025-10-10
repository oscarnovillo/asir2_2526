from typing import List, Optional
from domain.model.serie import Serie
from data.serie_repository import SerieRepositoryInMemory

class SerieManager:
    """Clase que maneja las operaciones CRUD de las series (Capa de Servicio)"""
    
    def __init__(self):
        self._repository = SerieRepositoryInMemory()
    
    # Los datos se manejan a través del repositorio, no hay necesidad de cargar/guardar archivos
    
    def crear_serie(self, titulo: str, genero: str, temporadas: int, año_estreno: int, calificacion: float = 0.0) -> Serie:
        """Crea una nueva serie"""
        # El repositorio manejará la asignación del ID
        nueva_serie = Serie(0, titulo, genero, temporadas, año_estreno, calificacion)  # ID temporal
        return self._repository.save(nueva_serie)
    
    def listar_series(self) -> List[Serie]:
        """Retorna todas las series"""
        return self._repository.find_all()
    
    def buscar_serie_por_id(self, id: int) -> Optional[Serie]:
        """Busca una serie por su ID"""
        return self._repository.find_by_id(id)
    
    def buscar_series_por_titulo(self, titulo: str) -> List[Serie]:
        """Busca series que contengan el título especificado"""
        return self._repository.find_by_titulo_containing(titulo)
    
    def buscar_series_por_genero(self, genero: str) -> List[Serie]:
        """Busca series por género"""
        return self._repository.find_by_genero_containing(genero)
    
    def actualizar_serie(self, id: int, titulo: Optional[str] = None, genero: Optional[str] = None, 
                        temporadas: Optional[int] = None, año_estreno: Optional[int] = None, 
                        calificacion: Optional[float] = None) -> bool:
        """Actualiza una serie existente"""
        serie = self._repository.find_by_id(id)
        if serie:
            if titulo is not None:
                serie.titulo = titulo
            if genero is not None:
                serie.genero = genero
            if temporadas is not None:
                serie.temporadas = temporadas
            if año_estreno is not None:
                serie.año_estreno = año_estreno
            if calificacion is not None:
                serie.calificacion = calificacion
            self._repository.save(serie)
            return True
        return False
    
    def eliminar_serie(self, id: int) -> bool:
        """Elimina una serie por su ID"""
        return self._repository.delete_by_id(id)
    
    def obtener_estadisticas(self) -> dict:
        """Obtiene estadísticas de las series"""
        series = self._repository.find_all()
        
        if not series:
            return {
                'total_series': 0,
                'promedio_calificacion': 0,
                'generos': {},
                'serie_mejor_calificada': None,
                'total_temporadas': 0
            }
        
        total_series = len(series)
        promedio_calificacion = sum(serie.calificacion for serie in series) / total_series
        
        # Contar géneros
        generos = {}
        for serie in series:
            generos[serie.genero] = generos.get(serie.genero, 0) + 1
        
        # Serie mejor calificada
        serie_mejor_calificada = max(series, key=lambda s: s.calificacion)
        
        # Total de temporadas
        total_temporadas = sum(serie.temporadas for serie in series)
        
        return {
            'total_series': total_series,
            'promedio_calificacion': round(promedio_calificacion, 2),
            'generos': generos,
            'serie_mejor_calificada': serie_mejor_calificada,
            'total_temporadas': total_temporadas
        }