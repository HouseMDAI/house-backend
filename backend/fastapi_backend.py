from fastapi import FastAPI, Body, Request, Response
from .models import (Question, FilledQuestionary, DoctorResponseAnswer, DoctorResponseQuestionary)
from .user_card import UserCardSimple
from .prompting import get_response
import json

app = FastAPI()

####################

from fastapi import FastAPI, APIRouter, Response, Request
from fastapi.routing import APIRoute
from typing import Callable

       
class LoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            req_body = await request.body()
            print(req_body)
            response = await original_route_handler(request)
            print(response.body)
            return response
            
        return custom_route_handler

router = APIRouter(route_class=LoggingRoute)

####################

# @router.post("/doctor", response_model = DoctorResponseAnswer | DoctorResponseQuestionary)
@router.post("/doctor")
def message(user_card: UserCardSimple, filled_questionary: FilledQuestionary, message: str = Body(...)):
    json_string = get_response(user_card, message, filled_questionary) # TODO: validate model format
    print('String:', json_string)
    loaded = json.loads(json_string.strip())
    print('Loaded:', loaded)
    return loaded

@router.get("/onboarding", response_model = DoctorResponseQuestionary)
def onboarding():
    return DoctorResponseQuestionary(question=[Question(text=text) for text in UserCardSimple.__fields__.keys()])

@router.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# @router.get("/doctor/{user_id}", response_model = DoctorResponseAnswer | DoctorResponseQuestionary)
# def message(user_id: int, message: str, filled_questionary: FilledQuestionary):
    # TODO: get card by user id
    # user_card: UserCard
    # ...
    
app.include_router(router, prefix="")
