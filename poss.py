import sys
import requests
import json
print ("hello")

if len(sys.argv) != 2:
    sys.exit

response=requests.get(" https://itunes.apple.com/lookup?id="+sys.argv[1])
o=response.json()
for result in o["results"]:
    print(result)
