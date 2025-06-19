from pydantic import BaseModel

class Student(BaseModel):

    name:str

new_student ={'name':'Krish'}
new_student1 ={'name':32} # because name should be a string

student=Student(**new_student)
# student1=Student(**new_student1)  this will through an error

print(type(student))
print(type(student1))