from setuptools import setup
from future import unicode_literals

requirements = [item for item in open('requirements.txt').read().splitlines()]

setup(name='GWS',
      version='.1',
      description='GWS',
      author='Eddie Welker',
      author_email='user@hoost.com',
      url='http://www.python.org/sigs/distutils-sig/',
      requirements = requirements,
     )
