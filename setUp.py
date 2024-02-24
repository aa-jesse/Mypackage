from setuptools import setup, find_packages

setup(
    name='Mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    license='RIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires = ['numpy'],
    author='jesse akowuah',
    author_email='akowuahadujesse@gmail.com'
)