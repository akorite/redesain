# Python in one page: values, lists, loops, functions.
prices = [120, 95, 140, 110]          # a list of four numbers

def average(values):                  # a function: a named recipe
    total = 0
    for v in values:                  # repeat for each element
        total = total + v
    return total / len(values)

print("count   =", len(prices))
print("average =", average(prices))
print("largest =", max(prices))
print("squares =", [p * p for p in prices[:2]])   # a list comprehension
