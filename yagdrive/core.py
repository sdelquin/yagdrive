from pathlib import Path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

ROOT_FOLDER_ID = 'root'


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
        self.cwd = 'root'

    def put(self, source_path: str, title=None, overwrite=True):
        source_file = Path(source_path)
        title = title or source_file.name
        file = self.drive.CreateFile(
            {
                'title': title,
                'parents': [{'id': self.cwd}],
            }
        )
        if overwrite:
            for remote_file in self.ls():
                if remote_file['title'] == title:
                    file = self.drive.CreateFile({'id': remote_file['id']})
                    break
        file.SetContentFile(source_file)
        file.Upload()
        return file

    def get_by_id(self, file_id: str):
        file = self.drive.CreateFile({'id': file_id})
        filename = file['title']
        file.GetContentFile(filename)
        return Path(filename), file

    def get_by_title(self, title: str):
        for file in self.ls():
            if file['title'] == title:
                return self.get_by_id(file['id'])

    def ls(self):
        q = f"'{self.cwd}' in parents and trashed=False"
        yield from self.drive.ListFile({'q': q}).GetList()

    def cd(self, folder_id='root'):
        self.cwd = folder_id
