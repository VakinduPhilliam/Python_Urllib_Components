# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# The following example uses an explicitly specified HTTP proxy, overriding environment settings:
# 

import urllib.request

proxies = {'http': 'http://proxy.example.com:8080/'}

opener = urllib.request.FancyURLopener(proxies)

with opener.open("http://www.python.org") as f:

          f.read().decode('utf-8')
