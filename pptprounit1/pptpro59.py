# page no 162/163

#def print_key1():
#    return "this is Gfg's value"

#test_dict = {"Gfg": print_key1, "is": 5, "best": 9}
#print("the original dictionary is "+str(test_dict))

#res = test_dict["Gfg"]()
#print("the required call result "+str(res))

def prkey():
    return "this is Gfg's value"

test = {"Gfg": prkey, "is": 5, "best": 9}
print("the original dictionary is "+str(test))

res = test["Gfg"]()
print("the required call result "+ str(res))