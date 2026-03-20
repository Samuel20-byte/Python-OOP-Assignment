# objects_and_classes.py

# Define a class
class Student:
    # Class attribute
    school = "Technical University"

    # Method
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Create objects (instances)
student1 = Student()
student2 = Student()
student3 = Student()
# Assign attributes to objects
student1.name = "Samuel"
student1.age = 21

student2.name = "Gloria"
student2.age = 22

student3.name = "Njuguna"
student3.age = 23
# Access attributes and methods
print(student1.name)
student1.introduce()

print(student2.name)
student2.introduce()

print(student3.name)
student3.introduce()