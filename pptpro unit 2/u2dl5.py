def selectionsort(alist):
    for i in range(0,len(alist)-1):
        smallest = i
        for j in range(i+1,len(alist)):
            if alist[j]  < alist[smallest]:
                smallest = j
        alist[i],alist[smallest] = alist[smallest],alist[i]

alist = input("Enter list of numbers (with spaces) : ").split()
alist = [int (x) for x in alist]
selectionsort(alist)
print("sorted list : ",end=" ")
print(alist)