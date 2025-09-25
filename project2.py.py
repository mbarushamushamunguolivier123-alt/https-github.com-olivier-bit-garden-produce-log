# Stack implementation using list
stack = []

# Push elements
stack.append("Topic1")
stack.append("Topic2")
stack.append("Topic3")

# Undo last 2 actions (pop 2 elements)
stack.pop()
stack.pop()

# Remaining stack
print("Remaining stack:", stack)
# Stack implementation
stack = []

# Push elements
stack.append("Fill Name")
stack.append("Upload File")
stack.append("Submit")

# Undo last action
stack.pop()

# Remaining stack
print("Remaining stack:", stack)
stack = []            # Step 1: empty stack

stack.append("X")     # Step 2
stack.append("Y")
stack.append("Z")

stack.pop()           # Step 3: remove "Z"
stack.pop()           # Step 3: remove "Y"

stack.append("W")     # Step 4: push "W"

top_element = stack[-1]   # Step 5: get top
print("Top element is:", top_element)
from collections import deque

# Queue implementation
queue = deque(["Bus1", "Bus2", "Bus3", "Bus4", "Bus5", "Bus6", "Bus7"])

# 3 buses depart
queue.popleft()
queue.popleft()
queue.popleft()

# Who is in front now?
print("Bus in front:", queue[0])
from collections import deque

# Queue of clients
queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5"])

# Third served (index 2)
third_client = queue[2]
print("Third client served:", third_client)


