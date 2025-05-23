from fastapi import FastAPI
from app.routers import cliente, empleado, roles, producto, categoria, empleado_asignacion, ubigeo_region, ubigeo_estado, ubigeo_ciudad,venta



app = FastAPI()
app.title = "VENTAS ONLINE"

app.include_router(cliente.router)
app.include_router(empleado.router)
app.include_router(roles.router)
app.include_router(categoria.router)
app.include_router(producto.router)
app.include_router(empleado_asignacion.router)
app.include_router(ubigeo_region.router)
app.include_router(ubigeo_estado.router)
app.include_router(ubigeo_ciudad.router)
app.include_router(venta.router)
@app.get("/")
def bienvenida():
    return {"message": "Bienvenido a la API de FastAPI"}

@app.get("/url_portafolio")
def url_portafolio():
    return "https://joanbend.github.io/portafolio/"


