#!/usr/bin/python
import os
if os.path.isdir('/tmp'):
    print('/tmp is a directory')
else:
    print('not a directory')
