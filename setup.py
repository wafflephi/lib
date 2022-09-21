#!/usr/bin/env python3

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_desc = f.read()

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
      install_requires=['numpy', 'requests', 'scipy'],
      python_requires='>=3.10',
      extras_require={
        'testing': [
          "pytest",
        ],
      },
      include_package_data=True)


