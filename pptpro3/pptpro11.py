import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,5,7,6]
plt.scatter(x, y, label= "stars", color= "green", marker= "*", s=30)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My scatter plot!')
plt.legend()
plt.show()
