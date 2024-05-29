#insert new value:
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
T.insert(2, [0,5,11,13,6])

for r in T:
   for c in r:
      print(c,end = " ")
   print()
print("*********************************************")
   #Updating the value:
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T[2] = [11,9]
T[0][3] = 7
for r in T:
   for c in r:
      print(c,end = " ")
   print()
print('*******************************')
#deleting value:
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

del T[3]

for r in T:
   for c in r:
      print(c,end = " ")
   print()
print("**************************************")
#Size of a 2-D array
a = [[3,9],[0,3,7,10]]
print(len(a))

print("*******************************")

#Slicing of a 2-D array in Python
a = [[1,2,3],[4,5,6,7]] 
b= a[1:3] 
print(b)
c= a[:1]
print(c)
print("*********************************")
#switch case:
class PythonSwitch:
    def day(self, dayOfWeek):

        default = "Incorrect day"

        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return "monday"
    def case_2(self):
        return "tuesday"
    def case_3(self):
        return "wednesday"
    def case_4(self):
       return "thursday"
    def case_5(self):
        return "friday"
    def case_7(self):
        return "saturday"
    def case_6(self):
        return "sunday"
my_switch = PythonSwitch()

print (my_switch.day(1))
print (my_switch.day(4))

