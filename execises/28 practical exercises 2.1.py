"""
1 student is a proffesor
1 student is assistant

a) ask for the age of the classmates who came to class today and sort the data form least to greatest
b) the oldes is the proffessor, and the youngest is the assistant. Who is who? 
"""


#function for get assistent and proffesor acccording to age
def ask_data_students(number_students):
    
    #creating a list with students
    students = []
    
    #making a for to ask information for every student
    for i in range(number_students):
        name = input ("enters the student name: ")
        age = int(input("enters the student age: "))
        student = (name,age)
        #append the data to the list
        students.append(student)
        #Sorting in ascending order
        students.sort(key= lambda student_info: student_info[1])
        
        
    #students[x] return a tuple whith (name, age) and after access to for define professor and assitant 
    Assistant_group = students[0][0]
    proffesor = students[-1][0]
    #return a tuple 
    return Assistant_group,proffesor

number_students = input("enters the number of students: ")
#unpacking returnig data from function ask_data_students()
Assistant_group,proffesor = ask_data_students(int(number_students))

#showing result
print(f"the new professor is {proffesor} and the new assistan {Assistant_group}")
        
    


