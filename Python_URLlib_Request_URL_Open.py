# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# This example gets the python.org main page and displays the first 300 bytes of it.
# 

import urllib.request

with urllib.request.urlopen('http://www.python.org/') as f:

              print(f.read(300))
