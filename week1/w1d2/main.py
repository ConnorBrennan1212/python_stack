


from random import random


class Student:
    #constructor
    def __init__( self, first_name, last_name, age ):
        # attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.instructor = None
        self.course = None
        
    def print_info( self, message ):
        print(message)
        print( f"Name: {self.first_name} {self.last_name}" )
        print( f"Age: {self.age}" )
        print(f"Instructor: {self.instructor}")
        print(f"Course: {self.course}")

    def enroll(self, course):
        self.course = course
        instructor = random.choice(course.instructors)
        self.instructor = instructor
        return self



student_alex = Student( "Alex", "Miller", 20 )
student_Jane = Student( "Jane", "Mill", 25 )
# print( student_alex )

# print(student_alex.first_name, student_alex.last_name)
# student_alex.print_info( "Hello" )
# student_Jane.print_info( "howdy" )

list_students = []
list_students.append( student_alex )
list_students.append( student_Jane )

for student in list_students:
    student.print_info("hey there")

        # subject
        # first_name
        # last_name
        # ACS_GEQUALgpa
        # instructor

class Course:
    @classmethod
    def print_all_courses(cls):
        for course in cls.all_courses:
            print(course)

    all_courses = []
    def __init__(self, data):
        self.name = data["name"]
        self.instructors = data["instructors"]
        self.program = data["program"]
        Course.all_courses.append(self)

    def print_instructor_list(self):
        for instructor in self.instructors:
            print(instructor)
            # return self to enable chain
        return self
    
    def update_instructor(self, new_name, index):
        if index < len(self.instructors):
            self.instructors[index] = new_name
        return self
    
    def print_info(self):
        print(f"program: {self.program}")
        print(f"Name: {self.name}")
        self.print_instructor_list()
        return self

    @staticmethod
    def determine_eligibility(age):
        if age >= 18:
            return True
        return False


    def __repr__(self):
        return f"{self.name} is a {self.program} course"


python={
    "name" : "Python/flask",
    "instructors": ["Alfredo", "Spencer", "Pablo", "Tyler"],
    "program": "full stack"
}

java={
    "name" : "java",
    "instructors": ["Alfredo", "Spencer", "Pablo", "Tyler"],
    "program": "full stack"
}

mern={
    "name" : "mern",
    "instructors": ["Alfredo", "Spencer", "Pablo", "Tyler"],
    "program": "full stack"
}

course_python = Course(python)
course_java = Course(java)
course_mern = Course(mern)

Course.print_all_courses()
# course_python = Course(python)

# course_python.print_info().update_instructor("ryan", 2).print_info()

student_Jane.print_info("yo")

if Course.determine_eligibility(student_alex.age):
    student_alex.enroll(course_java)
    print("welcome to java")
else:
    print("Im sorry you are not quite old enough")

student_alex.print_info("ak;ljsdfh;'aslkjhdf")
