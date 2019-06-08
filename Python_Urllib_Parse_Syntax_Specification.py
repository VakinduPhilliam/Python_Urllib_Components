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
# Following the syntax specifications in RFC 1808, urlparse recognizes a netloc only if it is properly introduced by ‘//’.
# Otherwise the input is presumed to be a relative URL and thus to start with a path component.
# 

from urllib.parse import urlparse

urlparse('//www.cwi.nl:80/%7Eguido/Python.html')

#
# OUTPUT:
#
# ParseResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
#            params='', query='', fragment='')
#

urlparse('www.cwi.nl/%7Eguido/Python.html')

#
# OUTPUT:
#
# ParseResult(scheme='', netloc='', path='www.cwi.nl/%7Eguido/Python.html',
#            params='', query='', fragment='')
#

urlparse('help/Python.html')

#
# OUTPUT:
#
# ParseResult(scheme='', netloc='', path='help/Python.html', params='',
#            query='', fragment='')
#