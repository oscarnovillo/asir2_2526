class Serie:
    """Clase que representa una serie de TV"""
    
    def __init__(self, id: int, titulo: str, genero: str, temporadas: int, año_estreno: int, calificacion: float = 0.0):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.temporadas = temporadas
        self.año_estreno = año_estreno
        self.calificacion = calificacion
    
    def __str__(self):
        return f"ID: {self.id} | {self.titulo} ({self.año_estreno}) - {self.genero} | {self.temporadas} temporadas | Calificación: {self.calificacion}/10"
    
    def to_dict(self):
        """Convierte la serie a diccionario para guardado en JSON"""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero,
            'temporadas': self.temporadas,
            'año_estreno': self.año_estreno,
            'calificacion': self.calificacion
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea una serie desde un diccionario"""
        return cls(
            data['id'],
            data['titulo'],
            data['genero'],
            data['temporadas'],
            data['año_estreno'],
            data.get('calificacion', 0.0)
        )