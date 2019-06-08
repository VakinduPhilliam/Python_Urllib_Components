# Python Urllib
# Fetching Internet Resources Using The urllib Package
# urllib.request is a Python module for fetching URLs (Uniform Resource Locators).
# It offers a very simple interface, in the form of the urlopen function.
# This is capable of fetching URLs using a variety of different protocols.
# It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on.
# These are provided by objects called handlers and openers.
# 
# urllib.request supports fetching URLs for many “URL schemes” (identified by the string before the ":" in URL - for example "ftp" is the URL scheme of
# "ftp://python.org/") using their associated network protocols (e.g. FTP, HTTP).
# This tutorial focuses on the most common case, HTTP.
# 
# For straightforward situations urlopen is very easy to use.
# But as soon as you encounter errors or non-trivial cases when opening HTTP URLs, you will need some understanding of the HyperText Transfer Protocol.
# The most comprehensive and authoritative reference to HTTP is RFC 2616.
# This is a technical document and not intended to be easy to read.
# This aim here is to illustrate using urllib, with enough detail about HTTP to help you through.
# It is not intended to replace the urllib.request docs, but is supplementary to them.
#

#
# Sockets and Layers:
# The Python support for fetching resources from the web is layered. urllib uses the http.client library, which in turn uses the socket library.
# 

#
# As of Python 2.3 you can specify how long a socket should wait for a response before timing out.
# This can be useful in applications which have to fetch web pages.
# By default the socket module has no timeout and can hang. Currently, the socket timeout is not exposed at the http.client or urllib.request levels.
# However, you can set the default timeout globally for all sockets using
# 

import socket
import urllib.request

# timeout in seconds

timeout = 10
socket.setdefaulttimeout(timeout)

# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module

req = urllib.request.Request('http://www.voidspace.org.uk')

response = urllib.request.urlopen(req)
 
