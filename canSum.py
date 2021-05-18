# def canSum(n):
#     if(n==0):
#         return True
#     if(n<0):
#         return False
#     val = False
#     for i in range(0,len(l1)):
#         val =val or canSum(n-l1[i])
#     return val

# l1=[7,14]

# print(canSum(300))


# DP
def canSum(n,d1={},l1=[]):
    if(n in d1):
        return d1[n]
    if(n==0):
        return True
    if(n<0):
        return False
    val = False

    for i in range(0,len(l1)):
        
        val =val or canSum(n-l1[i],d1,l1)
        d1[n-l1[i]] = val
        
    
    return val



print(canSum(8,{},l1=[3,5]))

