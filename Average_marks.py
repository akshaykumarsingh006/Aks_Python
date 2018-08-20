#Code to Insert values into the dictionary:

n = int(input('enter the no. of students '))
dx = {}
for i in range(0,n):
    name = input('enter the name of the student ')
    grade = list(map(int, input('Enter subject marks: ').split()))
    dx[name] = grade
    #i = i+1

#Code to calculate the average marks for the specific student:

student_name = input('enter the student name for getting avg. marks ')
average_marks = round((sum(dx[name]))/3,2)
print(average_marks)