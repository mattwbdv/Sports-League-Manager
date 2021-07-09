#!/usr/bin/env python

from distutils.core import setup

setup(name='curling_league',
      version='1.0',
      description='Sports League Manager',
      author='Matt Koenig',
      author_email='matthewkoenig@acm.org',
      url='https://github.com/mattwbdv/Sports-League-Manager',
      packages=['curling_league'],
      install_requires=[
            'PyQt5',
            'yagmail'
      ],
      dependency_links=['https://pypi.org/project/PyQt5/', 'https://pypi.org/project/yagmail/']
      )
