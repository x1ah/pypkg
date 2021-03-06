# coding: utf-8

import io

from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='{{cookiecutter.pypi_name}}',

    version='0.0.1',

    description='{{cookiecutter.desc}}',
    long_description=long_description,
    url='https://github.com/{{cookiecutter.author}}/{{cookiecutter.project_name}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    packages=find_packages(exclude=['docs', 'tests*']),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[],
    include_package_data=True
)
