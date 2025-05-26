from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Crear el objeto Base para heredar en los modelos
Base = declarative_base()


# Formato del string de conexión
# DRIVER y SERVER dependen de tu configuración
SERVER = "DESKTOP-JI4V2CK\SQLDEVELOPER2022"
DATABASE = "Retail_ventas"
DRIVER = "ODBC Driver 17 for SQL Server"

# Cadena sin autenticación (usuario de Windows)
connection_string = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER.replace(' ', '+')}"

# Crear el engine
engine = create_engine(connection_string)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)