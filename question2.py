# QUESTION 2: NON CONSECUTIVE CONVERSION
# ==================================================================================

def p(x):
  print("in P with", x)
  # If x is divisible by 3, return true
  return x % 3 == 0
def a(x):
  print("in A")

def b(x):
  print("in B")

def f(x):
  print("in F with", x)
  # Update x by adding 1
  return x + 1

def r(x):
  if p(x):
    a(x)
  else:
    b(x)
    r(f(x))

def no_r(x):
  while not p(x):
    b(x)
    x = f(x)
  a(x)

print("Running recursive function")
print("==========================\n")
r(1)

print("\nRunning non-recursive function")
print("==========================\n")
no_r(1)