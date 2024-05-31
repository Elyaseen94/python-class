#Subtraction operation:
a=6
b=3
a-=b
print(a)
print("*************************")
#Multiplication operation:
a=6
b=3
a*=b
print(a)
print("*************************")
#Division operation:
a=6
b=3
a/=b
print(a)
print("*************************")
#Modulus operation:
a=63
b=6
a%=b
print(a)
print("*************************")
#Exponent operation:
a=2
b=3
a**=b
print(a)
print("*************************")
#logical operation:
x=200
print(x>4 or x<300)
x=200
print(not(x>4 or x<300))
print("********************************")
x = 10
print(x > 5 and x < 15)
#AND
#This returns True because 10 is greater than 5 AND 10 is less than 15.


#OR
x = 10
print(x > 5 or x < 2)

#This returns True because one of the conditions are true.
#10 is greater than 5, but 10 is not less than 2.
#NOT
x = 10
print(not(x > 5 and x < 15))
#This returns False because not reverses the result of and.