# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# Adding HTTP headers:
# Use the headers argument to the Request constructor, or:
# 

import urllib.request

req = urllib.request.Request('http://www.example.com/')
req.add_header('Referer', 'http://www.python.org/')

# Customize the default User-Agent header value:

req.add_header('User-Agent', 'urllib-example/0.1 (Contact: . . .)')

r = urllib.request.urlopen(req)

# 
# OpenerDirector automatically adds a User-Agent header to every Request. To change this:
# 

import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

opener.open('http://www.example.com/')
