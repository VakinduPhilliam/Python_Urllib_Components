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
# URLError:
# Often, URLError is raised because there is no network connection (no route to the specified server), or the specified server doesn’t exist.
# In this case, the exception raised will have a ‘reason’ attribute, which is a tuple containing an error code and a text error message.
#

# 
# For Example;
# 

req = urllib.request.Request('http://www.pretend_server.org')

try: urllib.request.urlopen(req)

    except urllib.error.URLError as e:
        print(e.reason)      

# OUTPUT: '(4, 'getaddrinfo failed')'
