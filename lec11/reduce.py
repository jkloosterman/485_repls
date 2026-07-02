import sys

# Input: 
# [student] [contribution to grade]
# John  28
# John  48
# Alex  40

# Output:
# [student] [total grade ]
# John  76
# Alex  40

cur_student = None
cur_score = 0
for line in sys.stdin:
  student, contribution = line.split("\t")
  contribution = float(contribution)

  if cur_student is None:
    # Case 1: we are the first student
    # Your code here
    pass
  elif student != cur_student:
    # Case 2: the student on this line IS NOT the
    #  same as the student on the previous line
    # Your code here
    pass
  else:
    # Case 3: the student on this line IS the
    #  same as the student on the previous line
    # Your code here
    pass

# Make sure we print the information for the last student
if cur_student is not None:
  print(cur_student, cur_score)
