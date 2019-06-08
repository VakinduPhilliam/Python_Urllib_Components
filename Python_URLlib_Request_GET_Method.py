# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# An example session that uses the GET method to retrieve a URL containing parameters:
# 

import urllib.request
import urllib.parse

params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})

url = "http://www.musi-cal.com/cgi-bin/query?%s" % params

with urllib.request.urlopen(url) as f:

           print(f.read().decode('utf-8'))
