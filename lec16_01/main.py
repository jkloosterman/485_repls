def pageRank(adjacency_matrix):
  # Initialize PageRank for each node
  num_nodes = len(adjacency_matrix)
  initial = 1 / num_nodes
  pageranks = [initial for x in range(num_nodes)]
  print("Initial PageRanks:", pageranks)
  print()

  # If a node is a sink, add outgoing edges to every
  #  other node
  for i, out_links in enumerate(adjacency_matrix):
    if sum(out_links) == 0:
      adjacency_matrix[i] = [1] * len(adjacency_matrix)
      adjacency_matrix[i][i] = 0
  
  # Dampening factor
  d = 0.85
  
  converged = False
  convergence_radius = 0.001
  iteration = 0
  while not converged:
    converged = True
    prev_pageranks = pageranks
    pageranks = []
    
    for i in range(num_nodes):
      # Calculate PageRank coming from other nodes that link to us
      incoming_pagerank = 0
      for j in range(num_nodes):
        # [j][i] because we're looking at *incoming* links
        # [i][j] would be *outgoing* links
        if adjacency_matrix[j][i]:
          j_out_degree = sum(adjacency_matrix[j])
          incoming_pagerank += prev_pageranks[j] / j_out_degree
    
      # Compute full PageRank by including first term and dampening factor
      new_pagerank = ((1 - d) / num_nodes) + (d * incoming_pagerank)
    
      # Assume we have converged until we change a value by more than
      #  convergence_radius
      if abs(prev_pageranks[i] - new_pagerank) > convergence_radius:
        converged = False
      pageranks.append(new_pagerank)
    
    print("Iteration", iteration)
    print([round(x, 3) for x in pageranks])
    print()
    iteration += 1
    
  # format with fewer decimal places
  return [round(x, 3) for x in pageranks]

# Sample from lecture
sample_adjacency_matrix = [
    [0, 1, 1, 0],  # Read as: node 0 links to node 1 and node 2
    [1, 0, 1, 1],
    [0, 0, 0, 0],
    [1, 1, 0, 0],
]
print("Sample graph PageRanks:", pageRank(sample_adjacency_matrix))

# Exercise 1: Look at the first graph in the slides.
# Before writing code, write in your notes:
#   1. Which node will have the highest PageRank?
#   2. Which node will have the lowest PageRank?
#   3. Approximately how many iterations do you think it will take for
#       PageRank to converge?
# Create the adjacency matrix for this graph and compute the pageRanks.


# Exercise 2: Look at the second graph in the slides.
# Before writing code, write in your notes:
#   1. Which node will have the highest PageRank?
#   2. Which node will have the lowest PageRank?
#   3. Approximately how many iterations do you think it will take for
#       PageRank to converge?
# Create the adjacency matrix for this graph and compute the pageRanks.
