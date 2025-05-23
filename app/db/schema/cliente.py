from pydantic import BaseModel  


class Cliente(BaseModel):
    Id_Cliente: int
    Nombre: str
    Apellido: str
    Genero: str
    Edad: int   
    
    class config:
        or_model = True
        schema_extra = {
            "example": {
                "Id_Cliente": 1,
                "Nombre": "Juan",
                "Apellido": "Pérez",
                "Genero": "Masculino",
                "Edad": 30
            }
        }


class ClienteConsulta(BaseModel):
    Nombre: str
    Apellido: str
    Genero: str
    Edad: int

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Nombre": "Juan",
                "Apellido": "Pérez",
                "Genero": "Masculino",
                "Edad": 30
            }
        }
