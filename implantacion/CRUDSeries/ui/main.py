import os
import sys
from domain.serie_manager import SerieManager

class MenuCRUD:
    """Clase que maneja el menú y la interfaz de usuario"""
    
    def __init__(self):
        self.manager = SerieManager()
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pausar(self):
        """Pausa la ejecución hasta que el usuario presione Enter"""
        input("\nPresiona Enter para continuar...")
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        print("=" * 50)
        print("          CRUD DE SERIES DE TV")
        print("=" * 50)
        print("1. Crear nueva serie")
        print("2. Listar todas las series")
        print("3. Buscar series")
        print("4. Actualizar serie")
        print("5. Eliminar serie")
        print("6. Estadísticas")
        print("7. Salir")
        print("=" * 50)
    
    def crear_serie(self):
        """Interfaz para crear una nueva serie"""
        print("\n--- CREAR NUEVA SERIE ---")
        try:
            titulo = input("Título de la serie: ").strip()
            if not titulo:
                print("❌ El título no puede estar vacío.")
                return
            
            genero = input("Género: ").strip()
            if not genero:
                print("❌ El género no puede estar vacío.")
                return
            
            temporadas = int(input("Número de temporadas: "))
            if temporadas < 1:
                print("❌ El número de temporadas debe ser mayor a 0.")
                return
            
            año_estreno = int(input("Año de estreno: "))
            if año_estreno < 1900 or año_estreno > 2030:
                print("❌ Año de estreno inválido.")
                return
            
            calificacion_input = input("Calificación (0-10, opcional): ").strip()
            calificacion = float(calificacion_input) if calificacion_input else 0.0
            
            if calificacion < 0 or calificacion > 10:
                print("❌ La calificación debe estar entre 0 y 10.")
                return
            
            serie = self.manager.crear_serie(titulo, genero, temporadas, año_estreno, calificacion)
            print(f"\n✅ Serie creada exitosamente:")
            print(f"   {serie}")
            
        except ValueError:
            print("❌ Error: Ingresa valores numéricos válidos.")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def listar_series(self):
        """Muestra todas las series"""
        print("\n--- LISTA DE SERIES ---")
        series = self.manager.listar_series()
        
        if not series:
            print("📺 No hay series registradas.")
            return
        
        print(f"Total de series: {len(series)}\n")
        for serie in series:
            print(f"  {serie}")
    
    def mostrar_menu_busqueda(self):
        """Muestra el submenú de búsqueda"""
        print("\n--- BUSCAR SERIES ---")
        print("1. Buscar por ID")
        print("2. Buscar por título")
        print("3. Buscar por género")
        print("4. Volver al menú principal")
    
    def buscar_series(self):
        """Interfaz para buscar series"""
        while True:
            self.mostrar_menu_busqueda()
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == '1':
                self.buscar_por_id()
            elif opcion == '2':
                self.buscar_por_titulo()
            elif opcion == '3':
                self.buscar_por_genero()
            elif opcion == '4':
                break
            else:
                print("❌ Opción no válida.")
            
            if opcion in ['1', '2', '3']:
                self.pausar()
    
    def buscar_por_id(self):
        """Busca una serie por ID"""
        try:
            id_serie = int(input("Ingresa el ID de la serie: "))
            serie = self.manager.buscar_serie_por_id(id_serie)
            
            if serie:
                print(f"\n✅ Serie encontrada:")
                print(f"   {serie}")
            else:
                print(f"❌ No se encontró una serie con ID {id_serie}.")
                
        except ValueError:
            print("❌ Error: Ingresa un ID válido (número).")
    
    def buscar_por_titulo(self):
        """Busca series por título"""
        titulo = input("Ingresa el título (o parte del título): ").strip()
        if not titulo:
            print("❌ El título no puede estar vacío.")
            return
        
        series = self.manager.buscar_series_por_titulo(titulo)
        
        if series:
            print(f"\n✅ Se encontraron {len(series)} serie(s):")
            for serie in series:
                print(f"   {serie}")
        else:
            print(f"❌ No se encontraron series que contengan '{titulo}'.")
    
    def buscar_por_genero(self):
        """Busca series por género"""
        genero = input("Ingresa el género: ").strip()
        if not genero:
            print("❌ El género no puede estar vacío.")
            return
        
        series = self.manager.buscar_series_por_genero(genero)
        
        if series:
            print(f"\n✅ Se encontraron {len(series)} serie(s) del género '{genero}':")
            for serie in series:
                print(f"   {serie}")
        else:
            print(f"❌ No se encontraron series del género '{genero}'.")
    
    def actualizar_serie(self):
        """Interfaz para actualizar una serie"""
        print("\n--- ACTUALIZAR SERIE ---")
        try:
            id_serie = int(input("Ingresa el ID de la serie a actualizar: "))
            serie = self.manager.buscar_serie_por_id(id_serie)
            
            if not serie:
                print(f"❌ No se encontró una serie con ID {id_serie}.")
                return
            
            print(f"\nSerie actual: {serie}")
            print("\n(Deja vacío para mantener el valor actual)")
            
            titulo = input(f"Nuevo título [{serie.titulo}]: ").strip()
            genero = input(f"Nuevo género [{serie.genero}]: ").strip()
            
            temporadas_input = input(f"Nuevas temporadas [{serie.temporadas}]: ").strip()
            temporadas = int(temporadas_input) if temporadas_input else None
            
            año_input = input(f"Nuevo año de estreno [{serie.año_estreno}]: ").strip()
            año_estreno = int(año_input) if año_input else None
            
            calificacion_input = input(f"Nueva calificación [{serie.calificacion}]: ").strip()
            calificacion = float(calificacion_input) if calificacion_input else None
            
            # Validaciones
            if temporadas is not None and temporadas < 1:
                print("❌ El número de temporadas debe ser mayor a 0.")
                return
            
            if año_estreno is not None and (año_estreno < 1900 or año_estreno > 2030):
                print("❌ Año de estreno inválido.")
                return
            
            if calificacion is not None and (calificacion < 0 or calificacion > 10):
                print("❌ La calificación debe estar entre 0 y 10.")
                return
            
            exito = self.manager.actualizar_serie(
                id_serie,
                titulo if titulo else None,
                genero if genero else None,
                temporadas,
                año_estreno,
                calificacion
            )
            
            if exito:
                serie_actualizada = self.manager.buscar_serie_por_id(id_serie)
                print(f"\n✅ Serie actualizada exitosamente:")
                print(f"   {serie_actualizada}")
            else:
                print("❌ Error al actualizar la serie.")
                
        except ValueError:
            print("❌ Error: Ingresa valores numéricos válidos.")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def eliminar_serie(self):
        """Interfaz para eliminar una serie"""
        print("\n--- ELIMINAR SERIE ---")
        try:
            id_serie = int(input("Ingresa el ID de la serie a eliminar: "))
            serie = self.manager.buscar_serie_por_id(id_serie)
            
            if not serie:
                print(f"❌ No se encontró una serie con ID {id_serie}.")
                return
            
            print(f"\nSerie a eliminar: {serie}")
            confirmacion = input("¿Estás seguro? (s/N): ").strip().lower()
            
            if confirmacion in ['s', 'si', 'sí']:
                if self.manager.eliminar_serie(id_serie):
                    print("✅ Serie eliminada exitosamente.")
                else:
                    print("❌ Error al eliminar la serie.")
            else:
                print("❌ Eliminación cancelada.")
                
        except ValueError:
            print("❌ Error: Ingresa un ID válido (número).")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas de las series"""
        print("\n--- ESTADÍSTICAS ---")
        stats = self.manager.obtener_estadisticas()
        
        if stats['total_series'] == 0:
            print("📊 No hay series registradas para mostrar estadísticas.")
            return
        
        print(f"📊 Total de series: {stats['total_series']}")
        print(f"⭐ Calificación promedio: {stats['promedio_calificacion']}/10")
        print(f"📺 Total de temporadas: {stats['total_temporadas']}")
        
        if stats['serie_mejor_calificada']:
            print(f"🏆 Serie mejor calificada: {stats['serie_mejor_calificada'].titulo} ({stats['serie_mejor_calificada'].calificacion}/10)")
        
        print("\n🎭 Distribución por géneros:")
        for genero, cantidad in stats['generos'].items():
            print(f"   {genero}: {cantidad} serie(s)")
    
    def ejecutar(self):
        """Ejecuta el menú principal"""
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu_principal()
            
            opcion = input("Selecciona una opción: ").strip()
            
            if opcion == '1':
                self.crear_serie()
            elif opcion == '2':
                self.listar_series()
            elif opcion == '3':
                self.buscar_series()
            elif opcion == '4':
                self.actualizar_serie()
            elif opcion == '5':
                self.eliminar_serie()
            elif opcion == '6':
                self.mostrar_estadisticas()
            elif opcion == '7':
                print("\n👋 ¡Gracias por usar el CRUD de Series!")
                sys.exit(0)
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
            
            self.pausar()

if __name__ == "__main__":
    menu = MenuCRUD()
    try:
        menu.ejecutar()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        input("Presiona Enter para salir...")