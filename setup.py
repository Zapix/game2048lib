# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='game2048lib',
    version='0.1.0',
    author='Aleksandr Aibulatov',
    author_email='zap.aibulatov@gmail.com',
    packages=['game2048lib', 'game2048lib.test'],
    url='https://github.com/Zapix/game2048lib',
    license='LICENSE',
    description='Simple library for playing 2048(http://gabrielecirulli.github.io/2048/) on python.',
    long_description=open('README.md').read(),
    install_requires=[
        "selenium >= 2.42.1",
    ],
)