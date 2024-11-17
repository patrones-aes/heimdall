import os

from setuptools import setup, find_packages

README_PATH = os.path.join(os.getcwd(), 'README.md')

with open(README_PATH, 'r',encoding='UTF-8') as f:
    readme = f.read()

VERSION = '0.0.2'

setup(
    name='shared',
    version=VERSION,
    description='Shared library for Heimdall services',
    long_description=readme,
    author='Heimdall',
    packages=find_packages(
        include=[
            'shared'
        ],
        exclude=[
            'test',
        ]
    ),
    install_requires=[
        'boto3==1.35.63'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.13',
        'Intended Audience :: Developers',
        'Operating System :: Unix'
    ]
)
