from setuptools import setup, find_packages

setup(
    name='flask-lte-admin',
    packages=find_packages(),
    version='0.2',
    description='Integrates LteAdmin into flask-admin',
    author='Alex Belyaev',
    author_email='a.v.belyaev@gmail.com',
    setup_requires=[
        'setuptools-bower'
    ],
    install_requires=[
        'flask-admin>=1.4.0'
    ],
)
