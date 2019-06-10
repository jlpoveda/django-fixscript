import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-fixscript',
    version='0.1',
    packages=['fixscript'],
    description='A library to run scripts on deploy process',
    long_description=README,
    author='Jose Luis Poveda',
    author_email='jlpoveda@gmail.com',
    url='https://github.com/jlpoveda/django-fixscript/',
    license='MIT',
    install_requires=[
        'Django>=2.0,<2.3',
    ]
)