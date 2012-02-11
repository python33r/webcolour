# Setup for webcolour
# (NDE, 2012-02-11)

from distutils.core import setup

setup(
  name='webcolour',
  version='0.2',
  description='Tools for analysing colour & contrast in web pages',
  long_description=open('README').read(),
  author='Nick Efford',
  author_email='nick.efford@gmail.com',
  url='http://bitbucket.org/pythoneer/webcolour',
  py_modules=['webcolour'],
  scripts=['scripts/contrastchecker.py'],
  platforms='any',
  license='MIT',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.2',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ],
)
