# Claculating maximum no. of modes in an optical fiber, given the type of the fiber
print("Types of Optical fiber are Step-index and Graded index")
print("Press 1 for Step Index fiber")
print("Press 2 for  Graded Index fiber")

type = int(input("Enter choice: "))
v_number = float("Enter V-number: ")
if type == 1:
  n_m = (v_number*v_number)/2
  print("Maximum number of modes:", n_m)
elif type == 2:
  n_m = (v_number*v_number)/4
  print("Maximum number of modes:", n_m)
else:
  print("Invalid choice. Begin again.")
