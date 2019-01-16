
#lambda
def add(x, y): 
    return x + y
print(add(1, 2))

add = lambda x, y : x + y 
print(add(1, 2))

#map
def multiply(x):
  return x * 2
print(list(map(multiply, [1, 2, 3, 4])))

