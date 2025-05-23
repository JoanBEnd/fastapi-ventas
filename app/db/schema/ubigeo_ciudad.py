from pydantic import BaseModel

class UbigeoCiudad(BaseModel):  
    Id_UbigeoCiudad: int
    Id_UbigeoEstado: int
    Ciudad: str
    Latitud: float
    Longitud: float

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Id_UbigeoCiudad": 1,
                "Id_UbigeoEstado": 1,
                "Ciudad": "Lima",
                "Latitud": -12.0464,
                "Longitud": -77.0428
            }
        }

class UbigeoCiudadConsulta(BaseModel):
    Id_UbigeoEstado: int
    Ciudad: str
    Latitud: float
    Longitud: float

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Id_UbigeoEstado": 1,
                "Ciudad": "Lima",
                "Latitud": -12.0464,
                "Longitud": -77.0428
            }
        }
    