from pydantic import BaseModel

class EmpleadoAsignacion(BaseModel):
    id_Asignacion: int
    id_Empleado: int
    id_UbigeoPermiso: int
    Ubigeo_Descripcion: str

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id_Asignacion": 1,
                "id_Empleado": 1,
                "id_UbigeoPermiso": 1,
                "Ubigeo_Descripcion": "Lima"
            }

        }

class EmpleadoAsignacionConsulta(BaseModel):
    id_Empleado: int
    id_UbigeoPermiso: int    
    Ubigeo_Descripcion: str

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id_Empleado": 1,
                "id_UbigeoPermiso": 1,
                "Ubigeo_Descripcion": "Lima"
            }
        }