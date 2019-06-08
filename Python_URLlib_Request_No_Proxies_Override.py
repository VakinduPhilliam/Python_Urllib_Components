# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# The following example uses no proxies at all, overriding environment settings:
# 

import urllib.request

opener = urllib.request.FancyURLopener({})

with opener.open("http://www.python.org/") as f:
        f.read().decode('utf-8')
