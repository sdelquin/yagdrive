# Folder Management

YagDrive keeps the state of the present remote work folder. Initially **the uploaded files go to the root of the drive**, but this behaviour can be modified.

## Change directory

You can change the remote work directory (for yagmail) on Google Drive using the following:

```python
drive.cd('IOx1Q2ZuQb7ZfGjdmwfnD6Fig1pBlnAnp)
```

The only required argument is the id of the folder. **It returns the title of the folder**.

:::{seealso}
{fa}`cogs, text-primary mr-1` [yagdrive.core.GDrive.cd](yagdrive.core.GDrive.cd)
:::

## Present work directory

You can check the present (remote) work directory using the following code:

```python
print(drive.pwd)
# python-scripts
```

## List contents of a folder

You can list the files (and directories) within a remote folder on Google Drive as follows:

```ipython
>>> for file in drive.ls():
...     print(file['title'], '|', file['id'])

Hello world | lV16YGlUV52eapO2QYlmLNQw0pRkvMJLQGIsWtTpk1VxayZtKTZe10W2RtEXiB655XVnMHfO
Salut monde | MVZ1T51mt22p2LiTRGltBnkeQ0YvQlVJfeHYw1GWZREVKOs0OVIaatLkpQpx566XUyNlMW5X
Ahoj světe | JKVM5tpRYtkpGHwY60fOOatak1LTRVWTpZQV5l1y0MlxUWLm5V2Z2eEGe1NQXn6lXIQsi2vB
Ciao mondo | ykZ62R21QMiLsMavYRXfet0OVVtmVWknVI5X5llpKJGQH65YaGTQNwW1l21xBEp0TOtpLUeZ
```

:::{hint}
[`ls()`](yagdrive.core.GDrive.ls) returns a **generator**. Keep that in mind!
:::

## Delete a file

You can [delete a file using its **identifier**](yagdrive.core.GDrive.del_by_id):

```python
drive.del_by_id('2QFfbG1IjBnAndp6gwZD7nQixOlup1Zfm')
```

Or you can even [delete a file using its **title**](yagdrive.core.GDrive.del_by_title):

```python
drive.del_by_title('hello.json')
```

:::{danger}
These methods **do not move the files to the trash**; they **definitely removes** them.
:::
