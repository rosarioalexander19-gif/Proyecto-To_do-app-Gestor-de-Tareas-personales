from model.Tarea import Proyecto, Tarea
from uuid import UUID
import uuid


#Repositorio para proyecto>



class proyectoRepository:

    def __init__(self):
         self._proyect = []
   

    def obtener_proyecto(self) -> list[Proyecto]:
        return self._proyect

    def borrar_proyecto(self, uuid: UUID) -> None:
         self._proyect = [p for p in self._proyect if p.uuid != uuid]
    pass

    def crear_proyecto(self, nombre: str) -> Proyecto:
        proyecto: Proyecto = Proyecto(nombre)
        self._proyect.append(proyecto)
        return proyecto 

    def actualizar_proyecto(self, uuid: UUID, nombre: str):
        for proyecto in self._proyect:
            if proyecto.uuid == uuid:
                proyecto.nombre = nombre
                return proyecto
        
        pass


    #Repositorio para Tarea>



class tareaRepository:

    def __init__(self):
         self._asg = []
   

    def obtener_tarea(self) -> list[Tarea]:
        
            return self._asg

    def eliminar_tarea(self, uuid: UUID) -> None:
            self._asg = [t for t in self._asg if t.uuid != uuid]
       
            pass

    def crear_tarea(self, nombre: str, descripcion: str, proyecto_uuid: str) -> Tarea:
        
            tarea = Tarea(nombre, descripcion, proyecto_uuid)
            self._asg.append(tarea)
            return tarea

    def actualizar_tarea(self, uuid: UUID, nombre: str, descripcion: str, completada: bool):
       
            for tarea in self._asg:
                if tarea.uuid == uuid:
                    tarea.nombre = nombre
                    tarea.descripcion = descripcion
                    tarea.completada = completada
                    return tarea

            pass
