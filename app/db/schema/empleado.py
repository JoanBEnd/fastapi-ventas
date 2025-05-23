from pydantic import BaseModel


class Empleado(BaseModel):
    Id_Empleado: int
    Nombre: str
    Apellido: str
    id_rol: int
    correo: str

    class config:
        orm_mode = True

class EmpleadoConsulta(BaseModel):
    Nombre: str
    Apellido: str
    id_rol: int
    correo: str
    
    class config:
        orm_mode = True

