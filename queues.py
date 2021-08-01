from collections import deque

# FILO first in last out
#
# numbers =list(map((lambda x: x in range(10)))

Queues = deque()
#Queues.append(numbers)
Queues.append(10)
Queues.append(11)
Queues.append(12)
print(Queues)

Queues.popleft()
print(Queues)

Queues.append(12)
print(Queues)

Queues.clear()
print(Queues)

