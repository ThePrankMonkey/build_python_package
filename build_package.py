# import getopt
import os
import sys


package_name = sys.argv[1]


# Make Folders
folders = [
    f"./{package_name}/src/{package_name}",
    f"./{package_name}/tests"
]
for folder in folders:
    try:
        os.makedirs(folder)
    except FileExistsError:
        pass


# Make setup.py
content = f'''from setuptools import find_packages, setup

setup(
    name='{package_name}',
    version='0.1.0',
    package_dir={ "{" }'': 'src'{ "}" },
    packages=find_packages(where='src')
)
'''
filepath = f"./{package_name}/setup.py"
with open(filepath, 'w') as f:
    f.write(content)


# Make __init__.py
filepaths = [
    f"./{package_name}/src/{package_name}/__init__.py",
    f"./{package_name}/tests/__init__.py"
]
for filepath in filepaths:
    with open(filepath, 'w') as f:
        f.write("")


# Make README.md
content = f'''# {package_name}

## Description

## Setup

## References
'''
filepath = f"./{package_name}/README.md"
with open(filepath, 'w') as f:
    f.write(content)


# Make sample test
content = f'''import pytest
import {package_name}

def test_start():
    assert 1 == 1
'''
filepath = f"./{package_name}/tests/test_{package_name}.py"
with open(filepath, 'w') as f:\
    f.write(content)
