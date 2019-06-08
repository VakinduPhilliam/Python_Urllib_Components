# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# Use of Basic HTTP Authentication:
# 

import urllib.request

# Create an OpenerDirector with support for Basic HTTP Authentication...

auth_handler = urllib.request.HTTPBasicAuthHandler()

auth_handler.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')

opener = urllib.request.build_opener(auth_handler)

# ...and install it globally so it can be used with urlopen.

urllib.request.install_opener(opener)

urllib.request.urlopen('http://www.example.com/login.html')
