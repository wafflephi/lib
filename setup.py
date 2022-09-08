#!/usr/bin/env python3

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_desc = f.read()


with open(os.path.join(directory, 'requirements.txt'), encoding='utf-8') as f:
  requirements = [line for line in f.read().strip().split('\n')]

setup(name='wafflephi',
      version='0.1.0',
      description='wafflephi tools library',
      author='Piotr Rybiec',
      license='MIT',
      long_description=long_desc,
      long_description_content_type='text/markdown',
      packages=['wafflephi'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=requirements,
      python_requires='>=3.9',
      include_package_data=True)


