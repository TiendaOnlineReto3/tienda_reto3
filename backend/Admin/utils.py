import os
from werkzeug.utils import secure_filename
import base64


def save_uploaded_file(file):
    try:
        file_data = file.read()
        return base64.b64encode(file_data)
    except Exception as e:
        raise ValueError(f"No se pudo leer el archivo: {str(e)}")
