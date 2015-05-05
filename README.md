[![Build Status](https://travis-ci.org/p0bailey/python_pip.svg?branch=master)](https://travis-ci.org/p0bailey/python_pip)

# Python Pip boilerplate.

A simple python project boilerplate to start packaging python code with Pip.

Based on Scott Torborg "How To Package Your Python Code" howto.

http://www.scotttorborg.com/python-packaging/




```
git clone git@bitbucket.org:p0bailey/python_pip.git

virtualenv .env

source .env/bin/activate

python setup.py test

python setup.py sdist

pip install dist/dummy-0.1.tar.gz

$ dummy
Lorem ipsum dolor sit amet, consectetuer adipiscing elit.

```
