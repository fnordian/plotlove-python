#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='plotlove',
      version='0.1',
      description='plot on plot.love',
      author='Marcus Hunger',
      author_email='marcus.hunger@gmail.com',
      url='https://github.com/fnordian/plotlove-python',
      packages=['plotlove'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      install_requires=['requests>=2.11']
      )
