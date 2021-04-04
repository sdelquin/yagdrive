# Download a file

Every file in Google Drive has [its own **identifier**](https://stackoverflow.com/a/48855034) represented as a large unique slug, but it also has a title. YagDrive provides both methods to retrieve a remote resource:

````{tabbed} Downloading by identifier

```pycon
>>> local_file, remote_file = drive.get_by_id('2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm')

>>> local_file
PosixPath('hello.json')

>>> type(remote_file)
pydrive.files.GoogleDriveFile
```

````

````{tabbed} Downloading by title

```pycon
>>> local_file, remote_file = drive.get_by_title('hello.json')

>>> local_file
PosixPath('hello.json')

>>> type(remote_file)
pydrive.files.GoogleDriveFile
```

:::{important}
File is searched by its title in the _present work directory_. You [can change it](folder.md#change-directory).
:::

````

## Setting a filename

Both approaches allow you to indicate an **explicit filename** for the downloaded resource:

```pycon
>>> local_file, remote_file = drive.get_by_id(
...     file_id='2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm',
...     output_filename='testing.json'
... )

>>> local_file
PosixPath('testing.json')
```

## Using mimetype

Both approaches allow **mimetype**[^mimetype] specification:

```pycon
>>> local_file, remote_file = drive.get_by_id(
...     file_id='2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm',
...     mimetype='application/json'
... )
```

:::{tip}
This is quite useful when handling with **Google Drive native formats** (Docs, Sheets, Slides, Forms, Drawings).
:::

:::{seealso}
Here you can check out the [list of available mimetypes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types).
:::

### Mimetype automatic detection

If an output filename is indicated when downloading a file, an automatic detection of the mimetype is performed based on the filename suffix, as long as the remote file won't be downloadable.

Guess that we need to download a remote file which is a Google Spreadsheet:

```python
local_file, remote_file = drive.get_by_id(
    file_id='jfi1xD1punnQwdFlAO6QZG7mBZIb2nfpg',
    output_filename='/tmp/data.xlsx'
)
```

On the above example, no mimetype is indicated, hence the automatic detection passes `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` as mimetype.

:::{seealso}
{fa}`cogs, text-primary mr-1` [yagdrive.core.GDrive.get_by_id](yagdrive.core.GDrive.get_by_id) \
{fa}`cogs, text-primary mr-1` [yagdrive.core.GDrive.get_by_title](yagdrive.core.GDrive.get_by_title)
:::

[^mimetype]: A media type (formerly known as MIME type) is a two-part identifier for file formats and format contents transmitted on the Internet.
