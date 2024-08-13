import os
from pydrive.auth import GoogleAuth

os.remove("credentials_module.json") # delete old acccess token file

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
