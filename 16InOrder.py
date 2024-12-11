def InOrder(arr,out):
    '''
    1. Since the input is in polish form, the input tree will be from left to right
    2. Each time we pop the first element of the input array, if this element is null return None
    3. We traverse to the left by recalling the function (given the nature of the polish form)
       if it arrived at the end it will append for first the rightmost node 
    4. It will traverse to the right when we can't move the left anymore, appending the leftmost right node
    O(n) we need traverse all the nodes anyway
    '''
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
