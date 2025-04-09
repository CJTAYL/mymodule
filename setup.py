from setuptools import setup, find_packages

setup(
    name='mymodule',
    version='0.1.0',
    description='A simple hello world Python module',
    author='Christopher Taylor',
    author_email='CJTAYL2@gmail.com',
    packages=find_packages(),
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)