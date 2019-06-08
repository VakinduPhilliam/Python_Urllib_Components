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
# Headers:
# How to add headers to your HTTP request.
#

# 
# Some websites dislike being browsed by programs, or send different versions to different browsers.
# By default urllib identifies itself as Python-urllib/x.y (where x and y are the major and minor version numbers of the Python release,
# e.g. Python-urllib/2.5), which may confuse the site, or just plain not work.
# The way a browser identifies itself is through the User-Agent header.
# When you create a Request object you can pass a dictionary of headers in.
#

#
# The following example makes the same request as above, but identifies itself as a version of Internet Explorer.
# 

import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }

headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')

req = urllib.request.Request(url, data, headers)

with urllib.request.urlopen(req) as response:

            the_page = response.read()
