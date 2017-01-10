#!/usr/bin/env python

# shodanUltimate.py
#
# thewoosterisroot


import shodan
import sys


# Configuration
API_KEY = "YOUR_API_KEY"


# Input validiation
if len(sys.argv) == 1:
    print ("Usage: {} <search query".format(sys.argv[0]))
    sys.exit(1)
    
try:
    # Setup api
    api = shodan.Shodan(API_KEY)
    
    # Perform the search
    query = ' '.join(sys.argv[1:])
    result = api.search(query)
    
    # Loop through matches and print each IP
    for service in result['matches']:
        print(service['ip_str'])
except Exception as e:
    print ("Error: {}".format(e))
    sys.exit(1)