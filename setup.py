#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy',
    'pandas',
    'gplearn',
    'scipy',
    'deap',
    'bluepyopt',
    'icecream',
    'scikit-learn',
]

test_requirements = []

setup(
    author="Hengzhe Zhang",
    author_email='zhenlingcn@foxmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An open source python library for non-linear piecewise symbolic regression based on Genetic Programming",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pstree',
    name='pstree',
    packages=find_packages(include=['pstree', 'pstree.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hengzhe-zhang/pstree',
    version='0.1.1',
    zip_safe=False,
)
