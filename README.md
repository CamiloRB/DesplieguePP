## Bienvenido ^^

## este proyecto esta desarrollado en python 3.8.5

## Arquitectura del proyecto

 |- Buscador - Carpeta que contiene toda la logica del proyecto
 |- static - Carpeta que contiene todos los archivos que usa el proyecto
	*--
	  |- css - Carpeta que contiene todo lo relacionado con estilos
	  |- img - Carpeta que contiene las imagenes del proyecto
	  |- js - Carpeta que contiene los script
	  |- RedNeu - Carpeta que contiene los modelos que se ejecutan
	  |- Resoluciones - Carpeta que contiene los pdf de las resoluciones
	  |- scss - Carpeta que contiene estilos
	*--
 |- templates - Carpeta que contiene las vistas que se muestran en el proyecto
 |- Tesis - Carpeta que contiene la configuracion del proyecto 
	

## Paso 1. Instalar Conda
https://www.anaconda.com/products/individual

## Paso 2. Crear ambiente
Con conda instalado se ejecuta el comando

conda create --name py38 python=3.8.5

## Paso 3. Inciar el ambiente
Se inicia con el comando

conda activate py38

## Paso 4. Nos movilizamos a la carpeta del proyectoc con el ambiente iniciado

## Paso 5. Ya en la carpeta del proyecto se instalan las librerias con el comando
pip install -r requirements.txt

## Paso 5. Iniciar el proyecto
python manage.py runserver