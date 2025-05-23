from pydantic import BaseModel

class Categoria(BaseModel):
    id_Categoria: int
    Categoria: str

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id_Categoria": 1,
                "Categoria": "Electronics"
            }
        }

class CategoriaConsulta(BaseModel):
    Categoria: str

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Categoria": "Electronics"
            }
        }

 

