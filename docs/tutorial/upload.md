# Upload a file

Guess you want to upload a local file located in `/home/yagdrive/hello.json`. This is as easy as:

```python
drive.put('/home/yagdrive/hello.json')
```

![Boom easy](https://i.imgur.com/UIMz2Lu.gif)

[put()](yagdrive.core.GDrive.put) method returns an instance of [pydrive.files.GoogleDriveFile](https://pythonhosted.org/PyDrive/pydrive.html#pydrive.files.GoogleDriveFile). Many fields are available in that object as a _parsed json_. For instance you could get the **download link**:

```python
f = drive.put('/home/yagdrive/hello.json')

print(f['webContentLink'])
# https://drive.google.com/uc?id=2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm&export=download
```

:::{tip}
Check `f.keys()` for the whole list of fields.
:::

## Custom title

By default, when you upload a file, YagDrive takes the name from its filename (last part of the path). You can specify a custom title, though:

```python
drive.put('/home/yagdrive/hello.json', title='Say hi to the world')
```

## Overwriting

By default, when you upload a file, YagDrive overwrite an existing remote file with the same name (title). You can change this behaviour, though:

```
drive.put('/home/yagdrive/hello.json', overwrite=False)
```

In this case a new `hello.json` file will be stored even if it already exists in Google Drive.

:::{caution}
By default, `put()` uploads the file to the `root` of your Google Drive. This behaviour can be changed [using `cd()` method](folder.md#change-directory).
:::
