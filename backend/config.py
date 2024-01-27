# este archivo es para configurar la base de datos en postgresql con docker
# para que funcione, debe coincidir las credenciales y puerto de postgresql en docker-compose.yml con las de este archivo

import os

# Obtén las credenciales de las variables de entorno si están definidas, de lo contrario, utiliza valores predeterminados
DB_USER = os.environ.get("POSTGRES_USER", "user")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "pass")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5433")
DB_NAME = os.environ.get("POSTGRES_DB", "base_datos")

SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
