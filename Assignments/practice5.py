#Function with one argument:
def my_function(fname):
    print(fname)
my_function("Yaseen")
my_function("Elton")
my_function("Samson")
print("***********************************")
#Function with two arguments:
def my_function(fname,lname):
    print(fname,lname)
my_function("Yaseen","Fadol")
print("***********************************")
#Function with unknown number of argument:
def my_function(*students):
    print("the students name:"+students[3])
my_function("Yaseen", "Elton","Samson" ,"Martha")
print("************************************")
#Function with default parameter value:
def my_function(programlanguage="Python"):
    print("I am from :"+programlanguage)
my_function()
print("************************************")
#Function with two parameters value:
def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)
add_numbers(2, 3)







