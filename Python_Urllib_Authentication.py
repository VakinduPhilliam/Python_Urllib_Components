# Python Urllib
# Fetching Internet Resources Using The urllib Package
# urllib.request is a Python module for fetching URLs (Uniform Resource Locators).
# It offers a very simple interface, in the form of the urlopen function.
# This is capable of fetching URLs using a variety of different protocols.
# It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on.
# These are provided by objects called handlers and openers.
# 
# urllib.request supports fetching URLs for many “URL schemes” (identified by the string before the ":" in URL - for example "ftp" is the URL scheme of
# "ftp://python.org/") using their associated network protocols (e.g. FTP, HTTP).
# This tutorial focuses on the most common case, HTTP.
# 
# For straightforward situations urlopen is very easy to use.
# But as soon as you encounter errors or non-trivial cases when opening HTTP URLs, you will need some understanding of the HyperText Transfer Protocol.
# The most comprehensive and authoritative reference to HTTP is RFC 2616.
# This is a technical document and not intended to be easy to read.
# This aim here is to illustrate using urllib, with enough detail about HTTP to help you through.
# It is not intended to replace the urllib.request docs, but is supplementary to them.
#

#
# The top-level URL is the first URL that requires authentication. URLs “deeper” than the URL you pass to .add_password() will also match.
# 

# create a password manager

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.

top_level_url = "http://example.com/foo/"

password_mgr.add_password(None, top_level_url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)

opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL

opener.open(a_url)

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.

urllib.request.install_opener(opener)
