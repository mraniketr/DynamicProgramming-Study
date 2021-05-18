def trvlr(m,n,l1={}):
    if((str(m)+','+str(n) in l1)  ):
        return (l1[str(m)+','+str(n)])
    if((str(n)+','+str(m) in l1)  ):
        return (l1[str(n)+','+str(m)])
    if(n<=1 and m<=1):
        return 1
    elif(m==0 or n==0):
        return 0
    
    val=trvlr(m-1,n,l1) +trvlr(m,n-1,l1)
    l1[str(m)+','+str(n)]=val
    return val

print(trvlr(18,18))

# m=5
# y='asda'
# print (f'{5}{y}')
# l1={'1,2':3,'4,2':1}
# l1['5,6']=5
# print(l1)
# # if('1,2' in l1):
# #     print("Hello")