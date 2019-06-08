# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# The following example uses the POST method instead.
# Note that params output from urlencode is encoded to bytes before it is sent to urlopen as data:
# 

import urllib.request
import urllib.parse

data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
data = data.encode('ascii')

with urllib.request.urlopen("http://requestb.in/xrbl82xr", data) as f:

                print(f.read().decode('utf-8'))
