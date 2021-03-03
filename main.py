from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fakedb = []

class myinfo(BaseModel):
    Name: str
    SRN: str
    Fun_fact: str

class Course(BaseModel):
    id: int
    name: str
    price: float 

@app.get("/")
def read_root():
    return {"greetings": "Welcome to LetsUsLearn.in a course based website"}

@app.get("/myinfo")
def return_myinfo():
    res = {"name":"Samriddhi V", 
            "SRN": "PES2UG19CS359",
            "Fun_fact":"xyz"}
    return res

    

@app.get("/courses")
def get_courses():
    return fakedb

@app.get("/courses/{course_id}")
def get_a_course(course_id:  int):
    course = course_id - 1
    return fakedb[course]

@app.post("/courses")
def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1]

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    fakedb.pop(course_id-1)
    return {"task": "deletion successfull"}
