# QUESTION 1: JAGGED LIST
# ==================================================================================

# ==================================================================================
# FUNCTIONS 

# Function designing for jagged list that starts with uptrend
# Return the desired trend for current element given its index 
def up_trend(index):
    return not bool(index % 2)

# Function designing for jagged list that starts with downtrend
# Return the desired trend for current element given its index 
def down_trend(index):
    return bool(index % 2)

# Function to check if the values need to be swap
# ---- Inputs: three consecutive numbers in the array
# ------------- & the desired trend
# ---- Outputs: (is swap needed & the swap order)
def test_jagged(n1, n2, next_value, trend):
  # True is up trend, False is down trend
  # Compare n1 and n2 to check if they follow up trend
    is_up = n1 <= n2 

    # If the current trend is different than desired trend
    if is_up != trend:
        if next_value is not None:
            # Calculate swap position based on trend and (first and third element)
            swap_position = int(trend) if n1 < next_value else int(not trend)
            if swap_position == 0:
                return (True, n2, n1, next_value) # Swap the first pair
            return (True, n1, next_value, n2) # Swap the second pair
        return (True, n2, n1, next_value) # If the next value is none & different trend, swap the first pair
    return (False, n1, n2, next_value) # If n1 and n2 trend is the same as the desired trend, no swap need

# Function to run simulation for swapping array into two types of jagged list 
# and calculate distance required
def simulate_run(arr):
    if len(arr) < 2: return 0, 0
    # Initialize distances
    down_distance = up_distance = 0

    # down_n1 and down_n2 are pointers for down jagged list
    # up_n1 and  up_n2 are pointers for up jagged list
    down_n1 = up_n1 = arr[0]
    down_n2 = up_n2 = arr[1]

    for i in range(len(arr) - 1):
        # Get the element at index i + 2 if possible 
        next_value = arr[i+2] if i + 2 < len(arr) else None

        # Simulate downtrend jagged list conversion
        down_result = test_jagged(down_n1, down_n2, next_value, down_trend(i))
        if down_result[0] is True: down_distance += 2
        down_n1, down_n2 = down_result[2], down_result[3]

        # Simulate uptrend jagged list conversion
        up_result = test_jagged(up_n1, up_n2, next_value, up_trend(i))
        if up_result[0] is True: up_distance += 2
        up_n1, up_n2 = up_result[2], up_result[3]
    # Return two distances    
    return down_distance, up_distance

# MAIN function to convert normal list to the jagged list
def jagged_list(arr):
    # If array has 2 elements or less, no change need
    if len(arr) <= 2: return 0 
    # Run simulation 
    distance_down, distance_up = simulate_run(arr)
    # Decide trend based on distance
    func = up_trend if distance_up < distance_down else down_trend

    # Actual swap
    for i in range(len(arr) - 1):
        desired_trend = func(i)
        next_value = arr[i+2] if i + 2 < len(arr) else None

        # Test if need swap
        result = test_jagged(arr[i], arr[i+1], next_value, desired_trend)
        
        if result[0] is True: # If need, update array
            arr[i], arr[i + 1] = result[1] , result[2]
            if next_value is not None: 
                arr[i+2] = result[3]
    return min(distance_up, distance_down)

# Support function to test if the array is successfully converted into jagged list
def is_jagged(arr):
    for i in range(len(arr) - 2):
        is_up1 = arr[i] <= arr[i + 1]
        is_up2 = arr[i + 1] <= arr[i + 2]
        if is_up1 == is_up2: 
            return False
        i+=1
    return True

def run_tests(arr_list):
    for arr in arr_list:
        print("Initial list", arr)
        dist = jagged_list(arr)
        print("Jagged list:", arr)
        print("Distance between two lists: ", dist)
        print("Is the array jagged?", is_jagged(arr))
        print("\n")

run_tests([
    # Sample jagged list
    [4,3,7,8,6,2,1],
    # Ascending sorted list with odd numbers of elements     
    [10, 20, 30, 40, 50],
    # Ascending sorted list with even numbers of elements
    [10, 20, 30, 40],
    # Descending sorted list with odd numbers of elements
    [50, 40, 30, 20, 10],
    # Descending sorted list with even numbers of elements
    [50, 40, 30, 20],
    # Contains: sub jagged list with trend of "up down up down up down"
    [1,2,3,0,4,6,5,8,7,10,9],
    # Contains: sub jagged list with trend of "down up down up down up"
    [1,2,3,0,4,9,10,7,8,5,6],
    # Contains: sub jagged list [10,20,5,7] with trend of "up down up" but result is down up down 
    [3, 10, 20, 5, 7, 9]
])

