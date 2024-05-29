#append:
list=["CPU","ROM","RAM", 2 , 5.5]
print(list)
list.append("NIC")
print("new list:", list)
list.append(200)

#insert:
print("new list:", list)
aList = [123, 'xyz', 'zara', 'abc']
aList.insert(3, 2009)
print("Final List : ", aList)

#pop:
aList = [123, 'xyz', 'zara', 'abc']
print("Popped Element : ", aList.pop())
print("Updated List:")
print(aList)

#Extend:
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)
print("Extended List : ", aList)

#count:
aList = [12, 'as', 12, 'abc', '12', 12]
print("Count for 12 : ", aList.count(12))
print("Count for '12' : ", aList.count('12'))

#sort:
aList = ['123', 'xyz', 'zara', 'abc', 'xyz']
aList.sort()
print("List : ", aList)

#remove:
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.remove('xyz')
print("List : ", aList)
aList.remove('abc')
print("List : ", aList)

#reverse:
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.reverse()
print("List : ", aList)
