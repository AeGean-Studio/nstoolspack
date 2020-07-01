# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages


setup(
    name='nstoolspack',
    use_scm_version=True,
    description='A fraction of features in skydark/nstools',
    author='AeGean-Studio',
    author_email='wyqsmith@aegeanstudio.com',
    url='https://github.com/AeGean-Studio/nstoolspack',
    license='BSD',
    packages=find_packages(exclude=('tests*', 'example*')),
    setup_requires=['setuptools_scm'],
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
