import yt_dlp
import pandas as pd
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Variables Excel
file_path = "enlaces_videos/enlaces.xlsx"
sheet_name = "Hoja 1"
column_name = "Videos"

# Credenciales de Google Drive
directorio_credenciales = "credencials_module.json"
id_folder = "1WEM4xNMo94oOduRXwVgqM8TSF9vmY4HR"

# Iniciar sesión en Google Drive
def login():
    GoogleAuth.DEFAULT_SETTINGS["client_config_file"] = directorio_credenciales
    gauth = GoogleAuth()

    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8032])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    gauth.SaveCredentialsFile(directorio_credenciales)
    drive = GoogleDrive(gauth)
    return drive

# Subir un archivo a Google Drive
def subir_archivo(ruta_archivo, id_folder):
    drive = login()
    archivo = drive.CreateFile({"parents": [{"id": id_folder}]})
    archivo['title'] = ruta_archivo.split('/')[-1]
    archivo.SetContentFile(ruta_archivo)
    archivo.Upload()

# Descargar video de YouTube
def download_video(link_video, numero):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'/home/ander/Vídeos/Python/Fundamentos/{numero}.- %(title)s.%(ext)s',
        'noplaylist': True  # Permitir la descarga de toda la playlist
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(link_video, download=True)
        return ydl.prepare_filename(result)  # Devuelve la ruta del archivo descargado

def main():
    try:
        # Leer los links del Excel
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        videos = df[column_name].values

        index = 1
        for link_video in videos:
            # Establecer opciones para descargar toda la playlist si el link es una playlist
            ydl_opts = {
                'format': 'best',
                'outtmpl': f'/home/ander/Vídeos/Python/Fundamentos/{index}.- %(title)s.%(ext)s',
                'noplaylist': False  # Permitir la descarga de toda la playlist
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Verificar si es una playlist y extraer los videos
                info_dict = ydl.extract_info(link_video, download=False)
                
                if 'entries' in info_dict:  # Es una playlist
                    for entry in info_dict['entries']:
                        ruta_archivo = download_video(entry['webpage_url'], index)
                        index += 1
                        print(f"Video {entry['webpage_url']} descargado exitosamente como {ruta_archivo}.")
                else:  # Es un video único
                    ruta_archivo = download_video(link_video, index)
                    index += 1
                    print(f"Video {link_video} descargado exitosamente como {ruta_archivo}.")
    except Exception as e:
        print(f"Error al procesar el video {link_video}: {e}")

if __name__ == '__main__':
    main()
