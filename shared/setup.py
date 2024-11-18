from setuptools import setup, find_packages
import os

README_PATH = os.path.join(os.getcwd(), 'README.md')

with open(README_PATH, 'r', encoding='UTF-8') as f:
    readme = f.read()

VERSION = '0.0.1'

setup(
    name='modi',
    version=VERSION,
    description='Shared library for Heimdall services',
    long_description=readme,
    long_description_content_type='text/markdown', 
    author='Heimdall',
    packages=find_packages(include=['modi', 'modi.*']),
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
