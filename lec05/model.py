import sqlite3

# This code is designed to be similar to
#  code we supply in the starter code for P2

def dict_factory(cursor, row):
    """Convert database row objects to a dictionary keyed on column name.
    This is useful for building dictionaries which are then used to render a
    template.  Note that this would be inefficient for large queries.
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

db = None
def get_db():
  global db
  if db is None:
    db = sqlite3.connect("database.sqlite3")
    db.row_factory = dict_factory
    db.execute("PRAGMA foreign_keys = ON")
  return db