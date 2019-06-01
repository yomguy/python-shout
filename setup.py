# distutils build script
# To install shout-python, run 'python setup.py install'

from distutils.core import setup, Extension
import os
import sys
import setuptools

ver = '0.2.5'

with open("README", "r") as fh:
    long_description = fh.read()

# write default shout.pc path into environment if PKG_CONFIG_PATH is unset
if not 'PKG_CONFIG_PATH' in os.environ: # os.environ.has_key('PKG_CONFIG_PATH'):
    if os.path.exists('/usr/lib/pkgconfig'):
        os.environ['PKG_CONFIG_PATH'] = '/usr/lib/pkgconfig'
    else:
        os.environ['PKG_CONFIG_PATH'] = '/usr/local/lib/pkgconfig'

print('Using PKG_CONFIG_PATH=' + os.environ['PKG_CONFIG_PATH'])

# Find shout compiler/linker flag via pkgconfig or shout-config
if os.system('pkg-config --exists shout 2> /dev/null') == 0:
  pkgcfg = os.popen('pkg-config --cflags shout')
  cflags = pkgcfg.readline().strip()
  pkgcfg.close()
  pkgcfg = os.popen('pkg-config --libs shout')
  libs = pkgcfg.readline().strip()
  pkgcfg.close()

else:
  if os.system('pkg-config --usage 2> /dev/null') == 0:
    print("pkg-config could not find libshout: check PKG_CONFIG_PATH")
  if os.system('shout-config 2> /dev/null') == 0:
    scfg = os.popen('shout-config --cflags')
    cflags = scfg.readline().strip()
    scfg.close()
    scfg = os.popen('shout-config --libs')
    libs = scfg.readline().strip()
    scfg.close()

  else:
    print("pkg-config and shout-config unavailable, build terminated")
    sys.exit(1)

# there must be an easier way to set up these flags!
iflags = [x[2:] for x in cflags.split() if x[0:2] == '-I']
extra_cflags = [x for x in cflags.split() if x[0:2] != '-I']
libdirs = [x[2:] for x in libs.split() if x[0:2] == '-L']
libsonly = [x[2:] for x in libs.split() if x[0:2] == '-l']

# include_dirs=[]
# libraries=[]
# runtime_library_dirs=[]
# extra_objects, extra_compile_args, extra_link_args
shout = Extension('shout', sources = ['shout.c'],
                  include_dirs = iflags,
                  extra_compile_args = extra_cflags,
                  library_dirs = libdirs,
                  libraries = libsonly)

# data_files = []
setup (name = 'python-shout',
       version = ver,
       description = 'Bindings for libshout 2',
       long_description=long_description,
       url = 'http://icecast.org/download.php',
       author = 'Brendan Cully',
       author_email = 'brendan@xiph.org',
       packages=setuptools.find_packages(),
       classifiers=[
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 2",
                   "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
                   "Operating System :: OS Independent",
               ],

       )
