def registration(name, age, course):
    #perform registration takes here:
    print("Registration completed for:", name, "Age:", age,"Course:", course)
    pass
    return name, age, course
def profile():
    #print porfile information:
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    return name, age, course
def main():
    #call registration function:
    registration("Yaseen", 29, "Python data science AI & Machine learning")
    #call profile function:
    profile("Yaseen", 29, "Python data science AI & Machine learning")
    #call main function to start the program:
main()
print(profile())

    
    
