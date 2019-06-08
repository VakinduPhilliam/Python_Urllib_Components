# Python Urllib Parse
# urllib.parse — Parse URLs into components.
# This module defines a standard interface to break Uniform Resource Locator (URL) strings up in components (addressing scheme, network location, path etc.),
# to combine the components back into a URL string, and to convert a “relative URL” to an absolute URL given a “base URL.”
# The module has been designed to match the Internet RFC on Relative Uniform Resource Locators.
# It supports the following URL schemes: file, ftp, gopher, hdl, http, https, imap, mailto, mms, news, nntp, prospero, rsync, rtsp, rtspu, sftp, shttp, sip,
# sips, snews, svn, svn+ssh, telnet, wais, ws, wss.
# 
# The urllib.parse module defines functions that fall into two broad categories: URL parsing and URL quoting.
#

#
# URL Parsing
# 
# The URL parsing functions focus on splitting a URL string into its components, or on combining URL components into a URL string.
#
# urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True) 
# Parse a URL into six components, returning a 6-tuple.
# This corresponds to the general structure of a URL: scheme://netloc/path;parameters?query#fragment. Each tuple item is a string, possibly empty.
# The components are not broken up in smaller parts (for example, the network location is a single string), and % escapes are not expanded.
# The delimiters as shown above are not part of the result, except for a leading slash in the path component, which is retained if present.
#

#
# For example:
# 

from urllib.parse import urlparse

o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
o   # doctest: +NORMALIZE_WHITESPACE

#
# OUTPUT: 
#
# ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
#            params='', query='', fragment='')
#


o.scheme

# OUTPUT: 'http'

o.port

# OUTPUT: '80'

o.geturl()

# OUTPUT: 'http://www.cwi.nl:80/%7Eguido/Python.html'
