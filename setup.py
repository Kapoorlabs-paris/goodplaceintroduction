import setuptools
from setuptools import setup
from os import path

_dir = path.dirname(__file__)


with open('README.md') as f:
    long_description = f.read()
with open(path.join(_dir,'goodplaceintroduction','_version.py'), encoding="utf-8") as f:
    exec(f.read())

setup(
    name="goodplaceintroduction",

    version=__version__,

    author='Varun Kapoor',
    author_email='randomaccessiblekapoor@gmail.com',
    url='https://github.com/Kapoorlabs-paris/goodplaceintroduction/',
    description='Create a basic python package.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        
        "slimoneat",
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
    ],
)
