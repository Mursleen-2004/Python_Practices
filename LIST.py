# LIst is data type.
 # it is mutable (value can be change.)
# a= [23,34,23,"musa",56,65,766];
# print(a,type(a))
#
# #Nested list
#
# b = [12,32,56,98,[12,"musa",11]];
# print(b[4][1])                  #ALL ABOUT INDEX NUMBERS
#
# print(a[0:2]);

#List iteration

z = [10,20,30,40,50,60];

x = len(z)
print( "length is",x)
print("")

for i in range(x):
    print(z[i]);

#Reverse iteration
print("reverse")
for d in range(x-1,-1,-1):
    print(z[d]);