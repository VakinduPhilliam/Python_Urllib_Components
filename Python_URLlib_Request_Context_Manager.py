# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# The following W3C document, https://www.w3.org/International/O-charset, lists the various ways in which an (X)HTML or an XML document could have specified
# its encoding information.
# As the python.org website uses utf-8 encoding as specified in its meta tag, we will use the same for decoding the bytes object.
# 

with urllib.request.urlopen('http://www.python.org/') as f:

        print(f.read(100).decode('utf-8'))

#
# OUTPUT:
#
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
# "http://www.w3.org/TR/xhtml1/DTD/xhtm
#

# 
# It is also possible to achieve the same result without using the context manager approach.
# 

import urllib.request

f = urllib.request.urlopen('http://www.python.org/')

print(f.read(100).decode('utf-8'))

#
# OUTPUT:
#
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
# "http://www.w3.org/TR/xhtml1/DTD/xhtm
#