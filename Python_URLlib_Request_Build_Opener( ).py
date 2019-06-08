# Python URLlib Request
# urllib.request — Extensible library for opening URLs
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.
#

#
# build_opener() provides many handlers by default, including a ProxyHandler.
# By default, ProxyHandler uses the environment variables named <scheme>_proxy, where <scheme> is the URL scheme involved.
# For example, the http_proxy environment variable is read to obtain the HTTP proxy’s URL.
#

# 
# This example replaces the default ProxyHandler with one that uses programmatically-supplied proxy URLs, and adds proxy authorization support with
# ProxyBasicAuthHandler.
# 

proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()

proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)

# This time, rather than install the OpenerDirector, we use it directly:

opener.open('http://www.example.com/login.html')
