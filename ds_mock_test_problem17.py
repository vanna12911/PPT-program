def even_returns(l):
    e =  [i for i in l if i%2 ==0]
    return e

l =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = (even_returns(l))
print(x)