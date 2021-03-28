from pathlib import Path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

ROOT_FOLDER_ID = 'root'


class GDrive:
    """
    Wrapper on pydrive.drive.GoogleDrive.
    """

    def __init__(
        self,
        credentials_file='gdrive-credentials.json',
        secrets_file='gdrive-secrets.json',
    ):
        """
        Load credentials and build Google Drive handler.

        Parameters
        ----------
        credentials_file: str
            Path to the file containing credentials to access Google Drive.
        secrets_file: str
            Path to the file containing client secrets to access Google Drive.
        """
        GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = secrets_file
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(credentials_file)
        self.drive = GoogleDrive(gauth)
        self.workdir = 'root'

    def put(self, source_path: str, title=None, overwrite=True):
        """
        Upload a file to Google Drive.

        Parameters
        ----------
        source_path: str
            Path to the local file to upload.
        title: str
            Title for the uploaded file. If not specified the filename of the local file is
            used as the title for the uploaded file.
        overwrite: bool
            If True no duplicates can happen on uploaded files. Otherwise a new remote file
            is created (with the same name) if a same file exists.

        Returns
        -------
        pydrive.files.GoogleDriveFile
            Object representing the remote file on Google Drive.
        """
        source_file = Path(source_path)
        title = title or source_file.name
        file = self.drive.CreateFile(
            {
                'title': title,
                'parents': [{'id': self.workdir}],
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
        """
        Download a file through its identifier.

        Parameters
        ----------
        file_id: str
            Google Drive identifier (slug) of the file to be downloaded.

        Returns
        -------
        pathlib.Path
            Handler of the local downloaded file (same name as the uploaded file).
        pydrive.files.GoogleDriveFile
            Object representing the remote file on Google Drive.
        """
        file = self.drive.CreateFile({'id': file_id})
        filename = file['title']
        file.GetContentFile(filename)
        return Path(filename), file

    def get_by_title(self, title: str):
        """
        Download a file through its title.

        Parameters
        ----------
        title: str
            Google Drive title of the file to be downloaded.

        Returns
        -------
        pathlib.Path
            Handler of the local downloaded file (same name as the uploaded file).
        pydrive.files.GoogleDriveFile
            Object representing the remote file on Google Drive.
        """
        for file in self.ls():
            if file['title'] == title:
                return self.get_by_id(file['id'])

    def ls(self):
        """
        List of files/folders on the present work remote directory.

        Yields
        ------
        pydrive.files.GoogleDriveFile
            Object representing the remote file on Google Drive.
        """
        q = f"'{self.workdir}' in parents and trashed=False"
        yield from self.drive.ListFile({'q': q}).GetList()

    @property
    def pwd(self):
        """
        Present work directory.

        Returns
        -------
        str
            Title of the present work directory (remote folder on Google Drive).
        """
        file = self.drive.CreateFile({'id': self.workdir})
        return file['title']

    def cd(self, folder_id='root'):
        """
        Change present work directory on remote Google Drive.

        Parameters
        ----------
        folder_id: str
            Google Drive identifier of the folder to change to.

        Returns
        -------
        str
            Title of the present work directory (remote folder on Google Drive).
        """
        self.workdir = folder_id
        return self.pwd

    def del_by_id(self, file_id: str):
        """
        Delete a file through its identifier (no trash recovery).

        Parameters
        ----------
        file_id: str
            Google Drive identifier (slug) of the file to be downloaded.
        """
        file = self.drive.CreateFile({'id': file_id})
        file.Delete()

    def del_by_title(self, title: str):
        """
        Delete a file through its title.

        Parameters
        ----------
        title: str
            Google Drive title of the file to be downloaded.
        """
        for file in self.ls():
            if file['title'] == title:
                file.Delete()
                break
