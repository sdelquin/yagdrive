![yagdrive-logo](https://raw.githubusercontent.com/sdelquin/yagdrive/main/yagdrive-logo.svg)

**Yet Another Google Drive API Python wrapper!**

`yagdrive` is a Python package based on [PyDrive](https://pythonhosted.org/PyDrive/) which aims to simplify and enhance the operations over the [Google Drive API](https://developers.google.com/drive).

# Installation

```console
$ pip install yagdrive
```

# Auth

In order to get the proper authorization to your Google Drive, it's necessary to perform a couple of steps:

## I. Get client secrets

1. Go to [APIs Console](https://console.cloud.google.com/) and create a new project (or reuse an existing one).
2. Go to [APIs Dashboard](https://console.cloud.google.com/apis/dashboard) inside your project and click on "Enable API and Services". Search for the "Google Drive API" and activate it.
3. Go to [APIS Credentials](https://console.cloud.google.com/apis/credentials) on the left panel and click on "Create Credentials". Select "OAuth client ID". Then select "Desktop application" and give a name.
4. Click on "Download JSON", save the file as `client_secrets.json` and place it on the current work directory.

## II. Get credentials

Having `client_secrets.json` in the current work directory (as explained at previous section), just run:

```console
$ python -c "from yagdrive import auth; auth.get_credentials()"
```

A browser is launched and you'll have to authorize the access to Google Drive. Follow the instructions. Note that enabling [Less secure apps](https://support.google.com/accounts/answer/6010255) might be required.

If everything was fine, you'll get two files on the current work directory:

- `gdrive-credentials.json`: authorization token next to other relevant fields.
- `gdrive-secrets.json`: renamed file from `client-secrets.json`.

> 🎒 &nbsp;These two files are required for yagmail to properly work.

> ⚠️️ &nbsp;You shouldn't share these files or include them in a public respository.

# Usage

First of all you must create the **handler**:

```python
>>> from yagdrive import GDrive

>>> drive = GDrive()
```

You can pass two arguments to `GDrive()`:

- `credentials_file` (default: `'gdrive-credentials.json'`)
- `secrets_file` (default: `'gdrive-secrets.json'`)

## Upload a file

```python
>>> drive.put('/home/yagdrive/hello.json')
```

![Boom easy](https://i.imgur.com/UIMz2Lu.gif)

`put()` method returns an instance of [pydrive.files.GoogleDriveFile](https://pythonhosted.org/PyDrive/pydrive.html#pydrive.files.GoogleDriveFile). Many fields are available in that object as a _parsed json_. For instance you could get the **download link**:

```python
>>> f = drive.put('/home/yagdrive/hello.json')

>>> f['webContentLink']
'https://drive.google.com/uc?id=2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm&export=download'

# check f.keys() for the whole list of fields
```

See more **use cases**:

```python
# Set a custom title for the uploaded file
>>> drive.put('/home/yagdrive/hello.json', title='Say hi to the world')
# Do not overwrite files with the same name
>>> drive.put('/home/yagdrive/hello.json', overwrite=False)
```

> ⚠️️ &nbsp;By default, `put()` uploads the file to the `root` of Google Drive. This behaviour can be changed using `cd()` method.

## Change directory

You can change the remote work directory (for yagmail) on Google Drive using the following:

```python
>>> drive.cd('IOx1Q2ZuQb7ZfGjdmwfnD6Fig1pBlnAnp)
'python-scripts'
```

The only argument is the id of the folder. It returns the title of the folder.

### Present work directory

You can check the present work directory using the following code:

```python
>>> drive.pwd
'python-scripts'
```

## Download a file

You can download a file using its **identifier**:

```python
>>> local_file, remote_file = drive.get_by_id('2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm')

>>> local_file
PosixPath('hello.json')

>>> type(remote_file)
pydrive.files.GoogleDriveFile
```

Or you can even download a file using its **title**:

```python
>>> local_file, remote_file = drive.get_by_title('hello.json')

>>> local_file
PosixPath('hello.json')

>>> type(remote_file)
pydrive.files.GoogleDriveFile
```

### Filename

Both approaches allow you to indicate an **explicit filename** for the downloaded resource:

```python
>>> local_file, remote_file = drive.get_by_id(
        file_id='2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm',
        output_filename='testing.json'
    )

>>> local_file
PosixPath('testing.json')
```

### Mimetype

Both approaches allow **mimetype** specification:

```python
>>> local_file, remote_file = drive.get_by_id(
        file_id='2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm',
        mimetype='application/json'
    )
```

> 🎒 &nbsp;This is quite useful when handling **Google Drive native formats** (Docs, Sheets, Slides, Forms, Drawings).

You can check out the [list of mimetypes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types).

#### Mimetype automatic detection

If an output filename is indicated when downloading a file, an automatic detection of the mimetype is performed based on the filename suffix, as long as the remote file won't be downloadable:

```python
>>> local_file, remote_file = drive.get_by_id(
        # Suppose the remote file is a Google Spreadsheet
        file_id='jfi1xD1punnQwdFlAO6QZG7mBZIb2nfpg',
        output_filename='/tmp/data.xlsx'
    )
```

On the above example, no mimetype is indicated, hence the automatic detection passes `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` as mimetype.

## Delete a file

You can delete a file using its **identifier**:

```python
>>> drive.del_by_id('2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm')
```

Or you can even delete a file using its **title**:

```python
>>> drive.del_by_title('hello.json')
```

> ⚠️️ &nbsp;These methods **do not move the files to the trash**; they **definitely removes** the file.

## List contents of a folder

You can list the files (and directories) within a remote folder on Google Drive as follows:

```python
>>> for file in drive.ls():
...     print(file['title'], '|', file['id'])

Hello world | lV16YGlUV52eapO2QYlmLNQw0pRkvMJLQGIsWtTpk1VxayZtKTZe10W2RtEXiB655XVnMHfO
Salut monde | MVZ1T51mt22p2LiTRGltBnkeQ0YvQlVJfeHYw1GWZREVKOs0OVIaatLkpQpx566XUyNlMW5X
Ahoj světe | JKVM5tpRYtkpGHwY60fOOatak1LTRVWTpZQV5l1y0MlxUWLm5V2Z2eEGe1NQXn6lXIQsi2vB
Ciao mondo | ykZ62R21QMiLsMavYRXfet0OVVtmVWknVI5X5llpKJGQH65YaGTQNwW1l21xBEp0TOtpLUeZ
```

> ⚠️️ &nbsp;`ls()` returns a **generator**. Keep that in mind!

# Changelog

Check the [Changelog](CHANGELOG.md) for bug fixes, enhancements and features.

# License

[MIT](LICENSE)
