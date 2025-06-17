from pydantic import BaseModel
from datetime import date, datetime

from app.db.conect import Base


class venta(BaseModel):
    Transaccion_ID: int
    Id_Cliente: int
    Id_Empleado: int
    Id_UbigeoCiudad: int
    Venta_Total: float
    fecha_registro: datetime

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                " Transaccion_ID": "1",
                "Id_Cliente": "1",
                "Id_Empleado": "1",
                "Id_UbigeoCiudad": "10",
                "Venta_Total": 30.15,
                "fecha_registro": "2023-10-01T12:00:00Z"
            }
        }


class ventaConsulta(BaseModel):
    Id_Cliente: int
    Id_Empleado: int
    Id_UbigeoCiudad: int
    Venta_Total: float
    fecha_registro: datetime

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Id_Cliente": "1",
                "Id_Empleado": "1",
                "Id_UbigeoCiudad": "10",
                "Venta_Total": 30.15,
                "fecha_registro": "2023-10-01T12:00:00Z"
            }
        }


class ventaAleatoria(BaseModel):
    Id_Cliente: int
    Id_Empleado: int
    Id_Producto: int
    fecha_registro: datetime
    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Id_Cliente": 1,
                "Id_Empleado": 1,
                "Id_Producto": 1,
                "fecha_registro": "2023-10-01"
            }
        }