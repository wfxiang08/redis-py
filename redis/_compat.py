# -*- coding:utf-8 -*-
"""Internal module for Python 2 backwards compatibility."""
import sys

from urllib import unquote
from urlparse import parse_qs, urlparse
from itertools import imap, izip
from string import letters as ascii_letters
from Queue import Queue
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

# special unicode handling for python2 to avoid UnicodeDecodeError
def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)

def iteritems(x): return x.iteritems()

def iterkeys(x): return x.iterkeys()

def itervalues(x): return x.itervalues()

def nativestr(x):
    return x if isinstance(x, str) else x.encode('utf-8', 'replace')

def u(x): return x.decode()

def b(x): return x

def next(x): return x.next()

def byte_to_chr(x): return x

unichr = unichr
xrange = xrange
basestring = basestring
unicode = unicode
bytes = str
long = long

from Queue import Empty, Full
from Queue import LifoQueue

# 通过_compact实现不同版本的Python的兼容