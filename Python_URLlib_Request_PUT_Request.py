# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# An example of doing a PUT request using Request:
# 

import urllib.request

DATA = b'some data'

req = urllib.request.Request(url='http://localhost:8080', data=DATA,method='PUT')

with urllib.request.urlopen(req) as f:
              pass

print(f.status)

print(f.reason)
