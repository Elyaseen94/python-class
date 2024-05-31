#append:
list=["CPU","ROM","RAM", 2 , 5.5]
print(list)
list.append("NIC")
print("new list:", list)
list.append(200)
print("*********************************")
#insert:
print("new list:", list)
aList = [123, 'xyz', 'zara', 'abc']
aList.insert(3, 2009)
print("Final List : ", aList)
print("*********************************")
#pop:
aList = [123, 'xyz', 'zara', 'abc']
print("Popped Element : ", aList.pop())
print("Updated List:")
print(aList)
print("*********************************")
#Extend:
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)
print("Extended List : ", aList)
print("*********************************")
#count:
aList = [12, 'as', 12, 'abc', '12', 12]
print("Count for 12 : ", aList.count(12))
print("Count for '12' : ", aList.count('12'))
print("*********************************")
#sort:
aList = ['123', 'xyz', 'zara', 'abc', 'xyz']
aList.sort()
print("List : ", aList)
print("*********************************")
#remove:
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.remove('xyz')
print("List : ", aList)
aList.remove('abc')
print("List : ", aList)
print("*********************************")
#reverse:
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.reverse()
print("List : ", aList)
print("*********************************")
#concatenation:
x = "Python for data science"
y = " machine learning & AI"
z = x + y
print(z)