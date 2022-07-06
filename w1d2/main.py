


class Student:
    #constructor
    def __init__( self, first_name, last_name, age, instructor, course):
        # attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.instructor = instructor
        self.course = course
    def print_info( self, message ):
        print(message)
        print( f"Name: {self.first_name} {self.last_name}" )
        print( f"Age: {self.age}" )
        print(f"Instructor: {self.instructor}")
        print(f"Course: {self.course}")

student_alex = Student( "Alex", "Miller", 20, "Nichole", "Web Fundamentals" )
student_Jane = Student( "Jane", "Mill", 25, "Jim", "Web Fun" )
print( student_alex )

# print(student_alex.first_name, student_alex.last_name)
student_alex.print_info( "Hello" )
student_Jane.print_info( "howdy" )

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
    def __init__(self, data):
        self.name = data["name"]
        self.instructors = data["instructors"]
        self.program = data["program"]

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


python={
    "name" : "Python/flask",
    "instructors": ["Alfredo", "Spencer", "Pablo", "Tyler"],
    "program": "full stack"
}
course_python = Course(python)

course_python.print_info().update_instructor("ryan", 2).print_info()

