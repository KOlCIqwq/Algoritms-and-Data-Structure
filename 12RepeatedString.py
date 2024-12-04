def rep(s):
    '''
    1. We gonna init an array called borderLength in which we count the maxlenght of
       a border in that position. A border is a substring that is prefix and suffix
    2. Loop the string, each time we compare the current and the previous, the previous
       is not i - 1 but rather we need to extract that from the borderLength
    3. If they're not equal we gonna check if the border's corrisponding position corrispond.
    4. If both case fail, we gonna decrement till we find a new char that is equal to the current
       and set the found position and current as the max length border
    
    e.g.:
    s = "abcabcab"
    1I: i=1, s[1]=b, s[1]!=s[0] -> no border, bL[1] = 0
    2I: i=2, s[2]=c, s[2]!=s[0](0 from bL[1]) -> no border, bL[2]=0
    3I: i=3, s[3]=a, s[3]=s[0] -> possible border found, bL[3]=prev+1=1
    4I: i=4, s[4]=b, s[4]=s[1](1 from bL[3]) -> border corrispond, bL[4]=prev+1=2
    and so on... at the end we gonna find bL = [0,0,0,1,2,3,4,5] which represents the
    max length of border in each prefix. We return the n - maxLength of border.
    
    The runtime will be O(n), n represents the length of s. We loop once the string.
    The nested while won't change the runtime, because the prev will be at max n,
    and the prev will never overpass the substring already iterated (bacause it takes 
    only values at borderLength), so it won't affect the overall runtime
    '''
    n = len(s)
    borderLength = [0] * n

    for i in range(1,n):
        prev = borderLength[i - 1]
        while prev > 0 and s[i] != s[prev]:
            prev = borderLength[prev - 1]
        if s[i] == s[prev]:
            prev += 1
        borderLength[i] = prev
    
    return n - borderLength[-1]

s = str(input())
print(rep(s))
