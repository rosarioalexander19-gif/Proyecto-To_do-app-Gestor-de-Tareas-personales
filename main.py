from proyecto_service import ProyectoService
from ui import AppWindow

def main():
    try:
        # Inicializar servicio de proyectos
        proyecto_service = ProyectoService()

        print("Sistema iniciado correctamente")
        print("ProyectoService listo para usar")

        # Integración con la interfaz gráfica (UI)
        app = AppWindow(proyecto_service)
        app.run()

    except Exception as e:
        print("Error al iniciar el sistema:", e)


if __name__ == "__main__":
    main()
