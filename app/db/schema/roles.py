from  pydantic import BaseModel

class rol(BaseModel):
    id_rol: int
    cargo: str
    
    class config:
        orm_mode = True
        schema_extra = {
            "example":{
                "id_rol": 1,
                "cargo": "Administrador"
            }
        }


class rolConsulta(BaseModel):
    cargo: str

    class config:
        orm_mode = True
        schema_extra = {
            "example":{
                "cargo": "Administrador"
            }
        }