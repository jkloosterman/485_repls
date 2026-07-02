import requests
import pprint

api_url = "https://jkloosterman.net/485/astronauts.json"

# Send an HTTP request to the server
response = requests.get(api_url)

# Turn the text response into a Python object by
#  parsing it as JSON
data = response.json()

# pprint stands for "pretty print"
#  and makes the data easier to read than using
#  regular print()
pprint.pprint(data)

# Print data about one astronaut
print()
print("One astronaut:")
print("==============")
thomas_pesquet = data["results"][0]
pprint.pprint(thomas_pesquet)

# Exercise 1:
# Print out the name and nationality of each astronaut
#  in the format:
#
#  Thomas Pesquet - French
#  Claude Nicollier - Swiss

# Your code here

# Exercise 2:
# Inside the JSON for the astronauts, there is a URL
#  for an endpoint about NASA.
# It looks like http://jkloosterman.net/485/agency/...
#
# Use that to print the names of all NASA spacecraft.
# There is a key "spacecraft_list" that will be helpful

# your code here