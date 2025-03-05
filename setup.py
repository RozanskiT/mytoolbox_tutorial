from setuptools import setup, find_packages

setup(
    name='mytoolbox',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20',
    ],
    python_requires='>=3.8',
)
