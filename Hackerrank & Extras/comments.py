# Pass a list to this function to check for minimum number
def min_check(x):
  min_val = x[0]
  for check in x:
    if check < min_val:
      min_val = check
  return min_val
