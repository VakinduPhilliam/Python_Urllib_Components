# Python Ftplib
# ftplib — FTP protocol client
# This module defines the class FTP and a few related items.
# The FTP class implements the client side of the FTP protocol.
# You can use this to write Python programs that perform a variety of automated FTP jobs, such as mirroring other FTP servers.
# It is also used by the module urllib.request to handle URLs that use FTP.
#

# 
# Here’s a sample session using the ftplib module:
# 

from ftplib import FTP

ftp = FTP('ftp.debian.org')     # connect to host, default port
ftp.login()                     # user anonymous, passwd anonymous@

#  OUTPUT: '230 Login successful.'

ftp.cwd('debian')               # change into "debian" directory
ftp.retrlines('LIST')           # list directory contents

ftp.retrbinary('RETR README', open('README', 'wb').write)

#  OUTPUT: '226 Transfer complete.'

ftp.quit()
