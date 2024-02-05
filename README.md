# Tienda Online con Flask y React

![Logo de la tienda](ruta/al/logo.png)

Este proyecto es una tienda online desarrollada utilizando Flask para el backend y VUE para el frontend.

## Contenido

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación](#instalación)
3. [Configuración](#configuración)
4. [Contribuciones](#contribuciones)

## Requisitos del Sistema

- [Python](https://www.python.org/) (3.6 o superior)
- [Node.js](https://nodejs.org/) (v12 o superior)
- [npm](https://www.npmjs.com/)
- [docker-compose](https://docs.docker.com/compose/)

# Instalación

1. Instalación de Docker

Asegúrate de tener Docker instalado en tu sistema. Puedes seguir las [instrucciones de instalación](https://docs.docker.com/get-docker/) específicas para tu sistema operativo.

2. Clonar el Repositorio

   Navega hasta la carpeta deseada y clona el repositorio de la aplicación:

   ```bash
   git clone https://github.com/TiendaOnlineReto3/tienda_reto3.git
   ```

3. Ejecuta Docker compose:

   ```bash
   docker-compose up --build
   ```

4. Navega al servidor:

   ```bash
   localhost o ip:5000/
   ```

5. Navega a la pagina web:

   ```bash
   localhost o ip:8080/
   ```
### Tecnologías Utilizadas:

-   Backend:

    -   Flask: Un framework de desarrollo web en Python que proporciona una base sólida para la creación de aplicaciones web.
    -   SQLAlchemy: Se empleó como un ORM (Mapeo Objeto-Relacional) para interactuar con la base de datos PostgreSQL de manera eficiente.
    -   PostgreSQL: Una potente base de datos relacional que almacena la información de los productos, usuarios y pedidos.
-   Frontend:

    -   Vue.js: Un framework progresivo de JavaScript que facilita la creación de interfaces de usuario interactivas y dinámicas.
    -   Vuex: Utilizado para la gestión del estado de la aplicación, especialmente para el manejo del carrito de compras.
    -   Vue Router: Facilita la navegación dentro de la aplicación, permitiendo transiciones suaves entre las distintas páginas.
-   Autenticación y Autorización:

    -   Se implementó un sistema de inicio de sesión y registro de usuarios utilizando Flask-Login.
    -   Se utilizó JSON Web Tokens (JWT) para gestionar la autenticación y autorización del usuario.

### Funcionalidades:

1.  Inicio de Sesión y Registro:

    -   Los usuarios pueden crear cuentas o iniciar sesión con credenciales existentes.
    -   Las contraseñas se almacenan de manera segura utilizando técnicas de hash.
2.  Catálogo de Productos:

    -   Los productos se muestran de manera atractiva y organizada en el frontend.
    -   Información detallada sobre cada producto, incluyendo imágenes, descripciones y precios.
3.  Añadir al Carrito:

    -   Los usuarios pueden agregar productos al carrito de compras con un solo clic.
    -   El estado del carrito se gestiona en el frontend mediante Vuex.
4.  Gestión de Pedidos:

    -   Implementación de un sistema de pedidos para realizar el seguimiento de las transacciones.
    -   Los pedidos se almacenan en la base de datos y están vinculados a los usuarios autenticados.
5.  Interfaz Intuitiva y Responsive:

    -   El diseño de la interfaz se ha optimizado para ofrecer una experiencia de usuario intuitiva y agradable.
    -   La aplicación es totalmente responsive, adaptándose a diferentes dispositivos y tamaños de pantalla.

### Configuración y Ejecución:

1.  Backend:

    -   Configurar la base de datos PostgreSQL y actualizar la conexión en el archivo de configuración.
    -   Instalar dependencias mediante el archivo `requirements.txt`.
    -   Ejecutar el servidor Flask.
2.  Frontend:

    -   Instalar dependencias con `npm install` en el directorio del frontend.
    -   Configurar las rutas y la URL de la API en el archivo de configuración.
    -   Iniciar la aplicación Vue.js con `npm run serve`.
3.  Navegación:

    -   Acceder a la aplicación desde el navegador mediante la URL proporcionada por Vue.js.
