from pydantic import BaseModel


class UbigeoEstado(BaseModel):
    Id_UbigeoEstado: int
    Id_Ubigeo: int
    Estado: str

    class config:
        orm_mode = True
        schema_extra = {
                "example": {
                    "Id_UbigeoEstado": 1,
                    "Id_Ubigeo": 1,
                    "Estado": "Lima"
                }
        }


class UbigeoEstadoConsulta(BaseModel):
    Id_Ubigeo: int
    Estado: str

    class config:
        orm_mode = True
        schema_extra = {
                "example": {
                    "Id_Ubigeo": 1,
                    "Estado": "Lima"
                }
        }
