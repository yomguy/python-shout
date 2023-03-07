# python-shout

python-shout is a fork of the original shout-python, a set of bindings for libshout 2.

python-shout allows you to act as a source for icecast 1 and 2, and
shoutcast. This module includes inline documentation, or see
the included example.py for a demonstration of its usage.

## Compatibilty

This version supports both Python 2 and Python 3

For libshout <= 2.2.2, use python-shout==0.2.5

## Installation

You need to have Python and libshout 2 development packages installed.

For example on Debian:

`sudo apt-get install python3-dev python3-pip libshout3-dev`

If you have pkg-config installed, make sure it can find shout
(you may need to adjust PKG_CONFIG_PATH to contain
 $shout_prefix/lib/pkgcofig). Otherwise, shout-config must
appear in your path.

Then install through pip:

`sudo pip3 install python-shout`

or though the git repository:

```
git clone https://github.com/yomguy/python-shout.git
python3 setup.py install
```

## License

python-shout is licensed under the GNU LGPL. See COPYING for details.




