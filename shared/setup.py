import os

from setuptools import setup, find_packages

README_PATH = os.path.join(os.getcwd(), 'README.md')

with open(README_PATH, 'r',encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='shared',
    version='0.0.1',
    description='Shared library for Heimdall services',
    long_description=readme,
    author='Heimdall',
    packages=find_packages(
        exclude=[
            'test',
        ]
    )
)
