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
