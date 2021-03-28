from pydrive.auth import GoogleAuth
import os


def get_credentials():
    """
    Get credentials to access Google Drive API.

    A browser is opened with an authorization window.
    Keep in mind that less secure apps might needed be enabled.

    This function expects a file called client_secrets.json in the current folder.
    """
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile('gdrive-credentials.json')
    os.rename('client_secrets.json', 'gdrive-secrets.json')
