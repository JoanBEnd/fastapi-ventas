from pydantic import BaseModel

class Producto(BaseModel):
    Id_Producto: int
    Id_Categoria: int
    Producto: str
    Precio_Actual: float

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Id_Producto": 1,
                "Id_Categoria": 1,
                "Producto": "Laptop",
                "Precio_Actual": 1200.50
            }
        }


class ProductoConsulta(BaseModel):
    Id_Categoria: int
    Producto: str
    Precio_Actual: float

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Id_Categoria": 1,
                "Producto": "Laptop",
                "Precio_Actual": 1200.50
            }
        }

