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
# Fetching URLs
# 
# The simplest way to use urllib.request is as follows:
# 

import urllib.request

with urllib.request.urlopen('http://python.org/') as response:

           html = response.read()
 
#
# If you wish to retrieve a resource via URL and store it in a temporary location, you can do so via the shutil.copyfileobj() and
# tempfile.NamedTemporaryFile() functions:
# 

import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:

                 shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:

                 pass

#
# Many uses of urllib will be that simple (note that instead of an ‘http:’ URL we could have used a URL starting with ‘ftp:’, ‘file:’, etc.).
# However, it’s the purpose of this tutorial to explain the more complicated cases, concentrating on HTTP.
#

# 
# HTTP is based on requests and responses - the client makes requests and servers send responses.
# urllib.request mirrors this with a Request object which represents the HTTP request you are making.
# In its simplest form you create a Request object that specifies the URL you want to fetch.
# Calling urlopen with this Request object returns a response object for the URL requested.
# This response is a file-like object, which means you can for example call .read() on the response:
# 

import urllib.request

req = urllib.request.Request('http://www.voidspace.org.uk')

with urllib.request.urlopen(req) as response:

             the_page = response.read()

# 
# Note that urllib.request makes use of the same Request interface to handle all URL schemes.
# For example, you can make an FTP request like so:
# 

req = urllib.request.Request('ftp://example.com/')

# 
# In the case of HTTP, there are two extra things that Request objects allow you to do: First, you can pass data to be sent to the server.
# Second, you can pass extra information (“metadata”) about the data or the about request itself, to the server - this information is sent as HTTP
# “headers”.
# Let’s look at each of these in turn.
#