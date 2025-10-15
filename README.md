# 🧠 FastAPI Student Details Backend

The repository contains a simple **Python backend** built with **FastAPI** and tested using **Postman**.  
The data is stored in an array of JSON objects inside the file **`student_details.json`**.

---

## 📄 `main.py`

This file defines **three API endpoints:**

- `get_all`  
- `get_average`  
- `add`

---

## 🟦 `get_all` Endpoint

Retrieves all the student objects stored in **`student_details.json`**.

> ⚠️ **Issue:**  
> Original text said: “retrieves all the objects present in get_all” — this is circular.  
> ✅ Should be: “retrieves all the student records from `student_details.json`.”

---

## 🟩 `get_average` Endpoint

Computes the average marks of each student present in the file.

> ⚠️ **Potential Issue:**  
> Clarify whether it computes **average per student** (average of marks for each student)  
> or **overall class average**.  
> ✅ Suggested fix: “Computes the average marks **for each student**, based on their scores stored in `student_details.json`.”

---

## 🟥 `add` Endpoint

Accepts a new student object matching the schema of the **`Student`** class (defined in the same file).  
If the schema does not match, it throws a **400 Bad Request** error.  
If the roll number already exists, it throws a **409 Conflict** error.  
If successful, it appends the object to **`student_details.json`** and saves it.

> ⚠️ **Issue 1:**  
> File name mismatch — text alternates between `student_detail.json` and `student_details.json`.  
> ✅ Use consistent naming throughout (`student_details.json`).

> ⚠️ **Issue 2:**  
> “Requests the user to enter a valid object” — misleading phrasing.  
> ✅ Better phrasing: “Accepts a valid JSON object in the POST request body.”

---

## 💡 Suggested Code Insertion Points

1. **Under each endpoint heading**, insert example code blocks:
   ```python
   # Example: GET /get_all
   @app.get("/get_all")
   async def get_all():
       ...
   ```

2. **After describing `Student` class**, include its schema:
   ```python
   class Student(BaseModel):
       roll_no: int
       name: str
       marks: list[int]
   ```

3. **After `add` endpoint**, include example error responses:
   ```python
   # 400 - Invalid schema
   # 409 - Duplicate roll number
   ```
