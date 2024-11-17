from setuptools import setup, find_packages

with open('README.md', 'r',encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='shared',
    version='0.1.0',
    description='Shared library for Heimdall services',
    long_description=readme,
    author='Heimdall',
    url='http://10.43.102.250:3000/Heimdall/shared',
    packages=find_packages(
        include=(
            'shared'
        ),
        exclude=(
            'test',
            '.venv'
        )
    )
)
