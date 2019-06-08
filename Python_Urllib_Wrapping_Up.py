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
# Wrapping it Up:
# So if you want to be prepared for HTTPError or URLError there are two basic approaches.
# 

#
# Number 1:
# 

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

req = Request(someurl)

try:
    response = urlopen(req)

except HTTPError as e:
    print('The server couldn\'t fulfill the request.')

    print('Error code: ', e.code)

except URLError as e:
    print('We failed to reach a server.')

    print('Reason: ', e.reason)

else:
    # everything is fine
 
#
# Note:
# The except HTTPError must come first, otherwise except URLError will also catch an HTTPError.
# 

#
# Number 2:
# 

from urllib.request import Request, urlopen
from urllib.error import URLError

req = Request(someurl)

try:
    response = urlopen(req)

except URLError as e:

    if hasattr(e, 'reason'):
        print('We failed to reach a server.')

        print('Reason: ', e.reason)

    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')

        print('Error code: ', e.code)

else:
    # everything is fine
