from pydantic import BaseModel


class Question(BaseModel):
    text: str

class FilledQuestionary(BaseModel):
    filledQuestions: dict[str, str]

#   Answers

class DoctorResponseAnswer(BaseModel):
    text: str

class DoctorResponseQuestionary(BaseModel):
    questions: list[str]
