import pprint

# returns a set of the k-shingles in document
def shingles(document, k):
	shingles = set()
	words = document.lower().split(" ")
	for i in range(len(words) - k + 1):
		shingles.add(tuple(words[i:i + k]))
	return shingles

# Return a hash value for the shingle.
# Different values of x will return different hashes.
# Prof. Kloosterman implemented this in a quick and dirty way
#  so you can ignore the details of this implementation.
max_hashes = 10000
hash_as = [(x * 23 + 37) % 255 for x in range(max_hashes)]
hash_bs = [(x * 13 + 47) % 1023 for x in range(max_hashes)]
def generate_hash(shingle, x):
	assert (x < max_hashes)
	return ((hash_as[x] * hash(shingle)) + hash_bs[x]) & 0xfffff

# Generate a minhash signature given a set of shingles.
# A minhash signature is a list of the minimum hash across
#  all shingles, using num_hashes different hash functions.
def minhash_signature(document_shingles, num_hashes):
  print("Generating signatures for", document_shingles)
  signature = []
  for i in range(num_hashes):
    hashes = [generate_hash(x, i) for x in document_shingles]
    signature.append(min(hashes))
    print("Hashes with function", i, hashes)
    print("Min: ", min(hashes))
  print("Signature:", signature)
  print()
  return signature


# Compute the similarity between new_document and each of a list of documents,
#  using num_hashes number of hash functions.
def minhash_similarity(documents, new_document, num_hashes):
	assert (num_hashes < max_hashes)

	shingle_k = 2
	documents_shingles = [shingles(d, shingle_k) for d in documents]

	# Compute signatures for all documents
	signatures = [minhash_signature(x, num_hashes) for x in documents_shingles]
	# Uncomment this to see what the signatures look like
	print("Signatures of existing documents:")
	pprint.pprint(signatures)

	# Compute signature of new document
	new_shingles = shingles(new_document, shingle_k)
	new_signature = minhash_signature(new_shingles, num_hashes)

	# Compute number of matching values in the signature
	similarities = []
	for s in signatures:
		similarity = 0
		for i in range(num_hashes):
			if s[i] == new_signature[i]:
				similarity += 1
		similarities.append(similarity / num_hashes)

	return similarities

documents = [
    "Canada is a large country",
    "there are many large trees in Canada",
    "Ontario is a large province and rocky",
]

new_document = "Quebec is a large province and northern"

num_hashes = 5
print("Minhash similarity with", num_hashes, "hashes:",
      minhash_similarity(documents, new_document, num_hashes))
