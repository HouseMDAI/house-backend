from fastapi import FastAPI
from .models import (Question, FilledQuestionary, DoctorResponseAnswer, DoctorResponseQuestionary)
from .user_card import UserCard
from .prompting import get_response

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# @app.get("/doctor/{user_id}", response_model = DoctorResponseAnswer | DoctorResponseQuestionary)
# def message(user_id: int, message: str, filled_questionary: FilledQuestionary):
    # TODO: get card by user id
    # user_card: UserCard
    # ...

@app.post("/doctor", response_model = DoctorResponseAnswer | DoctorResponseQuestionary)
def message(user_card: UserCard, message: str, filled_questionary: FilledQuestionary):
    return get_response(user_card, message, filled_questionary) # TODO: validate model format
