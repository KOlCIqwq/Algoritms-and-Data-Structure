def InOrder(arr,out):
    if not arr: # Parsed the whole tree
        return 
    current = arr.pop(0) # Current node
    if current == "NULL": # Null child
        return
    InOrder(arr,out) # Traverse to left (since its left first)
    out.append(current) # Append the current node
    InOrder(arr,out) # Traverse to the right
    
    return out

a = input()
arr = a.split()

print(' '.join(InOrder(arr,[])))
