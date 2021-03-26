from pathlib import Path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GDrive:
    def __init__(
        self,
        credentials_file='gdrive-credentials.json',
        secrets_file='gdrive-secrets.json',
    ):
        GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = secrets_file
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(credentials_file)
        self.drive = GoogleDrive(gauth)

    def upload(self, source_path: str, title=None, folder_id='root'):
        source_file = Path(source_path)
        title = title or source_file.name
        file = self.drive.CreateFile(
            {
                'title': title,
                'parents': [{'id': folder_id}],
            }
        )
        file.SetContentFile(source_file)
        file.Upload()
        return file['id']
