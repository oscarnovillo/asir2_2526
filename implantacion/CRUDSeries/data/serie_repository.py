from typing import List, Optional
from domain.model.serie import Serie

class SerieRepositoryInMemory:
    """Repositorio en memoria para las series"""
    
    def __init__(self):
        self._series: List[Serie] = []
        self._next_id: int = 1
        self._initialize_data()
    
    def _initialize_data(self):
        """Inicializa datos de ejemplo"""
        series_ejemplo = [
            Serie(1, "Breaking Bad", "Drama", 5, 2008, 9.5),
            Serie(2, "The Office", "Comedia", 9, 2005, 8.8),
            Serie(3, "Game of Thrones", "Fantasía", 8, 2011, 8.5),
            Serie(4, "Stranger Things", "Ciencia Ficción", 4, 2016, 8.7),
            Serie(5, "Friends", "Comedia", 10, 1994, 8.9),
            Serie(6, "The Mandalorian", "Fantasía", 2, 2019, 8.7),
            Serie(7, "The Crown", "Drama", 4, 2016, 8.6),
            Serie(8, "Black Mirror", "Ciencia Ficción", 5, 2011, 8.8),
            Serie(9, "Narcos", "Crimen", 3, 2015, 8.8),
            Serie(10, "The Witcher", "Fantasía", 2, 2019, 8.2)
        ]
        
        for serie in series_ejemplo:
            self._series.append(serie)
        
        self._next_id = 6
    
    def save(self, serie: Serie) -> Serie:
        """Guarda una serie (crear o actualizar)"""
        if serie.id == 0:
            # Nueva serie - asignar nuevo ID
            serie.id = self._next_id
            self._next_id += 1
            self._series.append(serie)
        else:
            # Actualizar serie existente
            existing_serie = self.find_by_id(serie.id)
            if existing_serie:
                index = self._series.index(existing_serie)
                self._series[index] = serie
            else:
                # Si no existe, la agregamos
                self._series.append(serie)
        
        return serie
    
    def find_by_id(self, id: int) -> Optional[Serie]:
        """Busca una serie por ID"""
        for serie in self._series:
            if serie.id == id:
                return serie
        return None
    
    def find_all(self) -> List[Serie]:
        """Retorna todas las series"""
        return self._series.copy()
    
    def find_by_titulo_containing(self, titulo: str) -> List[Serie]:
        """Busca series que contengan el título especificado"""
        titulo_lower = titulo.lower()
        return [serie for serie in self._series if titulo_lower in serie.titulo.lower()]
    
    def find_by_genero_containing(self, genero: str) -> List[Serie]:
        """Busca series por género"""
        genero_lower = genero.lower()
        return [serie for serie in self._series if genero_lower in serie.genero.lower()]
    
    def delete_by_id(self, id: int) -> bool:
        """Elimina una serie por ID"""
        serie = self.find_by_id(id)
        if serie:
            self._series.remove(serie)
            return True
        return False
    
    def count(self) -> int:
        """Retorna el número total de series"""
        return len(self._series)
    
    def exists_by_id(self, id: int) -> bool:
        """Verifica si existe una serie con el ID especificado"""
        return self.find_by_id(id) is not None