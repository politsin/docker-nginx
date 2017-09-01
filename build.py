#!/usr/bin/python

import os
if os.path.exists('/opt/docker-nginx'):
  os.chdir('/opt/docker-nginx')
  os.system('docker build -t nginx:1.11 .')
  os.system('docker tag nginx:1.11 nginx:latest')
