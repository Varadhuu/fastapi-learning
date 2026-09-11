
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    interest: List[str]

class UserResponse(BaseModel):
    message: str
    user: User
    recommendation: List[str]

@app.get("/")
def hello():
    return {"Welcome to the page man"}

@app.get("/recommend")
def recommendation(age:int,interest:str):
    if age < 18:
        category = "Teen"
    elif age < 40:
        category = "Adult"
    else:
        category = "Senior"

    recommendation = []
    if interest.lower() == "sports":
        recommendation = ["Football", "Basketball", "Tennis"]
    elif interest.lower() == "music":
        recommendation = ["Concerts", "Recording Studio", "Music Classes"]
    elif interest.lower() == "technology":
        recommendation = ["Tech Conferences", "Coding Bootcamps", "Innovation Labs"]
    else:
        recommendation = ["General Activities", "Community Events", "Workshops"]

    return {"category": category, 
            "interest": interest,
            "recommendation": recommendation}

@app.post("/users",response_model=UserResponse)
def create_user(user: User):
    first_interest = user.interest[0] if user.interest else "General"
    recommendation = []
    if first_interest.lower() == "sports":
        recommendation = ["Football", "Basketball", "Tennis"]
    elif first_interest.lower() == "music":
        recommendation = ["Concerts", "Recording Studio", "Music Classes"]
    elif first_interest.lower() == "technology":
        recommendation = ["Tech Conferences", "Coding Bootcamps", "Innovation Labs"]
    else:
        recommendation = ["General Activities", "Community Events", "Workshops"]

    return {"message": "User profile created successfully", 
            "user": user,
            "recommendation": recommendation}