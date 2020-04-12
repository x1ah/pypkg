# coding: utf-8

import io

from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ipanda',

    version='0.0.1',

    description='Generate by cookiecutter',
    long_description=long_description,
    url='https://github.com/x1ah/ipanda',
    author='x1ah',
    author_email='x1ahgxq@gmail.com',
    packages=find_packages(exclude=['docs', 'tests*']),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[],
    include_package_data=True
)
