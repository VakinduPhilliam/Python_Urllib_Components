# Python Ftplib
# ftplib — FTP protocol client
# This module defines the class FTP and a few related items.
# The FTP class implements the client side of the FTP protocol.
# You can use this to write Python programs that perform a variety of automated FTP jobs, such as mirroring other FTP servers.
# It is also used by the module urllib.request to handle URLs that use FTP.
#

#
# class ftplib.FTP_TLS(host='', user='', passwd='', acct='', keyfile=None, certfile=None, context=None, timeout=None, source_address=None):
# A FTP subclass which adds TLS support to FTP as described in RFC 4217.
# Connect as usual to port 21 implicitly securing the FTP control connection before authenticating.
# Securing the data connection requires the user to explicitly ask for it by calling the prot_p() method.
# context is a ssl.SSLContext object which allows bundling SSL configuration options, certificates and private keys into a single (potentially long-lived)
# structure.
#

#
# Here’s a sample session using the FTP_TLS class:
# 

ftps = FTP_TLS('ftp.pureftpd.org')
ftps.login()

# OUTPUT: '230 Anonymous user logged in'

ftps.prot_p()

# OUTPUT: '200 Data protection level set to "private"'

ftps.nlst()
