# QUESTION 4: CONSECUTIVE LIST
# ==================================================================================

# ==================================================================================
# FUNCTIONS 

# Function to check if the array contains consecutive elements
# ---- if no, return None
# ---- if yes, return a tuple representing the value range in the range [min, max]
def consecutive(arr):
  if len(arr) == 0: # If array is empty
    return None

  # my_min and my_max is to store the current min & max element so far when travering
  # initialize as first element
  my_min = my_max = arr[0]

  # LOOP from the second element till the end
  for i in range(1, len(arr)):
    # Between the current min and current element, the smaller one will be stored to my_min
    my_min = min(my_min, arr[i])
    # Between the current max and current element, the bigger one will be stored to my_max
    my_max = max(my_max, arr[i])

  # If the [min, max] range matches with the formula, return range; Else, return None
  return (my_min, my_max) if len(arr) == (my_max - my_min + 1) else None


# Function to validate input from user and convert input to set of integers
# ---- Params: user_input is an array of string
# ---- Output: a set of integer
def validate_input(user_input):
  # Save values into a set to access in O(1)
  set_of_inputs = set()
  arr = []

  if len(user_input) == 0: # If user input is empty 
    print("\nError: Empty list")
  
  # LOOP through every input
  for input in user_input:
    try: # Try to parse input string to integer
      num = int(input)
    except ValueError: # If error happened, the input isn't a number
      print("\nError: Invalid input. Your input has non-numeric value:", input)
      return {}
    
    if num in set_of_inputs: # If num exists in the set of inputs, num is repeated
      print("\nError: Invalid input. Your input has duplicates:", num)
      return {}
    
    # If num is valid, save it to the set
    set_of_inputs.add(num)
    arr.append(num)
  return arr

# ==================================================================================
# MAIN PROGRAM

# Print instruction
print("Please input each number separated by whitespace. No duplicates allowed. Ex: 2 3 1 4")

# Split the input string to get list of elements, validate them and save into an array
arr = validate_input(input("\nEnter list: ").strip().split())

if len(arr) > 0: # If the array is not empty => array is valid
  print("\nInput list is:", arr)

  # Check consecutive
  result = consecutive(arr)
  if result is None:
    print("\nNot consecutive!")
  else:
    print("\nConsecutive! List contains elements from", result[0], "to", result[1])

