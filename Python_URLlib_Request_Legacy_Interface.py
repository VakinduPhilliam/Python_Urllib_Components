# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# Legacy interface:
# The following functions and classes are ported from the Python 2 module urllib (as opposed to urllib2).
# They might become deprecated at some point in the future.
#

#
# urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None): 
# Copy a network object denoted by a URL to a local file.
# If the URL points to a local file, the object will not be copied unless filename is supplied.
# Return a tuple (filename, headers) where filename is the local file name under which the object can be found, and headers is whatever the info() method of
# the object returned by urlopen() returned (for a remote object).
# Exceptions are the same as for urlopen().
#

# 
# The second argument, if present, specifies the file location to copy to (if absent, the location will be a tempfile with a generated name).
# The third argument, if present, is a callable that will be called once on establishment of the network connection and once after each block read
# thereafter. The callable will be passed three arguments; a count of blocks transferred so far, a block size in bytes, and the total size of the file.
# The third argument may be -1 on older FTP servers which do not return a file size in response to a retrieval request.
#

# 
# The following example illustrates the most common usage scenario:
# 

import urllib.request

local_filename, headers = urllib.request.urlretrieve('http://python.org/')

html = open(local_filename)

html.close()
