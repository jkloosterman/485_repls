import model

db = model.get_db()

# Things to notice:
#  1. There is a space at the end of each of the
#      strings that make up the query. This is because
#      Python concatenates the strings without inserting
#      any whitespace.
#  2. To put variable values inside a SQL query, use ?s
#      and pass the variables in a tuple like (a, b, c)
#      as the second argument to .execute(). If you only
#      have one variable, you have to put a comma
#      at the end of the tuple like here.
user = 'jklooste'
cursor = db.execute(
  "SELECT promoted "
  "FROM users "
  "WHERE username = ?",
  (user,))

for row in cursor:
  # You know the key is "promoted" because that is the
  #  column name from the SQL query
  print(row["promoted"])

# Checkpoint 1: Print the text of all comments by the user in
#  the 'user' variable
# Remember you can view the CREATE TABLE statements in
#  schema.sql

# cursor = db.execute( ...
# your code here

# Checkpoint 2: Insert 20 users into the database
#  with the names user0, user1, ..., user19.
#  The even numbered users (0, 2, 4, ...) should be promoted.
#
#  You will find format strings useful here, for example:
#    n = 3
#    s = f"test{n}"
#    print(test)  # prints test3
  
# your code here