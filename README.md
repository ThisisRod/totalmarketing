
# Total Marketing Servicios Digitales

Esta aplicación web está diseñada para usuarios que desean adquirir paquetes o servicios de marketing digital de Total Marketing. La aplicación está desarrollada utilizando el framework Django, siguiendo el patrón MVT (Modelo Vista Plantilla).

## Características

- **Autenticación de Usuario**: Los usuarios deben iniciar sesión o registrarse para navegar por las secciones de la página web.
- **Visualizar Servicios**: Los usuarios pueden visualizar los paquetes de servicios de marketing disponibles.
- **Comentar sobre Paquetes**: Los usuarios autenticados pueden comentar sobre los paquetes de servicios.
- **Gestión del Perfil de Usuario**: Los usuarios pueden editar su perfil, cambiar su contraseña y cerrar sesión.

## Configuración e Instalación

### Prerrequisitos

- Python (se recomienda 3.8 o superior)
- Django (se recomienda 3.2 o superior)

### Instalación

1. Clona el repositorio
   ```sh
   git clone https://github.com/tu_usuario/totalmarketing.git
Navega al directorio del proyecto

sh
Copy code
cd totalmarketing
Instala los paquetes requeridos

sh
Copy code
pip3 install -r requirements.txt
Aplica las migraciones

sh
Copy code
python manage.py migrate
Ejecuta el servidor de desarrollo

sh
Copy code
python manage.py runserver
La aplicación debería estar disponible en http://127.0.0.1:8000/.

Uso
Después de configurar el proyecto, puedes usar las siguientes credenciales para iniciar sesión o puedes crear una nueva cuenta.

Usuario: demo

Contraseña: contraseñademo

Estructura del Proyecto

totalmarketing/: Carpeta principal del proyecto Django.

settings.py: Contiene la configuración del proyecto Django.

urls.py: Define las URLs del proyecto.

marketing/: App de Django que contiene la funcionalidad principal del proyecto.

templates/: Contiene las plantillas HTML.

models.py: Define los modelos de datos.

views.py: Contiene las vistas de la aplicación.

forms.py: Contiene los formularios utilizados en la aplicación.


Pruebas

Para ejecutar las pruebas de la aplicación, usa el siguiente comando:

sh
Copy code
python manage.py test
