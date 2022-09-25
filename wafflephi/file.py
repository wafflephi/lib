#!/usr/bin/env python3

import os
import requests
from hashlib import md5

def fetch(url: str) -> str:
  """Download a file from a given url, and save in /tmp/ directory.
    Returns file path.
  """
  fp = os.path.join('/tmp', md5(url.encode('utf-8')).hexdigest())

  if os.path.isfile(fp):
    with open(fp ,'rb') as file:
      data = file.read()
  else:
    with open(fp, 'wb') as file:
      data = requests.get(url).content
      file.write(data)
  return fp
