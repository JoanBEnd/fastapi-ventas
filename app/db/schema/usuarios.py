from pydantic import BaseModel
from datetime import datetime

class Usuarios(BaseModel):
    Id_Empleado: int
    UserName: str
    Password: str
    salt: bytes
    Fecha_Creacion: datetime

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Id_Empleado": 1,
                "UserName": "jdoe",
                "Password": "hashed_password",
                "salt": b"random_salt",
                "Fecha_Creacion": "2023-10-01T12:00:00Z"
            }
        }