import pytest

from yagdrive import GDrive


@pytest.fixture
def drive():
    return GDrive()


def test_init(drive):
    assert type(drive).__name__ == 'GDrive'
    assert type(drive.drive).__name__ == 'GoogleDrive'


def test_put(drive):
    filename = 'README.md'
    f = drive.put(filename)
    assert f['title'] == filename
    drive.del_by_id(f['id'])


def test_put_title(drive):
    title = 'Yet another README file'
    f = drive.put('README.md', title=title)
    assert f['title'] == title
    drive.del_by_id(f['id'])


def test_put_overwrite(drive):
    filename = 'README.md'
    f1 = drive.put(filename)
    f2 = drive.put(filename, overwrite=False)
    file_ids = [f['id'] for f in drive.ls()]
    f1_id, f2_id = f1['id'], f2['id']
    assert f1_id in file_ids
    assert f2_id in file_ids
    drive.del_by_id(f1_id)
    drive.del_by_id(f2_id)


def test_get_by_id(drive):
    filename = 'README.md'
    f = drive.put(filename)
    filepath, file = drive.get_by_id(f['id'])
    assert filepath.name == filename
    assert file['id'] == f['id']
    drive.del_by_id(f['id'])


def test_get_by_id_with_mimetype(drive):
    filename = 'README.md'
    f = drive.put(filename)
    filepath, file = drive.get_by_id(f['id'], mimetype='text/html')
    assert filepath.name == filename
    assert file['id'] == f['id']
    drive.del_by_id(f['id'])


def test_get_by_id_with_filename(drive):
    filename = 'README.md'
    f = drive.put(filename)
    output_filename = 'TEST.md'
    filepath, file = drive.get_by_id(f['id'], output_filename=output_filename)
    assert filepath.name == output_filename
    assert file['id'] == f['id']
    drive.del_by_id(f['id'])
    filepath.unlink()


def test_get_by_title(drive):
    filename = 'README.md'
    f = drive.put(filename)
    filepath, file = drive.get_by_title(filename)
    assert filepath.name == filename
    assert file['id'] == f['id']
    drive.del_by_id(f['id'])


def test_get_by_title_with_mimetype(drive):
    filename = 'README.md'
    f = drive.put(filename)
    filepath, file = drive.get_by_title(filename, mimetype='text/html')
    assert filepath.name == filename
    assert file['id'] == f['id']
    drive.del_by_id(f['id'])


def test_get_by_title_with_filename(drive):
    filename = 'README.md'
    f = drive.put(filename)
    output_filename = 'TEST.md'
    filepath, file = drive.get_by_title(filename, output_filename=output_filename)
    assert filepath.name == output_filename
    assert file['id'] == f['id']
    drive.del_by_id(f['id'])
    filepath.unlink()


def test_ls(drive):
    files = drive.ls()
    assert all(['id' in f for f in files])
    assert all(['title' in f for f in files])


def test_pwd(drive):
    assert drive.pwd.upper() == 'MI UNIDAD'


def test_cd(drive):
    assert drive.cd().upper() == 'MI UNIDAD'


def test_del_by_id(drive):
    filename = 'README.md'
    f = drive.put(filename)
    assert any([f['title'] == filename for f in drive.ls()])
    drive.del_by_id(f['id'])
    assert sum([f['title'] == filename for f in drive.ls()]) == 0


def test_del_by_title(drive):
    filename = 'README.md'
    f = drive.put(filename)
    assert any([f['title'] == filename for f in drive.ls()])
    drive.del_by_title(f['title'])
    assert sum([f['title'] == filename for f in drive.ls()]) == 0
