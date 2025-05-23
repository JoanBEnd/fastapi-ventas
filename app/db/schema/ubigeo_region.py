from pydantic import BaseModel

class UbigeoRegion(BaseModel):
    id_Ubigeo: int
    Region: str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id_Ubigeo": 1,
                "Region": "Lima"
            }
        }

class UbigeoRegionConsulta(BaseModel):
    Region: str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Region": "Lima"
            }
        }