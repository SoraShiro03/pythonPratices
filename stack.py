stack = [1,2,3,4,5]
# LIFO last in first out

stack.append(7)
print(stack)

stack.pop()
print(stack)

newStack = [9,0]
stack.extend(newStack)
print(stack)

stack.reverse()
print(stack)

stack.sort()
print(stack)

stack.insert(3, 11)
print(stack)