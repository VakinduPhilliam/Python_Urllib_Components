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
# Data
# Sometimes you want to send data to a URL (often the URL will refer to a CGI (Common Gateway Interface) script or other web application).
# With HTTP, this is often done using what’s known as a POST request.
# This is often what your browser does when you submit a HTML form that you filled in on the web.
# Not all POSTs have to come from forms: you can use a POST to transmit arbitrary data to your own application.
# In the common case of HTML forms, the data needs to be encoded in a standard way, and then passed to the Request object as the data argument.
# The encoding is done using a function from the urllib.parse library.
# 

import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'

values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes

req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:

         the_page = response.read()
 
#
# Note that other encodings are sometimes required.
#

# 
# If you do not pass the data argument, urllib uses a GET request. One way in which GET and POST requests differ is that POST requests often have
# “side-effects”: they change the state of the system in some way (for example by placing an order with the website for a hundredweight of tinned spam to 
# be delivered to your door).
# Though the HTTP standard makes it clear that POSTs are intended to always cause side-effects, and GET requests never to cause side-effects, nothing
# prevents a GET request from having side-effects, nor a POST requests from having no side-effects.
# Data can also be passed in an HTTP GET request by encoding it in the URL itself.
#

# 
# This is done as follows:
# 

import urllib.request
import urllib.parse

data = {}

data['name'] = 'Somebody Here'
data['location'] = 'Northampton'

data['language'] = 'Python'

url_values = urllib.parse.urlencode(data)

print(url_values)  # The order may differ from below.  

# OUTPUT: 'name=Somebody+Here&language=Python&location=Northampton'

url = 'http://www.example.com/example.cgi'

full_url = url + '?' + url_values

data = urllib.request.urlopen(full_url)

# 
# Notice that the full URL is created by adding a ? to the URL, followed by the encoded values.
#
