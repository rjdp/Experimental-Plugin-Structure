import os
from setuptools import setup

abspathconfig = '/etc/ee/plugins.d'
abspathplugins = '/usr/lib/ee/plugins'

if not os.path.exists(abspathconfig):
    os.makedirs(abspathconfig)

if not os.path.exists(abspathplugins):
    os.makedirs(abspathplugins)


setup(name='Demo Plugin 4 ee',
      version='0.1',
      description='Demo Plugin',
      url='http://github.com/rjdp',
      author='rajdeep',
      author_email='rajdeep.sharma@rtcamp.com',
      license='MIT',
      #  Move plugin config/file where to a directory where ee searches for
      #  plugin configs/files.
      data_files=[(abspathconfig, ['config/plugn4ee.conf']),
                  (abspathplugins, ['src/plugn4ee.py'])],
      install_requires=[
          'ee',
      ],
      zip_safe=False)
