from pydantic import BaseModel


class Question(BaseModel):
    text: str

class FilledQuestionary(BaseModel):
    filled_questions: dict[str, str]

#   Answers

class DoctorResponseAnswer(BaseModel):
    text: str

class DoctorResponseQuestionary(BaseModel):
    questions: list[str]
