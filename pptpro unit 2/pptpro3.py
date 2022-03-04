# page no 28

def keltofan(temp):
   assert (temp>=0),"Colder than absolute zero!"
   return ((temp-273)*1.8)+32
print(keltofan(273))
print (int(keltofan(505.78)))
print(keltofan(-5))
