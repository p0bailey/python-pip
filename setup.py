
from setuptools import setup



setup(name='dummy',
      version='0.1',
      description='Dummy words',
      url='git@bitbucket.org:p0bailey/python_pip.git',
      author='Phillip Bailey',
      author_email='phillip@bailey.st',
      license='MIT',
      scripts=['bin/dummy'],
      packages=['dummy'],
      install_requires=['nose'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
