#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Fetch",
    author_email='jl13122@nyu.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Fetch the Lattest",
    entry_points={
        'console_scripts': [
            'Fetch=Fetch.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='Fetch',
    name='Fetch',
    packages=find_packages(include=['Fetch', 'Fetch.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/VincentPit/Fetch',
    version='0',
    zip_safe=False,
)
