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
# urllib.parse.urljoin(base, url, allow_fragments=True): 
# Construct a full (“absolute”) URL by combining a “base URL” (base) with another URL (url).
# Informally, this uses components of the base URL, in particular the addressing scheme, the network location and (part of) the path, to provide missing
# components in the relative URL.
#

#
# For example:
# 

from urllib.parse import urljoin

urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')

# OUTPUT: 'http://www.cwi.nl/%7Eguido/FAQ.html'

# 
# The allow_fragments argument has the same meaning and default as for urlparse().
# 

#
# Note:
# If url is an absolute URL (that is, starting with // or scheme://), the url’s host name and/or scheme will be present in the result.
#

#
# For example:
# 

urljoin('http://www.cwi.nl/%7Eguido/Python.html',
            '//www.python.org/%7Eguido')

# OUTPUT: 'http://www.python.org/%7Eguido'
