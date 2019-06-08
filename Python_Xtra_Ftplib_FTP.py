# Python Ftplib
# ftplib — FTP protocol client
# This module defines the class FTP and a few related items.
# The FTP class implements the client side of the FTP protocol.
# You can use this to write Python programs that perform a variety of automated FTP jobs, such as mirroring other FTP servers.
# It is also used by the module urllib.request to handle URLs that use FTP.
#

#
# class ftplib.FTP(host='', user='', passwd='', acct='', timeout=None, source_address=None):
# Return a new instance of the FTP class. When host is given, the method call connect(host) is made.
# When user is given, additionally the method call login(user, passwd, acct) is made (where passwd and acct default to the empty string when not given).
# The optional timeout parameter specifies a timeout in seconds for blocking operations like the connection attempt (if is not specified, the global default
# timeout setting will be used).
# source_address is a 2-tuple (host, port) for the socket to bind to as its source address before connecting.
#

# 
# The FTP class supports the with statement, e.g.:
# 

from ftplib import FTP

with FTP("ftp1.at.proftpd.org") as ftp:
        ftp.login()

        ftp.dir()

# doctest: +SKIP
