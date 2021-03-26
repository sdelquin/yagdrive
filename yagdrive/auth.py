from pydrive.auth import GoogleAuth
import os


def get_credentials():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile('gdrive-credentials.json')
    os.rename('client_secrets.json', 'gdrive-secrets.json')
