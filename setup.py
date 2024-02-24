from setuptools import setup, find_packages

readmeText=""

with open("README.md", "r") as f:
    readmeText+=f.read()

setup(
    name='azol',
    version='0.1.1b3',
    packages=find_packages(),
    url='https://github.com/cdburkard/azol',
    author='Cody Burkard',
    description='A python-based pentesting library for Azure and Entra ID',
    long_description=readmeText,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests==2.31.0",
        "dataclasses==0.6"
    ]
)