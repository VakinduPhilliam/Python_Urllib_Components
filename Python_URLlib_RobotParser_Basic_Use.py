# Python URLlib RobotParser
# urllib.robotparser — Parser for robots.txt
# This module provides a single class, RobotFileParser, which answers questions about whether or not a particular user agent can fetch a URL on the Web site
# that published the robots.txt file.
#

#
# The following example demonstrates basic use of the RobotFileParser class:
# 

import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://www.musi-cal.com/robots.txt")

rp.read()

rrate = rp.request_rate("*")
rrate.requests

# OUTPUT: '3'

rrate.seconds

# OUTPUT: '20'

rp.crawl_delay("*")

# OUTPUT: '6'

rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")

# OUTPUT: 'False'

rp.can_fetch("*", "http://www.musi-cal.com/")

# OUTPUT: 'True'
