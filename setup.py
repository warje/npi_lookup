import sys

from setuptools import setup, find_packages


setup(
    name='npi_lookup',
    version='1.0.0',
    packages=find_packages(),
    description=('NPI regestry lookup scripts for axuall homework'),
    install_requires=[
        'requests',
        'openpyxl'
    ],
    scripts=['bin/lookup_sync'],
)
