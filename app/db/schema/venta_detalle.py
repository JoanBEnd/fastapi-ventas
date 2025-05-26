from pydantic import BaseModel

class venta_detalle(BaseModel):
    Id_VentaDetalle: int
    Transaccion_ID: int
    Id_Producto: int
    Cantidad: int
    Precio_Unitario: float
    Total: float

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Id_VentaDetalle": "1",
                "Transaccion_ID": "1",
                "Id_Producto": "2",
                "Cantidad": "15",
                "Precio_Unitario": "3",
                "Total": "45.00"
            }
        }

class venta_detalleConsulta(BaseModel):
    Transaccion_ID: int
    Id_Producto: int
    Cantidad: int
    Precio_Unitario: float
    Total: float

    class config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Transaccion_ID": "1",
                "Id_Producto": "2",
                "Cantidad": "15",
                "Precio_Unitario": "3",
                "Total": "45.00"
            }
        }


class venta_detalleUpdate(BaseModel):
    Cantidad: int
    Precio_Unitario: float
    Total: float

    class config:
        orm_mode = True
        schema_extra = {
            "example": {                
                "Cantidad": "15",
                "Precio_Unitario": "3",
                "Total": "45.00"
            }
        }