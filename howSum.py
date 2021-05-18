# def howSum(n,l):
#     if(n==0): return []
#     if(n<0): 
#         return None
#     # print(n)
#     for x in l:
#         ans=howSum(n-x,l)
#         if ans is not None:
#             ans.append(x)
#             return ans
   
#     return None

# print(howSum(7,[5,3,4,7]))
# print(howSum(8,[5,3,2]))
# print(howSum(14,[5,8]))


# DP

def howSum(n,l,d={}):
    if n in d: return d[n]
    if(n==0): return []
    if(n<0): 
        return None
    # print(n)
    for x in l:
        ans=howSum(n-x,l)
        if ans is not None:
            ans.append(x)
            d[n]=ans
            return ans
        else:
            d[n]=None
   
    return None

# print(howSum(7,[5,3,4,7]))
# print(howSum(8,[5,3,2]))
# print(howSum(14,[5,8]))
print(howSum(5,[2,3,1]))
