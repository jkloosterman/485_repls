from collections import OrderedDict
from math import sqrt
from linalg import norm, dot

documents = [
  "kangaroos can jump",
  "cows can not jump"
  # You can add more of your own documents here
]

# Find all unique words in documents
# Using an OrderedDict instead of a regular unordered dictionary means
#  that the sequence of the keys in the OrderedDict can also
#  be the sequence of the words in the document vectors.
# For example, if the keys in the OrderedDict are
#  "kangaroos", "can", "cows",
# then the document vector [1, 0, 0] means that "kangaroos" was in
#  the document but not "can" or "cows"
words = OrderedDict()
for document in documents:
  for word in document.split(" "):
    words[word] = True

# Create a vector from a document
def build_vector(document):
  document_words = set(document.split(" "))
  v = []
  for word in words.keys():
    if word in document_words:
      v.append(1)
    else:
      v.append(0)
  return v

# Build vectors from documents
vectors = []
for document in documents:
  v = build_vector(document)
  vectors.append(v)

print("Key order: ", list(words.keys()))
print("Vectors:", vectors)

# Returns the cosine between two vectors
# Based on https://stackoverflow.com/a/43043160
def cosine_similarity(a, b):
  norms = norm(a) * norm(b)
  if norms == 0:
    return 0
  return dot(a, b)/norms

# Ask the user for a query (can be multiple words)
# and print cosine similarity of the query to all the documents.
query = input("Enter query (can be multiple words): ")

query_vec = build_vector(query)
# Compute the cosine similarity of query_vec against all the documents
