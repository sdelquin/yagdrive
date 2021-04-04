# Getting Started

This page describes how to get started with YagDrive, with a focus on authentication process.

## Installation

{{ pypi }}

```console
$ pip install yagdrive
```

## Authentication

In order to get the proper authorization to your Google Drive, it's necessary to perform a couple of steps:

{fa}`user-secret,text-secondary mr-1` [Get client secrets from the Google Cloud Console](#get-client-secrets). \
{fa}`key,text-secondary mr-1` [Get credentials from the authentication process](#get-credentials).

### Get client secrets

1. Go to [APIs Console](https://console.cloud.google.com/) and create a new project (or reuse an existing one).
2. Go to [APIs Dashboard](https://console.cloud.google.com/apis/dashboard) inside your project and click on "Enable API and Services". Search for the "Google Drive API" and activate it.
3. Go to [APIS Credentials](https://console.cloud.google.com/apis/credentials) on the left panel and click on "Create Credentials". Select "OAuth client ID". Then select "Desktop application" and give a name.
4. Click on "Download JSON", save the file as `client_secrets.json` and place it on the current work directory.

### Get credentials

Having `client_secrets.json` in the current work directory (as explained at previous section), just run:

```console
$ python -c "from yagdrive import auth; auth.get_credentials()"
```

A browser is launched and you'll have to authorize the access to Google Drive. Follow the instructions. Note that enabling [Less secure apps](https://support.google.com/accounts/answer/6010255) might be required.

If everything was fine, you'll get two files on the current work directory:

- `gdrive-credentials.json`: authorization token next to other relevant fields.
- `gdrive-secrets.json`: renamed file from `client-secrets.json`.

:::{important}
These two files are required for yagmail to properly work.
:::

:::{danger}
For security reasons, you shouldn't share these files or include them in a public respository.
:::

## Handler

Yagdrive is an OOP oriented package. First of all you must create the handler:

```python
from yagdrive import GDrive

drive = GDrive()
```

You can pass two arguments to [GDrive](yagdrive.core.GDrive.__init__):

| Parameter          | Default                   |
| ------------------ | ------------------------- |
| `credentials_file` | `gdrive-credentials.json` |
| `secrets_file`     | `gdrive-secrets.json`     |

% Links
[pypi-badge]: https://img.shields.io/pypi/v/yagdrive
[pypi-url]: https://pypi.org/project/yagdrive/
