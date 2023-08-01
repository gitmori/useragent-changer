#!/usr/bin/env python3
from setuptools import setup, find_packages
from useragent_changer import __version__, __description__, __author__, __author_email__, __keywords__, __url__, __license__

PACKAGES = find_packages()
NAME = find_packages()[0]
VERSION = __version__
DESCRIPTION = __description__

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
AUTHOR = __author__
AUTHOR_EMAIL = __author_email__
KEYWORDS = __keywords__
URL = __url__

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11'
]

LICENSE = __license__
PYTHON_REQUIRES = '>=3.6.5'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    keywords=KEYWORDS,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    package_dir={NAME: NAME},
    package_data={NAME: ['platform_list/*']},
    classifiers=CLASSIFIERS,
    license=LICENSE,
    python_requires=PYTHON_REQUIRES
)