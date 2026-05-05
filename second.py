from email.policy import strict

from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import Annotated, List,Dict,Optional

class Student(BaseModel):
    name: Annotated[str,Field(max_length=50,description="Name of Student with max_ch=50")]
    age: Annotated[int,Field(gt=0,lt=120,strict=True)]
    email: EmailStr
    linkedIN: AnyUrl
    rollno: Annotated[str,Field(description="Add roll_no of the student",title="ROLLNO")]
    married: bool=False
    subjects: List[str]=Field(max_length=8)
    family_info: Optional[Dict[str,str]]=None


def add_student(student: Student):
    print("Name: ",student.name)
    print("Age: ",student.age)
    print("Email: ",student.email)
    print("LinkedIN: ",student.linkedIN)
    print("Rollno: ",student.rollno)
    print("Married: ",student.married)
    print("Subjects: ",student.subjects)
    print("family_info: ",student.family_info)

student_info={"name":"Hasan",
              "age":22,
              "email":"hassanimtiaz15@gmail.com",
              "linkedIN":"http://linkedin.com/hassanimtiaz158",
              "rollno":"bsdsf23m014",
              "subjects":["PF","OOP","DSA","AOA"]
              }

student1=Student(**student_info)

add_student(student1)