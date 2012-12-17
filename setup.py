import os
from setuptools import setup, find_packages

import singleactiveobject


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-singleactiveobject',
    version=singleactiveobject.__version__,
    description='Model mixin that ensures there is only one active model instance in your database.',
    long_description=read('README.md'),
    license=read('LICENSE'),
    author='byteweaver',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-singleactiveobject',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
    ],
    test_suite='singleactiveobject.tests',
)
