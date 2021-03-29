from pathlib import Path

from setuptools import setup

setup(
    name="yagdrive",
    version="1.1.0",
    url="https://github.com/sdelquin/yagdrive.git",
    author="Sergio Delgado Quintero",
    author_email="sdelquin@gmail.com",
    license='MIT',
    description="Yet Another Google Drive API Python wrapper",
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=["yagdrive"],
    install_requires=["pydrive"],
    python_requires='>=3.6',
)
