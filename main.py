from service.proyecto_service import ProyectoService
from service.tarea_service import TareaService
from ui.app_window import AppWindow
from repository.Tarea_repository import proyectoRepository, tareaRepository

def main():
    try:
        # Inicializar servicio

        proyecto_repo = proyectoRepository()
        tarea_repo = tareaRepository()

        proyecto_service = ProyectoService(proyecto_repo)
        tarea_service = TareaService(proyecto_repo, tarea_repo)


        print("Sistema iniciado correctamente")
        
        # Prueba básica de integración (opcional pero PRO)
        proyectos = proyecto_service.obtener_proyectos()
        print(f"Proyectos cargados: {len(proyectos)}")

        # Aquí luego se conectará la UI
        # from ui import AppWindow
        app = AppWindow(proyecto_service, tarea_service)
        app.run()

    except Exception as e:
        print("Error al iniciar el sistema:", e)

if __name__ == "__main__":
    main()
