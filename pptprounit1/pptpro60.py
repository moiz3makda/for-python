# page no 165/166

def fun_sum(a,b):
    return a+b

test = {"Gfg":fun_sum, "is": 5, "best": 9}
print("the original dictionary is :: "+str(fun_sum))

res = test["Gfg"](30,32)
print("the required call value is :: "+ str(res))