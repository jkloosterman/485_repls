documents = [
  "kangaroos can jump",
  "cows can not jump"
  # You can add more of your own documents here
]

# Build inverted index
index = {}
for i, document in enumerate(documents):
  for word in document.split(" "):
    if word in index:
      index[word].append(i)
    else:
      index[word] = [i]

print("Inverted index:", index)

# Exercise
# ========
# Ask the user to input a word
# If the word is in the index, print out the document ids that
#  contain that word.
# Otherwise, print "Not found"
query = input("Enter a word to search for: ")
