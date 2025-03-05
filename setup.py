from setuptools import setup, find_packages

setup(
    name='mytoolbox',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['numpy>=1.20'],
    author='Tomasz Rozanski',
    description='Minimal local toolbox module.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)
