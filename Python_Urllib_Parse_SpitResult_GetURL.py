# Python Urllib Parse
# urllib.parse — Parse URLs into components.
# This module defines a standard interface to break Uniform Resource Locator (URL) strings up in components (addressing scheme, network location, path etc.),
# to combine the components back into a URL string, and to convert a “relative URL” to an absolute URL given a “base URL.”
# The module has been designed to match the Internet RFC on Relative Uniform Resource Locators.
# It supports the following URL schemes: file, ftp, gopher, hdl, http, https, imap, mailto, mms, news, nntp, prospero, rsync, rtsp, rtspu, sftp, shttp, sip,
# sips, snews, svn, svn+ssh, telnet, wais, ws, wss.
# 
# The urllib.parse module defines functions that fall into two broad categories: URL parsing and URL quoting.
#

#
# urllib.parse.SplitResult.geturl(): 
# Return the re-combined version of the original URL as a string.
# This may differ from the original URL in that the scheme may be normalized to lower case and empty components may be dropped.
# Specifically, empty parameters, queries, and fragment identifiers will be removed.
#

# 
# For urldefrag() results, only empty fragment identifiers will be removed.
# For urlsplit() and urlparse() results, all noted changes will be made to the URL returned by this method.
#

# 
# The result of this method remains unchanged if passed back through the original parsing function:
# 

from urllib.parse import urlsplit

url = 'HTTP://www.Python.org/doc/#'

r1 = urlsplit(url)
r1.geturl()

# OUTPUT: 'http://www.Python.org/doc/'

r2 = urlsplit(r1.geturl())
r2.geturl()

# OUTPUT: 'http://www.Python.org/doc/'
