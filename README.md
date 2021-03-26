![yagdrive-logo](yagdrive-logo.svg)

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

## Upload a file

```python
>>> drive.put('/home/yagdrive/hello.json')
```

![Boom easy](https://im3.ezgif.com/tmp/ezgif-3-5ff55c12e859.gif)

`put()` method returns an instance of [pydrive.files.GoogleDriveFile](https://pythonhosted.org/PyDrive/pydrive.html#pydrive.files.GoogleDriveFile). Many fields are available in that object as a _parsed json_. For instance you could get the **download link**:

```python
>>> f = drive.put('/home/yagdrive/hello.json')

>>> f['webContentLink']
'https://drive.google.com/uc?id=2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm&export=download'

# check f.keys() for the whole list of fields
```

<details>
  <summary>See more use cases:</summary>

```python
# Set a custom title for the uploaded file
>>> drive.put('/home/yagdrive/hello.json', title='Say hi to the world')
# Do not overwrite files with the same name
>>> drive.put('/home/yagdrive/hello.json', overwrite=False)
```

</details><br>

> ⚠️️ &nbsp;By default, `put()` uploads the file to the `root` of Google Drive. This behaviour can be changed using `cd()` method.

## Change directory

You can change the remote work directory (for yagmail) on Google Drive using the following:

```python
>>> drive.cd('IOx1Q2ZuQb7ZfGjdmwfnD6Fig1pBlnAnp)
```

> 🎒 &nbsp;Argument is the id of the folder.

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

## Delete a file

You can delete a file using its **identifier**:

```python
>>> drive.del_by_id('2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm')
```

Or you can even delete a file using its **title**:

```python
>>> drive.del_by_title('hello.json')
```

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
