# page no 145/146

def apply(l,f):
    result = []
    for i in range(len(l)):
        result.append(f(l[i]))

    return result

l = [-1,2.3,3,-4,5]

print(apply(l,abs))
print(apply(l,int))
