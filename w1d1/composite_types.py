# DICTIONARIES

# in js an array [item, item, item, item]: python this is lists

grades = [9.8, 8.7, 7.6]
#          0    1     2   (last index is always 1 less than the length)
print( grades )

print( grades[1] )

# in js we used .push to add to an element. in python we use .append

grades.append( 10.0 )
print(grades)

grades_copy = grades
grades_copy = grades[:]
# the copy will not be effected by the changes when the : is used. when it isnt used, if you change the copy you change the original

print( grades_copy )
# onjects in js are dictionaries in pytrhon

student = {

    "first_name" : "Alex",
    "last_name": "Miller",
    "age": 20,
    "grade": 9.6,
    "stack": "Python/Flask",
    "passed": True
}
print( student["first_name"] )
# l_n = "last name"
# print( student[l_n] )
print(student)

student["instuctor"] = "Alfredo"

print(student)

# Tuple is simalir to a array in python, but it is immutable

course = ( "Python", "4 weeks", "spencer rauch" )

print(course)

# course.append ( "pablo" ) 

# course [0] = "web fundamentals"
# this append and reassignment will not work because it is immutable




