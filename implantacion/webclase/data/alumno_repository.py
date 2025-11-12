from domain.model.Alumno import Alumno


class AlumnoRepository:

    def get_all(self,db) -> list[Alumno]:
        cursor = db.cursor()
    
        cursor.execute("SELECT * FROM alumnos")

        alumnos_en_db = cursor.fetchall()
        alumnos : list[Alumno]= list()
        for alumno in alumnos_en_db:
            alumno = Alumno(alumno[0], alumno[1])
            alumnos.append(alumno)
        cursor.close()
        
        return alumnos
    
    def insertar_alumno(self, db, alumno: Alumno) -> None:
        cursor = db.cursor()
    
        cursor.execute("INSERT INTO alumnos (nombre) VALUES (%s)", (alumno.nombre,))

        db.commit()
        cursor.close()