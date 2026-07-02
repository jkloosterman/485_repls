# returns a set of the k-shingles in document
def shingles(document, k):
	shingles = set()
	words = document.lower().split(" ")
	for i in range(len(words) - k + 1):
		shingles.add(tuple(words[i:i + k]))
	return shingles


# Returns the Jaccard similarity of two Python sets
def jaccard_similarity(a, b):
	# This can be done in one line using Python set operations
	#   a | b   means "a union b"
	#   a & b   means "a intersect b"
	# your code here
  pass

# Exercise 1:
#  (1) Complete the jaccard_similarity function above.
#  (2) Use it to compute the Jaccard similarity between these two documents
#       using 2-shingles.
#      The correct result is 0.25
document_a = "Canada is a large country"
document_b = "the Vatican is not a large country"

# your code here and in the jaccard_similarity function above
# shingles_a = ...

# Exercise 2:
#  Use Jaccard similarity with 3-shingles to identify the
#   document in the list most similar to new_document
documents = [
    "Canada is a large country",
    "there are many large trees in Canada",
    "Ontario is a large province",
    "Prince Edward Island is not a large province",
    "there are few large trees in Nunavut"
]

new_document = "Ontario is a large province and northern"

# your code here
