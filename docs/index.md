# YagDrive documentation

{{ pypi }} {{ github }}

**Yet Another Google Drive API Python wrapper**.

Welcome to YagDrive's documentation. This is a Python package based on [PyDrive][pydrive] which aims to simplify and enhance the operations over the [Google Drive API][gda].

YagDrive has the following main features:

{fa}`check,text-success mr-1` Simplified authentication process
: Forget about complicated steps to get authentication.

{fa}`check,text-success mr-1` Upload & Download files made easy
: Direct access to local & remote files.

{fa}`check,text-success mr-1` Management of mimetypes
: Get any remote contents with mimetype autodetection.

{fa}`check,text-success mr-1` File listing & folder selection
: Setting remote pwd and listing files is so simple.

## Site contents

```{toctree}
---
maxdepth: 2
---
tutorial/intro.md
tutorial/upload.md
tutorial/folder.md
tutorial/download.md
api/core.md
```

## Acknowledgements

This project is heavily inspired by (and dependent on) [PyDrive package][pydrive] for its base structure and configuration.

% Links
[pydrive]: https://pythonhosted.org/PyDrive/
[gda]: https://developers.google.com/drive
