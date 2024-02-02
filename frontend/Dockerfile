FROM nginx:alpine

COPY . /usr/share/nginx/html

# Instalar apache2-utils para obtener htpasswd
RUN apt-get update && \
    apt-get install -y apache2-utils && \
    rm -rf /var/lib/apt/lists/*

# Definir variables de entorno para usuario y contraseña
ENV NGINX_USER usuario
ENV NGINX_PASSWORD contraseña

# Crear el archivo .htpasswd con el usuario y la contraseña
RUN htpasswd -cb /etc/nginx/.htpasswd $NGINX_USER $NGINX_PASSWORD

# Copiar tu configuración personalizada de Nginx
COPY ./nginx_config/mynginx.conf /etc/nginx/nginx.conf
COPY . /usr/share/nginx/html

# Exponer el puerto
EXPOSE 80

# Comando para iniciar Nginx
CMD ["nginx", "-g", "daemon off;"]


#Crear variables entorno en el servidor
#docker run -e NGINX_USER=usuario -e NGINX_PASSWORD=contraseña -p 80:80 nombre_de_tu_imagen
