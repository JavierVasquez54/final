# Usa la imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 para que la aplicación Flask sea accesible
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]