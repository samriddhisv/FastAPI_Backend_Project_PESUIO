# FastAPI_Backend_Project_PESUIO

<p>
  I’ve created a basic CRUD course details application.
  I’ve pushed all the data into an array (fakedb). I’m using a class of Course which is going to be run by the BaseModel imported from pydantic
  With the fields: id, name, price.
</p>

##details: 

•	@app.get("/courses")
can be used to refer to courses and return the entire array. 
•	@app.get("/courses/{course_id}")
can be used to refer to find the specified course_id from course array
•	@app.post("/courses")
can be used to take the course details, convert them into a dictionary and append it to the fakedb(array).
•	@app.delete("/courses/{course_id}")
can be used to delete a particular course_id
•	@app.get("/myinfo")
can be used to refer My information.




