import math

# Returns: a set() of node indices that are in the base set
# The base set includes the root set and all nodes that link
#  to a node in the base set
def build_base_set(adjacency_graph, root_set):
  base_set = set(root_set)
  for i in root_set:
    for j in range(len(adjacency_graph)):
      if adjacency_graph[j][i]:
        base_set.add(j)
  return base_set

# Return True iff the values for the keys in the
#  two dictionaries differ by less than the radius
def has_converged(dict1, dict2):
  radius = 0.01
  for k in dict1.keys():
    if abs(dict1[k] - dict2[k]) > radius:
      return False
  return True

# Divide every value in the scores dictionary
#  by the square root of the sum of the values
def normalize(scores):
  factor = math.sqrt(sum(scores.values()))
  if factor == 0:
    return
  for k in scores.keys():
    scores[k] /= factor

# Run HITS algorithm on adjacency_graph with the given root set.
def hits(adjacency_graph, root_set):
  print("Root set:", root_set)
  base_set = build_base_set(adjacency_graph, root_set)
  print("Base set:", base_set)
  print("==============")

  # Initialize authority and hub scores to 1
  authority_scores = {}
  hub_scores = {}
  for i in base_set:
    authority_scores[i] = 1
    hub_scores[i] = 1

  # Loop until converged
  iteration = 0
  while True:
    new_authority_scores = {}
    new_hub_scores = {}

    # Authority update
    for i in base_set:
      new_authority_scores[i] = 0
      for j in range(len(adjacency_graph)):
        # only look at nodes in the base set that link to us
        if adjacency_graph[j][i] and j in base_set:
          new_authority_scores[i] += hub_scores[j]

    # Hub update
    for i in base_set:
      new_hub_scores[i] = 0
      for j in range(len(adjacency_graph)):
        # only look at nodes in the base set that *we* link to
        if adjacency_graph[i][j] and j in base_set:
          new_hub_scores[i] += authority_scores[j]

    # Normalize scores
    normalize(new_authority_scores)
    normalize(new_hub_scores)

    # Print current scores
    print("Iteration", iteration)
    print("authority:", new_authority_scores)
    print("hub:", new_hub_scores)
    print()

    # Detect convergence
    if has_converged(authority_scores, new_authority_scores) and has_converged(hub_scores, new_hub_scores):
      print("========================")
      print("Converged after", iteration, "iterations")
      print("Final authority scores:", authority_scores)
      print("Final hub scores:", hub_scores)
      return authority_scores, hub_scores
  
    # Copy new scores over
    authority_scores = new_authority_scores
    hub_scores = new_hub_scores
    iteration += 1

sample_adjacency_matrix = [
  [0, 1, 1, 0, 0],     # Read as: node 0 links to node 1 and node 2
  [0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 1, 0, 0, 0]
]
hits(sample_adjacency_matrix, set([1, 2]))

# Exercise: Create the adjacency matrix for the graph in the slides.
# If the root set is [1]:
# 1. Which node do you expect to have the highest authority score?
# 2. Which node do you expect to have the highest hub score?
# If the root is [4, 5]:
# 1. Which node do you expect to have the highest authority score?
# 2. Which node do you expect to have the highest hub score?
#
# After you have made your predictions, run HITS on the graphs
#  and root sets
#  to determine the answers.
