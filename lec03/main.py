routes = {}

def route(path):
  """Add a function to the routing table"""
  def inner(fn):
    global routes
    # your code here
  return inner

def get(path):
  """Call the function associated with a route in the routing table"""
  # your code here
  pass

## Do not modify anything below here

@route("/")
def index():
  print("called index()")

@route("/explore")
def explore():
  print("called explore()")

get("/explore")
# Expected output: called explore()
