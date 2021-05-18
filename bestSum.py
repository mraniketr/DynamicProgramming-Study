# def bestSum(n,l):
#   if(n==0):
#     return []
#   if(n<0):
#     return None
#   sp=None
#   for x in l:
#     ans=bestSum(n-x,l)
#     if ans is not None:
#       a2=ans
#       a2.append(x)
#       if( sp is None or len(ans)<len(sp)):
#         sp=a2
#   return sp

# print(bestSum(8,[4,3,5]))


def bestSum(n,l,d={}):
  if(n in d): return d[n]
  if(n==0):
    return []
  if(n<0):
    return None
  sp=None
  for x in l:
    ans=bestSum(n-x,l,d)
    d[n]=ans
    if ans is not None:
      a2=ans
      a2.append(x)
      if( sp is None or len(ans)<len(sp)):
        sp=a2
  return sp

print(bestSum(1000,[25,4,5]))