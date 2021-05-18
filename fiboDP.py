def fibo(n,ls={}):
    if(n in ls):
        return(ls[n])

    if(n<=2):
        return 1
    ls[n]=fibo(n-1,ls)+fibo(n-2,ls)
    return (ls[n])

print(fibo(50))



# ls={1:1,2:1,3:2}

# if(2 in ls): print (ls[2])