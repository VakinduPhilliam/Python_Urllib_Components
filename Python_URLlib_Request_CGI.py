# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# In the following example, we are sending a data-stream to the stdin of a CGI and reading the data it returns to us.
# Note that this example will only work when the Python installation supports SSL.
# 

import urllib.request

req = urllib.request.Request(url='https://localhost/cgi-bin/test.cgi',
                          data=b'This data is passed to stdin of the CGI')

with urllib.request.urlopen(req) as f:
           print(f.read().decode('utf-8'))

# OUTPUT: 'Got Data: "This data is passed to stdin of the CGI"'
 
#
# The code for the sample CGI used in the above example is:
# 

#!/usr/bin/env python

import sys

data = sys.stdin.read()

print('Content-type: text/plain\n\nGot Data: "%s"' % data)
