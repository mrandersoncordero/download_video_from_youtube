# Proyecto de Descarga y Subida de Videos de YouTube a Google Drive

Este proyecto automatiza la descarga de videos de YouTube y su posterior subida a Google Drive. Utiliza `yt-dlp` para la descarga de videos y `pydrive2` para la autenticación y subida de archivos a Google Drive. El proyecto está diseñado para trabajar con una lista de enlaces de YouTube almacenados en un archivo Excel.

## Estructura del Proyecto

La estructura de directorios y archivos del proyecto es la siguiente:

```sh
.
├── assets # Carpeta para recursos adicionales, como imágenes
├── credencials_module.json # Archivo para almacenar credenciales de Google Drive (generado automáticamente)
├── documents # Carpeta para documentos relacionados con el proyecto
├── downloas.py # Script principal para descargar videos y subirlos a Google Drive
├── drive_quickstart.py # Script para la autenticación inicial con Google Drive
├── enlaces_videos # Carpeta que contiene el archivo Excel con los enlaces de los videos
│   └── enlaces.xlsx # Archivo Excel con la lista de enlaces de YouTube
├── requirements.txt # Archivo con las dependencias del proyecto
├── settings.yaml # Archivo de configuración para pydrive2
└── YT # Carpeta donde se almacenan los videos descargados
```

## Funciones Principales

### `downloas.py`

Este es el script principal del proyecto. Contiene las siguientes funciones:

- **`login()`**: Maneja la autenticación con Google Drive utilizando `pydrive2`. Guarda las credenciales en un archivo JSON.

- **`subir_archivo(ruta_archivo, id_folder)`**: Sube un archivo a una carpeta específica en Google Drive. Utiliza las credenciales guardadas para autenticar la operación.

- **`download_video(link_video)`**: Descarga un video de YouTube usando `yt-dlp` y devuelve la ruta del archivo descargado.

- **`main()`**: Función principal que lee los enlaces de YouTube desde un archivo Excel, descarga cada video, y luego lo sube a Google Drive.

### `drive_quickstart.py`

Este script se utiliza para manejar la autenticación inicial con Google Drive, generando el archivo de credenciales necesario para las operaciones de subida.

## Dependencias

El proyecto requiere las siguientes dependencias, especificadas en el archivo `requirements.txt`:

- **`pandas`**: Utilizado para manejar y leer el archivo Excel con los enlaces de YouTube.
- **`pydrive2`**: Utilizado para la autenticación y la subida de archivos a Google Drive.
- **`yt-dlp`**: Utilizado para la descarga de videos de YouTube.
- **`openpyxl`**: Necesario para leer archivos Excel.

Para instalar las dependencias, utiliza el siguiente comando:

```bash
pip install -r requirements.txt
```

## Configuración
### `settings.yaml`
Este archivo contiene la configuración para pydrive2, incluyendo las credenciales de cliente de Google y los detalles de autenticación.

Ejemplo de configuración (settings.yaml):
```yaml
client_config_backend: settings
client_config:
  client_id: YOUR_CLIENT_ID
  client_secret: YOUR_CLIENT_SECRET

save_credentials: True
save_credentials_backend: file
save_credentials_file: credentials_module.json

get_refresh_token: True

oauth_scope:
 - https://www.googleapis.com/auth/drive
```

## Uso
1. Coloca los enlaces de los videos de YouTube en el archivo enlaces.xlsx dentro de la carpeta enlaces_videos.
2. Ejecuta el script principal:
```sh
python downloas.py
```
El script descargará los videos y los subirá automáticamente a la carpeta especificada en Google Drive.

## Notas
- Asegúrate de que las credenciales de Google Drive estén configuradas correctamente antes de ejecutar el script.
- Los videos descargados se almacenan temporalmente en la carpeta YT.