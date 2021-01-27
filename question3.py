# QUESTION 3: TOWER OF HANOI
# ==================================================================================

import pandas as pd 
from tabulate import tabulate

# ==================================================================================
# FUNCTIONS 

def tower_of_hanoi(n, from_peg, to_peg):
  if from_peg > 3 or from_peg < 1 or to_peg > 3 or to_peg < 1:
    print("Invalid input")
    return
  
  spare_peg = 6 - from_peg - to_peg
  # Move all discs sitting on top of target disc from "from_peg" to the "spare_peg"
  n == 1 or tower_of_hanoi(n - 1, from_peg, spare_peg)

  # Print movement
  print("Move", discs[n - 1][0], "from", pegs[from_peg - 1].strip(), "to", pegs[to_peg - 1].strip())

  # Move back top discs from "spare_peg" to "to_peg"
  n == 1 or tower_of_hanoi(n - 1, spare_peg, to_peg)



def tower_of_hanoi_2(n, from_peg, to_peg, stacks):
  if from_peg > 3 or from_peg < 1 or to_peg > 3 or to_peg < 1:
    print("Invalid input")
    return
  
  spare_peg = 6 - from_peg - to_peg
  # Move all discs sitting on top of target disc from "from_peg" to the "spare_peg"
  n == 1 or tower_of_hanoi_2(n - 1, from_peg, spare_peg, stacks)

  # Pop target disc from "from_peg" and push to "to_peg"
  my_disc = stacks[from_peg - 1].pop()
  stacks[to_peg - 1].append(my_disc)
  print_toh(my_disc, from_peg, to_peg, stacks)

  # Move back top discs from "spare_peg" to "to_peg"
  n == 1 or tower_of_hanoi_2(n - 1, spare_peg, to_peg, stacks)


def print_toh(disc, from_peg, to_peg, stacks):
  # Init header/column name
  pegs = ['   X   ', '   Y   ', '   Z   ']

  # Print Description
  if (from_peg == to_peg):
    print(disc, "\n")
  else:
    print("Description:", disc[-1:] + " move from " + pegs[from_peg - 1].strip() + " to " + pegs[to_peg - 1].strip(), "\n")

  # Create a copy version of current stacks for printing purpose
  printing_stacks = []
  for stack in stacks:
    printing_stacks.append(['|'] * (len(discs) - len(stack)) + stack[::-1])
  
  print(tabulate(pd.DataFrame(printing_stacks).T, headers=pegs, showindex=False, stralign="center"), "\n")
  print("===============================\n")

# ==================================================================================
# MAIN PROGRAM

discs = ["a", "bbb", "ccccc", "ddddddd"]
pegs = ['   X   ', '   Y   ', '   Z   ']

print("TOH Solution with text description")
print("----------------------------------\n")
tower_of_hanoi(len(discs), 1, 3)

stacks = [discs[::-1], [], []]

print("\nTOH Solution with illustration")
print("----------------------------------\n")
print_toh("The initial TOH", 0, 0, stacks)
tower_of_hanoi_2(len(discs), 1, 3, stacks)
