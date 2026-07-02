import sys

# Input: 
# [student] [assignment] [weight in %] [score in %]
# John  Project 1  40  70
# John  Project 2  60  80

# Output:
# [student] [contribution to grade]
# John  28
# John  48
for line in sys.stdin:
  student, assignment, weight, score = line.split("\t")
  
  # Compute contribution and put it in the
  #  contribution variable.
  # Hint: do you need to do some type conversions?
  contribution = 0
  
  print(f"{student}\t{contribution}")
