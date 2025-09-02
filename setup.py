from setuptools import setup

setup(
    name='Fuentes',
    version='0.1',
    description='Package for plotting decision regions and data manipulation',
    author='Cesar Estrebou',
    packages=['Fuentes'],
    install_requires=[
        'numpy',
        'matplotlib',
        'pandas',
        'IPython',
    ],
)