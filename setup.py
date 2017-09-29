# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
setup(
    name='ithin',
    version='0.0',
    entry_points={'console_scripts': ['ithin=ithin.cli:cli']},
    author='Valohai',
    author_email='hait@valohai.com',
    license='MIT',
    install_requires=[
        'click>=6.0',
        'Pillow>=4.0',
    ],
    packages=find_packages(include=('ithin*',)),
)
